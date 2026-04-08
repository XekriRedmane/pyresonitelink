"""Code generator for component classes from ComponentDefinition data.

Takes the JSON definition returned by GetComponentDefinition and produces
a Python source file with a typed wrapper class.
"""

import json
import re
from pathlib import Path
from typing import Any

_DOCS_DIR = Path(__file__).resolve().parent / "docs"


def _load_wiki_docs(class_name: str) -> dict[str, Any] | None:
    """Load wiki documentation for a component if available.

    Args:
        class_name: The Python class name (PascalCase).

    Returns:
        Parsed docs dict or None if no docs file exists.
    """
    filename = _to_snake_case(class_name) + ".json"
    path = _DOCS_DIR / filename
    if not path.exists():
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None

# Wire-format primitive type names that should NOT generate stub classes.
# These are Resonite's built-in value types that already have Python
# representations in our type system.
_PRIMITIVE_WIRE_NAMES: frozenset[str] = frozenset({
    "bool", "byte", "sbyte", "short", "ushort", "int", "uint",
    "long", "ulong", "float", "double", "string", "Uri",
    "TimeSpan", "DateTime", "decimal", "char",
    "color", "colorX", "color32",
    "float2", "double2", "byte2", "ushort2", "uint2", "ulong2",
    "sbyte2", "short2", "int2", "long2", "bool2",
    "float3", "double3", "byte3", "ushort3", "uint3", "ulong3",
    "sbyte3", "short3", "int3", "long3", "bool3",
    "float4", "double4", "byte4", "ushort4", "uint4", "ulong4",
    "sbyte4", "short4", "int4", "long4", "bool4",
    "floatQ", "doubleQ",
    "float2x2", "double2x2", "float3x3", "double3x3",
    "float4x4", "double4x4",
    "Rect", "BoundingBox",
})


# Known primitive value type names that map directly to data $types.
# Maps: valueType.type from definition → (python_type_str, field_class, is_array)
# is_array is implicit: entries without [] are scalar fields, entries with []
# are array fields. The python_type_str for arrays is the element type.
_PRIMITIVE_FIELD_MAP: dict[str, tuple[str, str]] = {
    "bool": ("primitives.Bool", "FieldBool"),
    "byte": ("primitives.Byte", "FieldByte"),
    "sbyte": ("primitives.SByte", "FieldSbyte"),
    "short": ("primitives.Short", "FieldShort"),
    "ushort": ("primitives.UShort", "FieldUshort"),
    "int": ("primitives.Int", "FieldInt"),
    "uint": ("primitives.UInt", "FieldUint"),
    "long": ("primitives.Long", "FieldLong"),
    "ulong": ("primitives.ULong", "FieldUlong"),
    "float": ("primitives.Float", "FieldFloat"),
    "double": ("primitives.Double", "FieldDouble"),
    "decimal": ("Decimal", "FieldDecimal"),
    "char": ("primitives.Char", "FieldChar"),
    "string": ("primitives.String", "FieldString"),
    "Uri": ("str", "FieldUri"),
    "TimeSpan": ("str", "FieldTimeSpan"),
    "DateTime": ("str", "FieldDateTime"),
    # Composite primitives (vectors, colors, quaternions, matrices)
    "color": ("primitives.Color", "FieldColor"),
    "colorX": ("primitives.ColorX", "FieldColorX"),
    "color32": ("primitives.Color32", "FieldColor32"),
    "float2": ("primitives.Float2", "FieldFloat2"),
    "double2": ("primitives.Double2", "FieldDouble2"),
    "byte2": ("primitives.Byte2", "FieldByte2"),
    "ushort2": ("primitives.UShort2", "FieldUshort2"),
    "uint2": ("primitives.UInt2", "FieldUint2"),
    "ulong2": ("primitives.ULong2", "FieldUlong2"),
    "sbyte2": ("primitives.SByte2", "FieldSbyte2"),
    "short2": ("primitives.Short2", "FieldShort2"),
    "int2": ("primitives.Int2", "FieldInt2"),
    "long2": ("primitives.Long2", "FieldLong2"),
    "bool2": ("primitives.Bool2", "FieldBool2"),
    "float3": ("primitives.Float3", "FieldFloat3"),
    "double3": ("primitives.Double3", "FieldDouble3"),
    "byte3": ("primitives.Byte3", "FieldByte3"),
    "ushort3": ("primitives.UShort3", "FieldUshort3"),
    "uint3": ("primitives.UInt3", "FieldUint3"),
    "ulong3": ("primitives.ULong3", "FieldUlong3"),
    "sbyte3": ("primitives.SByte3", "FieldSbyte3"),
    "short3": ("primitives.Short3", "FieldShort3"),
    "int3": ("primitives.Int3", "FieldInt3"),
    "long3": ("primitives.Long3", "FieldLong3"),
    "bool3": ("primitives.Bool3", "FieldBool3"),
    "float4": ("primitives.Float4", "FieldFloat4"),
    "double4": ("primitives.Double4", "FieldDouble4"),
    "byte4": ("primitives.Byte4", "FieldByte4"),
    "ushort4": ("primitives.UShort4", "FieldUshort4"),
    "uint4": ("primitives.UInt4", "FieldUint4"),
    "ulong4": ("primitives.ULong4", "FieldUlong4"),
    "sbyte4": ("primitives.SByte4", "FieldSbyte4"),
    "short4": ("primitives.Short4", "FieldShort4"),
    "int4": ("primitives.Int4", "FieldInt4"),
    "long4": ("primitives.Long4", "FieldLong4"),
    "bool4": ("primitives.Bool4", "FieldBool4"),
    "floatQ": ("primitives.FloatQ", "FieldFloatQ"),
    "doubleQ": ("primitives.DoubleQ", "FieldDoubleQ"),
    "float2x2": ("primitives.Float2x2", "FieldFloat2x2"),
    "double2x2": ("primitives.Double2x2", "FieldDouble2x2"),
    "float3x3": ("primitives.Float3x3", "FieldFloat3x3"),
    "double3x3": ("primitives.Double3x3", "FieldDouble3x3"),
    "float4x4": ("primitives.Float4x4", "FieldFloat4x4"),
    "double4x4": ("primitives.Double4x4", "FieldDouble4x4"),
    # Geometry types
    "Rect": ("primitives.Rect", "FieldRect"),
    "BoundingBox": ("primitives.BoundingBox", "FieldBoundingBox"),
    # Nullable variants — wire format uses "type?" suffix.
    # The value can be None or the inner type.
    "bool?": ("primitives.Bool", "FieldNullableBool"),
    "byte?": ("primitives.Byte", "FieldNullableByte"),
    "sbyte?": ("primitives.SByte", "FieldNullableSbyte"),
    "short?": ("primitives.Short", "FieldNullableShort"),
    "ushort?": ("primitives.UShort", "FieldNullableUshort"),
    "int?": ("primitives.Int", "FieldNullableInt"),
    "uint?": ("primitives.UInt", "FieldNullableUint"),
    "long?": ("primitives.Long", "FieldNullableLong"),
    "ulong?": ("primitives.ULong", "FieldNullableUlong"),
    "float?": ("primitives.Float", "FieldNullableFloat"),
    "double?": ("primitives.Double", "FieldNullableDouble"),
    "TimeSpan?": ("str", "FieldNullableTimeSpan"),
    "DateTime?": ("str", "FieldNullableDateTime"),
    "color?": ("primitives.Color", "FieldNullableColor"),
    "colorX?": ("primitives.ColorX", "FieldNullableColorX"),
    "color32?": ("primitives.Color32", "FieldNullableColor32"),
    "float2?": ("primitives.Float2", "FieldNullableFloat2"),
    "double2?": ("primitives.Double2", "FieldNullableDouble2"),
    "float3?": ("primitives.Float3", "FieldNullableFloat3"),
    "double3?": ("primitives.Double3", "FieldNullableDouble3"),
    "float4?": ("primitives.Float4", "FieldNullableFloat4"),
    "double4?": ("primitives.Double4", "FieldNullableDouble4"),
    "floatQ?": ("primitives.FloatQ", "FieldNullableFloatQ"),
    "doubleQ?": ("primitives.DoubleQ", "FieldNullableDoubleQ"),
    # Array variants — wire format uses "type[]" suffix.
    # The python_type_str is the element type; the field class stores a list.
    "bool[]": ("primitives.Bool", "ArrayBool"),
    "byte[]": ("primitives.Byte", "ArrayByte"),
    "sbyte[]": ("primitives.SByte", "ArraySbyte"),
    "short[]": ("primitives.Short", "ArrayShort"),
    "ushort[]": ("primitives.UShort", "ArrayUshort"),
    "int[]": ("primitives.Int", "ArrayInt"),
    "uint[]": ("primitives.UInt", "ArrayUint"),
    "long[]": ("primitives.Long", "ArrayLong"),
    "ulong[]": ("primitives.ULong", "ArrayUlong"),
    "float[]": ("primitives.Float", "ArrayFloat"),
    "double[]": ("primitives.Double", "ArrayDouble"),
    "string[]": ("primitives.String", "ArrayString"),
    "Uri[]": ("str", "ArrayUri"),
    "TimeSpan[]": ("str", "ArrayTimeSpan"),
    "DateTime[]": ("str", "ArrayDateTime"),
    "color[]": ("primitives.Color", "ArrayColor"),
    "colorX[]": ("primitives.ColorX", "ArrayColorX"),
    "color32[]": ("primitives.Color32", "ArrayColor32"),
    "float2[]": ("primitives.Float2", "ArrayFloat2"),
    "double2[]": ("primitives.Double2", "ArrayDouble2"),
    "byte2[]": ("primitives.Byte2", "ArrayByte2"),
    "ushort2[]": ("primitives.UShort2", "ArrayUshort2"),
    "uint2[]": ("primitives.UInt2", "ArrayUint2"),
    "ulong2[]": ("primitives.ULong2", "ArrayUlong2"),
    "sbyte2[]": ("primitives.SByte2", "ArraySbyte2"),
    "short2[]": ("primitives.Short2", "ArrayShort2"),
    "int2[]": ("primitives.Int2", "ArrayInt2"),
    "long2[]": ("primitives.Long2", "ArrayLong2"),
    "bool2[]": ("primitives.Bool2", "ArrayBool2"),
    "float3[]": ("primitives.Float3", "ArrayFloat3"),
    "double3[]": ("primitives.Double3", "ArrayDouble3"),
    "byte3[]": ("primitives.Byte3", "ArrayByte3"),
    "ushort3[]": ("primitives.UShort3", "ArrayUshort3"),
    "uint3[]": ("primitives.UInt3", "ArrayUint3"),
    "ulong3[]": ("primitives.ULong3", "ArrayUlong3"),
    "sbyte3[]": ("primitives.SByte3", "ArraySbyte3"),
    "short3[]": ("primitives.Short3", "ArrayShort3"),
    "int3[]": ("primitives.Int3", "ArrayInt3"),
    "long3[]": ("primitives.Long3", "ArrayLong3"),
    "bool3[]": ("primitives.Bool3", "ArrayBool3"),
    "float4[]": ("primitives.Float4", "ArrayFloat4"),
    "double4[]": ("primitives.Double4", "ArrayDouble4"),
    "byte4[]": ("primitives.Byte4", "ArrayByte4"),
    "ushort4[]": ("primitives.UShort4", "ArrayUshort4"),
    "uint4[]": ("primitives.UInt4", "ArrayUint4"),
    "ulong4[]": ("primitives.ULong4", "ArrayUlong4"),
    "sbyte4[]": ("primitives.SByte4", "ArraySbyte4"),
    "short4[]": ("primitives.Short4", "ArrayShort4"),
    "int4[]": ("primitives.Int4", "ArrayInt4"),
    "long4[]": ("primitives.Long4", "ArrayLong4"),
    "bool4[]": ("primitives.Bool4", "ArrayBool4"),
    "floatQ[]": ("primitives.FloatQ", "ArrayFloatQ"),
    "doubleQ[]": ("primitives.DoubleQ", "ArrayDoubleQ"),
    "float2x2[]": ("primitives.Float2x2", "ArrayFloat2x2"),
    "double2x2[]": ("primitives.Double2x2", "ArrayDouble2x2"),
    "float3x3[]": ("primitives.Float3x3", "ArrayFloat3x3"),
    "double3x3[]": ("primitives.Double3x3", "ArrayDouble3x3"),
    "float4x4[]": ("primitives.Float4x4", "ArrayFloat4x4"),
    "double4x4[]": ("primitives.Double4x4", "ArrayDouble4x4"),
}

