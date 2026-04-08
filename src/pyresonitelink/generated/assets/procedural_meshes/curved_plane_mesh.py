"""Generated component: CurvedPlaneMesh."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CurvedPlaneMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CurvedPlaneMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CurvedPlaneMesh"

    def __init__(self, high_priority_integration: bool | None = None, override_bounding_box: bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, size: primitives.Float2 | None = None, curvature: np.float32 | None = None, tilt_angle: np.float32 | None = None, uv_scale: primitives.Float2 | None = None, uv_offset: primitives.Float2 | None = None, segments: np.int32 | None = None, flat_shading: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            size: Initial value for Size.
            curvature: Initial value for Curvature.
            tilt_angle: Initial value for TiltAngle.
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
        if size is not None:
            self.size = size
        if curvature is not None:
            self.curvature = curvature
        if tilt_angle is not None:
            self.tilt_angle = tilt_angle
        if uv_scale is not None:
            self.uv_scale = uv_scale
        if uv_offset is not None:
            self.uv_offset = uv_offset
        if segments is not None:
            self.segments = segments
        if flat_shading is not None:
            self.flat_shading = flat_shading

    @property
    def high_priority_integration(self) -> bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def override_bounding_box(self) -> bool | None:
        """The OverrideBoundingBox field value."""
        member = self.get_member("OverrideBoundingBox")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_bounding_box.setter
    def override_bounding_box(self, value: bool) -> None:
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
    def profile(self) -> members.FieldEnum | None:
        """The Profile member."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @profile.setter
    def profile(self, value: members.FieldEnum) -> None:
        """Set the Profile member."""
        self.set_member("Profile", value)

    @property
    def size(self) -> primitives.Float2 | None:
        """The Size field value."""
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
    def curvature(self) -> np.float32 | None:
        """The Curvature field value."""
        member = self.get_member("Curvature")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @curvature.setter
    def curvature(self, value: np.float32) -> None:
        """Set the Curvature field value."""
        member = self.get_member("Curvature")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Curvature", fields.FieldFloat(value=value)
            )

    @property
    def tilt_angle(self) -> np.float32 | None:
        """The TiltAngle field value."""
        member = self.get_member("TiltAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tilt_angle.setter
    def tilt_angle(self, value: np.float32) -> None:
        """Set the TiltAngle field value."""
        member = self.get_member("TiltAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TiltAngle", fields.FieldFloat(value=value)
            )

    @property
    def aspect_ratio_compensation(self) -> members.FieldEnum | None:
        """The AspectRatioCompensation member."""
        member = self.get_member("AspectRatioCompensation")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @aspect_ratio_compensation.setter
    def aspect_ratio_compensation(self, value: members.FieldEnum) -> None:
        """Set the AspectRatioCompensation member."""
        self.set_member("AspectRatioCompensation", value)

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
    def segments(self) -> np.int32 | None:
        """The Segments field value."""
        member = self.get_member("Segments")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @segments.setter
    def segments(self, value: np.int32) -> None:
        """Set the Segments field value."""
        member = self.get_member("Segments")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Segments", fields.FieldInt(value=value)
            )

    @property
    def flat_shading(self) -> bool | None:
        """The FlatShading field value."""
        member = self.get_member("FlatShading")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flat_shading.setter
    def flat_shading(self, value: bool) -> None:
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

