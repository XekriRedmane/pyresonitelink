"""Generated component: ColorWheelTriangleMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorWheelTriangleMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ColorWheelTriangleMesh.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ColorWheelTriangleMesh"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, hue: primitives.Float | None = None, outer_radius: primitives.Float | None = None, inner_radius: primitives.Float | None = None, ring_segments: primitives.Int | None = None, cursor_position: primitives.Float3 | None = None, cursor_segments: primitives.Int | None = None, cursor_color: primitives.ColorX | None = None, cursor_outer_radius: primitives.Float | None = None, cursor_inner_radius: primitives.Float | None = None, cursor_zoffset: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            hue: Initial value for Hue.
            outer_radius: Initial value for OuterRadius.
            inner_radius: Initial value for InnerRadius.
            ring_segments: Initial value for RingSegments.
            cursor_position: Initial value for CursorPosition.
            cursor_segments: Initial value for CursorSegments.
            cursor_color: Initial value for CursorColor.
            cursor_outer_radius: Initial value for CursorOuterRadius.
            cursor_inner_radius: Initial value for CursorInnerRadius.
            cursor_zoffset: Initial value for CursorZOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if hue is not None:
            self.hue = hue
        if outer_radius is not None:
            self.outer_radius = outer_radius
        if inner_radius is not None:
            self.inner_radius = inner_radius
        if ring_segments is not None:
            self.ring_segments = ring_segments
        if cursor_position is not None:
            self.cursor_position = cursor_position
        if cursor_segments is not None:
            self.cursor_segments = cursor_segments
        if cursor_color is not None:
            self.cursor_color = cursor_color
        if cursor_outer_radius is not None:
            self.cursor_outer_radius = cursor_outer_radius
        if cursor_inner_radius is not None:
            self.cursor_inner_radius = cursor_inner_radius
        if cursor_zoffset is not None:
            self.cursor_zoffset = cursor_zoffset

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
    def hue(self) -> primitives.Float | None:
        """The Hue field value."""
        member = self.get_member("Hue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hue.setter
    def hue(self, value: primitives.Float) -> None:
        """Set the Hue field value."""
        member = self.get_member("Hue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Hue", fields.FieldFloat(value=value)
            )

    @property
    def outer_radius(self) -> primitives.Float | None:
        """The OuterRadius field value."""
        member = self.get_member("OuterRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outer_radius.setter
    def outer_radius(self, value: primitives.Float) -> None:
        """Set the OuterRadius field value."""
        member = self.get_member("OuterRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OuterRadius", fields.FieldFloat(value=value)
            )

    @property
    def inner_radius(self) -> primitives.Float | None:
        """The InnerRadius field value."""
        member = self.get_member("InnerRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @inner_radius.setter
    def inner_radius(self, value: primitives.Float) -> None:
        """Set the InnerRadius field value."""
        member = self.get_member("InnerRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InnerRadius", fields.FieldFloat(value=value)
            )

    @property
    def ring_segments(self) -> primitives.Int | None:
        """The RingSegments field value."""
        member = self.get_member("RingSegments")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ring_segments.setter
    def ring_segments(self, value: primitives.Int) -> None:
        """Set the RingSegments field value."""
        member = self.get_member("RingSegments")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RingSegments", fields.FieldInt(value=value)
            )

    @property
    def cursor_position(self) -> primitives.Float3 | None:
        """The CursorPosition field value."""
        member = self.get_member("CursorPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cursor_position.setter
    def cursor_position(self, value: primitives.Float3) -> None:
        """Set the CursorPosition field value."""
        member = self.get_member("CursorPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CursorPosition", fields.FieldFloat3(value=value)
            )

    @property
    def cursor_segments(self) -> primitives.Int | None:
        """The CursorSegments field value."""
        member = self.get_member("CursorSegments")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cursor_segments.setter
    def cursor_segments(self, value: primitives.Int) -> None:
        """Set the CursorSegments field value."""
        member = self.get_member("CursorSegments")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CursorSegments", fields.FieldInt(value=value)
            )

    @property
    def cursor_color(self) -> primitives.ColorX | None:
        """The CursorColor field value."""
        member = self.get_member("CursorColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cursor_color.setter
    def cursor_color(self, value: primitives.ColorX) -> None:
        """Set the CursorColor field value."""
        member = self.get_member("CursorColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CursorColor", fields.FieldColorX(value=value)
            )

    @property
    def cursor_outer_radius(self) -> primitives.Float | None:
        """The CursorOuterRadius field value."""
        member = self.get_member("CursorOuterRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cursor_outer_radius.setter
    def cursor_outer_radius(self, value: primitives.Float) -> None:
        """Set the CursorOuterRadius field value."""
        member = self.get_member("CursorOuterRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CursorOuterRadius", fields.FieldFloat(value=value)
            )

    @property
    def cursor_inner_radius(self) -> primitives.Float | None:
        """The CursorInnerRadius field value."""
        member = self.get_member("CursorInnerRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cursor_inner_radius.setter
    def cursor_inner_radius(self, value: primitives.Float) -> None:
        """Set the CursorInnerRadius field value."""
        member = self.get_member("CursorInnerRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CursorInnerRadius", fields.FieldFloat(value=value)
            )

    @property
    def cursor_zoffset(self) -> primitives.Float | None:
        """The CursorZOffset field value."""
        member = self.get_member("CursorZOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cursor_zoffset.setter
    def cursor_zoffset(self, value: primitives.Float) -> None:
        """Set the CursorZOffset field value."""
        member = self.get_member("CursorZOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CursorZOffset", fields.FieldFloat(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