# Set of $type keys that are array types (use `values` instead of `value`)
_ARRAY_TYPES: frozenset[str] = frozenset(
    k for k in _PRIMITIVE_FIELD_MAP if k.endswith("[]")
)

# Maps data $type strings for non-field members to (member_class, module)
_MEMBER_CLASS_MAP: dict[str, tuple[str, str]] = {
    "reference": ("Reference", "members"),
    "list": ("SyncList", "members"),
    "syncObject": ("SyncObject", "members"),
    "enum": ("FieldEnum", "members"),
    "enum?": ("FieldEnum", "members"),
    "empty": ("EmptyElement", "members"),
    "playback": ("SyncPlayback", "members"),
    "dictionary": ("SyncDictionary", "members"),
    "dictionary<enum>": ("SyncDictionary", "members"),
}

# Python reserved words that need a trailing underscore
_PYTHON_KEYWORDS = frozenset({
    "and", "as", "assert", "async", "await", "break", "class", "continue",
    "def", "del", "elif", "else", "except", "finally", "for", "from",
    "global", "if", "import", "in", "is", "lambda", "nonlocal", "not",
    "or", "pass", "raise", "return", "try", "type", "while", "with", "yield",
    # Builtins that would shadow type annotations used in generated code
    "str", "int", "float", "bool", "bytes", "list", "dict", "set",
    "id", "input", "hash", "range", "slice", "format", "object",
    # Base class attribute that must not be overridden as a property
    "component",
})

# Base component members present on every component — skip in generated code
_BASE_MEMBERS = frozenset({"persistent", "UpdateOrder", "Enabled"})


# Known abbreviations that should be treated as indivisible tokens.
# Longer entries must come first so "ColorX" matches before "Color".
_ABBREVIATIONS: tuple[str, ...] = (
    "Color32", "ColorX",
    "UIX",
    "HSV", "HSL", "RGB",
    "URLs", "URL", "URI",
    "2D", "3D", "4D",
)

# Pre-compiled pattern: match any abbreviation.
_ABBREV_RE = re.compile(
    "|".join(re.escape(a) for a in _ABBREVIATIONS)
)


def _to_snake_case(name: str) -> str:
    """Convert PascalCase/camelCase to snake_case.

    Handles consecutive uppercase runs (acronyms) by keeping them
    grouped: "ActiveSessionURLs" -> "active_session_urls",
    "UIXButton" -> "uix_button".

    Known abbreviations (ColorX, HSV, RGB, UIX, etc.) are recognised
    and kept as single tokens.

    Args:
        name: The name to convert.

    Returns:
        The snake_case version.
    """
    # Phase 1: wrap known abbreviations in underscores so the generic
    # regex treats them as atomic.  Underscores act as explicit word
    # boundaries and are deduplicated at the end.
    result = _ABBREV_RE.sub(lambda m: "_" + m.group(0).lower() + "_", name)

    # Phase 2: generic PascalCase → snake_case conversion.
    # Split on boundaries between lowercase/digit and uppercase run
    result = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", result)
    # Split acronyms from following PascalCase word, but not from
    # trailing lowercase (plural s, etc.):
    result = re.sub(r"([A-Z]{2,})([A-Z][a-z]{2,})", r"\1_\2", result)
    result = result.lower()

    # Clean up: collapse multiple underscores, strip leading/trailing.
    result = re.sub(r"_+", "_", result).strip("_")
    return result


def _safe_python_name(name: str) -> str:
    """Convert a Resonite member name to a safe Python identifier.

    Handles Python keywords, dunder-prefix name mangling, and names
    starting with digits.

    Args:
        name: The Resonite member name (PascalCase or camelCase).

    Returns:
        A valid snake_case Python identifier.
    """
    py = _to_snake_case(name)
    if py in _PYTHON_KEYWORDS:
        py += "_"
    # Avoid double-underscore prefix (triggers Python name mangling)
    py = py.lstrip("_")
    if not py:
        py = "field"
    # Names can't start with a digit
    if py[0].isdigit():
        py = "f_" + py
    return py


