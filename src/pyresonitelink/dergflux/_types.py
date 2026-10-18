"""Type mapping and implicit conversions for Dergflux expressions.

Maps Python literal types to Resonite primitive types for automatic
type inference in expression trees, and decides which numeric types
convert to which without an explicit call. The rules are C#'s implicit
numeric conversions, which only widen: an int becomes a long, float, or
double, but a float never becomes an int without dergflux.math.convert.
"""

import datetime

from pyresonitelink.data import primitives

# Maps Python built-in types to their Resonite primitive equivalents.
PYTHON_TO_RESONITE: dict[type, type] = {
    int: primitives.Int,
    float: primitives.Float,
    bool: primitives.Bool,
    str: primitives.String,
    datetime.datetime: primitives.DateTime,
    datetime.timedelta: primitives.TimeSpan,
}

# C#'s implicit numeric conversions. Each type maps to the types it widens
# to, not including itself. decimal and char aren't Dergflux types.
_SCALAR_WIDENING: dict[type, tuple[type, ...]] = {
    primitives.SByte: (
        primitives.Short, primitives.Int, primitives.Long,
        primitives.Float, primitives.Double,
    ),
    primitives.Byte: (
        primitives.Short, primitives.UShort, primitives.Int, primitives.UInt,
        primitives.Long, primitives.ULong, primitives.Float, primitives.Double,
    ),
    primitives.Short: (
        primitives.Int, primitives.Long, primitives.Float, primitives.Double,
    ),
    primitives.UShort: (
        primitives.Int, primitives.UInt, primitives.Long, primitives.ULong,
        primitives.Float, primitives.Double,
    ),
    primitives.Int: (primitives.Long, primitives.Float, primitives.Double),
    primitives.UInt: (
        primitives.Long, primitives.ULong, primitives.Float, primitives.Double,
    ),
    primitives.Long: (primitives.Float, primitives.Double),
    primitives.ULong: (primitives.Float, primitives.Double),
    primitives.Float: (primitives.Double,),
}

# When two operands differ, they're converted to the first type in this
# order that both widen to. int and uint therefore meet at long, as in C#.
_NUMERIC_ORDER: tuple[type, ...] = (
    primitives.SByte, primitives.Byte, primitives.Short, primitives.UShort,
    primitives.Int, primitives.UInt, primitives.Long, primitives.ULong,
    primitives.Float, primitives.Double,
)

# Vector types by element type and dimension. A vector widens to the
# vector of the same dimension whose element type its own widens to, so
# int3 becomes float3.
_VECTORS: dict[type, tuple[type, int]] = {}
for _element, _prefix in (
    (primitives.SByte, "SByte"), (primitives.Byte, "Byte"),
    (primitives.Short, "Short"), (primitives.UShort, "UShort"),
    (primitives.Int, "Int"), (primitives.UInt, "UInt"),
    (primitives.Long, "Long"), (primitives.ULong, "ULong"),
    (primitives.Float, "Float"), (primitives.Double, "Double"),
):
    for _dim in (2, 3, 4):
        _VECTORS[getattr(primitives, f"{_prefix}{_dim}")] = (_element, _dim)
_VECTOR_BY_PARTS: dict[tuple[type, int], type] = {
    parts: vector for vector, parts in _VECTORS.items()
}


def type_name(resonite_type: type | None) -> str:
    """Returns a readable name for a Resonite type, for error messages.

    Args:
        resonite_type: A primitive type such as primitives.Int.

    Returns:
        e.g. "Int" or "Float3".
    """
    if resonite_type is None:
        return "an untyped value"
    for name in dir(primitives):
        if getattr(primitives, name) is resonite_type and name[:1].isupper():
            return name
    return getattr(resonite_type, "__name__", str(resonite_type))


def can_widen(source: type, target: type) -> bool:
    """Returns True if source converts to target without an explicit call.

    Args:
        source: The type of the value.
        target: The type it's needed as.

    Returns:
        True for the same type and for C#'s implicit numeric conversions,
        including element-wise ones between vectors of the same dimension.
    """
    if source == target:
        return True
    if source in _SCALAR_WIDENING:
        return target in _SCALAR_WIDENING[source]
    if source in _VECTORS and target in _VECTORS:
        source_element, source_dim = _VECTORS[source]
        target_element, target_dim = _VECTORS[target]
        return source_dim == target_dim and can_widen(source_element, target_element)
    return False


def common_type(left: type, right: type) -> type | None:
    """Returns the type that two operands of a binary operation convert to.

    Args:
        left: The left operand's type.
        right: The right operand's type.

    Returns:
        The narrowest type both widen to, or None if there's none. A long
        and a float meet at float, while a bool and an int never meet.
    """
    if left == right:
        return left
    if left in _VECTORS and right in _VECTORS:
        left_element, left_dim = _VECTORS[left]
        right_element, right_dim = _VECTORS[right]
        if left_dim != right_dim:
            return None
        element = common_type(left_element, right_element)
        if element is None:
            return None
        return _VECTOR_BY_PARTS.get((element, left_dim))
    for candidate in _NUMERIC_ORDER:
        if can_widen(left, candidate) and can_widen(right, candidate):
            return candidate
    return None


def literal_type(value: object) -> type | None:
    """Returns the Resonite type of a Python literal on its own.

    Args:
        value: A Python literal such as 3, 2.5, True, or "text".

    Returns:
        The type, or None for a value with no Resonite equivalent.
    """
    return PYTHON_TO_RESONITE.get(type(value))


def infer_result_type(
    left_type: type | None,
    right_type: type | None = None,
) -> type | None:
    """Infer the result type of a binary operation.

    Uses the left operand's type if available, otherwise the right's.
    Operands of different types are converted to their common type
    before this is called.

    Args:
        left_type: Type of the left operand.
        right_type: Type of the right operand.

    Returns:
        The inferred Resonite primitive type, or None.
    """
    if left_type is not None:
        return left_type
    return right_type


def resolve_const_type(value: object, context_type: type | None) -> type:
    """Resolve the Resonite type for a Python literal constant.

    Uses the context type (from the other operand) if available,
    otherwise maps from the Python type.

    Args:
        value: The Python literal value.
        context_type: Type of the other operand in the expression.

    Returns:
        The Resonite primitive type.
    """
    if context_type is not None:
        return context_type
    py_type = type(value)
    return PYTHON_TO_RESONITE.get(py_type, primitives.Float)
