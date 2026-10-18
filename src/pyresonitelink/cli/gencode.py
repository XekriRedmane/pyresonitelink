"""CLI tool for generating component wrapper classes from a live ResoniteLink server.

Connects to the server, fetches the component definition (and optionally
instantiates it to get concrete member types), generates a Python source
file, and writes it into the ``generated/`` directory tree with the
category path as the directory structure.

Referenced target types are recursively generated using GetTypeDefinition.
Types that are components get full wrapper classes; other types (interfaces,
abstract classes, assets) get proper Python classes in ``_types/`` with
their full type hierarchy.
"""

import argparse
import asyncio
import os
import re
from pathlib import Path
from typing import Any, cast

from pyresonitelink import client
from pyresonitelink.data import messages
from pyresonitelink.cli.wikidocs import fetch_wiki_docs, save_docs
from pyresonitelink.generated._generator import (
    generate_component_source,
    generate_enum_source,
    generate_type_source,
    get_enum_module_name,
    get_reference_target_types,
    _CLASS_NAME_OVERRIDES,
    _arity_key,
    _collect_referenced_type_keys,
    _collect_referenced_types,
    _is_generic_param_name,
    _is_primitive_wire_name,
    _PRIMITIVE_WIRE_NAMES,
    _ref_stub_module_name,
    _simple_class_name,
    _to_class_name,
    _to_module_path,
)

# Root of the generated package
_GENERATED_DIR = Path(__file__).resolve().parent.parent / "generated"
# Every file the generator writes passes newline="\n". Text mode on Windows
# would otherwise write CRLF, and the repository stores LF (.gitattributes).

# Category paths that should be skipped during generation.
# These contain internal ProtoFlux proxy types (auto-generated
# plumbing with hex suffixes and many generic parameters).
_SKIP_CATEGORIES: frozenset[str] = frozenset({
    "ProtoFlux/FrooxEngine/ProtoFlux/CoreNodes",
})


def _ensure_init_files(path: Path) -> None:
    """Create __init__.py in all directories between generated/ and path.

    Args:
        path: A file path under _GENERATED_DIR.
    """
    for parent in reversed(
        list(path.relative_to(_GENERATED_DIR).parents)
    ):
        init_path = _GENERATED_DIR / parent / "__init__.py"
        if not init_path.exists() and parent != Path("."):
            init_path.write_text("", newline="\n")


def _output_path_for_component(
    component_type: str, category: str,
) -> Path:
    """Determine the output file path for a component.

    Args:
        component_type: Fully qualified Resonite type name.
        category: Category path from the definition (e.g. "Audio").

    Returns:
        Absolute path for the generated .py file.
    """
    if category:
        category_dir = "/".join(
            part.lower().replace(" ", "_") for part in category.split("/")
        )
    else:
        category_dir = ""

    rel_path = _to_module_path(component_type)
    if category_dir:
        return _GENERATED_DIR / category_dir / os.path.basename(rel_path)
    return _GENERATED_DIR / rel_path


async def _get_type_definition_cached(
    resolink: client.Client,
    type_name: str,
    cache: dict[str, dict[str, Any] | None],
) -> dict[str, Any] | None:
    """Fetch a type definition, using a cache to avoid repeated requests.

    Args:
        resolink: Connected ResoniteLink client.
        type_name: Full Resonite type name.
        cache: Shared cache mapping type name to definition (or None
            if the request failed).

    Returns:
        The definition dict, or None if the type definition failed.
    """
    if type_name in cache:
        return cache[type_name]
    resp = await resolink.request_json(
        messages.GetTypeDefinition(type=type_name)
    )
    if resp.get("success"):
        defn = cast(dict[str, Any], resp.get("definition", {}))
        cache[type_name] = defn
        return defn
    cache[type_name] = None
    return None


# Cache for _collect_component_interfaces results, keyed by the
# component type's _arity_key.
_interface_cache: dict[str, list[str]] = {}

# Maps each component seen so far, by its _arity_key, to the module and
# class that define it, e.g. "[FrooxEngine]FrooxEngine.TextRenderer" to
# ("pyresonitelink.generated.rendering.text_renderer", "TextRenderer").
# A component that references another component imports it from there
# for type checking. The full type name keeps FrooxEngine.Slider and
# FrooxEngine.UIX.Slider apart, and the arity marker keeps UIX.Slider and
# UIX.Slider<T> apart.
_component_modules: dict[str, tuple[str, str]] = {}

# GetComponentDefinition responses by type name, or None when the request
# failed, which is also how a type that isn't a component shows up.
_component_definitions: dict[str, dict[str, Any] | None] = {}