def _to_class_name(component_type: str) -> str:
    """Extract a Python class name from a fully-qualified Resonite type.

    Strips assembly prefix, takes the last dotted segment, and removes
    generic arity markers like ``<>`` or ``<T>``.

    Args:
        component_type: e.g. "[FrooxEngine]FrooxEngine.ValueField<>"

    Returns:
        e.g. "ValueField"
    """
    name = re.sub(r"^\[.*?\]", "", component_type)
    name = name.rsplit(".", 1)[-1]
    # Remove generic markers: <>, <T>, <T1, T2>, etc.
    name = re.sub(r"<[^>]*>", "", name)
    return name


def _to_module_path(component_type: str) -> str:
    """Convert a component type to a relative module file path.

    Maps the namespace hierarchy (after the root namespace) to directories.
    e.g. "[FrooxEngine]FrooxEngine.Common.WorldLink" -> "common/world_link.py"
    Generic markers are stripped: "ValueField<>" -> "value_field.py"

    Args:
        component_type: Fully qualified type name.

    Returns:
        Relative path string.
    """
    name = re.sub(r"^\[.*?\]", "", component_type)
    # Strip generic markers before splitting
    name = re.sub(r"<[^>]*>", "", name)
    parts = name.split(".")
    if len(parts) > 1:
        parts = parts[1:]
    dirs = [_to_snake_case(p) for p in parts[:-1]]
    filename = _to_snake_case(parts[-1]) + ".py"
    if dirs:
        return "/".join(dirs) + "/" + filename
    return filename


def _reconstruct_type_string(type_ref: dict[str, Any]) -> str:
    """Reconstruct a full Resonite type string from a definition TypeReference.

    Handles generic arguments recursively, e.g.::

        {"type": "[FrooxEngine]FrooxEngine.IAssetProvider<>",
         "genericArguments": [{"type": "[FrooxEngine]FrooxEngine.AudioClip"}]}

    becomes ``"[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>"``.

    Args:
        type_ref: A TypeReference dict from the definition.

    Returns:
        The reconstructed type string.
    """
    base = type_ref.get("type", "")
    args = type_ref.get("genericArguments")
    if not args or "<>" not in base:
        return base
    arg_strs = [_reconstruct_type_string(a) for a in args if isinstance(a, dict)]
    return base.replace("<>", f"<{', '.join(arg_strs)}>")


def _extract_reference_target_type(
    member_name: str,
    data_members: dict[str, Any],
    def_members: dict[str, Any],
) -> str:
    """Extract the targetType string for a reference member.

    Prefers the data source (already a flat string), falls back to
    reconstructing from the definition TypeReference.

    Args:
        member_name: The member name.
        data_members: Members from GetComponent data.
        def_members: Members from GetComponentDefinition.

    Returns:
        The target type string, or empty string if not found.
    """
    # From data: targetType is a flat string
    if member_name in data_members:
        tt = data_members[member_name].get("targetType", "")
        if isinstance(tt, str) and tt:
            return tt

    # From definition: targetType is a TypeReference dict
    if member_name in def_members:
        mem_def = def_members[member_name]
        tt_ref = mem_def.get("targetType")
        if isinstance(tt_ref, dict):
            return _reconstruct_type_string(tt_ref)

    return ""


def _resolve_member_from_data(
    member_data: dict[str, Any],
) -> tuple[str, str, str, bool]:
    """Resolve member info from actual component data.

    Args:
        member_data: A single member dict from GetComponent response.

    Returns:
        (python_value_type, member_class, import_module, is_array).
        python_value_type is non-empty only for field types.
        is_array is True for array field types (use ``values`` not ``value``).
    """
    dtype = member_data.get("$type", "")

    if dtype in _PRIMITIVE_FIELD_MAP:
        py_type, field_cls = _PRIMITIVE_FIELD_MAP[dtype]
        return (py_type, field_cls, "fields", dtype in _ARRAY_TYPES)

    if dtype in _MEMBER_CLASS_MAP:
        cls, mod = _MEMBER_CLASS_MAP[dtype]
        return ("", cls, mod, False)

    return ("", "Member", "members", False)


def _resolve_member_from_definition(
    member_def: dict[str, Any],
) -> tuple[str, str, str, bool]:
    """Resolve member info from a ComponentDefinition member.

    The definition uses $type like "field", "reference", or "array" with
    nested valueType/targetType info. We map these to the concrete data types.

    Args:
        member_def: A member definition dict.

    Returns:
        (python_value_type, member_class, import_module, is_array).
    """
    dtype = member_def.get("$type", "")

    if dtype == "field":
        value_type = member_def.get("valueType", {})
        vt_name = value_type.get("type", "") if isinstance(value_type, dict) else ""

        # Handle Nullable<> wrapper: unwrap to get inner type, then
        # look up the nullable variant (e.g. "int" → "int?")
        if vt_name == "Nullable<>":
            generic_args = value_type.get("genericArguments") or []
            if generic_args and isinstance(generic_args[0], dict):
                inner_name = generic_args[0].get("type", "")
                nullable_name = inner_name + "?"
                if nullable_name in _PRIMITIVE_FIELD_MAP:
                    py_type, field_cls = _PRIMITIVE_FIELD_MAP[nullable_name]
                    return (py_type, field_cls, "fields", False)
                # Nullable enum
                return ("", "FieldEnum", "members", False)
            return ("", "Member", "members", False)

        if vt_name in _PRIMITIVE_FIELD_MAP:
            py_type, field_cls = _PRIMITIVE_FIELD_MAP[vt_name]
            return (py_type, field_cls, "fields", False)
        # Non-primitive field (enum, complex type) — treat as enum if
        # it's not a known primitive and not a generic parameter
        is_generic = value_type.get("isGenericParameter", False) if isinstance(value_type, dict) else False
        if is_generic:
            return ("", "Member", "members", False)
        # Likely an enum type
        return ("", "FieldEnum", "members", False)

    if dtype == "array":
        value_type = member_def.get("valueType", {})
        vt_name = value_type.get("type", "") if isinstance(value_type, dict) else ""
        array_name = vt_name + "[]"
        if array_name in _PRIMITIVE_FIELD_MAP:
            py_type, field_cls = _PRIMITIVE_FIELD_MAP[array_name]
            return (py_type, field_cls, "fields", True)
        return ("", "Member", "members", False)

    if dtype in _MEMBER_CLASS_MAP:
        cls, mod = _MEMBER_CLASS_MAP[dtype]
        return ("", cls, mod, False)

    return ("", "Member", "members", False)


def _is_generic_type(component_type: str) -> bool:
    """Check if a component type is a generic type definition.

    Args:
        component_type: e.g. "[FrooxEngine]FrooxEngine.ValueField<>"

    Returns:
        True if the type has an empty generic marker ``<>``.
    """
    return "<>" in component_type


def _is_generic_parameter(member_def: dict[str, Any]) -> bool:
    """Check if a definition member's value type is a generic parameter.

    Only returns True for field members whose valueType is itself a
    generic parameter (e.g. ``T``). Reference members with generic
    target types (e.g. ``INodeValueOutput<T>``) are NOT generic
    parameters — they are references that happen to have a
    parameterized target type.

    Args:
        member_def: A member definition dict from ComponentDefinition.

    Returns:
        True if the member is a field with a generic value type.
    """
    dtype = member_def.get("$type", "")
    if dtype == "field":
        vt = member_def.get("valueType", {})
        return isinstance(vt, dict) and vt.get("isGenericParameter", False)
    return False


