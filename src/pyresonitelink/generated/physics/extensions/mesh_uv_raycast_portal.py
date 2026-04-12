"""Generated component: MeshUVRaycastPortal."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.filter_combine_mode import FilterCombineMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iuvto_ray_converter import IUVToRayConverter
from pyresonitelink.generated._types.iraycast_portal import IRaycastPortal
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MeshUVRaycastPortal(GeneratedComponent, IRaycastPortal, IWorldEventReceiver):
    """This component also known as a raycast portal allows users to interact with objects through a camera.

    Category: Physics/Extensions

    **Behavior**: * The camera needs to be in orthographic mode for best results. it still works in perspective but because of perspective warping it only works well in the center. This component is used for the dash, but can be utilized in real world space, allowing for some interesting effects.

* This component only works with mesh colliders. The type of mesh does not matter, since it uses the UVs; the mesh triangles have to determine what point on the camera output to project the raycast out of.

* The mesh collider can only be a front sided collider for this component to work.

* Only user interaction lasers are allowed to pass through, and only press button interactions.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MeshUVRaycastPortal"

    def __init__(self, offset: primitives.Float | None = None, ray_exit: str | IUVToRayConverter | None = None, uv_offset: primitives.Float2 | None = None, uv_scale: primitives.Float2 | None = None, repeat_uv: primitives.Bool | None = None, override_hit_triggers: primitives.Bool | None = None, filter_mode: FilterCombineMode | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            offset: Initial value for Offset.
            ray_exit: Initial value for RayExit.
            uv_offset: Initial value for UVOffset.
            uv_scale: Initial value for UVScale.
            repeat_uv: Initial value for RepeatUV.
            override_hit_triggers: Initial value for OverrideHitTriggers.
            filter_mode: Initial value for FilterMode.
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
        if filter_mode is not None:
            self.filter_mode = filter_mode

    @property
    def offset(self) -> primitives.Float | None:
        """How far back from the camera's actual view direction to project from"""
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
        """Usually a camera"""
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
        """The added offset to the UV point you hit on the mesh before it's projected out; best to keep this (0,0) unless needed"""
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
        """The multiplied offset to the UV point you hit on the mesh before it's projected out; best to keep this (1,1) unless needed"""
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
        """Whether to repeat between the 0-1 range when the laser on the source hits a UV beyond 0-1"""
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
        """Whether to hit colliders, requires Filter to have a sync delegate, but doesn't need to be enabled for this component to work"""
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
    def filter_mode(self) -> FilterCombineMode | None:
        """how to use the ``Filter`` if provided."""
        member = self.get_member("FilterMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return FilterCombineMode(member.value)
        return None

    @filter_mode.setter
    def filter_mode(self, value: FilterCombineMode | str) -> None:
        """Set FilterMode. how to use the ``Filter`` if provided."""
        member = self.get_member("FilterMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "FilterMode",
                members.FieldEnum(value=str(value)),
            )

