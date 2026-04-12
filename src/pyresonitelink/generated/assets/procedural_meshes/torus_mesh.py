"""Generated component: TorusMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.color_profile import ColorProfile
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TorusMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The TorusMesh component generates procedural geometry that is used with MeshRenderer.

This mesh resembles a Donut.

    Category: Assets/Procedural Meshes

    Attach to a slot and insert this component into a MeshRenderer to view
    its geometry. Don't forget to add a Material
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TorusMesh"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, profile: ColorProfile | str | None = None, minor_segments: primitives.Int | None = None, major_segments: primitives.Int | None = None, major_radius: primitives.Float | None = None, minor_radius: primitives.Float | None = None, uv_scale: primitives.Float2 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            profile: Initial value for Profile.
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
        if profile is not None:
            self.profile = profile
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
    def minor_segments(self) -> primitives.Int | None:
        """The amount of detail/cuts along the circle of the torus. Making this 4 will make the torus a square instead of a circle shape."""
        member = self.get_member("MinorSegments")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @minor_segments.setter
    def minor_segments(self, value: primitives.Int) -> None:
        """Set the MinorSegments field value."""
        member = self.get_member("MinorSegments")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinorSegments", fields.FieldInt(value=value)
            )

    @property
    def major_segments(self) -> primitives.Int | None:
        """The amount of detail/cuts going around and through the center along the outside and inside."""
        member = self.get_member("MajorSegments")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @major_segments.setter
    def major_segments(self, value: primitives.Int) -> None:
        """Set the MajorSegments field value."""
        member = self.get_member("MajorSegments")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MajorSegments", fields.FieldInt(value=value)
            )

    @property
    def major_radius(self) -> primitives.Float | None:
        """The size of the torus"""
        member = self.get_member("MajorRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @major_radius.setter
    def major_radius(self, value: primitives.Float) -> None:
        """Set the MajorRadius field value."""
        member = self.get_member("MajorRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MajorRadius", fields.FieldFloat(value=value)
            )

    @property
    def minor_radius(self) -> primitives.Float | None:
        """the fatness/thickness of the torus. If this is too big than the hole in the center will seal up."""
        member = self.get_member("MinorRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @minor_radius.setter
    def minor_radius(self, value: primitives.Float) -> None:
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
        """the scale of the material detail on the surface of the torus."""
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