def generate_component_source(
    component_type: str,
    definition: dict[str, Any],
    interfaces: list[str] | None = None,
    all_type_defs: dict[str, dict[str, Any]] | None = None,
) -> str:
    """Generate Python source code for a component wrapper class.

    Resolves member types from the definition's ``TypeReference``
    dicts, which include full generic arguments (e.g.
    ``INodeValueOutput<>`` with ``genericArguments: [{type: "float"}]``).

    For generic component types (those with ``<>``), generates a class
    inheriting from ``GenericComponent`` with ``_GENERIC_TYPE_TEMPLATE``
    set. Members whose type is a generic parameter get runtime-resolved
    properties that use ``self._type_info``.

    When *interfaces* are provided, the generated class inherits from
    the corresponding ``_types/`` stubs so that the type checker can
    verify wiring correctness (e.g. that a ``ValueAdd`` can be passed
    where ``INodeValueOutput[T]`` is expected).

    Args:
        component_type: The fully-qualified component type string.
        definition: The "definition" dict from ComponentDefinitionData.
        interfaces: Resonite interface type strings implemented by
            this component (collected from the type hierarchy).
        all_type_defs: All known TypeDefinitions (for MRO dedup).

    Returns:
        The Python source code as a string.
    """
    class_name = _to_class_name(component_type)
    category = definition.get("categoryPath", "")
    is_generic = _is_generic_type(component_type)

    data_members: dict[str, Any] = {}
    def_members = definition.get("members", {})

    # Union of all member names from both sources, preserving definition order
    all_member_names: list[str] = list(def_members.keys())
    for name in data_members:
        if name not in all_member_names:
            all_member_names.append(name)

    # Determine which members are generic-parameterized
    generic_members: set[str] = set()
    if is_generic:
        for name, mem_def in def_members.items():
            if _is_generic_parameter(mem_def):
                generic_members.add(name)

    # Resolve each member
    # (resonite_name, python_name, python_type, member_class, import_module,
    #  is_generic_param, is_array)
    member_infos: list[tuple[str, str, str, str, str, bool, bool]] = []
    imports_needed: set[str] = set()
    # For reference members: maps resonite_name -> targetType string
    ref_target_types: dict[str, str] = {}
    # For enum members: maps resonite_name -> full Resonite enum type string
    enum_types: dict[str, str] = {}
    for name, mem_def in def_members.items():
        if name in _BASE_MEMBERS:
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
                    enum_types[name] = vt_name

    for member_name in all_member_names:
        if member_name in _BASE_MEMBERS:
            continue

        is_gp = member_name in generic_members

        if is_gp:
            # Generic parameter member — resolved at runtime via _type_info
            py_name = _safe_python_name(member_name)
            member_infos.append(
                (member_name, py_name, "", "", "", True, False)
            )
            continue

        if member_name in data_members:
            info = _resolve_member_from_data(data_members[member_name])
        elif member_name in def_members:
            info = _resolve_member_from_definition(def_members[member_name])
        else:
            continue

        py_type, member_class, import_mod, is_arr = info
        py_name = _safe_python_name(member_name)
        member_infos.append(
            (member_name, py_name, py_type, member_class, import_mod, False,
             is_arr)
        )
        imports_needed.add(import_mod)

        # Extract targetType for reference members
        if member_class == "Reference":
            tt = _extract_reference_target_type(
                member_name, data_members, def_members
            )
            if tt:
                ref_target_types[member_name] = tt

    has_generic_members = any(gp for _, _, _, _, _, gp, _ in member_infos)

    # Pre-compute reference type info for imports and property annotations
    # Maps: resonite_name -> (annotation_str, module_name)
    ref_stub_imports: dict[str, tuple[str, str]] = {}
    # All type classes that need importing: (class_name, module_name)
    ref_stub_classes: list[tuple[str, str]] = []
    for res_name, tt in ref_target_types.items():
        ref_stub_imports[res_name] = (
            _ref_type_annotation(tt),
            _ref_stub_module_name(tt),
        )
        for ref_base in _collect_referenced_types(tt):
            cls = _simple_class_name(ref_base)
            # Skip generic parameter names (T, V, A, etc.)
            if len(cls) <= 2 and cls.isupper():
                continue
            mod = _ref_stub_module_name(ref_base)
            ref_stub_classes.append((cls, mod))

    # Check for sync methods
    sync_methods = definition.get("methods", [])
    has_sync_methods = bool(sync_methods)

    # Build source lines
    lines: list[str] = []
    lines.append(f'"""Generated component: {class_name}."""')
    lines.append("")

    # Check if imports are needed for member types or reference annotations
    ref_annotations = [ann for ann, _ in ref_stub_imports.values()]

    # Find generic type parameter names (E, S, U, etc.) used in
    # reference annotations that aren't provided by the base class.
    # For GenericComponent subclasses T is defined; all others need
    # to be aliased to Any.
    defined_params = {"T"} if is_generic else set()
    extra_type_params: set[str] = set()
    for ann in ref_annotations:
        for token in re.findall(r"\b([A-Z])\b", ann):
            if token not in defined_params:
                extra_type_params.add(token)

    # Collect Python type annotations used in sync method parameters
    # so we can check if np/primitives/Decimal imports are needed.
    method_param_types: list[str] = []
    for method_def in sync_methods:
        if not isinstance(method_def, dict):
            continue
        for _pname, ptype_ref in method_def.get("parameters", {}).items():
            if isinstance(ptype_ref, dict):
                py_prim = _primitive_python_name(ptype_ref.get("type", ""))
                if py_prim:
                    method_param_types.append(py_prim)

    needs_any = bool(extra_type_params)
    needs_np = (
        any(t.startswith("np.") for _, _, t, _, _, gp, _ in member_infos if not gp)
        or any("np." in a for a in ref_annotations)
        or any("np." in t for t in method_param_types)
    )
    needs_primitives = (
        any(t.startswith("primitives.") for _, _, t, _, _, gp, _ in member_infos if not gp)
        or any("primitives." in a for a in ref_annotations)
        or any("primitives." in t for t in method_param_types)
    )
    needs_decimal = (
        any(t == "Decimal" for _, _, t, _, _, gp, _ in member_infos if not gp)
        or any("Decimal" in a for a in ref_annotations)
        or any("Decimal" in t for t in method_param_types)
    )
    if needs_any or needs_np or needs_decimal:
        imports: list[str] = []
        if needs_decimal:
            imports.append("from decimal import Decimal")
        if needs_any:
            imports.append("from typing import Any")
        if needs_np:
            imports.append("import numpy as np")
        lines.extend(imports)
        lines.append("")
    # Alias undefined type params to Any so annotations are valid
    for param in sorted(extra_type_params):
        lines.append(f"{param} = Any")

    if "fields" in imports_needed:
        lines.append("from pyresonitelink.data import fields")
    if "members" in imports_needed:
        lines.append("from pyresonitelink.data import members")
    if needs_primitives:
        lines.append("from pyresonitelink.data import primitives")
    if has_sync_methods:
        lines.append("from pyresonitelink.data import protocols")

    # Import enum types used by this component
    enum_imports: dict[str, str] = {}  # python_class -> module_name
    for _ename, etype in enum_types.items():
        ecls = _simple_class_name(etype)
        emod = get_enum_module_name(etype)
        if ecls not in enum_imports:
            enum_imports[ecls] = emod
            lines.append(
                f"from pyresonitelink.generated._enums.{emod}"
                f" import {ecls}"
            )

    # workers is needed when __init__ is generated (for the
    # ``component: workers.Component`` parameter).  It is always needed
    # for generic components and for non-generic components that have
    # any init-able members (references, generic params, or scalar fields).
    needs_workers = is_generic or any(
        (
            is_gp
            or (mc == "Reference" and rn in ref_stub_imports)
            or (mc.startswith("Field") and not is_arr and pt)
        )
        for rn, _, pt, mc, _, is_gp, is_arr in member_infos
    )
    if needs_workers:
        lines.append("from pyresonitelink.data import workers")

    if is_generic:
        lines.append(
            "from pyresonitelink.generated._base import GenericComponent, T"
        )
        base_class = "GenericComponent[T]"
    else:
        lines.append(
            "from pyresonitelink.generated._base import GeneratedComponent"
        )
        base_class = "GeneratedComponent"

    # Import reference target stubs (from generated/_types/)
    seen_stubs: set[str] = set()
    for stub_cls, stub_mod in ref_stub_classes:
        if stub_cls and stub_mod and stub_cls not in seen_stubs:
            lines.append(
                f"from pyresonitelink.generated._types.{stub_mod}"
                f" import {stub_cls}"
            )
            seen_stubs.add(stub_cls)

    # Process implemented interfaces into base classes.
    # This enables type checkers to verify that a component can be
    # passed where an interface type is expected (e.g. ValueAdd
    # satisfies INodeValueOutput[T]).
    iface_bases: list[str] = []  # Python annotations for base classes
    if interfaces:
        # Build (class_name, annotation, module) for each interface
        iface_infos: list[tuple[str, str, str]] = []
        for iface_type in interfaces:
            iface_cls = _simple_class_name(iface_type)
            if not iface_cls or _is_primitive_wire_name(iface_type):
                continue
            if _is_generic_param_name(iface_cls):
                continue
            iface_mod = _to_snake_case(iface_cls)
            _, iface_args = _parse_target_type(iface_type)

            if iface_args or iface_type.endswith("<>"):
                # Generic interface — use [T] for generic components
                if is_generic:
                    annotation = f"{iface_cls}[T]"
                else:
                    annotation = _ref_type_annotation(iface_type)
                    if "<>" in annotation:
                        continue
            else:
                annotation = iface_cls

            iface_infos.append((iface_cls, annotation, iface_mod))

        # Deduplicate step 1: when both generic (IFoo[T]) and
        # non-generic (IFoo) versions of the same class exist, keep
        # only the generic version.  Also remove exact class name
        # duplicates (e.g. two non-generic IExecutionNode entries
        # from the generic and non-generic server reports).
        generic_cls_names: set[str] = set()
        for cls, ann, _ in iface_infos:
            if "[" in ann:
                generic_cls_names.add(cls)
        seen_cls: set[str] = set()
        deduped: list[tuple[str, str, str]] = []
        for cls, ann, mod in iface_infos:
            if cls in seen_cls:
                continue
            if "[" not in ann and cls in generic_cls_names:
                continue
            seen_cls.add(cls)
            deduped.append((cls, ann, mod))
        iface_infos = deduped

        # Deduplicate step 2: remove interfaces that are ancestors
        # of another interface in the list.  Uses all_type_defs to
        # compute the full ancestor set for each interface.
        all_iface_cls = {cls for cls, _, _ in iface_infos}
        ancestor_cls: set[str] = set()
        if all_type_defs:
            for cls in all_iface_cls:
                for anc in _get_all_ancestors(cls, all_type_defs):
                    if anc in all_iface_cls:
                        ancestor_cls.add(anc)

        keep = [
            (cls, ann, mod)
            for cls, ann, mod in iface_infos
            if cls not in ancestor_cls
        ]

        for cls, ann, mod in keep:
            if cls not in seen_stubs:
                lines.append(
                    f"from pyresonitelink.generated._types.{mod}"
                    f" import {cls}"
                )
                seen_stubs.add(cls)
            iface_bases.append(ann)

    # Build the full base class list
    all_bases = [base_class] + iface_bases
    bases_str = ", ".join(all_bases)

    lines.append("")
    lines.append("")

    # Load wiki documentation if available
    wiki_docs = _load_wiki_docs(class_name)

    # Class
    lines.append(f"class {class_name}({bases_str}):")
    if wiki_docs and wiki_docs.get("description"):
        lines.append(f'    """{wiki_docs["description"]}')
    else:
        lines.append(f'    """Wrapper for {component_type}.')
    if category:
        lines.append("")
        lines.append(f"    Category: {category}")
    if wiki_docs and wiki_docs.get("usage"):
        lines.append("")
        # Wrap usage text at ~72 chars with 4-space indent
        usage = wiki_docs["usage"]
        words = usage.split()
        usage_lines: list[str] = []
        current = "    "
        for word in words:
            if len(current) + len(word) + 1 > 76:
                usage_lines.append(current)
                current = "    " + word
            else:
                current += (" " if len(current) > 4 else "") + word
        if current.strip():
            usage_lines.append(current)
        lines.extend(usage_lines)
    if wiki_docs and wiki_docs.get("notes"):
        for note in wiki_docs["notes"]:
            lines.append("")
            lines.append(f"    **{note['title']}**: {note['text']}")
    if is_generic:
        lines.append("")
        lines.append(f"    Parameterize with a value type::")
        lines.append(f"")
        lines.append(f"        {class_name}[primitives.Float]")
        lines.append(f"        {class_name}[primitives.Float3]")
    lines.append('    """')
    lines.append("")
    lines.append(f'    COMPONENT_TYPE = "{component_type}"')
    if is_generic:
        lines.append(f'    _GENERIC_TYPE_TEMPLATE = "{component_type}"')
    lines.append("")

    # Generate __init__ with optional initial values for non-base members.
    # Collects: generic-param fields (typed T), references (typed
    # str | TargetType | None), and scalar fields (typed by their
    # Python value type).
    init_params: list[tuple[str, str, str]] = []
    # (python_name, type_annotation, resonite_name)
    for (res_name, py_name, py_type, member_class, import_mod,
         is_gp, is_arr) in member_infos:
        if is_gp:
            init_params.append((py_name, "T", res_name))
        elif member_class == "Reference" and res_name in ref_stub_imports:
            annotation, _ = ref_stub_imports[res_name]
            init_params.append(
                (py_name, f"str | {annotation}", res_name)
            )
        elif (
            member_class.startswith("Field")
            and not is_arr
            and py_type
        ):
            # Scalar field member (string, bool, int, float, etc.)
            init_params.append((py_name, py_type, res_name))
        elif member_class == "FieldEnum" and res_name in enum_types:
            # Enum member
            enum_cls = _simple_class_name(enum_types[res_name])
            init_params.append((py_name, f"{enum_cls} | str", res_name))

    # Deduplicate init params by Python name (different Resonite
    # members can map to the same snake_case name, e.g. a field
    # and a reference both named "PerObject" -> "per_object").
    seen_init_names: set[str] = set()
    deduped_params: list[tuple[str, str, str]] = []
    for pname, ptype, rname in init_params:
        if pname not in seen_init_names:
            seen_init_names.add(pname)
            deduped_params.append((pname, ptype, rname))
    init_params = deduped_params

    if init_params:
        # Build signature
        param_strs = [
            f"{pname}: {ptype} | None = None"
            for pname, ptype, _ in init_params
        ]
        sig = ", ".join(param_strs)
        lines.append(
            f"    def __init__(self, {sig}, *, "
            f"component: workers.Component | None = None) -> None:"
        )
        lines.append(f'        """Initialize with optional member values.')
        lines.append("")
        lines.append("        Args:")
        for pname, _, rname in init_params:
            lines.append(f"            {pname}: Initial value for {rname}.")
        lines.append(
            "            component: Existing Component to wrap."
        )
        lines.append('        """')
        lines.append("        super().__init__(component)")
        for pname, _, _ in init_params:
            lines.append(f"        if {pname} is not None:")
            lines.append(f"            self.{pname} = {pname}")
        lines.append("")

    # Properties
    for (res_name, py_name, py_type, member_class, import_mod,
         is_gp, is_arr) in member_infos:
        if is_gp:
            # Generic-parameter member: typed with T from Generic[T]
            lines.append(f"    @property")
            lines.append(f"    def {py_name}(self) -> T | None:")
            lines.append(f'        """The {res_name} field value (type depends on type parameter)."""')
            lines.append(f'        member = self.get_member("{res_name}")')
            lines.append(f"        if member is None:")
            lines.append(f"            return None")
            lines.append(f"        return getattr(member, 'value', None)")
            lines.append("")
            lines.append(f"    @{py_name}.setter")
            lines.append(f"    def {py_name}(self, value: T) -> None:")
            lines.append(f'        """Set the {res_name} field value."""')
            lines.append(f'        member = self.get_member("{res_name}")')
            lines.append(f"        if member is not None:")
            lines.append(f"            member.value = value  # type: ignore[attr-defined]")
            lines.append(
                f"        elif self._type_info is not None"
                f" and self._type_info.field_class is not None:"
            )
            lines.append(f"            self.set_member(")
            lines.append(
                f'                "{res_name}", self._type_info.field_class(value=value)'
            )
            lines.append(f"            )")
            lines.append("")
        elif is_arr and import_mod == "fields" and py_type:
            # Array field: property exposes the values list
            lines.append(f"    @property")
            lines.append(f"    def {py_name}(self) -> list[{py_type}] | None:")
            lines.append(f'        """The {res_name} array values."""')
            lines.append(f'        member = self.get_member("{res_name}")')
            lines.append(f"        if member is None:")
            lines.append(f"            return None")
            lines.append(f"        return getattr(member, 'values', None)")
            lines.append("")
            lines.append(f"    @{py_name}.setter")
            lines.append(f"    def {py_name}(self, value: list[{py_type}]) -> None:")
            lines.append(f'        """Set the {res_name} array values."""')
            lines.append(f'        member = self.get_member("{res_name}")')
            lines.append(f"        if member is not None:")
            lines.append(f"            member.values = value  # type: ignore[attr-defined]")
            lines.append(f"        else:")
            lines.append(f"            self.set_member(")
            lines.append(
                f'                "{res_name}", {import_mod}.{member_class}(values=value)'
            )
            lines.append(f"            )")
            lines.append("")
        elif import_mod == "fields" and py_type:
            # Scalar field: property exposes the value directly
            lines.append(f"    @property")
            lines.append(f"    def {py_name}(self) -> {py_type} | None:")
            field_doc = (
                wiki_docs.get("fields", {}).get(res_name, "")
                if wiki_docs else ""
            )
            if field_doc:
                lines.append(f'        """{field_doc}"""')
            else:
                lines.append(f'        """The {res_name} field value."""')
            lines.append(f'        member = self.get_member("{res_name}")')
            lines.append(f"        if member is None:")
            lines.append(f"            return None")
            lines.append(f"        return getattr(member, 'value', None)")
            lines.append("")
            lines.append(f"    @{py_name}.setter")
            lines.append(f"    def {py_name}(self, value: {py_type}) -> None:")
            lines.append(f'        """Set the {res_name} field value."""')
            lines.append(f'        member = self.get_member("{res_name}")')
            lines.append(f"        if member is not None:")
            lines.append(f"            member.value = value  # type: ignore[attr-defined]")
            lines.append(f"        else:")
            lines.append(f"            self.set_member(")
            lines.append(
                f'                "{res_name}", {import_mod}.{member_class}(value=value)'
            )
            lines.append(f"            )")
            lines.append("")
        elif member_class == "Reference" and res_name in ref_stub_imports:
            # Reference with known targetType: property exposes the target
            # ID, setter accepts ID string or a target stub/component.
            target_type = ref_target_types[res_name]
            annotation, _ = ref_stub_imports[res_name]

            lines.append(f"    @property")
            lines.append(f"    def {py_name}(self) -> str | None:")
            field_doc = (
                wiki_docs.get("fields", {}).get(res_name, "")
                if wiki_docs else ""
            )
            if field_doc:
                lines.append(f'        """{field_doc}"""')
            else:
                lines.append(
                    f'        """Target ID of the {res_name} reference '
                    f'(targets {annotation})."""'
                )
            lines.append(f'        member = self.get_member("{res_name}")')
            lines.append(
                f"        if isinstance(member, members.Reference):"
            )
            lines.append(f"            return member.targetId")
            lines.append(f"        return None")
            lines.append("")
            lines.append(f"    @{py_name}.setter")
            lines.append(
                f"    def {py_name}"
                f"(self, target: str | {annotation} | None) -> None:"
            )
            lines.append(
                f'        """Set the {res_name} reference by target ID '
                f'or {annotation} instance."""'
            )
            isinstance_cls = annotation.split("[")[0]
            if _is_generic_param_name(isinstance_cls):
                # Can't isinstance-check a TypeVar at runtime
                lines.append(
                    f"        target_id: str | None = "
                    f"target.id if hasattr(target, 'id') and not "
                    f"isinstance(target, str) "
                    f"else target  # type: ignore[union-attr,assignment]"
                )
            else:
                lines.append(
                    f"        target_id: str | None = "
                    f"target.id if isinstance(target, {isinstance_cls}) "
                    f"else target  # type: ignore[assignment]"
                )
            lines.append(f'        member = self.get_member("{res_name}")')
            lines.append(
                f"        if isinstance(member, members.Reference):"
            )
            lines.append(f"            member.targetId = target_id")
            lines.append(f"        else:")
            lines.append(f"            self.set_member(")
            lines.append(
                f'                "{res_name}",'
            )
            lines.append(
                f"                members.Reference("
                f"targetId=target_id,"
                f" targetType={target_type!r}),"
            )
            lines.append(f"            )")
            lines.append("")
        elif res_name in enum_types and member_class == "FieldEnum":
            # Enum member with a known enum type
            enum_cls = _simple_class_name(enum_types[res_name])
            field_doc = (
                wiki_docs.get("fields", {}).get(res_name, "")
                if wiki_docs else ""
            )
            lines.append(f"    @property")
            lines.append(f"    def {py_name}(self) -> {enum_cls} | None:")
            if field_doc:
                lines.append(f'        """{field_doc}"""')
            else:
                lines.append(f'        """The {res_name} enum value."""')
            lines.append(f'        member = self.get_member("{res_name}")')
            lines.append(
                f"        if isinstance(member, members.FieldEnum)"
                f" and member.value is not None:"
            )
            lines.append(f"            return {enum_cls}(member.value)")
            lines.append(f"        return None")
            lines.append("")
            lines.append(f"    @{py_name}.setter")
            lines.append(
                f"    def {py_name}"
                f"(self, value: {enum_cls} | str) -> None:"
            )
            if field_doc:
                lines.append(f'        """Set {res_name}. {field_doc}"""')
            else:
                lines.append(
                    f'        """Set the {res_name} enum value."""'
                )
            lines.append(f'        member = self.get_member("{res_name}")')
            lines.append(
                f"        if isinstance(member, members.FieldEnum):"
            )
            lines.append(f"            member.value = str(value)")
            lines.append(f"        else:")
            lines.append(f"            self.set_member(")
            lines.append(
                f'                "{res_name}",'
            )
            lines.append(
                f"                members.FieldEnum(value=str(value)),"
            )
            lines.append(f"            )")
            lines.append("")
        else:
            # Other non-field member (list, syncObject, playback, etc.)
            field_doc = (
                wiki_docs.get("fields", {}).get(res_name, "")
                if wiki_docs else ""
            )
            lines.append(f"    @property")
            lines.append(
                f"    def {py_name}(self) -> {import_mod}.{member_class} | None:"
            )
            if field_doc:
                lines.append(f'        """{field_doc}"""')
            else:
                lines.append(f'        """The {res_name} member."""')
            lines.append(f'        member = self.get_member("{res_name}")')
            lines.append(f"        if isinstance(member, {import_mod}.{member_class}):")
            lines.append(f"            return member")
            lines.append(f"        return None")
            lines.append("")
            lines.append(f"    @{py_name}.setter")
            lines.append(
                f"    def {py_name}"
                f"(self, value: {import_mod}.{member_class}) -> None:"
            )
            if field_doc:
                lines.append(f'        """Set {res_name}. {field_doc}"""')
            else:
                lines.append(f'        """Set the {res_name} member."""')
            lines.append(f'        self.set_member("{res_name}", value)')
            lines.append("")

    if not member_infos:
        lines.append("    pass")
        lines.append("")

    # Generate sync method wrappers from the definition's methods list.
    sync_methods = definition.get("methods", [])
    if sync_methods:
        # Group overloads by name (same name, different params)
        method_names_seen: set[str] = set()
        for method_def in sync_methods:
            if not isinstance(method_def, dict):
                continue
            method_name = method_def.get("name", "")
            if not method_name:
                continue
            py_method = _safe_python_name(method_name)
            params = method_def.get("parameters", {})
            return_type_ref = method_def.get("returnType", {})
            return_type = (
                return_type_ref.get("type", "void")
                if isinstance(return_type_ref, dict) else "void"
            )
            is_async_method = method_def.get("isAsync", False)

            # Build parameter list for the Python signature
            # Each param is name -> TypeReference dict
            py_params: list[str] = []
            call_args: list[str] = []
            for pname, ptype_ref in params.items():
                if isinstance(ptype_ref, dict):
                    ptype_str = ptype_ref.get("type", "")
                else:
                    ptype_str = str(ptype_ref)
                # Map Resonite type to Python annotation
                py_prim = _primitive_python_name(ptype_str)
                if py_prim:
                    py_ann = py_prim
                else:
                    # Reference types — accept str (ID)
                    py_ann = "str"
                safe_pname = _safe_python_name(pname)
                py_params.append(f"{safe_pname}: {py_ann}")
                call_args.append(f'"{pname}": {safe_pname}')

            # Handle overloads: append param count to avoid name clash
            if py_method in method_names_seen:
                py_method = f"{py_method}_{len(params)}"
            method_names_seen.add(py_method)

            # Build the method
            param_str = ", ".join(
                ["self", "resolink: protocols.ResoniteLinkClient"]
                + py_params
                + ["debug: bool = False"],
            )
            args_dict = "{" + ", ".join(call_args) + "}"

            method_doc = (
                wiki_docs.get("methods", {}).get(method_name, "")
                if wiki_docs else ""
            )
            lines.append(f"    async def {py_method}({param_str}) -> dict:")
            if method_doc:
                lines.append(f'        """{method_doc}')
            else:
                lines.append(
                    f'        """Call the {method_name} sync method.'
                )
            if params:
                lines.append("")
                lines.append("        Args:")
                lines.append(
                    "            resolink: Connected ResoniteLink client."
                )
                for pname in params:
                    lines.append(f"            {_safe_python_name(pname)}: "
                                 f"The {pname} parameter.")
                lines.append(
                    "            debug: Print request/response JSON."
                )
            lines.append("")
            lines.append("        Returns:")
            lines.append(
                "            The raw JSON response dict."
            )
            lines.append('        """')
            lines.append(
                f"        return await self.call_method("
            )
            lines.append(
                f'            resolink, "{method_name}", '
                f"{args_dict}, debug,"
            )
            lines.append(f"        )")
            lines.append("")

    return "\n".join(lines) + "\n"