# _arity_keys whose family has already been checked for name clashes.
_names_assigned: set[str] = set()


async def _get_component_definition(
    resolink: client.Client, component_type: str,
) -> dict[str, Any] | None:
    """Returns a component's flattened definition, or None if there's none.

    Args:
        resolink: Connected ResoniteLink client.
        component_type: Fully qualified Resonite type name.

    Returns:
        The "definition" dict from the response, or None if the request
        failed.
    """
    if component_type not in _component_definitions:
        resp = await resolink.request_json(
            messages.GetComponentDefinition(
                componentType=component_type, flattened=True,
            )
        )
        _component_definitions[component_type] = (
            cast(dict[str, Any], resp.get("definition", {}))
            if resp.get("success") else None
        )
    return _component_definitions[component_type]


def _describe_generic_param(name: str) -> str:
    """Returns the word a generic parameter adds to a class name.

    ProtoFlux names the execution context type parameter C, so it becomes
    "Context". A T-prefixed name such as TValue loses the T. Any other
    name is used as it is.

    Args:
        name: The generic parameter's name, e.g. "C" or "TValue".

    Returns:
        e.g. "Context" or "Value".
    """
    if name == "C":
        return "Context"
    if re.fullmatch(r"T[A-Z][A-Za-z0-9]*", name):
        return name[1:]
    return name


async def _assign_class_names(
    resolink: client.Client, component_type: str,
) -> None:
    """Gives distinct class names to components that share a plain name.

    Resonite treats X, X<T>, and X<T1, T2> as different types, but all
    three would become the Python class X in the same module. This looks
    up the whole family and records the names in _CLASS_NAME_OVERRIDES:

    - Among the generic forms, the one with the fewest parameters keeps
      the plain name. Each longer form adds "With" and its extra
      parameters, e.g. ValueWrite<C, T> becomes ValueWriteWithContext.
    - Of a non-generic X and a generic X<T>, when one derives from the
      other, the descendant keeps the plain name and the ancestor gets
      "Base". FireOnLocalTrue derives from FireOnLocalTrue<C>, which
      becomes FireOnLocalTrueBase. When neither derives from the other,
      the generic one gets "Of", e.g. SliderOf.

    Args:
        resolink: Connected ResoniteLink client.
        component_type: Fully qualified Resonite type name.
    """
    key = _arity_key(component_type)
    if key in _names_assigned:
        return
    stem = re.sub(r"<.*", "", key)
    family: dict[int, dict[str, Any]] = {}
    family_keys: dict[int, str] = {}
    for arity in range(4):
        member_key = stem if arity == 0 else f"{stem}<{',' * (arity - 1)}>"
        _names_assigned.add(member_key)
        definition = await _get_component_definition(resolink, member_key)
        if definition is not None:
            family[arity] = definition
            family_keys[arity] = member_key
    if len(family) < 2:
        return

    def params(arity: int) -> list[str]:
        type_def = family[arity].get("type") or {}
        return [
            str(p.get("name", ""))
            for p in type_def.get("genericParameters") or []
        ]

    async def base_key(arity: int) -> str:
        # A flattened definition leaves out the base type, so this asks
        # for the unflattened one.
        resp = await resolink.request_json(
            messages.GetComponentDefinition(
                componentType=family_keys[arity], flattened=False,
            )
        )
        definition = cast(dict[str, Any], resp.get("definition") or {})
        type_def = definition.get("type") or {}
        base = (type_def.get("baseType") or {}).get("type") or ""
        return _arity_key(str(base))

    plain = _to_class_name(stem, use_overrides=False)
    generic_arities = sorted(a for a in family if a > 0)
    for arity in generic_arities[1:]:
        shortest = params(generic_arities[0])
        extra = [p for p in params(arity) if p not in shortest]
        suffix = "".join(_describe_generic_param(p) for p in extra) or str(arity)
        _CLASS_NAME_OVERRIDES[family_keys[arity]] = f"{plain}With{suffix}"
    if 0 in family and generic_arities:
        generic = generic_arities[0]
        if await base_key(0) == family_keys[generic]:
            _CLASS_NAME_OVERRIDES[family_keys[generic]] = f"{plain}Base"
        elif await base_key(generic) == family_keys[0]:
            _CLASS_NAME_OVERRIDES[family_keys[0]] = f"{plain}Base"
        else:
            _CLASS_NAME_OVERRIDES[family_keys[generic]] = f"{plain}Of"


