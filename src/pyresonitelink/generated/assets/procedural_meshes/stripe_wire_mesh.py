"""Generated component: StripeWireMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StripeWireMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.StripeWireMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.StripeWireMesh"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, point0: primitives.Float3 | None = None, point1: primitives.Float3 | None = None, tangent0: primitives.Float3 | None = None, tangent1: primitives.Float3 | None = None, orientation0: primitives.FloatQ | None = None, orientation1: primitives.FloatQ | None = None, steps: primitives.Int | None = None, exp: primitives.Float | None = None, color0: primitives.ColorX | None = None, color1: primitives.ColorX | None = None, uv_scale: primitives.Float2 | None = None, uv_offset: primitives.Float2 | None = None, width0: primitives.Float | None = None, width1: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
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
            width0: Initial value for Width0.
            width1: Initial value for Width1.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
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
        if width0 is not None:
            self.width0 = width0
        if width1 is not None:
            self.width1 = width1

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
    def point0(self) -> primitives.Float3 | None:
        """The Point0 field value."""
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
        """The Point1 field value."""
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
        """The Tangent0 field value."""
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
        """The Tangent1 field value."""
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
        """The Orientation0 field value."""
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
        """The Orientation1 field value."""
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
        """The Steps field value."""
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
        """The Exp field value."""
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
        """The Color0 field value."""
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
        """The Color1 field value."""
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
    def width0(self) -> primitives.Float | None:
        """The Width0 field value."""
        member = self.get_member("Width0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @width0.setter
    def width0(self, value: primitives.Float) -> None:
        """Set the Width0 field value."""
        member = self.get_member("Width0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Width0", fields.FieldFloat(value=value)
            )

    @property
    def width1(self) -> primitives.Float | None:
        """The Width1 field value."""
        member = self.get_member("Width1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @width1.setter
    def width1(self, value: primitives.Float) -> None:
        """Set the Width1 field value."""
        member = self.get_member("Width1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Width1", fields.FieldFloat(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

