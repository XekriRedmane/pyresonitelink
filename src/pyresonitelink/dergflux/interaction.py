"""Grabbing in Dergflux expressions.

    held = interaction.is_grabbed(ball_grabbable)
    with g.If(held):
        ...
"""

from pyresonitelink.data import primitives
from pyresonitelink.dergflux import _expr
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types import igrabbable


def is_grabbed(grabbable: GeneratedComponent) -> _expr.ExprProxy:
    """Returns a Bool that is true while a grabbable component is held.

    Uses ProtoFlux's IsGrabbableGrabbed, which takes the component
    through a RefObjectInput<IGrabbable>.

    Args:
        grabbable: The component, such as a Grabbable, already added to a
            slot.
    """
    assert grabbable.id is not None, "Add the component to a slot first."
    reference = _expr.ExprProxy(_expr.ElementRefNode(
        grabbable.id, igrabbable.IGrabbable.RESONITE_TYPE, igrabbable.IGrabbable,
    ))
    return _expr.node_output(
        {"Grabbable": reference}, primitives.Bool,
        module="protoflux.interaction.grabbable", class_name="IsGrabbableGrabbed",
    )