def _avoid_namespace_clash(component_type: str, category: str) -> None:
    """Renames a component whose module already belongs to another one.

    Two components with the same name in different namespaces, such as
    Strings.NewLine and Strings.Characters.NewLine, can land in the same
    category and so the same file. The one that doesn't own the existing
    file gets the namespace segments that tell it apart as a prefix, e.g.
    CharactersNewLine.

    Args:
        component_type: Fully qualified Resonite type name.
        category: Category path from the component's definition.
    """
    key = _arity_key(component_type)
    if key in _CLASS_NAME_OVERRIDES:
        return
    path = _output_path_for_component(component_type, category)
    if not path.exists():
        return
    match = re.search(
        r'^    (?:COMPONENT_TYPE|_GENERIC_TYPE_TEMPLATE) = "([^"]+)"$',
        path.read_text(encoding="utf-8"),
        flags=re.MULTILINE,
    )
    if not match:
        return
    owner_stem = re.sub(r"<.*", "", match.group(1))
    stem = re.sub(r"<.*", "", key)
    if owner_stem == stem:
        return
    namespace = re.sub(r"^\[.*?\]", "", stem).split(".")[:-1]
    owner_namespace = re.sub(r"^\[.*?\]", "", owner_stem).split(".")[:-1]
    extra = [part for part in namespace if part not in owner_namespace]
    prefix = "".join(extra) if extra else namespace[-1]
    _CLASS_NAME_OVERRIDES[key] = prefix + _to_class_name(component_type)


def _record_component_module(component_type: str, category: str) -> None:
    """Records which module defines a component's wrapper class.

    Args:
        component_type: Fully qualified Resonite type name.
        category: Category path from the component's definition.
    """
    path = _output_path_for_component(component_type, category)
    rel = path.relative_to(_GENERATED_DIR.parent.parent).with_suffix("")
    _component_modules[_arity_key(component_type)] = (
        ".".join(rel.parts), _to_class_name(component_type),
    )


async def _collect_component_interfaces(
    resolink: client.Client,
    component_type: str,
    type_def_cache: dict[str, dict[str, Any] | None] | None = None,
) -> list[str]:
    """Collect all interface type strings implemented by a component.

    Traces the component's base type chain via ``GetTypeDefinition``
    and collects every interface reported at each level.  Results are
    cached so repeated calls for the same base type chain are free.

    Args:
        resolink: Connected ResoniteLink client.
        component_type: Full Resonite component type name.
        type_def_cache: Optional shared cache for GetTypeDefinition
            responses.

    Returns:
        List of full Resonite interface type strings (e.g.
        ``"[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<>"``).
    """
    cache_key = _arity_key(component_type)
    if cache_key in _interface_cache:
        return _interface_cache[cache_key]

    if type_def_cache is None:
        type_def_cache = {}

    interfaces: list[str] = []
    seen_ifaces: set[str] = set()
    types_to_visit = [component_type]
    visited: set[str] = set()

    while types_to_visit:
        t = types_to_visit.pop(0)
        simple = _simple_class_name(t)
        if simple in visited:
            continue
        visited.add(simple)

        type_def = await _get_type_definition_cached(
            resolink, t, type_def_cache,
        )
        if type_def is None:
            continue

        # Collect interfaces
        for iface in (type_def.get("interfaces") or []):
            if not isinstance(iface, dict):
                continue
            iface_type = iface.get("type", "")
            if iface_type and iface_type not in seen_ifaces:
                seen_ifaces.add(iface_type)
                interfaces.append(iface_type)

        # Trace base type
        base_ref = type_def.get("baseType")
        if isinstance(base_ref, dict):
            base_type = base_ref.get("type", "")
            if base_type and _simple_class_name(base_type) not in visited:
                types_to_visit.append(base_type)

    _interface_cache[cache_key] = interfaces
    return interfaces


