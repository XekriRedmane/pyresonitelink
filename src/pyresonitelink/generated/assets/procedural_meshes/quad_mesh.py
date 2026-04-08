"""Generated component: QuadMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class QuadMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.QuadMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.QuadMesh"

    def __init__(self, high_priority_integration: bool | None = None, override_bounding_box: bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, rotation: primitives.FloatQ | None = None, size: primitives.Float2 | None = None, uv_offset: primitives.Float2 | None = None, uv_scale: primitives.Float2 | None = None, scale_uv_with_size: bool | None = None, dual_sided: bool | None = None, use_vertex_colors: bool | None = None, upper_left_color: primitives.ColorX | None = None, lower_left_color: primitives.ColorX | None = None, lower_right_color: primitives.ColorX | None = None, upper_right_color: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            rotation: Initial value for Rotation.
            size: Initial value for Size.
            uv_offset: Initial value for UVOffset.
            uv_scale: Initial value for UVScale.
            scale_uv_with_size: Initial value for ScaleUVWithSize.
            dual_sided: Initial value for DualSided.
            use_vertex_colors: Initial value for UseVertexColors.
            upper_left_color: Initial value for UpperLeftColor.
            lower_left_color: Initial value for LowerLeftColor.
            lower_right_color: Initial value for LowerRightColor.
            upper_right_color: Initial value for UpperRightColor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if rotation is not None:
            self.rotation = rotation
        if size is not None:
            self.size = size
        if uv_offset is not None:
            self.uv_offset = uv_offset
        if uv_scale is not None:
            self.uv_scale = uv_scale
        if scale_uv_with_size is not None:
            self.scale_uv_with_size = scale_uv_with_size
        if dual_sided is not None:
            self.dual_sided = dual_sided
        if use_vertex_colors is not None:
            self.use_vertex_colors = use_vertex_colors
        if upper_left_color is not None:
            self.upper_left_color = upper_left_color
        if lower_left_color is not None:
            self.lower_left_color = lower_left_color
        if lower_right_color is not None:
            self.lower_right_color = lower_right_color
        if upper_right_color is not None:
            self.upper_right_color = upper_right_color

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
    def rotation(self) -> primitives.FloatQ | None:
        """The Rotation field value."""
        member = self.get_member("Rotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rotation.setter
    def rotation(self, value: primitives.FloatQ) -> None:
        """Set the Rotation field value."""
        member = self.get_member("Rotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Rotation", fields.FieldFloatQ(value=value)
            )

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
    def scale_uv_with_size(self) -> bool | None:
        """The ScaleUVWithSize field value."""
        member = self.get_member("ScaleUVWithSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale_uv_with_size.setter
    def scale_uv_with_size(self, value: bool) -> None:
        """Set the ScaleUVWithSize field value."""
        member = self.get_member("ScaleUVWithSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScaleUVWithSize", fields.FieldBool(value=value)
            )

    @property
    def dual_sided(self) -> bool | None:
        """The DualSided field value."""
        member = self.get_member("DualSided")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dual_sided.setter
    def dual_sided(self, value: bool) -> None:
        """Set the DualSided field value."""
        member = self.get_member("DualSided")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DualSided", fields.FieldBool(value=value)
            )

    @property
    def use_vertex_colors(self) -> bool | None:
        """The UseVertexColors field value."""
        member = self.get_member("UseVertexColors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_vertex_colors.setter
    def use_vertex_colors(self, value: bool) -> None:
        """Set the UseVertexColors field value."""
        member = self.get_member("UseVertexColors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseVertexColors", fields.FieldBool(value=value)
            )

    @property
    def upper_left_color(self) -> primitives.ColorX | None:
        """The UpperLeftColor field value."""
        member = self.get_member("UpperLeftColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @upper_left_color.setter
    def upper_left_color(self, value: primitives.ColorX) -> None:
        """Set the UpperLeftColor field value."""
        member = self.get_member("UpperLeftColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UpperLeftColor", fields.FieldColorX(value=value)
            )

    @property
    def lower_left_color(self) -> primitives.ColorX | None:
        """The LowerLeftColor field value."""
        member = self.get_member("LowerLeftColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lower_left_color.setter
    def lower_left_color(self, value: primitives.ColorX) -> None:
        """Set the LowerLeftColor field value."""
        member = self.get_member("LowerLeftColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LowerLeftColor", fields.FieldColorX(value=value)
            )

    @property
    def lower_right_color(self) -> primitives.ColorX | None:
        """The LowerRightColor field value."""
        member = self.get_member("LowerRightColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lower_right_color.setter
    def lower_right_color(self, value: primitives.ColorX) -> None:
        """Set the LowerRightColor field value."""
        member = self.get_member("LowerRightColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LowerRightColor", fields.FieldColorX(value=value)
            )

    @property
    def upper_right_color(self) -> primitives.ColorX | None:
        """The UpperRightColor field value."""
        member = self.get_member("UpperRightColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @upper_right_color.setter
    def upper_right_color(self, value: primitives.ColorX) -> None:
        """Set the UpperRightColor field value."""
        member = self.get_member("UpperRightColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UpperRightColor", fields.FieldColorX(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

