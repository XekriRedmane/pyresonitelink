"""Generated component: CopyGlobalScale."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CopyGlobalScale(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The CopyGlobalScale component is used to ensure that one object has the exact same global scale as another object.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CopyGlobalScale"

    def __init__(self, source: str | Slot | None = None, non_uniform: primitives.Bool | None = None, scale_drive: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            non_uniform: Initial value for NonUniform.
            scale_drive: Initial value for _scaleDrive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if non_uniform is not None:
            self.non_uniform = non_uniform
        if scale_drive is not None:
            self.scale_drive = scale_drive

    @property
    def source(self) -> str | None:
        """The object that serves as scale reference."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | Slot | None) -> None:
        """Set the Source reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def non_uniform(self) -> primitives.Bool | None:
        """If true, non-uniform scale is preserved, otherwise the X scale of the source serves as X, Y and Z of the target."""
        member = self.get_member("NonUniform")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @non_uniform.setter
    def non_uniform(self, value: primitives.Bool) -> None:
        """Set the NonUniform field value."""
        member = self.get_member("NonUniform")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NonUniform", fields.FieldBool(value=value)
            )

    @property
    def scale_drive(self) -> str | None:
        """The field that is driven to match the global scale of the source. This automatically gets populated with the scale field of the slot that this component is added to."""
        member = self.get_member("_scaleDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale_drive.setter
    def scale_drive(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _scaleDrive reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_scaleDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_scaleDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