def _simple_class_name(resonite_type: str) -> str:
    """Extract a simple class name from a Resonite type, stripping generics.

    Handles C# nested type separators (``+``): ``"Outer+Inner"`` →
    ``"Inner"``.

    Args:
        resonite_type: e.g. ``"[FrooxEngine]FrooxEngine.IAssetProvider<...>"``

    Returns:
        e.g. ``"IAssetProvider"``
    """
    name = re.sub(r"\[.*?\]", "", resonite_type)
    name = name.rsplit(".", 1)[-1]
    name = re.sub(r"<.*", "", name)
    # C# nested type separator: take the innermost name
    if "+" in name:
        name = name.rsplit("+", 1)[-1]
    return name


def _parse_target_type(resonite_type: str) -> tuple[str, list[str]]:
    """Parse a Resonite type string into base type and generic arguments.

    Args:
        resonite_type: e.g.
            ``"[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>"``

    Returns:
        Tuple of (full base type with ``<>`` stripped,
        list of full generic argument type strings).
        For non-generic types, the list is empty.
    """
    # Handle empty generic marker <> — strip it and return no args
    if resonite_type.endswith("<>"):
        return (resonite_type[:-2], [])
    # Match outermost < > (handles one level of nesting)
    m = re.match(r"^(.+?)<(.+)>$", resonite_type)
    if not m:
        return (resonite_type, [])
    base = m.group(1)
    # Split args on commas not inside < >
    args_str = m.group(2)
    args: list[str] = []
    depth = 0
    current: list[str] = []
    for ch in args_str:
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
        elif ch == "," and depth == 0:
            arg = "".join(current).strip()
            if arg:
                args.append(arg)
            current = []
            continue
        current.append(ch)
    if current:
        arg = "".join(current).strip()
        if arg:
            args.append(arg)
    return (base, args)


