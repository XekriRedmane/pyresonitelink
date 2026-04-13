"""Generated component: HandPoser."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.chirality import Chirality
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifinger_pose_source_component import IFingerPoseSourceComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HandPoser(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """This component modifies the rotation of the fingers of an avatar's hand based on a pose source.
The HandPoser works with whatever data is avilable, either precise finger tracking like a LeapMotion, or course grained like a vive wand, where grip and trigger affect the main finger positions.

The HandPoser is made of five duplicate finger objects, each of which contains four duplicate bone objects. Each bone object contains a Coordinate Compensation, Root, OrigionalRotation, and RotationDrive.
The below chart is difficult to read for this reason, but read it as: the same four fields, duplicated four times (one for each bone), duplicated five times (one for each finger).

Due to this pattern, the intermediate bone of the thumb should never be bound as a human thumb does not have an intermediate bone.

    Category: Users/Common Avatar System/Fingers

    This component forcibly assigns the rotation of each bound finger to a
    particular bone relative to the palm. As an example of this, if you only
    assign a Distal bone, that bone will spin 270 degrees starting pointing
    forwards, curling to point out the direction of the palm, back towards
    the wrist, then pointing out the back of the hand. It is often easiest
    to make changes to this component following this procedure: # Have the
    avatar be unequipped # Clear every RotationDrive field # Assign the Root
    field of each bone in the hand to be driven, this list will not be
    complete and some roots will be null. # Press InitializeHand at the
    bottom of the component (Note: This button only works once, to reset the
    button select another slot, then select the slot with the component
    again). # Re-Equip the avatar and see if the hands initialized
    successfully. # If a bone did not bind correctly, repeat. == Interaction
    with grabbable items ==
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HandPoser"

    def __init__(self, pose_source: str | IFingerPoseSourceComponent | None = None, side: Chirality | str | None = None, pose_metacarpals: primitives.Bool | None = None, hand_root: str | Slot | None = None, hand_forward: primitives.Float3 | None = None, hand_up: primitives.Float3 | None = None, hand_right: primitives.Float3 | None = None, debug_fingers: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            pose_source: Initial value for PoseSource.
            side: Initial value for Side.
            pose_metacarpals: Initial value for PoseMetacarpals.
            hand_root: Initial value for HandRoot.
            hand_forward: Initial value for HandForward.
            hand_up: Initial value for HandUp.
            hand_right: Initial value for HandRight.
            debug_fingers: Initial value for DebugFingers.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if pose_source is not None:
            self.pose_source = pose_source
        if side is not None:
            self.side = side
        if pose_metacarpals is not None:
            self.pose_metacarpals = pose_metacarpals
        if hand_root is not None:
            self.hand_root = hand_root
        if hand_forward is not None:
            self.hand_forward = hand_forward
        if hand_up is not None:
            self.hand_up = hand_up
        if hand_right is not None:
            self.hand_right = hand_right
        if debug_fingers is not None:
            self.debug_fingers = debug_fingers

    @property
    def pose_source(self) -> str | None:
        """What the finger transform data is derived from."""
        member = self.get_member("PoseSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pose_source.setter
    def pose_source(self, target: str | IFingerPoseSourceComponent | None) -> None:
        """Set the PoseSource reference by target ID or IFingerPoseSourceComponent instance."""
        target_id: str | None = target.id if isinstance(target, IFingerPoseSourceComponent) else target  # type: ignore[assignment]
        member = self.get_member("PoseSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PoseSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IFingerPoseSourceComponent'),
            )

    @property
    def side(self) -> Chirality | None:
        """Which hand this poser is representing"""
        member = self.get_member("Side")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Chirality(member.value)
        return None

    @side.setter
    def side(self, value: Chirality | str) -> None:
        """Set Side. Which hand this poser is representing"""
        member = self.get_member("Side")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Side",
                members.FieldEnum(value=str(value)),
            )

    @property
    def pose_metacarpals(self) -> primitives.Bool | None:
        """If metacarpals should be posed (this should normally be left as True)"""
        member = self.get_member("PoseMetacarpals")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pose_metacarpals.setter
    def pose_metacarpals(self, value: primitives.Bool) -> None:
        """Set the PoseMetacarpals field value."""
        member = self.get_member("PoseMetacarpals")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PoseMetacarpals", fields.FieldBool(value=value)
            )

    @property
    def hand_root(self) -> str | None:
        """The root of the hand (if null the slot the component is attached to is used)"""
        member = self.get_member("HandRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hand_root.setter
    def hand_root(self, target: str | Slot | None) -> None:
        """Set the HandRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("HandRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HandRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def hand_forward(self) -> primitives.Float3 | None:
        """A unit vector pointing forward from the wrist to the fingers."""
        member = self.get_member("HandForward")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hand_forward.setter
    def hand_forward(self, value: primitives.Float3) -> None:
        """Set the HandForward field value."""
        member = self.get_member("HandForward")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HandForward", fields.FieldFloat3(value=value)
            )

    @property
    def hand_up(self) -> primitives.Float3 | None:
        """A unit vector pointing from the back of the hand outwards (alternatively phrased, this is pointing into the palm)"""
        member = self.get_member("HandUp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hand_up.setter
    def hand_up(self, value: primitives.Float3) -> None:
        """Set the HandUp field value."""
        member = self.get_member("HandUp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HandUp", fields.FieldFloat3(value=value)
            )

    @property
    def hand_right(self) -> primitives.Float3 | None:
        """A unit vector pointing to the right of the hand, if the hand is facing down. This is roughly the direction of the thumb on the left hand, and the other side of the hand from the thumb on the right hand."""
        member = self.get_member("HandRight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hand_right.setter
    def hand_right(self, value: primitives.Float3) -> None:
        """Set the HandRight field value."""
        member = self.get_member("HandRight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HandRight", fields.FieldFloat3(value=value)
            )

    @property
    def thumb(self) -> members.SyncObject | None:
        """The Thumb on an anthro hand."""
        member = self.get_member("Thumb")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @thumb.setter
    def thumb(self, value: members.SyncObject) -> None:
        """Set Thumb. The Thumb on an anthro hand."""
        self.set_member("Thumb", value)

    @property
    def index_(self) -> members.SyncObject | None:
        """The Index on an anthro hand."""
        member = self.get_member("Index")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @index_.setter
    def index_(self, value: members.SyncObject) -> None:
        """Set Index. The Index on an anthro hand."""
        self.set_member("Index", value)

    @property
    def middle(self) -> members.SyncObject | None:
        """The Middle on an anthro hand."""
        member = self.get_member("Middle")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @middle.setter
    def middle(self, value: members.SyncObject) -> None:
        """Set Middle. The Middle on an anthro hand."""
        self.set_member("Middle", value)

    @property
    def ring(self) -> members.SyncObject | None:
        """The Ring on an anthro hand."""
        member = self.get_member("Ring")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @ring.setter
    def ring(self, value: members.SyncObject) -> None:
        """Set Ring. The Ring on an anthro hand."""
        self.set_member("Ring", value)

    @property
    def pinky(self) -> members.SyncObject | None:
        """The Pinky on an anthro hand."""
        member = self.get_member("Pinky")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @pinky.setter
    def pinky(self, value: members.SyncObject) -> None:
        """Set Pinky. The Pinky on an anthro hand."""
        self.set_member("Pinky", value)

    @property
    def debug_fingers(self) -> primitives.Bool | None:
        """Whether to show visuals for debugging the fingers."""
        member = self.get_member("DebugFingers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @debug_fingers.setter
    def debug_fingers(self, value: primitives.Bool) -> None:
        """Set the DebugFingers field value."""
        member = self.get_member("DebugFingers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DebugFingers", fields.FieldBool(value=value)
            )

