"""Generated component: HandPoser."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifinger_pose_source_component import IFingerPoseSourceComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HandPoser(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.HandPoser.

    Category: Users/Common Avatar System/Fingers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HandPoser"

    def __init__(self, pose_source: str | IFingerPoseSourceComponent | None = None, pose_metacarpals: bool | None = None, hand_root: str | Slot | None = None, hand_forward: primitives.Float3 | None = None, hand_up: primitives.Float3 | None = None, hand_right: primitives.Float3 | None = None, debug_fingers: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            pose_source: Initial value for PoseSource.
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
        """Target ID of the PoseSource reference (targets IFingerPoseSourceComponent)."""
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
    def side(self) -> members.FieldEnum | None:
        """The Side member."""
        member = self.get_member("Side")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @side.setter
    def side(self, value: members.FieldEnum) -> None:
        """Set the Side member."""
        self.set_member("Side", value)

    @property
    def pose_metacarpals(self) -> bool | None:
        """The PoseMetacarpals field value."""
        member = self.get_member("PoseMetacarpals")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pose_metacarpals.setter
    def pose_metacarpals(self, value: bool) -> None:
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
        """Target ID of the HandRoot reference (targets Slot)."""
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
        """The HandForward field value."""
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
        """The HandUp field value."""
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
        """The HandRight field value."""
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
        """The Thumb member."""
        member = self.get_member("Thumb")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @thumb.setter
    def thumb(self, value: members.SyncObject) -> None:
        """Set the Thumb member."""
        self.set_member("Thumb", value)

    @property
    def index(self) -> members.SyncObject | None:
        """The Index member."""
        member = self.get_member("Index")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @index.setter
    def index(self, value: members.SyncObject) -> None:
        """Set the Index member."""
        self.set_member("Index", value)

    @property
    def middle(self) -> members.SyncObject | None:
        """The Middle member."""
        member = self.get_member("Middle")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @middle.setter
    def middle(self, value: members.SyncObject) -> None:
        """Set the Middle member."""
        self.set_member("Middle", value)

    @property
    def ring(self) -> members.SyncObject | None:
        """The Ring member."""
        member = self.get_member("Ring")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @ring.setter
    def ring(self, value: members.SyncObject) -> None:
        """Set the Ring member."""
        self.set_member("Ring", value)

    @property
    def pinky(self) -> members.SyncObject | None:
        """The Pinky member."""
        member = self.get_member("Pinky")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @pinky.setter
    def pinky(self, value: members.SyncObject) -> None:
        """Set the Pinky member."""
        self.set_member("Pinky", value)

    @property
    def debug_fingers(self) -> bool | None:
        """The DebugFingers field value."""
        member = self.get_member("DebugFingers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @debug_fingers.setter
    def debug_fingers(self, value: bool) -> None:
        """Set the DebugFingers field value."""
        member = self.get_member("DebugFingers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DebugFingers", fields.FieldBool(value=value)
            )

