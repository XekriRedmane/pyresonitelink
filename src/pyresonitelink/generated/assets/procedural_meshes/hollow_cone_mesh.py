"""Generated component: HollowConeMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HollowConeMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.HollowConeMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HollowConeMesh"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, height: primitives.Float | None = None, outer_radius_base: primitives.Float | None = None, inner_radius_base: primitives.Float | None = None, outer_radius_top: primitives.Float | None = None, inner_radius_top: primitives.Float | None = None, segments: primitives.Int | None = None, uv_scale: primitives.Float2 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            height: Initial value for Height.
            outer_radius_base: Initial value for OuterRadiusBase.
            inner_radius_base: Initial value for InnerRadiusBase.
            outer_radius_top: Initial value for OuterRadiusTop.
            inner_radius_top: Initial value for InnerRadiusTop.
            segments: Initial value for Segments.
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
        if height is not None:
            self.height = height
        if outer_radius_base is not None:
            self.outer_radius_base = outer_radius_base
        if inner_radius_base is not None:
            self.inner_radius_base = inner_radius_base
        if outer_radius_top is not None:
            self.outer_radius_top = outer_radius_top
        if inner_radius_top is not None:
            self.inner_radius_top = inner_radius_top
        if segments is not None:
            self.segments = segments
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
    def height(self) -> primitives.Float | None:
        """The Height field value."""
        member = self.get_member("Height")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height.setter
    def height(self, value: primitives.Float) -> None:
        """Set the Height field value."""
        member = self.get_member("Height")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Height", fields.FieldFloat(value=value)
            )

    @property
    def outer_radius_base(self) -> primitives.Float | None:
        """The OuterRadiusBase field value."""
        member = self.get_member("OuterRadiusBase")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outer_radius_base.setter
    def outer_radius_base(self, value: primitives.Float) -> None:
        """Set the OuterRadiusBase field value."""
        member = self.get_member("OuterRadiusBase")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OuterRadiusBase", fields.FieldFloat(value=value)
            )

    @property
    def inner_radius_base(self) -> primitives.Float | None:
        """The InnerRadiusBase field value."""
        member = self.get_member("InnerRadiusBase")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @inner_radius_base.setter
    def inner_radius_base(self, value: primitives.Float) -> None:
        """Set the InnerRadiusBase field value."""
        member = self.get_member("InnerRadiusBase")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InnerRadiusBase", fields.FieldFloat(value=value)
            )

    @property
    def outer_radius_top(self) -> primitives.Float | None:
        """The OuterRadiusTop field value."""
        member = self.get_member("OuterRadiusTop")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outer_radius_top.setter
    def outer_radius_top(self, value: primitives.Float) -> None:
        """Set the OuterRadiusTop field value."""
        member = self.get_member("OuterRadiusTop")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OuterRadiusTop", fields.FieldFloat(value=value)
            )

    @property
    def inner_radius_top(self) -> primitives.Float | None:
        """The InnerRadiusTop field value."""
        member = self.get_member("InnerRadiusTop")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @inner_radius_top.setter
    def inner_radius_top(self, value: primitives.Float) -> None:
        """Set the InnerRadiusTop field value."""
        member = self.get_member("InnerRadiusTop")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InnerRadiusTop", fields.FieldFloat(value=value)
            )

    @property
    def segments(self) -> primitives.Int | None:
        """The Segments field value."""
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

