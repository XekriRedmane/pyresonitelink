"""Generated component: BentTubeMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.color_profile import ColorProfile
from pyresonitelink.generated._enums.ends import Ends
from pyresonitelink.generated._enums.shading import Shading
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BentTubeMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Bent tube mesh is a component that makes a tube structure.

When calculating the curve, the generator uses a quadratic bezier curve formula. ``StartPoint`` being P0, ``DirectTargetPoint`` being P1, and ``ActualTargetPoint`` being P2.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BentTubeMesh"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, profile: ColorProfile | str | None = None, radius: primitives.Float | None = None, sides: primitives.Int | None = None, segments: primitives.Int | None = None, start_point: primitives.Float3 | None = None, direct_target_point: primitives.Float3 | None = None, actual_target_point: primitives.Float3 | None = None, start_point_color: primitives.ColorX | None = None, end_point_color: primitives.ColorX | None = None, ends: Ends | str | None = None, shading: Shading | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            profile: Initial value for Profile.
            radius: Initial value for Radius.
            sides: Initial value for Sides.
            segments: Initial value for Segments.
            start_point: Initial value for StartPoint.
            direct_target_point: Initial value for DirectTargetPoint.
            actual_target_point: Initial value for ActualTargetPoint.
            start_point_color: Initial value for StartPointColor.
            end_point_color: Initial value for EndPointColor.
            ends: Initial value for Ends.
            shading: Initial value for Shading.
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
        if radius is not None:
            self.radius = radius
        if sides is not None:
            self.sides = sides
        if segments is not None:
            self.segments = segments
        if start_point is not None:
            self.start_point = start_point
        if direct_target_point is not None:
            self.direct_target_point = direct_target_point
        if actual_target_point is not None:
            self.actual_target_point = actual_target_point
        if start_point_color is not None:
            self.start_point_color = start_point_color
        if end_point_color is not None:
            self.end_point_color = end_point_color
        if ends is not None:
            self.ends = ends
        if shading is not None:
            self.shading = shading

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
    def radius(self) -> primitives.Float | None:
        """The radius of the tube (from center to outside)."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: primitives.Float) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    @property
    def sides(self) -> primitives.Int | None:
        """How many sides the tube should have around it"""
        member = self.get_member("Sides")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sides.setter
    def sides(self, value: primitives.Int) -> None:
        """Set the Sides field value."""
        member = self.get_member("Sides")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Sides", fields.FieldInt(value=value)
            )

    @property
    def segments(self) -> primitives.Int | None:
        """how many bends from end to end the tube should have"""
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
    def start_point(self) -> primitives.Float3 | None:
        """Where the tube should start at in local space. Also known as P0 on a quadratic bezier curve."""
        member = self.get_member("StartPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_point.setter
    def start_point(self, value: primitives.Float3) -> None:
        """Set the StartPoint field value."""
        member = self.get_member("StartPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartPoint", fields.FieldFloat3(value=value)
            )

    @property
    def direct_target_point(self) -> primitives.Float3 | None:
        """P1 on the quadratic bezier curve in local space."""
        member = self.get_member("DirectTargetPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @direct_target_point.setter
    def direct_target_point(self, value: primitives.Float3) -> None:
        """Set the DirectTargetPoint field value."""
        member = self.get_member("DirectTargetPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DirectTargetPoint", fields.FieldFloat3(value=value)
            )

    @property
    def actual_target_point(self) -> primitives.Float3 | None:
        """P2 on the quadratic bezier curve in local space."""
        member = self.get_member("ActualTargetPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @actual_target_point.setter
    def actual_target_point(self, value: primitives.Float3) -> None:
        """Set the ActualTargetPoint field value."""
        member = self.get_member("ActualTargetPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActualTargetPoint", fields.FieldFloat3(value=value)
            )

    @property
    def start_point_color(self) -> primitives.ColorX | None:
        """What the color of the tube should be at the start if using a material that supports vertex colors."""
        member = self.get_member("StartPointColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_point_color.setter
    def start_point_color(self, value: primitives.ColorX) -> None:
        """Set the StartPointColor field value."""
        member = self.get_member("StartPointColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartPointColor", fields.FieldColorX(value=value)
            )

    @property
    def end_point_color(self) -> primitives.ColorX | None:
        """What the color of the tube should be at the end if using a material that supports vertex colors."""
        member = self.get_member("EndPointColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_point_color.setter
    def end_point_color(self, value: primitives.ColorX) -> None:
        """Set the EndPointColor field value."""
        member = self.get_member("EndPointColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndPointColor", fields.FieldColorX(value=value)
            )

    @property
    def ends(self) -> Ends | None:
        """How to handle the geometry of the ends of the tube."""
        member = self.get_member("Ends")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Ends(member.value)
        return None

    @ends.setter
    def ends(self, value: Ends | str) -> None:
        """Set Ends. How to handle the geometry of the ends of the tube."""
        member = self.get_member("Ends")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Ends",
                members.FieldEnum(value=str(value)),
            )

    @property
    def shading(self) -> Shading | None:
        """Toggle this mesh being smooth shaded"""
        member = self.get_member("Shading")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Shading(member.value)
        return None

    @shading.setter
    def shading(self, value: Shading | str) -> None:
        """Set Shading. Toggle this mesh being smooth shaded"""
        member = self.get_member("Shading")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Shading",
                members.FieldEnum(value=str(value)),
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

