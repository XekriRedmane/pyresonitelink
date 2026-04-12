"""Generated component: CircleSegmentShaderMesh."""

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


class CircleSegmentShaderMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The CircleSegmentShaderMesh creates a single quad that covers the bounding box area of a flat torus circle defined by the given values. This is used to render the UI_CircleSegment material.

    Category: Assets/Procedural Meshes

    Used as a mesh to render the UI_CircleSegment material.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CircleSegmentShaderMesh"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, profile: ColorProfile | str | None = None, radius_start: primitives.Float | None = None, thickness: primitives.Float | None = None, angle_start: primitives.Float | None = None, arc_length: primitives.Float | None = None, fill_color: primitives.ColorX | None = None, border_color: primitives.ColorX | None = None, border_size: primitives.Float | None = None, rounded_corner_radius: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            profile: Initial value for Profile.
            radius_start: Initial value for RadiusStart.
            thickness: Initial value for Thickness.
            angle_start: Initial value for AngleStart.
            arc_length: Initial value for ArcLength.
            fill_color: Initial value for FillColor.
            border_color: Initial value for BorderColor.
            border_size: Initial value for BorderSize.
            rounded_corner_radius: Initial value for RoundedCornerRadius.
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
        if radius_start is not None:
            self.radius_start = radius_start
        if thickness is not None:
            self.thickness = thickness
        if angle_start is not None:
            self.angle_start = angle_start
        if arc_length is not None:
            self.arc_length = arc_length
        if fill_color is not None:
            self.fill_color = fill_color
        if border_color is not None:
            self.border_color = border_color
        if border_size is not None:
            self.border_size = border_size
        if rounded_corner_radius is not None:
            self.rounded_corner_radius = rounded_corner_radius

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
    def radius_start(self) -> primitives.Float | None:
        """The inner radius of the circle"""
        member = self.get_member("RadiusStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius_start.setter
    def radius_start(self, value: primitives.Float) -> None:
        """Set the RadiusStart field value."""
        member = self.get_member("RadiusStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RadiusStart", fields.FieldFloat(value=value)
            )

    @property
    def thickness(self) -> primitives.Float | None:
        """How thick the circle is outwards from the inner radius"""
        member = self.get_member("Thickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @thickness.setter
    def thickness(self, value: primitives.Float) -> None:
        """Set the Thickness field value."""
        member = self.get_member("Thickness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Thickness", fields.FieldFloat(value=value)
            )

    @property
    def angle_start(self) -> primitives.Float | None:
        """What angle the circle starts at in degrees"""
        member = self.get_member("AngleStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @angle_start.setter
    def angle_start(self, value: primitives.Float) -> None:
        """Set the AngleStart field value."""
        member = self.get_member("AngleStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AngleStart", fields.FieldFloat(value=value)
            )

    @property
    def arc_length(self) -> primitives.Float | None:
        """The amount of degrees of the circle arch"""
        member = self.get_member("ArcLength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @arc_length.setter
    def arc_length(self, value: primitives.Float) -> None:
        """Set the ArcLength field value."""
        member = self.get_member("ArcLength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ArcLength", fields.FieldFloat(value=value)
            )

    @property
    def fill_color(self) -> primitives.ColorX | None:
        """Used to color the vertices of the mesh (vertex colors)"""
        member = self.get_member("FillColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fill_color.setter
    def fill_color(self, value: primitives.ColorX) -> None:
        """Set the FillColor field value."""
        member = self.get_member("FillColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FillColor", fields.FieldColorX(value=value)
            )

    @property
    def border_color(self) -> primitives.ColorX | None:
        """The border color the Component:UI_CircleSegment rendering on this mesh."""
        member = self.get_member("BorderColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @border_color.setter
    def border_color(self, value: primitives.ColorX) -> None:
        """Set the BorderColor field value."""
        member = self.get_member("BorderColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BorderColor", fields.FieldColorX(value=value)
            )

    @property
    def border_size(self) -> primitives.Float | None:
        """The border thickness of the Component:UI_CircleSegment rendering on this mesh."""
        member = self.get_member("BorderSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @border_size.setter
    def border_size(self, value: primitives.Float) -> None:
        """Set the BorderSize field value."""
        member = self.get_member("BorderSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BorderSize", fields.FieldFloat(value=value)
            )

    @property
    def rounded_corner_radius(self) -> primitives.Float | None:
        """The radius of the corner rounding of the Component:UI_CircleSegment rendering on this mesh."""
        member = self.get_member("RoundedCornerRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rounded_corner_radius.setter
    def rounded_corner_radius(self, value: primitives.Float) -> None:
        """Set the RoundedCornerRadius field value."""
        member = self.get_member("RoundedCornerRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RoundedCornerRadius", fields.FieldFloat(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

