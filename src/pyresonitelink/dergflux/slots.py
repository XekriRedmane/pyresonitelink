"""Slots and components as values in Dergflux expressions.

A slot that a graph reads or moves is given to it as a reference. ref
makes the reference from a slot, and of_component finds the slot that a
component is on, such as the collider that a raycast hit.

    from pyresonitelink.dergflux import slots
    from pyresonitelink.dergflux import transform

    ball = slots.ref(ball_slot)
    with g.Under(graph_slot):
        g.SetGlobalPosition(ball, transform.global_position(ball) + (0, 0.01, 0))

The values are object types in ProtoFlux, so the only things to do with
them are to pass them to nodes that take them, to compare them with ==
and !=, and to test them with math.is_null. Their Python types are the
generated stubs, such as ICollider, and workers.Slot for a slot.
"""

from typing import Any

from pyresonitelink.data import workers
from pyresonitelink.dergflux import _expr
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types import icomponent

SLOT_TYPE = "[FrooxEngine]FrooxEngine.Slot"

# ObjectCast<I, O> converts a reference to a component of one type into a
# reference of another. GetSlot takes an IComponent, and a node output
# such as RaycastOne's HitCollider has a narrower type, which ProtoFlux
# doesn't accept in its place.
_OBJECT_CAST = (
    "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes."
    "Casts.ObjectCast<{source},{target}>"
)


def ref(slot: workers.Slot | str) -> _expr.ExprProxy:
    """Returns a reference to a slot, for the inputs of nodes that take one.

    The graph holds the reference in a RefObjectInput<Slot> node, and the
    builder adds one such node for each slot however often it is used.

    Args:
        slot: The slot, as a Slot or its ID.
    """
    slot_id = slot if isinstance(slot, str) else slot.id
    assert slot_id is not None, "The slot has no ID. Add it to the world first."
    return _expr.ExprProxy(_expr.ElementRefNode(slot_id, SLOT_TYPE, workers.Slot))


def component_ref(component: GeneratedComponent) -> _expr.ExprProxy:
    """Returns a reference to a component, for the inputs of nodes that take one.

    The reference has the type IComponent, which nodes such as GetSlot
    take. A node whose input has a narrower type, such as IsGrabbableGrabbed's
    IGrabbable, has a function of its own that makes its reference.

    Args:
        component: The component, already added to a slot.
    """
    assert component.id is not None, "Add the component to a slot first."
    return _expr.ExprProxy(_expr.ElementRefNode(
        component.id, icomponent.IComponent.RESONITE_TYPE, icomponent.IComponent,
    ))


def of_component(component: Any) -> _expr.ExprProxy:
    """Returns the slot that a component is on.

    Uses ProtoFlux's GetSlot node. A component of a narrower type than
    IComponent, such as RaycastOne's hit_collider, passes through an
    ObjectCast node first.

    Args:
        component: The component, as an expression such as
            r.hit_collider, or as a component already added to a slot.

    Returns:
        The slot, a workers.Slot expression. It is null if the component
        is null, for example on a raycast that missed.
    """
    if isinstance(component, GeneratedComponent):
        component = component_ref(component)
    node = _expr._coerce(component)._node
    source = node._type
    if source is not None and source is not icomponent.IComponent:
        source_name = getattr(source, "RESONITE_TYPE", None)
        if source_name is None:
            raise TypeError(f"of_component takes a component, not {source.__name__}.")
        component = _expr.node_output(
            {"Input": _expr.ExprProxy(node)},
            icomponent.IComponent,
            component_type=_OBJECT_CAST.format(
                source=source_name, target=icomponent.IComponent.RESONITE_TYPE,
            ),
        )
    return _expr.node_output(
        {"Component": component}, workers.Slot,
        module="protoflux.slots", class_name="GetSlot",
    )


def _slot(slot: Any) -> _expr.ExprProxy:
    """Returns a slot expression for a slot, an ID, or a slot expression."""
    if isinstance(slot, (workers.Slot, str)):
        return ref(slot)
    return _expr._coerce(slot)


def name(slot: Any) -> _expr.ExprProxy:
    """Returns a slot's name, a String.

    Args:
        slot: The slot, as a workers.Slot or a slot expression.
    """
    from pyresonitelink.data import primitives

    return _expr.node_output(
        {"Instance": _slot(slot)}, primitives.String,
        module="protoflux.slots.info", class_name="GetSlotName",
    )


def find_child(slot: Any, child_name: Any, *, depth: int = 0) -> _expr.ExprProxy:
    """Returns the first child of a slot with exactly a name, or null if there is none.

    Uses ProtoFlux's FindChildByName, with its substring match turned off,
    since the node matches any name that contains the given one unless it
    is told otherwise.

    Args:
        slot: The slot to search under, as a workers.Slot or a slot
            expression.
        child_name: The name, a String expression or literal.
        depth: How many levels below the direct children to search as
            well. 0 searches the direct children only, and -1 searches
            every descendant (Slot.FindChild).

    Returns:
        The child, a workers.Slot expression. math.is_null tells whether
        one was found.
    """
    from pyresonitelink.data import primitives

    return _expr.node_output(
        {
            "Instance": _slot(slot),
            "Name": _expr.implicit(child_name, primitives.String, "find_child"),
            "MatchSubstring": primitives.Bool(False),
            "IgnoreCase": primitives.Bool(False),
            "SearchDepth": primitives.Int(depth),
        },
        workers.Slot,
        module="protoflux.slots.searching", class_name="FindChildByName",
    )


def child_index(slot: Any) -> _expr.ExprProxy:
    """Returns a slot's index among its parent's children, an Int, or -1 for Root or null.

    Args:
        slot: The slot, as a workers.Slot or a slot expression.
    """
    from pyresonitelink.data import primitives

    return _expr.node_output(
        {"Instance": _slot(slot)}, primitives.Int,
        module="protoflux.slots", class_name="IndexOfChild",
    )


def parent(slot: Any) -> _expr.ExprProxy:
    """Returns a slot's parent, or null for Root or null.

    Args:
        slot: The slot, as a workers.Slot or a slot expression.
    """
    return _expr.node_output(
        {"Instance": _slot(slot)}, workers.Slot,
        module="protoflux.slots", class_name="GetParentSlot",
    )
