"""Makes slots into controls that a hand turns, such as cranks, wheels, and knobs.

A crank is a slot with two components. A Joint makes the slot grabbable,
and while it is held, the Joint turns the slot about an axis to follow the
hand. A KnobControl adds the change in the slot's angle about the axis,
scaled, to a float field, so the crank can turn any number of times and
the field counts the turns. add_crank adds both.

    crank = await resolink.add_slot(parent=panel, name="Crank")
    grip = await controls.add_crank(
        resolink, crank, axis=primitives.Float3(0, 0, 1),
        target_id=count.get_member("Value").id, per_turn=1.0,
    )

The slot needs a collider on itself or on a descendant, since a Grabber
finds the Joint by looking up from the collider it touches
(colliders.add_bounding_box). It also needs no rotation relative to its
parent when the Joint is added, because the Joint limits the slot's
rotation relative to the parent's axes.

Showing something other than the hand's angle
---------------------------------------------

A Joint can't be grabbed when its slot's rotation is driven
(Draggable.CanGrab), and a KnobControl counts every change of its slot's
rotation, including a change written by a script. So a crank whose shown
angle has to differ from the hand's, such as one wheel geared to another,
is two slots.

    Crank       no mesh, the Joint, add_crank's KnobControl, and
                track_angle's KnobControl
      Visual    the mesh, with its rotation driven
        Handle  the collider

track_angle adds a second KnobControl that counts the crank's turn in
degrees into another field. Drive the Visual's rotation relative to the
crank to the angle to show minus the crank's angle, and the Visual shows
that angle whatever the hand has done to the crank. drive_grabbed drives a
Bool field true while the crank is held, so that a graph can tell a held
crank from a free one.

The angles and the axis
-----------------------

KnobControl measures angles with MathX.AngleAroundAxis, which is the
negative of the angle in floatQ.AxisAngle's sense (decompiled from build
2026.9.18.82). In Resonite's left-handed coordinates, a positive angle
about an axis looks counterclockwise to someone looking along the axis. So
a turn that looks clockwise to that person adds a positive per_turn, and
track_angle counts angles in floatQ.AxisAngle's sense, as
transforms.twist_angle does. Both were checked live with a wheel whose
axis pointed away from the viewer (23 Oct 2026).
"""

from pyresonitelink import client
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated.protoflux.runtimes.execution.nodes.interaction.grabbable import (
    is_grabbable_grabbed,
)
from pyresonitelink.generated.transform.interaction import joint
from pyresonitelink.generated.transform.interaction import knob_control
from pyresonitelink.utils import wiring

GRABBABLE_TYPE = "[FrooxEngine]FrooxEngine.IGrabbable"


async def add_crank(
    resolink: client.Client,
    slot: str | workers.Slot,
    *,
    axis: primitives.Float3,
    target_id: str,
    per_turn: float,
    minimum: float | None = None,
    maximum: float | None = None,
) -> joint.Joint:
    """Makes a slot a crank that a hand turns about an axis, adding to a field.

    Each full turn adds per_turn to the field, and each part of a turn adds
    that part of per_turn. A turn that looks clockwise to someone looking
    along the axis adds, and the other way subtracts. The field stays
    between minimum and maximum, and the crank keeps turning past them.

    Args:
        resolink (client.Client): The connected client.
        slot (str | workers.Slot): The crank's slot, which has no rotation
            relative to its parent.
        axis (primitives.Float3): The axis, in the parent's space.
        target_id (str): The member ID of the float field to add to, such
            as a ValueField<float>'s or a DynamicValueVariable<float>'s
            Value. The KnobControl writes it, so it isn't driven.
        per_turn (float): How much one turn adds.
        minimum (float | None): The field's lowest value, or None for no
            limit.
        maximum (float | None): The field's highest value, or None for no
            limit.

    Returns:
        The Joint, which is the crank's grabbable component.
    """
    # A MaxSwing of 0 keeps the axis where it is. A MaxTwist of 180 or more
    # lets the slot turn freely about the axis (MathX.LimitTwist), and the
    # default of 0 would hold it still.
    grip = joint.Joint(
        axis=axis, max_swing=primitives.Float(0), max_twist=primitives.Float(180),
    )
    await grip.add_to_slot(resolink, slot)
    await _add_knob(resolink, slot, axis, target_id, per_turn, minimum, maximum)
    return grip


async def track_angle(
    resolink: client.Client,
    slot: str | workers.Slot,
    *,
    axis: primitives.Float3,
    target_id: str,
) -> knob_control.KnobControl:
    """Counts a crank's turn about its axis, in degrees, into a float field.

    The field gains a slot's angle in floatQ.AxisAngle's sense each time the
    slot turns, with no limit, so after one and a half turns in the
    positive sense it has gained 540. Only changes after this is added are
    counted.

    Args:
        resolink (client.Client): The connected client.
        slot (str | workers.Slot): The crank's slot.
        axis (primitives.Float3): The crank's axis, in the parent's space.
        target_id (str): The member ID of the float field to add to.

    Returns:
        The KnobControl that counts the angle.
    """
    # KnobControl adds the negative of the angle times Rate / 360, so a Rate
    # of -360 adds the angle itself.
    return await _add_knob(resolink, slot, axis, target_id, -360.0, None, None)


async def drive_grabbed(
    resolink: client.Client,
    slot: str | workers.Slot,
    grabbable: str | GeneratedComponent,
    field_id: str,
) -> None:
    """Drives a Bool field true while a grabbable component is held, and false otherwise.

    The nodes are an IsGrabbableGrabbed, which takes the grabbable through
    a RefObjectInput<IGrabbable>, and a ValueFieldDrive<bool>.

    Args:
        resolink (client.Client): The connected client.
        slot (str | workers.Slot): The slot to add the nodes to.
        grabbable (str | GeneratedComponent): The grabbable component, such
            as add_crank's Joint, or its ID.
        field_id (str): The member ID of the Bool field to drive, such as a
            DynamicValueVariable<bool>'s Value.
    """
    reference = await wiring.add_reference_input(resolink, slot, grabbable, GRABBABLE_TYPE)
    grabbed = is_grabbable_grabbed.IsGrabbableGrabbed()
    await wiring.add_node(resolink, slot, grabbed, {"Grabbable": reference})
    await wiring.drive_from(resolink, slot, grabbed, field_id, primitives.Bool)


async def _add_knob(
    resolink: client.Client,
    slot: str | workers.Slot,
    axis: primitives.Float3,
    target_id: str,
    rate: float,
    minimum: float | None,
    maximum: float | None,
) -> knob_control.KnobControl:
    """Adds a KnobControl that adds a slot's turn about an axis, times rate / 360, to a field.

    A limit given as None keeps the KnobControl's default, which is
    infinite.
    """
    # A KnobControl skips the first change after its axis differs from
    # _lastAxis, so _lastAxis starts at the axis.
    knob = knob_control.KnobControl(
        target=target_id,
        rotation_axis=axis,
        rate=primitives.Float(rate),
        min=None if minimum is None else primitives.Float(minimum),
        max=None if maximum is None else primitives.Float(maximum),
        last_axis=axis,
    )
    await knob.add_to_slot(resolink, slot)
    return knob