async def _generate_type_hierarchy(
    resolink: client.Client,
    resonite_type: str,
    generated: set[str],
    all_type_defs: dict[str, dict[str, Any]],
    dry_run: bool,
    type_def_cache: dict[str, dict[str, Any] | None] | None = None,
) -> None:
    """Recursively generate a type and all types it references.

    Fetches the TypeDefinition from the server and generates a Python
    class in ``_types/``. Recurses into base types, interfaces, and
    generic parameter constraints.

    Args:
        resolink: Connected ResoniteLink client.
        resonite_type: Full Resonite type name (base form, no generic args).
        generated: Set of already-generated class names.
        all_type_defs: Accumulator for all fetched TypeDefinitions.
        dry_run: If True, print source instead of writing.
    """
    cls_name = _simple_class_name(resonite_type)
    if cls_name in generated:
        return
    # Skip bare generic parameter names (T, V, A, etc.) and primitives
    if _is_generic_param_name(cls_name) or _is_primitive_wire_name(resonite_type):
        return
    generated.add(cls_name)

    if type_def_cache is None:
        type_def_cache = {}

    # In Resonite, non-generic X and generic X<> are separate types where
    # X<> inherits from X. In Python we merge them into one class: the
    # generic form with Generic[T]. Query both forms and merge.
    query_type = resonite_type

    # Get non-generic form
    resp_plain = await resolink.request_json(
        messages.GetTypeDefinition(type=query_type)
    )
    # Get generic form (only if the plain name doesn't already have <>)
    resp_generic = None
    if "<" not in query_type:
        resp_generic = await resolink.request_json(
            messages.GetTypeDefinition(type=query_type + "<>")
        )
        if not resp_generic.get("success"):
            resp_generic = None

    # Pick the best definition
    if resp_generic:
        # Use the generic form for the class (has type params)
        type_def = cast(dict[str, Any], resp_generic.get("definition", {}))
        # Merge interfaces from the non-generic form (the generic's
        # baseType points to non-generic, so its interfaces would be
        # inherited — but we use the non-generic's interfaces to capture
        # the full picture and let the dedup logic filter redundant ones)
        if resp_plain and resp_plain.get("success"):
            plain_def = cast(
                dict[str, Any], resp_plain.get("definition", {})
            )
            plain_ifaces = plain_def.get("interfaces") or []
            generic_ifaces = list(type_def.get("interfaces") or [])
            # Add non-generic interfaces that aren't already listed
            existing = {
                iface.get("type", "")
                for iface in generic_ifaces
                if isinstance(iface, dict)
            }
            for iface in plain_ifaces:
                if isinstance(iface, dict):
                    if iface.get("type", "") not in existing:
                        generic_ifaces.append(iface)
            type_def["interfaces"] = generic_ifaces
            # Skip the non-generic base (it's just the unparameterized self)
            base_ref = type_def.get("baseType")
            if isinstance(base_ref, dict):
                base_name = _simple_class_name(base_ref.get("type", ""))
                if base_name == cls_name:
                    # Replace with the non-generic's base type
                    type_def["baseType"] = plain_def.get("baseType")
    elif resp_plain and resp_plain.get("success"):
        type_def = cast(dict[str, Any], resp_plain.get("definition", {}))
    else:
        # GetTypeDefinition fails for component types, so the type may be
        # a component. Generating it as one records its module, and
        # referencing components then import it for type checking only.
        check = await resolink.request_json(
            messages.GetComponentDefinition(
                componentType=resonite_type, flattened=True,
            )
        )
        if check.get("success"):
            generated.discard(cls_name)
            await _generate_component(
                resolink, resonite_type, generated,
                all_type_defs, dry_run, type_def_cache,
            )
            return
        # Otherwise write a placeholder, so that modules importing the
        # type still import. It has no base types or members.
        print(f"  Warning: could not get type definition for {resonite_type}")
        mod_name = _ref_stub_module_name(resonite_type)
        placeholder = (
            f'"""Generated stub type: {cls_name}."""\n'
            f"\n"
            f"\n"
            f"class {cls_name}:\n"
            f'    """Stub for {resonite_type}.\n'
            f"\n"
            f"    The server returned no type definition for it, so the stub\n"
            f"    has no base types or members.\n"
            f'    """\n'
            f"\n"
            f'    RESONITE_TYPE: str = "{resonite_type}"\n'
            f"\n"
            f"    @property\n"
            f"    def id(self) -> str | None:\n"
            f'        """The element\'s unique ID."""\n'
            f"        return None\n"
        )
        if dry_run:
            print(f"\n--- {resonite_type} (_types/{mod_name}.py) ---")
            print(placeholder)
        else:
            placeholder_path = _GENERATED_DIR / "_types" / f"{mod_name}.py"
            placeholder_path.write_text(placeholder, encoding="utf-8", newline="\n")
            print(f"Wrote {placeholder_path}")
        return

    full_name = str(type_def.get("fullTypeName", resonite_type))
    all_type_defs[full_name] = type_def
    # Also register under the non-generic name for ancestor lookups
    plain_name = full_name.split("<")[0] if "<" in full_name else full_name
    all_type_defs[plain_name] = type_def

    # Collect all types referenced by this type and recurse FIRST
    # (so dependencies are generated before dependents)
    deps: list[str] = []

    # Base type
    base_ref = type_def.get("baseType")
    if isinstance(base_ref, dict):
        for t in _collect_referenced_types(base_ref.get("type", "")):
            deps.append(t)

    # Interfaces
    for iface in (type_def.get("interfaces") or []):
        if isinstance(iface, dict):
            for t in _collect_referenced_types(iface.get("type", "")):
                deps.append(t)

    # Generic parameter constraints
    for param in (type_def.get("genericParameters") or []):
        for ct in (param.get("types") or []):
            if isinstance(ct, dict):
                for t in _collect_referenced_types(ct.get("type", "")):
                    deps.append(t)

    # Recurse into dependencies
    for dep in deps:
        dep_cls = _simple_class_name(dep)
        # Skip self-references, generic parameter names, and primitives
        is_generic_param = any(
            p.get("name") == dep_cls
            for p in (type_def.get("genericParameters") or [])
        )
        if is_generic_param or dep_cls == cls_name:
            continue
        if _is_primitive_wire_name(dep):
            continue
        # Skip bare type parameter names (single letters like T, V, A)
        if _is_generic_param_name(dep_cls):
            continue
        if dep_cls not in generated:
            await _generate_type_hierarchy(
                resolink, dep, generated, all_type_defs, dry_run,
                type_def_cache,
            )

    # Now generate this type
    source = generate_type_source(type_def, all_type_defs)
    mod_name = _ref_stub_module_name(resonite_type)
    output_path = _GENERATED_DIR / "_types" / f"{mod_name}.py"

    if dry_run:
        print(f"\n--- {full_name} (_types/{mod_name}.py) ---")
        print(source)
    else:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        init_path = output_path.parent / "__init__.py"
        if not init_path.exists():
            init_path.write_text("", newline="\n")
        output_path.write_text(source, encoding="utf-8", newline="\n")
        print(f"Wrote {output_path}")


