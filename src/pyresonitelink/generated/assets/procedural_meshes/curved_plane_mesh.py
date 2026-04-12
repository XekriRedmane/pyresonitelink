"""Generated component: CurvedPlaneMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.color_profile import ColorProfile
from pyresonitelink.generated._enums.curvature_aspect_ratio_compensation import CurvatureAspectRatioCompensation
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CurvedPlaneMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Generates a plane mesh that is curved vertically. A picture in this page of it can be seen.

    Category: Assets/Procedural Meshes

    Attach to a slot and insert into a MeshRenderer to see the geometry.
    don't forget to use a Material.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CurvedPlaneMesh"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, profile: ColorProfile | str | None = None, size: primitives.Float2 | None = None, curvature: primitives.Float | None = None, tilt_angle: primitives.Float | None = None, aspect_ratio_compensation: CurvatureAspectRatioCompensation | str | None = None, uv_scale: primitives.Float2 | None = None, uv_offset: primitives.Float2 | None = None, segments: primitives.Int | None = None, flat_shading: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            profile: Initial value for Profile.
            size: Initial value for Size.
            curvature: Initial value for Curvature.
            tilt_angle: Initial value for TiltAngle.
            aspect_ratio_compensation: Initial value for AspectRatioCompensation.
            uv_scale: Initial value for UVScale.
            uv_offset: Initial value for UVOffset.
            segments: Initial value for Segments.
            flat_shading: Initial value for FlatShading.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if profile is not None:
            self.profile = profile
        if size is not None:
            self.size = size
        if curvature is not None:
            self.curvature = curvature
        if tilt_angle is not None:
            self.tilt_angle = tilt_angle
        if aspect_ratio_compensation is not None:
            self.aspect_ratio_compensation = aspect_ratio_compensation
        if uv_scale is not None:
            self.uv_scale = uv_scale
        if uv_offset is not None:
            self.uv_offset = uv_offset
        if segments is not None:
            self.segments = segments
        if flat_shading is not None:
            self.flat_shading = flat_shading

    @property
    def high_priority_integration(self) -> primitives.Bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: primitives.Bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def override_bounding_box(self) -> primitives.Bool | None:
        """The OverrideBoundingBox field value."""
        member = self.get_member("OverrideBoundingBox")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_bounding_box.setter
    def override_bounding_box(self, value: primitives.Bool) -> None:
        """Set the OverrideBoundingBox field value."""
        member = self.get_member("OverrideBoundingBox")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideBoundingBox", fields.FieldBool(value=value)
            )

    @property
    def overriden_bounding_box(self) -> primitives.BoundingBox | None:
        """The OverridenBoundingBox field value."""
        member = self.get_member("OverridenBoundingBox")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @overriden_bounding_box.setter
    def overriden_bounding_box(self, value: primitives.BoundingBox) -> None:
        """Set the OverridenBoundingBox field value."""
        member = self.get_member("OverridenBoundingBox")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverridenBoundingBox", fields.FieldBoundingBox(value=value)
            )

    @property
    def profile(self) -> ColorProfile | None:
        """The Profile enum value."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ColorProfile(member.value)
        return None

    @profile.setter
    def profile(self, value: ColorProfile | str) -> None:
        """Set the Profile enum value."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Profile",
                members.FieldEnum(value=str(value)),
            )

    @property
    def size(self) -> primitives.Float2 | None:
        """How big the curve plane mesh is, mostly a ratio"""
        member = self.get_member("Size")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size.setter
    def size(self, value: primitives.Float2) -> None:
        """Set the Size field value."""
        member = self.get_member("Size")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Size", fields.FieldFloat2(value=value)
            )

    @property
    def curvature(self) -> primitives.Float | None:
        """How much to bend the curve plane mesh by"""
        member = self.get_member("Curvature")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @curvature.setter
    def curvature(self, value: primitives.Float) -> None:
        """Set the Curvature field value."""
        member = self.get_member("Curvature")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Curvature", fields.FieldFloat(value=value)
            )

    @property
    def tilt_angle(self) -> primitives.Float | None:
        """How much to "rotate" the curve plane mesh length wise."""
        member = self.get_member("TiltAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tilt_angle.setter
    def tilt_angle(self, value: primitives.Float) -> None:
        """Set the TiltAngle field value."""
        member = self.get_member("TiltAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TiltAngle", fields.FieldFloat(value=value)
            )

    @property
    def aspect_ratio_compensation(self) -> CurvatureAspectRatioCompensation | None:
        """How to compensate for stretching due to curving the plane mesh backwards."""
        member = self.get_member("AspectRatioCompensation")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CurvatureAspectRatioCompensation(member.value)
        return None

    @aspect_ratio_compensation.setter
    def aspect_ratio_compensation(self, value: CurvatureAspectRatioCompensation | str) -> None:
        """Set AspectRatioCompensation. How to compensate for stretching due to curving the plane mesh backwards."""
        member = self.get_member("AspectRatioCompensation")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "AspectRatioCompensation",
                members.FieldEnum(value=str(value)),
            )

    @property
    def uv_scale(self) -> primitives.Float2 | None:
        """The inverse of the size the material should appear on the surface as."""
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
    def uv_offset(self) -> primitives.Float2 | None:
        """Shift the visual detail of the material around."""
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
    def segments(self) -> primitives.Int | None:
        """How many bends/angles the plane should have in it's curve"""
        member = self.get_member("Segments")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @segments.setter
    def segments(self, value: primitives.Int) -> None:
        """Set the Segments field value."""
        member = self.get_member("Segments")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Segments", fields.FieldInt(value=value)
            )

    @property
    def flat_shading(self) -> primitives.Bool | None:
        """Turn off smooth shading"""
        member = self.get_member("FlatShading")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flat_shading.setter
    def flat_shading(self, value: primitives.Bool) -> None:
        """Set the FlatShading field value."""
        member = self.get_member("FlatShading")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FlatShading", fields.FieldBool(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

