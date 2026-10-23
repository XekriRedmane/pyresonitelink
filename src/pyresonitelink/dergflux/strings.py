"""Strings in Dergflux expressions.

Strings join with +, which uses ProtoFlux's ConcatenateString. A number
or a vector becomes a string with to_string, and isn't converted
implicitly.

    s.log = s.log + strings.to_string(p.y) + "\\n"
"""

from typing import Any

from pyresonitelink.data import primitives
from pyresonitelink.dergflux import _expr
from pyresonitelink.dergflux import _types


def to_string(value: Any) -> _expr.ExprProxy:
    """Returns a value as a string.

    Uses ProtoFlux's ToString node for the value's type, such as
    ToString_Float, which formats with the invariant culture, so a float
    is written with a period and as few digits as read back to the same
    float. A string is returned unchanged.

    Args:
        value: An expression or a literal of a primitive type, such as
            Float, Int, Bool, or Float3.

    Raises:
        TypeError: The value has no type. An untyped None is one such value.
    """
    proxy = _expr._coerce(value)
    node = proxy._node
    value_type = node._type
    if value_type is None and isinstance(node, _expr.ConstNode):
        value_type = _types.literal_type(node.value)
        node._type = value_type
    if value_type is None:
        raise TypeError("to_string takes a value with a type.")
    if value_type is primitives.String:
        return proxy
    return _expr.node_output(
        {"V": proxy}, primitives.String,
        module="protoflux.strings", class_name=f"ToString_{_types.type_name(value_type)}",
    )
