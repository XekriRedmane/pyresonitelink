"""Reads dynamic variables from any slot in Dergflux expressions.

A Space's variables are read from the Space's own slot. read finds a
variable from a slot that the graph computes, such as the slot of the
collider that a raycast hit, so that each object can carry its own values.

    r = variables.read(slots.of_component(hit.hit_collider), "Physics/Friction",
                       primitives.Float)
    friction = dm.conditional(r.found, r.value, 0.5)

The path is "space/name". ProtoFlux looks for the nearest
DynamicVariableSpace with that space name on the slot or its ancestors
(DynamicVariableHelper.FindSpace), and then for the variable in that
space. A variable missing from the nearest such space isn't looked for in
spaces further up.
"""

import dataclasses

from pyresonitelink.data import primitives
from pyresonitelink.dergflux import _expr


@dataclasses.dataclass(frozen=True)
class DynamicRead:
    """Represents the outputs of a ReadDynamicValueVariable or ReadDynamicObjectVariable node.

    Attributes:
        value: The variable's value, or the type's default (0, false, the
            zero vector, or a null string) if it wasn't found.
        found: A Bool that is true if the variable was found.
    """

    value: _expr.ExprProxy
    found: _expr.ExprProxy


def read(source: object, path: str, value_type: type) -> DynamicRead:
    """Reads a dynamic variable of a value type or a string, looking for it from a slot.

    Uses ProtoFlux's ReadDynamicValueVariable<T>, or
    ReadDynamicObjectVariable<string> for a string, since a string is an
    object type in ProtoFlux. The object node reads a
    DynamicValueVariable<string>. The node reads the variable whenever
    the flow evaluates its outputs.

    Args:
        source: The slot to look from, as a Slot expression such as
            dergflux.slots.of_component(...).
        path: The variable's path, "space/name".
        value_type: The variable's type, such as primitives.Float or
            primitives.String. References aren't supported.

    Returns:
        The node's value and found outputs.
    """
    is_string = value_type is primitives.String
    call = _expr.NodeCall(
        {
            "Source": _expr._coerce(source)._node,
            "Path": _expr.ConstNode(path, primitives.String),
        },
        module="protoflux.variables.dynamic",
        class_name="ReadDynamicObjectVariable" if is_string else "ReadDynamicValueVariable",
        type_args=(value_type,),
    )
    return DynamicRead(
        value=_expr.ExprProxy(_expr.NodeOutputNode(call, "Value", value_type)),
        found=_expr.ExprProxy(_expr.NodeOutputNode(call, "FoundValue", primitives.Bool)),
    )