async def _generate_component(
    resolink: client.Client,
    component_type: str,
    generated: set[str],
    all_type_defs: dict[str, dict[str, Any]],
    dry_run: bool,
    type_def_cache: dict[str, dict[str, Any] | None] | None = None,
) -> None:
    """Generate a component and recursively generate referenced types.

    Args:
        resolink: Connected ResoniteLink client.
        component_type: Full Resonite component type name.
        generated: Set of already-generated class names.
        all_type_defs: Accumulator for all fetched TypeDefinitions.
        dry_run: If True, print source instead of writing.
        type_def_cache: Shared cache for GetTypeDefinition responses.
    """
    if type_def_cache is None:
        type_def_cache = {}
    cls_name = _simple_class_name(component_type)

    # Scrape wiki documentation early — before the generated check,
    # so that components first generated as dependencies still get
    # their wiki docs scraped when encountered as top-level components.
    if not dry_run:
        from pyresonitelink.generated._generator import _load_wiki_docs
        if _load_wiki_docs(cls_name) is None:
            is_mixed = (
                "_" in cls_name
                and not cls_name.startswith("UI_")
                and not cls_name.startswith("PBS_")
            )
            if not is_mixed:
                is_protoflux = "ProtoFlux" in component_type
                wiki_docs = fetch_wiki_docs(
                    cls_name, prefer_protoflux=is_protoflux,
                )
                if wiki_docs is not None:
                    save_docs(cls_name, wiki_docs)
                    # New docs found — force regeneration so the
                    # docs get merged into the component code.
                    generated.discard(_arity_key(component_type))

    # ValueWrite<T> and ValueWrite<C, T> are different components, so the
    # key keeps the arity.
    gen_key = _arity_key(component_type)
    if gen_key in generated:
        return
    generated.add(gen_key)

    definition = await _get_component_definition(resolink, component_type)
    if definition is None:
        def_resp = await resolink.request_json(
            messages.GetComponentDefinition(
                componentType=component_type, flattened=True
            )
        )
        print(f"Error: {def_resp.get('errorInfo')}")
        return
    category = str(definition.get("categoryPath", ""))

    if category in _SKIP_CATEGORIES:
        return

    await _assign_class_names(resolink, component_type)
    _avoid_namespace_clash(component_type, category)

    # Generate referenced types first.
    # The definition's TypeReference dicts contain full generic args
    # (e.g. INodeValueOutput<> with genericArguments: [{type: "float"}]),
    # so we don't need to instantiate the component to get concrete
    # member types.  comp_data is no longer used.
    ref_targets = get_reference_target_types(definition, None)
    for target_type_str in ref_targets.values():
        # The keys keep the arity, so a reference to Slider<float> finds
        # the generic UIX.Slider<T> and not the non-generic UIX.Slider.
        for ref_key in _collect_referenced_type_keys(target_type_str):
            ref_base = re.sub(r"<.*", "", ref_key)
            if ref_key not in generated:
                # Try as component first
                check_def = await _get_component_definition(
                    resolink, ref_key,
                )
                if check_def is not None:
                    check_category = str(check_def.get("categoryPath", ""))
                    if check_category not in _SKIP_CATEGORIES:
                        await _assign_class_names(resolink, ref_key)
                        _avoid_namespace_clash(ref_key, check_category)
                        _record_component_module(ref_key, check_category)
                    await _generate_component(
                        resolink, ref_key, generated,
                        all_type_defs, dry_run,
                        type_def_cache,
                    )
                else:
                    await _generate_type_hierarchy(
                        resolink, ref_base, generated,
                        all_type_defs, dry_run,
                        type_def_cache,
                    )

    # Generate enum types used by this component
    def_members = definition.get("members", {})
    for mem_name, mem_def in def_members.items():
        if mem_name in ("persistent", "UpdateOrder", "Enabled"):
            continue
        if mem_def.get("$type") == "field":
            vt = mem_def.get("valueType", {})
            if isinstance(vt, dict):
                vt_name = vt.get("type", "")
                if (
                    vt_name
                    and vt_name not in _PRIMITIVE_WIRE_NAMES
                    and not vt.get("isGenericParameter", False)
                    and vt_name != "Nullable<>"
                ):
                    enum_cls = _simple_class_name(vt_name)
                    enum_mod = get_enum_module_name(vt_name)
                    enum_path = _GENERATED_DIR / "_enums" / f"{enum_mod}.py"
                    if not dry_run:
                        enum_resp = await resolink.request_json(
                            messages.GetEnumDefinition(type=vt_name)
                        )
                        if enum_resp.get("success"):
                            enum_def = cast(
                                dict[str, Any],
                                enum_resp.get("definition", {}),
                            )
                            enum_src = generate_enum_source(enum_def)
                            enum_path.parent.mkdir(
                                parents=True, exist_ok=True,
                            )
                            enum_path.write_text(
                                enum_src, encoding="utf-8", newline="\n",
                            )
                            print(f"Wrote {enum_path}")

    # Collect interfaces implemented by this component
    component_interfaces = await _collect_component_interfaces(
        resolink, component_type, type_def_cache,
    )

    # Ensure interface types have _types/ stubs generated
    for iface_type in component_interfaces:
        for ref_base in _collect_referenced_types(iface_type):
            ref_cls = _simple_class_name(ref_base)
            if ref_cls not in generated:
                await _generate_type_hierarchy(
                    resolink, ref_base, generated,
                    all_type_defs, dry_run,
                    type_def_cache,
                )

    # Generate this component
    _record_component_module(component_type, category)
    source = generate_component_source(
        component_type, definition,
        interfaces=component_interfaces,
        all_type_defs=all_type_defs,
        component_modules=_component_modules,
    )
    output_path = _output_path_for_component(component_type, category)

    if dry_run:
        print(f"\n--- {component_type} (category: {category}) ---")
        print(source)
    else:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        _ensure_init_files(output_path)
        output_path.write_text(source, encoding="utf-8", newline="\n")
        print(f"Wrote {output_path}")


