"""Generated component: UVAtlasAnimator."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.atlas_info import AtlasInfo
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UVAtlasAnimator(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UVAtlasAnimator.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UVAtlasAnimator"

    def __init__(self, scale_field: str | IField[primitives.Float2] | None = None, offset_field: str | IField[primitives.Float2] | None = None, atlas_info: str | AtlasInfo | None = None, frame: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            scale_field: Initial value for ScaleField.
            offset_field: Initial value for OffsetField.
            atlas_info: Initial value for AtlasInfo.
            frame: Initial value for Frame.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if scale_field is not None:
            self.scale_field = scale_field
        if offset_field is not None:
            self.offset_field = offset_field
        if atlas_info is not None:
            self.atlas_info = atlas_info
        if frame is not None:
            self.frame = frame

    @property
    def scale_field(self) -> str | None:
        """Target ID of the ScaleField reference (targets IField[primitives.Float2])."""
        member = self.get_member("ScaleField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale_field.setter
    def scale_field(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the ScaleField reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ScaleField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ScaleField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def offset_field(self) -> str | None:
        """Target ID of the OffsetField reference (targets IField[primitives.Float2])."""
        member = self.get_member("OffsetField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @offset_field.setter
    def offset_field(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the OffsetField reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("OffsetField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OffsetField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def atlas_info(self) -> str | None:
        """Target ID of the AtlasInfo reference (targets AtlasInfo)."""
        member = self.get_member("AtlasInfo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @atlas_info.setter
    def atlas_info(self, target: str | AtlasInfo | None) -> None:
        """Set the AtlasInfo reference by target ID or AtlasInfo instance."""
        target_id: str | None = target.id if isinstance(target, AtlasInfo) else target  # type: ignore[assignment]
        member = self.get_member("AtlasInfo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AtlasInfo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AtlasInfo'),
            )

    @property
    def frame(self) -> primitives.Int | None:
        """The Frame field value."""
        member = self.get_member("Frame")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @frame.setter
    def frame(self, value: primitives.Int) -> None:
        """Set the Frame field value."""
        member = self.get_member("Frame")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Frame", fields.FieldInt(value=value)
            )

