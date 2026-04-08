"""Generated component: UV_Vertical_Adapter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UV_Vertical_Adapter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.UV_Vertical_Adapter.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.UV_Vertical_Adapter"

    def __init__(self, original_uv_offset: primitives.Float2 | None = None, original_uv_scale: primitives.Float2 | None = None, uv_offset: str | IField[primitives.Float2] | None = None, uv_scale: str | IField[primitives.Float2] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            original_uv_offset: Initial value for OriginalUVOffset.
            original_uv_scale: Initial value for OriginalUVScale.
            uv_offset: Initial value for UVOffset.
            uv_scale: Initial value for UVScale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if original_uv_offset is not None:
            self.original_uv_offset = original_uv_offset
        if original_uv_scale is not None:
            self.original_uv_scale = original_uv_scale
        if uv_offset is not None:
            self.uv_offset = uv_offset
        if uv_scale is not None:
            self.uv_scale = uv_scale

    @property
    def original_uv_offset(self) -> primitives.Float2 | None:
        """The OriginalUVOffset field value."""
        member = self.get_member("OriginalUVOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @original_uv_offset.setter
    def original_uv_offset(self, value: primitives.Float2) -> None:
        """Set the OriginalUVOffset field value."""
        member = self.get_member("OriginalUVOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OriginalUVOffset", fields.FieldFloat2(value=value)
            )

    @property
    def original_uv_scale(self) -> primitives.Float2 | None:
        """The OriginalUVScale field value."""
        member = self.get_member("OriginalUVScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @original_uv_scale.setter
    def original_uv_scale(self, value: primitives.Float2) -> None:
        """Set the OriginalUVScale field value."""
        member = self.get_member("OriginalUVScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OriginalUVScale", fields.FieldFloat2(value=value)
            )

    @property
    def uv_offset(self) -> str | None:
        """Target ID of the UVOffset reference (targets IField[primitives.Float2])."""
        member = self.get_member("UVOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @uv_offset.setter
    def uv_offset(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the UVOffset reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("UVOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UVOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def uv_scale(self) -> str | None:
        """Target ID of the UVScale reference (targets IField[primitives.Float2])."""
        member = self.get_member("UVScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @uv_scale.setter
    def uv_scale(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the UVScale reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("UVScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UVScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

