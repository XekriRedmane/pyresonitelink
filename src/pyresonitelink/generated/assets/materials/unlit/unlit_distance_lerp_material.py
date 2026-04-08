"""Generated component: UnlitDistanceLerpMaterial."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UnlitDistanceLerpMaterial(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UnlitDistanceLerpMaterial.

    Category: Assets/Materials/Unlit
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UnlitDistanceLerpMaterial"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, shader: str | IAssetProvider[Shader] | None = None, local_space: primitives.Bool | None = None, point: primitives.Float3 | None = None, distance: primitives.Float | None = None, transition_range: primitives.Float | None = None, near_texture: str | IAssetProvider[ITexture2D] | None = None, far_texture: str | IAssetProvider[ITexture2D] | None = None, near_texture_scale: primitives.Float2 | None = None, near_texture_offset: primitives.Float2 | None = None, far_texture_scale: primitives.Float2 | None = None, far_texture_offset: primitives.Float2 | None = None, near_color: primitives.ColorX | None = None, far_color: primitives.ColorX | None = None, use_vertex_colors: primitives.Bool | None = None, alpha_cutoff: primitives.Float | None = None, offset_factor: primitives.Float | None = None, offset_units: primitives.Float | None = None, render_queue: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            local_space: Initial value for LocalSpace.
            point: Initial value for Point.
            distance: Initial value for Distance.
            transition_range: Initial value for TransitionRange.
            near_texture: Initial value for NearTexture.
            far_texture: Initial value for FarTexture.
            near_texture_scale: Initial value for NearTextureScale.
            near_texture_offset: Initial value for NearTextureOffset.
            far_texture_scale: Initial value for FarTextureScale.
            far_texture_offset: Initial value for FarTextureOffset.
            near_color: Initial value for NearColor.
            far_color: Initial value for FarColor.
            use_vertex_colors: Initial value for UseVertexColors.
            alpha_cutoff: Initial value for AlphaCutoff.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            render_queue: Initial value for RenderQueue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if shader is not None:
            self.shader = shader
        if local_space is not None:
            self.local_space = local_space
        if point is not None:
            self.point = point
        if distance is not None:
            self.distance = distance
        if transition_range is not None:
            self.transition_range = transition_range
        if near_texture is not None:
            self.near_texture = near_texture
        if far_texture is not None:
            self.far_texture = far_texture
        if near_texture_scale is not None:
            self.near_texture_scale = near_texture_scale
        if near_texture_offset is not None:
            self.near_texture_offset = near_texture_offset
        if far_texture_scale is not None:
            self.far_texture_scale = far_texture_scale
        if far_texture_offset is not None:
            self.far_texture_offset = far_texture_offset
        if near_color is not None:
            self.near_color = near_color
        if far_color is not None:
            self.far_color = far_color
        if use_vertex_colors is not None:
            self.use_vertex_colors = use_vertex_colors
        if alpha_cutoff is not None:
            self.alpha_cutoff = alpha_cutoff
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units
        if render_queue is not None:
            self.render_queue = render_queue

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
    def shader(self) -> str | None:
        """Target ID of the _shader reference (targets IAssetProvider[Shader])."""
        member = self.get_member("_shader")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @shader.setter
    def shader(self, target: str | IAssetProvider[Shader] | None) -> None:
        """Set the _shader reference by target ID or IAssetProvider[Shader] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_shader")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_shader",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Shader>'),
            )

    @property
    def local_space(self) -> primitives.Bool | None:
        """The LocalSpace field value."""
        member = self.get_member("LocalSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_space.setter
    def local_space(self, value: primitives.Bool) -> None:
        """Set the LocalSpace field value."""
        member = self.get_member("LocalSpace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalSpace", fields.FieldBool(value=value)
            )

    @property
    def point(self) -> primitives.Float3 | None:
        """The Point field value."""
        member = self.get_member("Point")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @point.setter
    def point(self, value: primitives.Float3) -> None:
        """Set the Point field value."""
        member = self.get_member("Point")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Point", fields.FieldFloat3(value=value)
            )

    @property
    def distance(self) -> primitives.Float | None:
        """The Distance field value."""
        member = self.get_member("Distance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distance.setter
    def distance(self, value: primitives.Float) -> None:
        """Set the Distance field value."""
        member = self.get_member("Distance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Distance", fields.FieldFloat(value=value)
            )

    @property
    def transition_range(self) -> primitives.Float | None:
        """The TransitionRange field value."""
        member = self.get_member("TransitionRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @transition_range.setter
    def transition_range(self, value: primitives.Float) -> None:
        """Set the TransitionRange field value."""
        member = self.get_member("TransitionRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TransitionRange", fields.FieldFloat(value=value)
            )

    @property
    def near_texture(self) -> str | None:
        """Target ID of the NearTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("NearTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @near_texture.setter
    def near_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the NearTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("NearTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NearTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def far_texture(self) -> str | None:
        """Target ID of the FarTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("FarTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @far_texture.setter
    def far_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the FarTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("FarTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FarTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def near_texture_scale(self) -> primitives.Float2 | None:
        """The NearTextureScale field value."""
        member = self.get_member("NearTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_texture_scale.setter
    def near_texture_scale(self, value: primitives.Float2) -> None:
        """Set the NearTextureScale field value."""
        member = self.get_member("NearTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def near_texture_offset(self) -> primitives.Float2 | None:
        """The NearTextureOffset field value."""
        member = self.get_member("NearTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_texture_offset.setter
    def near_texture_offset(self, value: primitives.Float2) -> None:
        """Set the NearTextureOffset field value."""
        member = self.get_member("NearTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearTextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def far_texture_scale(self) -> primitives.Float2 | None:
        """The FarTextureScale field value."""
        member = self.get_member("FarTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_texture_scale.setter
    def far_texture_scale(self, value: primitives.Float2) -> None:
        """Set the FarTextureScale field value."""
        member = self.get_member("FarTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def far_texture_offset(self) -> primitives.Float2 | None:
        """The FarTextureOffset field value."""
        member = self.get_member("FarTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_texture_offset.setter
    def far_texture_offset(self, value: primitives.Float2) -> None:
        """Set the FarTextureOffset field value."""
        member = self.get_member("FarTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarTextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def near_color(self) -> primitives.ColorX | None:
        """The NearColor field value."""
        member = self.get_member("NearColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_color.setter
    def near_color(self, value: primitives.ColorX) -> None:
        """Set the NearColor field value."""
        member = self.get_member("NearColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearColor", fields.FieldColorX(value=value)
            )

    @property
    def far_color(self) -> primitives.ColorX | None:
        """The FarColor field value."""
        member = self.get_member("FarColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_color.setter
    def far_color(self, value: primitives.ColorX) -> None:
        """Set the FarColor field value."""
        member = self.get_member("FarColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarColor", fields.FieldColorX(value=value)
            )

    @property
    def use_vertex_colors(self) -> primitives.Bool | None:
        """The UseVertexColors field value."""
        member = self.get_member("UseVertexColors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_vertex_colors.setter
    def use_vertex_colors(self, value: primitives.Bool) -> None:
        """Set the UseVertexColors field value."""
        member = self.get_member("UseVertexColors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseVertexColors", fields.FieldBool(value=value)
            )

    @property
    def vertex_color_interpolation_space(self) -> members.FieldEnum | None:
        """The VertexColorInterpolationSpace member."""
        member = self.get_member("VertexColorInterpolationSpace")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @vertex_color_interpolation_space.setter
    def vertex_color_interpolation_space(self, value: members.FieldEnum) -> None:
        """Set the VertexColorInterpolationSpace member."""
        self.set_member("VertexColorInterpolationSpace", value)

    @property
    def blend_mode(self) -> members.FieldEnum | None:
        """The BlendMode member."""
        member = self.get_member("BlendMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @blend_mode.setter
    def blend_mode(self, value: members.FieldEnum) -> None:
        """Set the BlendMode member."""
        self.set_member("BlendMode", value)

    @property
    def alpha_cutoff(self) -> primitives.Float | None:
        """The AlphaCutoff field value."""
        member = self.get_member("AlphaCutoff")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @alpha_cutoff.setter
    def alpha_cutoff(self, value: primitives.Float) -> None:
        """Set the AlphaCutoff field value."""
        member = self.get_member("AlphaCutoff")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlphaCutoff", fields.FieldFloat(value=value)
            )

    @property
    def sidedness(self) -> members.FieldEnum | None:
        """The Sidedness member."""
        member = self.get_member("Sidedness")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @sidedness.setter
    def sidedness(self, value: members.FieldEnum) -> None:
        """Set the Sidedness member."""
        self.set_member("Sidedness", value)

    @property
    def zwrite(self) -> members.FieldEnum | None:
        """The ZWrite member."""
        member = self.get_member("ZWrite")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @zwrite.setter
    def zwrite(self, value: members.FieldEnum) -> None:
        """Set the ZWrite member."""
        self.set_member("ZWrite", value)

    @property
    def offset_factor(self) -> primitives.Float | None:
        """The OffsetFactor field value."""
        member = self.get_member("OffsetFactor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset_factor.setter
    def offset_factor(self, value: primitives.Float) -> None:
        """Set the OffsetFactor field value."""
        member = self.get_member("OffsetFactor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OffsetFactor", fields.FieldFloat(value=value)
            )

    @property
    def offset_units(self) -> primitives.Float | None:
        """The OffsetUnits field value."""
        member = self.get_member("OffsetUnits")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset_units.setter
    def offset_units(self, value: primitives.Float) -> None:
        """Set the OffsetUnits field value."""
        member = self.get_member("OffsetUnits")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OffsetUnits", fields.FieldFloat(value=value)
            )

    @property
    def render_queue(self) -> primitives.Int | None:
        """The RenderQueue field value."""
        member = self.get_member("RenderQueue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @render_queue.setter
    def render_queue(self, value: primitives.Int) -> None:
        """Set the RenderQueue field value."""
        member = self.get_member("RenderQueue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RenderQueue", fields.FieldInt(value=value)
            )

