"""Generated component: RectSizeDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RectSizeDriver(GeneratedComponent, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.RectSizeDriver.

    Category: UIX/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.RectSizeDriver"

    def __init__(self, target_size: str | IField[primitives.Float2] | None = None, scale: primitives.Float2 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_size: Initial value for TargetSize.
            scale: Initial value for Scale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_size is not None:
            self.target_size = target_size
        if scale is not None:
            self.scale = scale

    @property
    def target_size(self) -> str | None:
        """Target ID of the TargetSize reference (targets IField[primitives.Float2])."""
        member = self.get_member("TargetSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_size.setter
    def target_size(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the TargetSize reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def scale(self) -> primitives.Float2 | None:
        """The Scale field value."""
        member = self.get_member("Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale.setter
    def scale(self, value: primitives.Float2) -> None:
        """Set the Scale field value."""
        member = self.get_member("Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Scale", fields.FieldFloat2(value=value)
            )