def _primitive_python_name(wire_name: str) -> str | None:
    """Map a primitive wire name to its Python annotation string.

    Handles nullable variants (e.g. ``"bool?"`` → ``"bool | None"``).

    Args:
        wire_name: A primitive wire name like ``"float"``, ``"float2"``,
            or ``"bool?"``.

    Returns:
        Python annotation string, or None if not a known primitive.
    """
    bare = wire_name.rstrip("?")
    is_nullable = bare != wire_name
    if bare not in _PRIMITIVE_WIRE_NAMES:
        return None
    # Look up in the field map for the Python type string
    entry = _PRIMITIVE_FIELD_MAP.get(bare)
    if entry:
        py_type = entry[0]  # e.g. "primitives.Float" or "primitives.Float3"
        return f"{py_type} | None" if is_nullable else py_type
    return None


def _ref_type_annotation(resonite_type: str) -> str:
    """Produce the Python type annotation string for a reference target.

    Recursively maps Resonite type strings to Python annotations:
    ``"INodeValueOutput<float>"`` → ``"INodeValueOutput[primitives.Float]"``.
    ``"IAssetProvider<AudioClip>"`` → ``"IAssetProvider[AudioClip]"``.
    ``"INodeObjectOutput<IAssetProvider<AudioClip>>"``
        → ``"INodeObjectOutput[IAssetProvider[AudioClip]]"``.

    Non-generic types return just the class name: ``"Slot"``.

    Args:
        resonite_type: Full Resonite type string.

    Returns:
        Python annotation string.
    """
    # Check if the whole type is a primitive (including nullable)
    simple = _simple_class_name(resonite_type)
    py_prim = _primitive_python_name(simple)
    if py_prim:
        return py_prim

    # Single-letter uppercase names are generic type parameters.
    # Use "Any" unless the caller has T defined (handled separately
    # for GenericComponent subclasses).
    if _is_generic_param_name(resonite_type):
        return simple

    base, args = _parse_target_type(resonite_type)
    base_cls = _simple_class_name(base)
    if not args:
        return base_cls
    # Recurse into each generic argument
    arg_names: list[str] = []
    for a in args:
        arg_names.append(_ref_type_annotation(a))
    return f"{base_cls}[{', '.join(arg_names)}]"


