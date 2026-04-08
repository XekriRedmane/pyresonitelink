"""Generated component: TorusMesh."""

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


class TorusMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TorusMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TorusMesh"

    def __init__(self, high_priority_integration: bool | None = None, override_bounding_box: bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, minor_segments: np.int32 | None = None, major_segments: np.int32 | None = None, major_radius: np.float32 | None = None, minor_radius: np.float32 | None = None, uv_scale: primitives.Float2 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            minor_segments: Initial value for MinorSegments.
            major_segments: Initial value for MajorSegments.
            major_radius: Initial value for MajorRadius.
            minor_radius: Initial value for MinorRadius.
            uv_scale: Initial value for UVScale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if minor_segments is not None:
            self.minor_segments = minor_segments
        if major_segments is not None:
            self.major_segments = major_segments
        if major_radius is not None:
            self.major_radius = major_radius
        if minor_radius is not None:
            self.minor_radius = minor_radius
        if uv_scale is not None:
            self.uv_scale = uv_scale

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
    def minor_segments(self) -> np.int32 | None:
        """The MinorSegments field value."""
        member = self.get_member("MinorSegments")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @minor_segments.setter
    def minor_segments(self, value: np.int32) -> None:
        """Set the MinorSegments field value."""
        member = self.get_member("MinorSegments")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinorSegments", fields.FieldInt(value=value)
            )

    @property
    def major_segments(self) -> np.int32 | None:
        """The MajorSegments field value."""
        member = self.get_member("MajorSegments")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @major_segments.setter
    def major_segments(self, value: np.int32) -> None:
        """Set the MajorSegments field value."""
        member = self.get_member("MajorSegments")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MajorSegments", fields.FieldInt(value=value)
            )

    @property
    def major_radius(self) -> np.float32 | None:
        """The MajorRadius field value."""
        member = self.get_member("MajorRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @major_radius.setter
    def major_radius(self, value: np.float32) -> None:
        """Set the MajorRadius field value."""
        member = self.get_member("MajorRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MajorRadius", fields.FieldFloat(value=value)
            )

    @property
    def minor_radius(self) -> np.float32 | None:
        """The MinorRadius field value."""
        member = self.get_member("MinorRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @minor_radius.setter
    def minor_radius(self, value: np.float32) -> None:
        """Set the MinorRadius field value."""
        member = self.get_member("MinorRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinorRadius", fields.FieldFloat(value=value)
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

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