def _rebuild_init_exports(directory: Path) -> None:
    """Rebuild ``__init__.py`` re-exports for a package directory.

    Scans *directory* for ``.py`` modules and subdirectories,
    extracts the first ``class`` declaration from each module, and
    writes an ``__init__.py`` that re-exports every class.  Handles
    Python keyword module/directory names (``if``, ``for``, ``while``,
    ``async``) via ``importlib``.

    Args:
        directory: A package directory containing generated modules.
    """
    import keyword

    pkg_name = ".".join(directory.relative_to(
        _GENERATED_DIR.parent.parent  # src/pyresonitelink
    ).parts)

    modules: list[tuple[str, str, bool]] = []  # (mod_path, cls, needs_importlib)

    for py_file in sorted(directory.glob("*.py")):
        if py_file.name == "__init__.py":
            continue
        mod_name = py_file.stem
        if not mod_name.isidentifier():
            continue
        with open(py_file, encoding="utf-8") as f:
            for line in f:
                if line.startswith("class "):
                    cls_name = line.split("(")[0].replace("class ", "").strip()
                    modules.append((
                        mod_name, cls_name, keyword.iskeyword(mod_name),
                    ))
                    break

    for sub_dir in sorted(directory.iterdir()):
        if not sub_dir.is_dir() or sub_dir.name.startswith("_"):
            continue
        sub_name = sub_dir.name
        sub_is_kw = keyword.iskeyword(sub_name)
        _rebuild_init_exports(sub_dir)
        for py_file in sorted(sub_dir.glob("*.py")):
            if py_file.name == "__init__.py":
                continue
            mod_name = py_file.stem
            if not mod_name.isidentifier():
                continue
            with open(py_file, encoding="utf-8") as f:
                for line in f:
                    if line.startswith("class "):
                        cls_name = (
                            line.split("(")[0].replace("class ", "").strip()
                        )
                        modules.append((
                            f"{sub_name}.{mod_name}",
                            cls_name,
                            sub_is_kw or keyword.iskeyword(mod_name),
                        ))
                        break

    if not modules:
        # Every component that was here has moved to another category,
        # so the old re-exports must go.
        (directory / "__init__.py").write_text(
            f'"""Generated {directory.name} components."""\n',
            encoding="utf-8",
            newline="\n",
        )
        return

    needs_importlib = any(il for _, _, il in modules)
    lines = [f'"""Generated {directory.name} components."""', ""]
    if needs_importlib:
        lines.append("import importlib")
        lines.append("")
    for mod_path, cls_name, is_il in modules:
        if is_il:
            full_mod = f"{pkg_name}.{mod_path}"
            lines.append(
                f'{cls_name} = importlib.import_module("{full_mod}").{cls_name}'
            )
        else:
            lines.append(f"from .{mod_path} import {cls_name}")
    lines.append("")

    (directory / "__init__.py").write_text(
        "\n".join(lines), encoding="utf-8", newline="\n",
    )