def _ref_stub_module_name(resonite_type: str) -> str:
    """Module filename (without .py) for a reference target stub.

    Args:
        resonite_type: Full Resonite type string (no generic args).

    Returns:
        snake_case module name.
    """
    return _to_snake_case(_simple_class_name(resonite_type))


def _is_primitive_wire_name(resonite_type: str) -> bool:
    """Check if a Resonite type string is a known primitive value type.

    Args:
        resonite_type: Full or simple Resonite type name.

    Returns:
        True if this is a primitive that already exists in our type system.
    """
    simple = _simple_class_name(resonite_type)
    # Check the simple name against known wire names (case-sensitive).
    # Nullable variants (e.g. "bool?") are also primitives.
    bare = simple.rstrip("?")
    return (
        simple in _PRIMITIVE_WIRE_NAMES
        or bare in _PRIMITIVE_WIRE_NAMES
        or resonite_type in _PRIMITIVE_WIRE_NAMES
    )


def _is_generic_param_name(name: str) -> bool:
    """Check if a name looks like a generic type parameter (T, V, A, etc.).

    Args:
        name: A type name string.

    Returns:
        True if this is likely a generic type parameter name.
    """
    simple = _simple_class_name(name) if "[" in name or "." in name else name
    return len(simple) <= 2 and simple.isupper()


def _collect_referenced_types(resonite_type: str) -> list[str]:
    """Collect all non-primitive base types mentioned in a Resonite type string.

    Decomposes generic types into their base and arguments recursively.
    Skips types that are known primitives (float, int, float3, etc.)
    or generic parameter names (T, V, A) since those already exist
    in the Python type system.

    Args:
        resonite_type: Full Resonite type string.

    Returns:
        List of full Resonite base type strings (no generic args),
        excluding primitives and generic parameter names.
    """
    base, args = _parse_target_type(resonite_type)
    result: list[str] = []
    if not _is_primitive_wire_name(base) and not _is_generic_param_name(base):
        result.append(base)
    for arg in args:
        if arg and not _is_generic_param_name(arg):
            result.extend(_collect_referenced_types(arg))
    return result


def _get_all_ancestors(
    type_name: str,
    all_type_defs: dict[str, dict[str, Any]],
    visited: set[str] | None = None,
) -> set[str]:
    """Get all ancestor class names of a type (base types + interfaces).

    Args:
        type_name: Resonite class name (simple, no namespace).
        all_type_defs: All known TypeDefinitions.
        visited: Cycle guard.

    Returns:
        Set of ancestor simple class names.
    """
    if visited is None:
        visited = set()
    if type_name in visited:
        return set()
    visited.add(type_name)

    result: set[str] = set()
    # Find the type def by matching simple name
    td = None
    for fn, d in all_type_defs.items():
        if _simple_class_name(fn) == type_name:
            td = d
            break
    if td is None:
        return result

    # Base type
    base_ref = td.get("baseType")
    if isinstance(base_ref, dict):
        base_cls = _simple_class_name(base_ref.get("type", ""))
        if base_cls and base_cls != type_name:
            result.add(base_cls)
            result |= _get_all_ancestors(base_cls, all_type_defs, visited)

    # Interfaces
    for iface in (td.get("interfaces") or []):
        if isinstance(iface, dict):
            iface_cls = _simple_class_name(iface.get("type", ""))
            if iface_cls and iface_cls != type_name:
                result.add(iface_cls)
                result |= _get_all_ancestors(
                    iface_cls, all_type_defs, visited
                )

    return result


