"""Generated component: MeshUVRaycastPortal."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iuvto_ray_converter import IUVToRayConverter
from pyresonitelink.generated._types.iraycast_portal import IRaycastPortal
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MeshUVRaycastPortal(GeneratedComponent, IRaycastPortal, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.MeshUVRaycastPortal.

    Category: Physics/Extensions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MeshUVRaycastPortal"

    def __init__(self, offset: primitives.Float | None = None, ray_exit: str | IUVToRayConverter | None = None, uv_offset: primitives.Float2 | None = None, uv_scale: primitives.Float2 | None = None, repeat_uv: primitives.Bool | None = None, override_hit_triggers: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            offset: Initial value for Offset.
            ray_exit: Initial value for RayExit.
            uv_offset: Initial value for UVOffset.
            uv_scale: Initial value for UVScale.
            repeat_uv: Initial value for RepeatUV.
            override_hit_triggers: Initial value for OverrideHitTriggers.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if offset is not None:
            self.offset = offset
        if ray_exit is not None:
            self.ray_exit = ray_exit
        if uv_offset is not None:
            self.uv_offset = uv_offset
        if uv_scale is not None:
            self.uv_scale = uv_scale
        if repeat_uv is not None:
            self.repeat_uv = repeat_uv
        if override_hit_triggers is not None:
            self.override_hit_triggers = override_hit_triggers

    @property
    def offset(self) -> primitives.Float | None:
        """The Offset field value."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat(value=value)
            )

    @property
    def ray_exit(self) -> str | None:
        """Target ID of the RayExit reference (targets IUVToRayConverter)."""
        member = self.get_member("RayExit")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ray_exit.setter
    def ray_exit(self, target: str | IUVToRayConverter | None) -> None:
        """Set the RayExit reference by target ID or IUVToRayConverter instance."""
        target_id: str | None = target.id if isinstance(target, IUVToRayConverter) else target  # type: ignore[assignment]
        member = self.get_member("RayExit")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RayExit",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IUVToRayConverter'),
            )

    @property
    def uv_offset(self) -> primitives.Float2 | None:
        """The UVOffset field value."""
        member = self.get_member("UVOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv_offset.setter
    def uv_offset(self, value: primitives.Float2) -> None:
        """Set the UVOffset field value."""
        member = self.get_member("UVOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UVOffset", fields.FieldFloat2(value=value)
            )

    @property
    def uv_scale(self) -> primitives.Float2 | None:
        """The UVScale field value."""
        member = self.get_member("UVScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv_scale.setter
    def uv_scale(self, value: primitives.Float2) -> None:
        """Set the UVScale field value."""
        member = self.get_member("UVScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UVScale", fields.FieldFloat2(value=value)
            )

    @property
    def repeat_uv(self) -> primitives.Bool | None:
        """The RepeatUV field value."""
        member = self.get_member("RepeatUV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @repeat_uv.setter
    def repeat_uv(self, value: primitives.Bool) -> None:
        """Set the RepeatUV field value."""
        member = self.get_member("RepeatUV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RepeatUV", fields.FieldBool(value=value)
            )

    @property
    def override_hit_triggers(self) -> primitives.Bool | None:
        """The OverrideHitTriggers field value."""
        member = self.get_member("OverrideHitTriggers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_hit_triggers.setter
    def override_hit_triggers(self, value: primitives.Bool) -> None:
        """Set the OverrideHitTriggers field value."""
        member = self.get_member("OverrideHitTriggers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideHitTriggers", fields.FieldNullableBool(value=value)
            )

    @property
    def filter_mode(self) -> members.FieldEnum | None:
        """The FilterMode member."""
        member = self.get_member("FilterMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @filter_mode.setter
    def filter_mode(self, value: members.FieldEnum) -> None:
        """Set the FilterMode member."""
        self.set_member("FilterMode", value)

