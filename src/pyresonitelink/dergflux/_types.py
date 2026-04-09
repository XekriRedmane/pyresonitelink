"""Type mapping for Dergflux expressions.

Maps Python literal types to Resonite primitive types for automatic
type inference in expression trees.
"""

from pyresonitelink.data import primitives

# Maps Python built-in types to their Resonite primitive equivalents.
PYTHON_TO_RESONITE: dict[type, type] = {
    int: primitives.Int,
    float: primitives.Float,
    bool: primitives.Bool,
    str: primitives.String,
}


def infer_result_type(
    left_type: type | None,
    right_type: type | None = None,
) -> type | None:
    """Infer the result type of a binary operation.

    Uses the left operand's type if available, otherwise the right's.

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
