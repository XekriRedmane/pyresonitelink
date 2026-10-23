"""Reads slots' transforms and converts between world and local space in Dergflux.

Each function takes a slot as a reference from dergflux.slots, or as a
workers.Slot, which is turned into one.

    ball = slots.ref(ball_slot)
    head = slots.ref(club_head_slot)
    # The ball's center in the club head's space.
    q = transform.global_point_to_local(head, transform.global_position(ball))

The functions read the slot whenever the flow evaluates them, so a value
read after g.SetGlobalPosition in the same impulse is the new one.

global_position, global_rotation, and global_scale are the outputs of one
GlobalTransform node per slot reference. The conversions use the
GlobalPointToLocal family of nodes. A point is moved, scaled, and rotated,
a direction is only rotated, and a vector is scaled and rotated.
"""

from typing import Any

from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.dergflux import _expr
from pyresonitelink.dergflux import slots

_MODULE = "protoflux.transform"


def _slot(slot: Any) -> _expr.ExprProxy:
    """Returns a slot expression for a slot, an ID, or a slot expression."""
    if isinstance(slot, (workers.Slot, str)):
        return slots.ref(slot)
    return _expr._coerce(slot)


def _global_transform(slot: Any, output: str, result_type: type) -> _expr.ExprProxy:
    """Returns an output of the GlobalTransform node of a slot expression.

    The outputs of one slot expression share one node. A workers.Slot
    makes a new expression each time, so a graph that reads a slot more
    than once should make one reference with slots.ref and pass that.
    """
    call = _slot(slot)._node.shared_call(_MODULE, "GlobalTransform", "Instance")
    return _expr.ExprProxy(_expr.NodeOutputNode(call, output, result_type))


def global_position(slot: Any) -> _expr.ExprProxy:
    """Returns a slot's position in world space, a Float3."""
    return _global_transform(slot, "GlobalPosition", primitives.Float3)


def global_rotation(slot: Any) -> _expr.ExprProxy:
    """Returns a slot's rotation in world space, a FloatQ."""
    return _global_transform(slot, "GlobalRotation", primitives.FloatQ)


def global_scale(slot: Any) -> _expr.ExprProxy:
    """Returns a slot's scale in world space, a Float3."""
    return _global_transform(slot, "GlobalScale", primitives.Float3)


def _convert(class_name: str, slot: Any, input_name: str, value: Any) -> _expr.ExprProxy:
    """Returns the output of a conversion node such as GlobalPointToLocal."""
    return _expr.node_output(
        {
            "Instance": _slot(slot),
            input_name: _expr.implicit(value, primitives.Float3, class_name),
        },
        primitives.Float3,
        module=_MODULE, class_name=class_name,
    )


def global_point_to_local(slot: Any, point: Any) -> _expr.ExprProxy:
    """Returns a point given in world space, in a slot's space."""
    return _convert("GlobalPointToLocal", slot, "GlobalPoint", point)


def local_point_to_global(slot: Any, point: Any) -> _expr.ExprProxy:
    """Returns a point given in a slot's space, in world space."""
    return _convert("LocalPointToGlobal", slot, "LocalPoint", point)


def global_direction_to_local(slot: Any, direction: Any) -> _expr.ExprProxy:
    """Returns a direction given in world space, rotated into a slot's space."""
    return _convert("GlobalDirectionToLocal", slot, "GlobalDirection", direction)


def local_direction_to_global(slot: Any, direction: Any) -> _expr.ExprProxy:
    """Returns a direction given in a slot's space, rotated into world space."""
    return _convert("LocalDirectionToGlobal", slot, "LocalDirection", direction)
