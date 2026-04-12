"""Generated component: TubeWireMesh."""

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


class TubeWireMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The TubeWireMesh component acts as a source of procedural Mesh data. This creates a mesh like the StripeWireMesh but is a tube instead.

    Category: Assets/Procedural Meshes

    Attach to a slot, then insert into a MeshRenderer with a material to
    view what this mesh looks like.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TubeWireMesh"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, profile: ColorProfile | str | None = None, point0: primitives.Float3 | None = None, point1: primitives.Float3 | None = None, tangent0: primitives.Float3 | None = None, tangent1: primitives.Float3 | None = None, orientation0: primitives.FloatQ | None = None, orientation1: primitives.FloatQ | None = None, steps: primitives.Int | None = None, exp: primitives.Float | None = None, color0: primitives.ColorX | None = None, color1: primitives.ColorX | None = None, uv_scale: primitives.Float2 | None = None, uv_offset: primitives.Float2 | None = None, radius0: primitives.Float | None = None, radius1: primitives.Float | None = None, ends: Ends | str | None = None, shading: Shading | str | None = None, points: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            profile: Initial value for Profile.
            point0: Initial value for Point0.
            point1: Initial value for Point1.
            tangent0: Initial value for Tangent0.
            tangent1: Initial value for Tangent1.
            orientation0: Initial value for Orientation0.
            orientation1: Initial value for Orientation1.
            steps: Initial value for Steps.
            exp: Initial value for Exp.
            color0: Initial value for Color0.
            color1: Initial value for Color1.
            uv_scale: Initial value for UVScale.
            uv_offset: Initial value for UVOffset.
            radius0: Initial value for Radius0.
            radius1: Initial value for Radius1.
            ends: Initial value for Ends.
            shading: Initial value for Shading.
            points: Initial value for Points.
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
        if point0 is not None:
            self.point0 = point0
        if point1 is not None:
            self.point1 = point1
        if tangent0 is not None:
            self.tangent0 = tangent0
        if tangent1 is not None:
            self.tangent1 = tangent1
        if orientation0 is not None:
            self.orientation0 = orientation0
        if orientation1 is not None:
            self.orientation1 = orientation1
        if steps is not None:
            self.steps = steps
        if exp is not None:
            self.exp = exp
        if color0 is not None:
            self.color0 = color0
        if color1 is not None:
            self.color1 = color1
        if uv_scale is not None:
            self.uv_scale = uv_scale
        if uv_offset is not None:
            self.uv_offset = uv_offset
        if radius0 is not None:
            self.radius0 = radius0
        if radius1 is not None:
            self.radius1 = radius1
        if ends is not None:
            self.ends = ends
        if shading is not None:
            self.shading = shading
        if points is not None:
            self.points = points

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
    def point0(self) -> primitives.Float3 | None:
        """The starting point for the tube mesh."""
        member = self.get_member("Point0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @point0.setter
    def point0(self, value: primitives.Float3) -> None:
        """Set the Point0 field value."""
        member = self.get_member("Point0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Point0", fields.FieldFloat3(value=value)
            )

    @property
    def point1(self) -> primitives.Float3 | None:
        """The ending point for the tube mesh."""
        member = self.get_member("Point1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @point1.setter
    def point1(self, value: primitives.Float3) -> None:
        """Set the Point1 field value."""
        member = self.get_member("Point1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Point1", fields.FieldFloat3(value=value)
            )

    @property
    def tangent0(self) -> primitives.Float3 | None:
        """The bend towards point at the beginning."""
        member = self.get_member("Tangent0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tangent0.setter
    def tangent0(self, value: primitives.Float3) -> None:
        """Set the Tangent0 field value."""
        member = self.get_member("Tangent0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Tangent0", fields.FieldFloat3(value=value)
            )

    @property
    def tangent1(self) -> primitives.Float3 | None:
        """The bend towards point at the end."""
        member = self.get_member("Tangent1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tangent1.setter
    def tangent1(self, value: primitives.Float3) -> None:
        """Set the Tangent1 field value."""
        member = self.get_member("Tangent1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Tangent1", fields.FieldFloat3(value=value)
            )

    @property
    def orientation0(self) -> primitives.FloatQ | None:
        """The rotation of the end cap at the beginning of the tube."""
        member = self.get_member("Orientation0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @orientation0.setter
    def orientation0(self, value: primitives.FloatQ) -> None:
        """Set the Orientation0 field value."""
        member = self.get_member("Orientation0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Orientation0", fields.FieldFloatQ(value=value)
            )

    @property
    def orientation1(self) -> primitives.FloatQ | None:
        """The rotation of the end cap at the end of the tube."""
        member = self.get_member("Orientation1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @orientation1.setter
    def orientation1(self, value: primitives.FloatQ) -> None:
        """Set the Orientation1 field value."""
        member = self.get_member("Orientation1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Orientation1", fields.FieldFloatQ(value=value)
            )

    @property
    def steps(self) -> primitives.Int | None:
        """How many length wise subdivisions there is."""
        member = self.get_member("Steps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @steps.setter
    def steps(self, value: primitives.Int) -> None:
        """Set the Steps field value."""
        member = self.get_member("Steps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Steps", fields.FieldInt(value=value)
            )

    @property
    def exp(self) -> primitives.Float | None:
        """How much to stretch mesh geometry towards the tangent points."""
        member = self.get_member("Exp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exp.setter
    def exp(self, value: primitives.Float) -> None:
        """Set the Exp field value."""
        member = self.get_member("Exp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Exp", fields.FieldFloat(value=value)
            )

    @property
    def color0(self) -> primitives.ColorX | None:
        """The color of the vertex colors at the starting point."""
        member = self.get_member("Color0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color0.setter
    def color0(self, value: primitives.ColorX) -> None:
        """Set the Color0 field value."""
        member = self.get_member("Color0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Color0", fields.FieldColorX(value=value)
            )

    @property
    def color1(self) -> primitives.ColorX | None:
        """The color of the vertex colors at the ending point."""
        member = self.get_member("Color1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color1.setter
    def color1(self, value: primitives.ColorX) -> None:
        """Set the Color1 field value."""
        member = self.get_member("Color1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Color1", fields.FieldColorX(value=value)
            )

    @property
    def uv_scale(self) -> primitives.Float2 | None:
        """The scale of the texture detail on this mesh's surface."""
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
        """The offset of the texture detail on this mesh's surface."""
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
    def radius0(self) -> primitives.Float | None:
        """The starting radius of the tube."""
        member = self.get_member("Radius0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius0.setter
    def radius0(self, value: primitives.Float) -> None:
        """Set the Radius0 field value."""
        member = self.get_member("Radius0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius0", fields.FieldFloat(value=value)
            )

    @property
    def radius1(self) -> primitives.Float | None:
        """The ending radius of the tube."""
        member = self.get_member("Radius1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius1.setter
    def radius1(self, value: primitives.Float) -> None:
        """Set the Radius1 field value."""
        member = self.get_member("Radius1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius1", fields.FieldFloat(value=value)
            )

    @property
    def ends(self) -> Ends | None:
        """How to seal the ends of the mesh, if at all."""
        member = self.get_member("Ends")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Ends(member.value)
        return None

    @ends.setter
    def ends(self, value: Ends | str) -> None:
        """Set Ends. How to seal the ends of the mesh, if at all."""
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
        """How to shade the tube."""
        member = self.get_member("Shading")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Shading(member.value)
        return None

    @shading.setter
    def shading(self, value: Shading | str) -> None:
        """Set Shading. How to shade the tube."""
        member = self.get_member("Shading")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Shading",
                members.FieldEnum(value=str(value)),
            )

    @property
    def points(self) -> primitives.Int | None:
        """How many subdivisions circumference wise the tube has."""
        member = self.get_member("Points")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @points.setter
    def points(self, value: primitives.Int) -> None:
        """Set the Points field value."""
        member = self.get_member("Points")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Points", fields.FieldInt(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