def generate_type_source(
    type_def: dict[str, Any],
    all_type_defs: dict[str, dict[str, Any]],
) -> str:
    """Generate Python source for a Resonite type from its TypeDefinition.

    Produces a class with proper base classes, generic parameters, and
    interface implementations based on the type definition from the server.

    Args:
        type_def: The TypeDefinition dict from GetTypeDefinition.
        all_type_defs: All TypeDefinitions collected so far, keyed by
            full type name. Used to check which types exist for imports.

    Returns:
        Python source code string.
    """
    full_name = type_def.get("fullTypeName", "")
    class_name = _simple_class_name(full_name)
    is_interface = type_def.get("isInterface", False)
    is_abstract = type_def.get("isAbstract", False)
    is_generic_def = type_def.get("isGenericTypeDefinition", False)
    generic_params = type_def.get("genericParameters") or []

    # Collect base classes (base type + interfaces)
    bases: list[str] = []
    bases_class_names: set[str] = set()  # track to avoid duplicate bases
    imports: list[str] = []
    imported_names: set[str] = set()

    def _add_import(type_str: str) -> str | None:
        """Add an import for a type and return its class name."""
        cls = _simple_class_name(type_str)
        if cls == class_name:
            return None  # skip self-references
        mod = _to_snake_case(cls)
        if cls not in imported_names:
            imports.append(
                f"from pyresonitelink.generated._types.{mod} import {cls}"
            )
            imported_names.add(cls)
        return cls

    # Base type
    base_type_ref = type_def.get("baseType")
    if isinstance(base_type_ref, dict):
        base_type_str = base_type_ref.get("type", "")
        if base_type_str:
            base_base, base_args = _parse_target_type(base_type_str)
            base_cls = _add_import(base_base)
            if base_cls and base_cls not in bases_class_names:
                bases_class_names.add(base_cls)
                if base_args:
                    arg_names: list[str] = []
                    for a in base_args:
                        a_base, _ = _parse_target_type(a)
                        a_cls = _simple_class_name(a_base)
                        is_generic_param = any(
                            p.get("name") == a_cls for p in generic_params
                        )
                        if not is_generic_param:
                            _add_import(a_base)
                        arg_names.append(a_cls)
                    bases.append(f"{base_cls}[{', '.join(arg_names)}]")
                else:
                    bases.append(base_cls)

    # Compute ancestors already reachable through the base type so we
    # can skip redundant interfaces (the server lists ALL interfaces,
    # including inherited ones, which causes MRO conflicts in Python).
    already_inherited: set[str] = set()
    for b in bases:
        # Extract the class name from "Foo" or "Foo[Bar]"
        b_cls = b.split("[")[0]
        already_inherited |= _get_all_ancestors(
            b_cls, all_type_defs
        )

    # Also collect all listed interface names so we can skip interfaces
    # that are ancestors of other listed interfaces
    raw_iface_names: list[str] = []
    for iface in (type_def.get("interfaces") or []):
        if isinstance(iface, dict):
            raw_iface_names.append(
                _simple_class_name(iface.get("type", ""))
            )

    # An interface is redundant if it's an ancestor of any other
    # listed interface
    redundant: set[str] = set(already_inherited)
    for iname in raw_iface_names:
        ancestors = _get_all_ancestors(iname, all_type_defs)
        redundant |= ancestors

    # Interfaces — only include non-redundant ones
    for iface in (type_def.get("interfaces") or []):
        if not isinstance(iface, dict):
            continue
        iface_type = iface.get("type", "")
        iface_base, iface_args = _parse_target_type(iface_type)
        iface_cls_name = _simple_class_name(iface_base)
        if iface_cls_name in redundant:
            continue
        iface_cls = _add_import(iface_base)
        if iface_cls and iface_cls not in bases_class_names:
            bases_class_names.add(iface_cls)
            if iface_args:
                iarg_names: list[str] = []
                for a in iface_args:
                    a_base, _ = _parse_target_type(a)
                    a_cls = _simple_class_name(a_base)
                    is_gp = any(
                        p.get("name") == a_cls for p in generic_params
                    )
                    if not is_gp:
                        _add_import(a_base)
                    iarg_names.append(a_cls)
                bases.append(f"{iface_cls}[{', '.join(iarg_names)}]")
            else:
                bases.append(iface_cls)

    # Generic parameters
    typevars: list[tuple[str, str | None]] = []  # (name, bound_cls or None)
    if is_generic_def and generic_params:
        for param in generic_params:
            pname = param.get("name", "T")
            bound: str | None = None
            constraint_types = param.get("types") or []
            for ct in constraint_types:
                if not isinstance(ct, dict):
                    continue
                ct_type = ct.get("type", "")
                ct_base, ct_args = _parse_target_type(ct_type)
                # Skip self-referential constraints
                ct_cls = _simple_class_name(ct_base)
                is_self_ref = False
                if ct_args:
                    for ca in ct_args:
                        if _simple_class_name(ca) == pname:
                            is_self_ref = True
                            break
                if is_self_ref:
                    continue
                imported = _add_import(ct_base)
                if imported:
                    bound = imported
                    break  # use first non-self-referential constraint
            typevars.append((pname, bound))

    # Build source
    lines: list[str] = []
    lines.append(f'"""Generated type: {class_name}."""')
    lines.append("")

    # typing imports
    typing_names: list[str] = []
    if typevars:
        typing_names.append("Generic")
        typing_names.append("TypeVar")
    if typing_names:
        lines.append(f"from typing import {', '.join(typing_names)}")
        lines.append("")

    # Type imports
    for imp in imports:
        lines.append(imp)
    if imports:
        lines.append("")

    # TypeVar declarations — bounds are omitted because these are stub
    # types used for isinstance checks and annotations.  Keeping bounds
    # causes false-positive mypy errors in generated component code
    # where a component's own T (unbounded) is passed to a bounded
    # generic type stub.
    for pname, _bound in typevars:
        lines.append(f"{pname} = TypeVar('{pname}')")
    if typevars:
        lines.append("")

    if typevars or imports:
        lines.append("")

    # Class declaration
    all_bases = list(bases)
    if typevars:
        tv_names = ", ".join(p for p, _ in typevars)
        all_bases.append(f"Generic[{tv_names}]")

    if all_bases:
        bases_str = ", ".join(all_bases)
        lines.append(f"class {class_name}({bases_str}):")
    else:
        lines.append(f"class {class_name}:")

    # Docstring
    kind = "Interface" if is_interface else ("Abstract class" if is_abstract else "Class")
    lines.append(f'    """{kind}: {full_name}."""')
    lines.append("")

    # Add id property on root types (no bases) so they can be used
    # as reference targets.  Declared as a property (not a plain
    # attribute) to be compatible with GeneratedComponent.id which
    # is also a property — plain attributes conflict with properties
    # in multiple inheritance.
    if not bases:
        lines.append("    @property")
        lines.append("    def id(self) -> str | None:")
        lines.append('        """The element\'s unique ID."""')
        lines.append("        return None")
        lines.append("")

    return "\n".join(lines) + "\n"


def generate_enum_source(enum_definition: dict[str, Any]) -> str:
    """Generate a Python StrEnum class from an enum definition.

    Args:
        enum_definition: The "definition" dict from GetEnumDefinition.

    Returns:
        Python source code for the enum class.
    """
    type_info = enum_definition.get("type", {})
    full_name = type_info.get("fullTypeName", "")
    class_name = _simple_class_name(full_name)
    values = enum_definition.get("values", {})
    is_flags = enum_definition.get("isFlags", False)

    lines: list[str] = []
    lines.append(f'"""Generated enum: {class_name}."""')
    lines.append("")
    if is_flags:
        lines.append("from enum import Flag")
        lines.append("")
        lines.append("")
        lines.append(f"class {class_name}(Flag):")
    else:
        lines.append("from enum import StrEnum")
        lines.append("")
        lines.append("")
        lines.append(f"class {class_name}(StrEnum):")
    lines.append(f'    """Enum: {full_name}."""')
    lines.append("")

    if not values:
        lines.append("    pass")
    else:
        for name, int_val in values.items():
            safe_name = _safe_python_name(name)
            if is_flags:
                lines.append(f"    {safe_name} = {int_val}")
            else:
                lines.append(f'    {safe_name} = "{name}"')
    lines.append("")

    return "\n".join(lines) + "\n"


def get_enum_module_name(resonite_type: str) -> str:
    """Get the module filename for an enum type.

    Args:
        resonite_type: Full Resonite enum type string.

    Returns:
        Snake_case module name (without .py).
    """
    return _to_snake_case(_simple_class_name(resonite_type))


def get_reference_target_types(
    definition: dict[str, Any],
    component_data: dict[str, Any] | None = None,
) -> dict[str, str]:
    """Extract all reference target types from a component.

    Args:
        definition: The definition dict from ComponentDefinitionData.
        component_data: Deprecated, ignored. Kept for backward
            compatibility.

    Returns:
        Mapping of member name to target type string for all reference
        members that have a known target type.
    """
    def_members = definition.get("members", {})

    result: dict[str, str] = {}
    for name, mem_def in def_members.items():
        if name in _BASE_MEMBERS:
            continue
        if mem_def.get("$type") == "reference":
            tt = _extract_reference_target_type(name, {}, def_members)
            if tt:
                result[name] = tt

    return result
