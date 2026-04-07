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
from pathlib import Path
from typing import Any, cast

from pyresonitelink import client
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import messages
from pyresonitelink.data import workers
from pyresonitelink.generated._generator import (
    generate_component_source,
    generate_type_source,
    get_reference_target_types,
    _collect_referenced_types,
    _is_primitive_wire_name,
    _ref_stub_module_name,
    _simple_class_name,
    _to_module_path,
)

# Root of the generated package
_GENERATED_DIR = Path(__file__).resolve().parent.parent / "generated"


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
            init_path.write_text("")


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


async def _collect_component_interfaces(
    resolink: client.Client,
    component_type: str,
) -> list[str]:
    """Collect all interface type strings implemented by a component.

    Traces the component's base type chain via ``GetTypeDefinition``
    and collects every interface reported at each level.

    Args:
        resolink: Connected ResoniteLink client.
        component_type: Full Resonite component type name.

    Returns:
        List of full Resonite interface type strings (e.g.
        ``"[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<>"``).
    """
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

        resp = await resolink.request_json(
            messages.GetTypeDefinition(type=t)
        )
        if not resp.get("success"):
            continue
        type_def = cast(dict[str, Any], resp.get("definition", {}))

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

    return interfaces


async def _generate_type_hierarchy(
    resolink: client.Client,
    resonite_type: str,
    generated: set[str],
    all_type_defs: dict[str, dict[str, Any]],
    dry_run: bool,
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
    if (len(cls_name) <= 2 and cls_name.isupper()) or _is_primitive_wire_name(resonite_type):
        return
    generated.add(cls_name)

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
        print(f"  Warning: could not get type definition for {resonite_type}")
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
        if len(dep_cls) <= 2 and dep_cls.isupper():
            continue
        if dep_cls not in generated:
            await _generate_type_hierarchy(
                resolink, dep, generated, all_type_defs, dry_run,
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
            init_path.write_text("")
        output_path.write_text(source, encoding="utf-8")
        print(f"Wrote {output_path}")


async def _generate_component(
    resolink: client.Client,
    component_type: str,
    generated: set[str],
    all_type_defs: dict[str, dict[str, Any]],
    dry_run: bool,
) -> None:
    """Generate a component and recursively generate referenced types.

    Args:
        resolink: Connected ResoniteLink client.
        component_type: Full Resonite component type name.
        generated: Set of already-generated class names.
        all_type_defs: Accumulator for all fetched TypeDefinitions.
        dry_run: If True, print source instead of writing.
    """
    cls_name = _simple_class_name(component_type)
    if cls_name in generated:
        return
    generated.add(cls_name)

    # Get component definition
    def_resp = await resolink.request_json(
        messages.GetComponentDefinition(
            componentType=component_type, flattened=True
        )
    )
    if not def_resp.get("success"):
        print(f"Error: {def_resp.get('errorInfo')}")
        return

    definition = cast(dict[str, Any], def_resp.get("definition", {}))
    category = str(definition.get("categoryPath", ""))

    # Try to instantiate for concrete member types
    comp_data: dict[str, Any] | None = None
    is_generic = "<>" in component_type
    if not is_generic:
        slot_resp = await resolink.request_json(
            messages.AddSlot(
                data=workers.Slot(
                    parent=members.Reference(targetId="Root"),
                    name=fields.FieldString(value="__gencode_temp__"),
                )
            )
        )
        slot_id = cast(str, slot_resp.get("entityId"))

        add_resp = await resolink.request_json(
            messages.AddComponent(
                containerSlotId=slot_id,
                data=workers.Component(componentType=component_type),
            )
        )
        comp_id = add_resp.get("entityId")
        if isinstance(comp_id, str):
            comp_json = await resolink.request_json(
                messages.GetComponent(componentId=comp_id)
            )
            raw_data = comp_json.get("data")
            if isinstance(raw_data, dict):
                comp_data = cast(dict[str, Any], raw_data)

        await resolink.request_json(messages.RemoveSlot(slotId=slot_id))

    # Generate referenced types first
    ref_targets = get_reference_target_types(definition, comp_data)
    for target_type_str in ref_targets.values():
        for ref_base in _collect_referenced_types(target_type_str):
            ref_cls = _simple_class_name(ref_base)
            if ref_cls not in generated:
                # Try as component first
                check = await resolink.request_json(
                    messages.GetComponentDefinition(
                        componentType=ref_base, flattened=True
                    )
                )
                if check.get("success"):
                    await _generate_component(
                        resolink, ref_base, generated,
                        all_type_defs, dry_run,
                    )
                else:
                    await _generate_type_hierarchy(
                        resolink, ref_base, generated,
                        all_type_defs, dry_run,
                    )

    # Collect interfaces implemented by this component
    component_interfaces = await _collect_component_interfaces(
        resolink, component_type,
    )

    # Ensure interface types have _types/ stubs generated
    for iface_type in component_interfaces:
        for ref_base in _collect_referenced_types(iface_type):
            ref_cls = _simple_class_name(ref_base)
            if ref_cls not in generated:
                await _generate_type_hierarchy(
                    resolink, ref_base, generated,
                    all_type_defs, dry_run,
                )

    # Generate this component
    source = generate_component_source(
        component_type, definition, comp_data,
        interfaces=component_interfaces,
        all_type_defs=all_type_defs,
    )
    output_path = _output_path_for_component(component_type, category)

    if dry_run:
        print(f"\n--- {component_type} (category: {category}) ---")
        print(source)
    else:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        _ensure_init_files(output_path)
        output_path.write_text(source, encoding="utf-8")
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

    (directory / "__init__.py").write_text("\n".join(lines), encoding="utf-8")


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

    await _generate_component(
        resolink, component_type, generated,
        all_type_defs, dry_run,
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
        help=(
            "Fully qualified component type name, e.g. "
            '"[FrooxEngine]FrooxEngine.ValueField<>"'
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

    args = parser.parse_args()

    asyncio.run(
        generate(args.port, args.host, args.component, args.dry_run)
    )


if __name__ == "__main__":
    main()
