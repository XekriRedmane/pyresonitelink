"""Generated component: AssetFrameSlot."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.box_collider import BoxCollider
from pyresonitelink.generated._types.igrabbable_receiver import IGrabbableReceiver
from pyresonitelink.generated._types.igrabbable_reparent_block import IGrabbableReparentBlock
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AssetFrameSlot(GenericComponent[T], IGrabbableReceiver, IGrabbableReparentBlock, IWorldEventReceiver):
    """An asset frame slot is a component that takes any Asset Type as an attach component type argument, and allows for snapping assets to a frame. The asset in the frame can be used as a source to drive a list of asset fields which is defined in Targets.
Optionally it calls a sync delegate that takes an argument of the chosen asset type for this component.

    Category: Transform/Interaction

    Parameterize with a value type::

        AssetFrameSlot[primitives.Float]
        AssetFrameSlot[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AssetFrameSlot<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.AssetFrameSlot<>"

    def __init__(self, frame_size_field: primitives.Float | None = None, frame_anim_speed: primitives.Float | None = None, snap_anim_time: primitives.Float | None = None, current: str | Slot | None = None, current_ratio: primitives.Float2 | None = None, frame_size_ref: str | IField[primitives.Float2] | None = None, collider: str | BoxCollider | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            frame_size_field: Initial value for FrameSize.
            frame_anim_speed: Initial value for FrameAnimSpeed.
            snap_anim_time: Initial value for SnapAnimTime.
            current: Initial value for _current.
            current_ratio: Initial value for _currentRatio.
            frame_size_ref: Initial value for _frameSize.
            collider: Initial value for _collider.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if frame_size_field is not None:
            self.frame_size_field = frame_size_field
        if frame_anim_speed is not None:
            self.frame_anim_speed = frame_anim_speed
        if snap_anim_time is not None:
            self.snap_anim_time = snap_anim_time
        if current is not None:
            self.current = current
        if current_ratio is not None:
            self.current_ratio = current_ratio
        if frame_size_ref is not None:
            self.frame_size_ref = frame_size_ref
        if collider is not None:
            self.collider = collider

    @property
    def frame_size_field(self) -> primitives.Float | None:
        """how thick the frame should be."""
        member = self.get_member("FrameSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @frame_size_field.setter
    def frame_size_field(self, value: primitives.Float) -> None:
        """Set the FrameSize field value."""
        member = self.get_member("FrameSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FrameSize", fields.FieldFloat(value=value)
            )

    @property
    def frame_anim_speed(self) -> primitives.Float | None:
        """how fast the frame should fit to the asset's bounding box in seconds"""
        member = self.get_member("FrameAnimSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @frame_anim_speed.setter
    def frame_anim_speed(self, value: primitives.Float) -> None:
        """Set the FrameAnimSpeed field value."""
        member = self.get_member("FrameAnimSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FrameAnimSpeed", fields.FieldFloat(value=value)
            )

    @property
    def snap_anim_time(self) -> primitives.Float | None:
        """How long the animation should be for the asset going into the frame when snapped in seconds."""
        member = self.get_member("SnapAnimTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @snap_anim_time.setter
    def snap_anim_time(self, value: primitives.Float) -> None:
        """Set the SnapAnimTime field value."""
        member = self.get_member("SnapAnimTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SnapAnimTime", fields.FieldFloat(value=value)
            )

    @property
    def targets(self) -> members.SyncList | None:
        """The items to drive with the snapped object's asset."""
        member = self.get_member("Targets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @targets.setter
    def targets(self, value: members.SyncList) -> None:
        """Set Targets. The items to drive with the snapped object's asset."""
        self.set_member("Targets", value)

    @property
    def current(self) -> str | None:
        """The slot of the asset item inside of the frame."""
        member = self.get_member("_current")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current.setter
    def current(self, target: str | Slot | None) -> None:
        """Set the _current reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_current")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_current",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def current_ratio(self) -> primitives.Float2 | None:
        """The ratio of the asset's bounding box held in the frame"""
        member = self.get_member("_currentRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_ratio.setter
    def current_ratio(self, value: primitives.Float2) -> None:
        """Set the _currentRatio field value."""
        member = self.get_member("_currentRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_currentRatio", fields.FieldFloat2(value=value)
            )

    @property
    def frame_size_ref(self) -> str | None:
        """The field to drive with what the size of the frame should be for the held asset's bounding box."""
        member = self.get_member("_frameSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @frame_size_ref.setter
    def frame_size_ref(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _frameSize reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_frameSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_frameSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def collider(self) -> str | None:
        """The collider to drive the values of the size of the held asset's bounding box."""
        member = self.get_member("_collider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider.setter
    def collider(self, target: str | BoxCollider | None) -> None:
        """Set the _collider reference by target ID or BoxCollider instance."""
        target_id: str | None = target.id if isinstance(target, BoxCollider) else target  # type: ignore[assignment]
        member = self.get_member("_collider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_collider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BoxCollider'),
            )