async def generate(
    port: int,
    host: str,
    component_type: str,
    dry_run: bool,
) -> None:
    """Connect to Resonite and generate component wrapper classes.

    Args:
        port: ResoniteLink server port.
        host: ResoniteLink server host.
        component_type: Fully qualified component type name.
        dry_run: If True, print generated source without writing.
    """
    resolink = client.Client()
    await resolink.connect(port, host)
    print(f"Connected to ws://{host}:{port}")

    generated: set[str] = set()
    all_type_defs: dict[str, dict[str, Any]] = {}
    type_def_cache: dict[str, dict[str, Any] | None] = {}

    # Clear the global interface cache so stale data from a previous
    # run doesn't carry over.
    _interface_cache.clear()
    _component_modules.clear()
    # Record where the existing components live, so that references to
    # them are imported from the right modules.
    _existing_component_types()

    await _generate_component(
        resolink, component_type, generated,
        all_type_defs, dry_run,
        type_def_cache,
    )

    if not dry_run:
        # Rebuild __init__.py re-exports for all category directories
        # under the generated tree so that short imports like
        # ``from pyresonitelink.protoflux.core import ValueInput``
        # stay up to date.
        nodes_dir = _GENERATED_DIR / "protoflux" / "runtimes" / "execution" / "nodes"
        if nodes_dir.is_dir():
            for cat_dir in sorted(nodes_dir.iterdir()):
                if cat_dir.is_dir() and not cat_dir.name.startswith("_"):
                    _rebuild_init_exports(cat_dir)
        data_dir = _GENERATED_DIR / "data"
        if data_dir.is_dir():
            _rebuild_init_exports(data_dir)
        enums_dir = _GENERATED_DIR / "_enums"
        if enums_dir.is_dir():
            _rebuild_init_exports(enums_dir)

    await resolink.close()


def _existing_component_types() -> list[str]:
    """Returns the COMPONENT_TYPE of every generated component module.

    Also records each module in ``_component_modules``, so that a
    component referencing one of them imports it from the right place
    even before it's regenerated.

    Returns:
        The fully qualified Resonite type names, in path order.
    """
    found: list[str] = []
    for path in sorted(_GENERATED_DIR.rglob("*.py")):
        rel_parts = path.relative_to(_GENERATED_DIR).parts
        if any(part.startswith("_") for part in rel_parts):
            continue
        text = path.read_text(encoding="utf-8")
        match = re.search(
            r'^    (?:COMPONENT_TYPE|_GENERIC_TYPE_TEMPLATE) = "([^"]+)"$',
            text,
            flags=re.MULTILINE,
        )
        class_match = re.search(r"^class (\w+)", text, flags=re.MULTILINE)
        if match and class_match:
            found.append(match.group(1))
            rel = path.relative_to(_GENERATED_DIR.parent.parent).with_suffix("")
            _component_modules[_arity_key(match.group(1))] = (
                ".".join(rel.parts), class_match.group(1),
            )
    return found


