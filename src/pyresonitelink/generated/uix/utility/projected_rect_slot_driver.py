"""Generated component: ProjectedRectSlotDriver."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ProjectedRectSlotDriver(GeneratedComponent, IUIComputeComponent, IWorldEventReceiver):
    """The ProjectedRectSlotDriver component takes a Slot in the ``Target`` field and places that slot in the center of where this compoennt's UIX element's transform is. This target slot will be resized to match a pizel scale that the UIX Canvas uses.

}}

    Category: UIX/Utility

    This can be used if you want to place a slot to where some UIX is at
    anytime.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.ProjectedRectSlotDriver"

    def __init__(self, position: str | IField[primitives.Float3] | None = None, target: str | Slot | None = None, rotation: str | IField[primitives.FloatQ] | None = None, scale: str | IField[primitives.Float3] | None = None, original_parent: str | Slot | None = None, last_target: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            position: Initial value for _position.
            target: Initial value for Target.
            rotation: Initial value for _rotation.
            scale: Initial value for _scale.
            original_parent: Initial value for _originalParent.
            last_target: Initial value for _lastTarget.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if position is not None:
            self.position = position
        if target is not None:
            self.target = target
        if rotation is not None:
            self.rotation = rotation
        if scale is not None:
            self.scale = scale
        if original_parent is not None:
            self.original_parent = original_parent
        if last_target is not None:
            self.last_target = last_target

    @property
    def position(self) -> str | None:
        """Internal - The position of the target slot."""
        member = self.get_member("_position")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position.setter
    def position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _position reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_position")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_position",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def target(self) -> str | None:
        """The slot to reposition onto this UIX."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | Slot | None) -> None:
        """Set the Target reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def rotation(self) -> str | None:
        """Internal - The rotation of the target slot."""
        member = self.get_member("_rotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation.setter
    def rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _rotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def scale(self) -> str | None:
        """Internal - The scale of the target slot."""
        member = self.get_member("_scale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale.setter
    def scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _scale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_scale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_scale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def original_parent(self) -> str | None:
        """Internal - The original parent this slot came from."""
        member = self.get_member("_originalParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @original_parent.setter
    def original_parent(self, target: str | Slot | None) -> None:
        """Set the _originalParent reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_originalParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_originalParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def last_target(self) -> str | None:
        """Internal - The last known slot target this component used."""
        member = self.get_member("_lastTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @last_target.setter
    def last_target(self, target: str | Slot | None) -> None:
        """Set the _lastTarget reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_lastTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_lastTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