def _rebuild_all_init_exports() -> None:
    """Rebuilds the ``__init__.py`` re-exports of every generated package.

    Packages are rebuilt deepest first, since each ``__init__.py`` also
    re-exports its subpackages.
    """
    package_dirs = [
        path for path in _GENERATED_DIR.rglob("*")
        if path.is_dir()
        and "__pycache__" not in path.parts
        and not any(
            part.startswith("_")
            for part in path.relative_to(_GENERATED_DIR).parts
        )
    ]
    package_dirs.sort(key=lambda path: len(path.parts), reverse=True)
    for package_dir in package_dirs:
        _rebuild_init_exports(package_dir)
    _rebuild_init_exports(_GENERATED_DIR / "_enums")


async def generate_all(
    port: int,
    host: str,
    dry_run: bool,
) -> None:
    """Connect to Resonite and regenerate all components.

    Recursively walks all component categories on the server and
    generates wrapper classes for every component found.

    Args:
        port: ResoniteLink server port.
        host: ResoniteLink server host.
        dry_run: If True, print generated source without writing.
    """
    resolink = client.Client()
    await resolink.connect(port, host)
    print(f"Connected to ws://{host}:{port}")

    generated: set[str] = set()
    all_type_defs: dict[str, dict[str, Any]] = {}
    type_def_cache: dict[str, dict[str, Any] | None] = {}
    _interface_cache.clear()
    _component_modules.clear()

    # Recursively walk categories to find all component types
    async def walk_category(category_path: str) -> list[str]:
        """Return all component type names under a category."""
        resp = await resolink.request_json(
            messages.GetComponentTypeList(categoryPath=category_path),
        )
        types: list[str] = []
        for ct in cast(list[str], resp.get("componentTypes") or []):
            types.append(ct)
            if category_path.lstrip("/") not in _SKIP_CATEGORIES:
                walked_categories[ct] = category_path.lstrip("/")
        for sub in cast(list[str], resp.get("subcategories") or []):
            sub_path = f"{category_path}/{sub}" if category_path else f"/{sub}"
            types.extend(await walk_category(sub_path))
        return types

    walked_categories: dict[str, str] = {}
    print("Discovering component types...")
    all_types = await walk_category("")
    print(f"Found {len(all_types)} component types")
    # The category walk doesn't list every component. Components in the
    # Hidden category, for one, only turn up as reference targets. Those
    # generated earlier are regenerated too, so that none are left stale.
    listed = set(all_types)
    for existing in _existing_component_types():
        if existing not in listed:
            all_types.append(existing)
            listed.add(existing)
    print(f"Regenerating {len(all_types)} component types, "
          f"including those already generated")
    # Name every component and record its module before generating any,
    # so that the order of generation can't decide how a reference to a
    # component is imported.
    print("Assigning class names...")
    for ct in walked_categories:
        await _assign_class_names(resolink, ct)
    for ct, category in walked_categories.items():
        _avoid_namespace_clash(ct, category)
        _record_component_module(ct, category)

    errors = 0
    for i, comp_type in enumerate(all_types):
        try:
            await _generate_component(
                resolink, comp_type, generated,
                all_type_defs, dry_run,
                type_def_cache,
            )
        except Exception as e:
            errors += 1
            if errors <= 10:
                print(f"  Error generating {comp_type}: {e}")
            elif errors == 11:
                print("  (suppressing further errors)")
        if (i + 1) % 100 == 0:
            print(f"  Progress: {i + 1}/{len(all_types)} "
                  f"({len(generated)} generated, {errors} errors)")

    print(f"\nDone: {len(generated)} generated, {errors} errors")

    if not dry_run:
        _rebuild_all_init_exports()

    await resolink.close()


def main() -> None:
    """Run the gencode CLI tool."""
    parser = argparse.ArgumentParser(
        description=(
            "Generate component wrapper classes from a live "
            "ResoniteLink server"
        ),
    )
    parser.add_argument(
        "port", type=int, help="Port number for ResoniteLink connection"
    )
    parser.add_argument(
        "component",
        type=str,
        nargs="?",
        default=None,
        help=(
            "Fully qualified component type name, e.g. "
            '"[FrooxEngine]FrooxEngine.ValueField<>". '
            "Omit when using --all."
        ),
    )
    parser.add_argument(
        "--host", default="localhost", help="Host address (default: localhost)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print generated source without writing to disk",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Regenerate all components from the server",
    )

    args = parser.parse_args()

    if args.all:
        asyncio.run(
            generate_all(args.port, args.host, args.dry_run)
        )
    elif args.component:
        asyncio.run(
            generate(args.port, args.host, args.component, args.dry_run)
        )
    else:
        parser.error("Either provide a component name or use --all")


if __name__ == "__main__":
    main()
