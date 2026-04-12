"""Generated component: OverlayFresnelMaterial."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.blend_mode import BlendMode
from pyresonitelink.generated._enums.sidedness import Sidedness
from pyresonitelink.generated._enums.zwrite import ZWrite
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OverlayFresnelMaterial(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The Overlay Fresnel Material functions similar to a Fresnel Material with the added attribute of displaying through objects.

    Category: Assets/Materials/Unlit

    Attach to a slot and put into the materials of a renderer like a
    SkinnedMeshRenderer or a MeshRenderer with a mesh to view what the
    material looks like.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.OverlayFresnelMaterial"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, shader: str | IAssetProvider[Shader] | None = None, exponent: primitives.Float | None = None, gamma_curve: primitives.Float | None = None, behind_far_color: primitives.ColorX | None = None, behind_near_color: primitives.ColorX | None = None, front_far_color: primitives.ColorX | None = None, front_near_color: primitives.ColorX | None = None, behind_far_texture: str | IAssetProvider[ITexture2D] | None = None, behind_near_texture: str | IAssetProvider[ITexture2D] | None = None, front_far_texture: str | IAssetProvider[ITexture2D] | None = None, front_near_texture: str | IAssetProvider[ITexture2D] | None = None, behind_far_texture_scale: primitives.Float2 | None = None, behind_far_texture_offset: primitives.Float2 | None = None, behind_near_texture_scale: primitives.Float2 | None = None, behind_near_texture_offset: primitives.Float2 | None = None, front_far_texture_scale: primitives.Float2 | None = None, front_far_texture_offset: primitives.Float2 | None = None, front_near_texture_scale: primitives.Float2 | None = None, front_near_texture_offset: primitives.Float2 | None = None, normal_map: str | IAssetProvider[ITexture2D] | None = None, blend_mode: BlendMode | str | None = None, sidedness: Sidedness | str | None = None, zwrite: ZWrite | str | None = None, render_queue: primitives.Int | None = None, offset_factor: primitives.Float | None = None, offset_units: primitives.Float | None = None, polar_uvmapping: primitives.Bool | None = None, polar_power: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            exponent: Initial value for Exponent.
            gamma_curve: Initial value for GammaCurve.
            behind_far_color: Initial value for BehindFarColor.
            behind_near_color: Initial value for BehindNearColor.
            front_far_color: Initial value for FrontFarColor.
            front_near_color: Initial value for FrontNearColor.
            behind_far_texture: Initial value for BehindFarTexture.
            behind_near_texture: Initial value for BehindNearTexture.
            front_far_texture: Initial value for FrontFarTexture.
            front_near_texture: Initial value for FrontNearTexture.
            behind_far_texture_scale: Initial value for BehindFarTextureScale.
            behind_far_texture_offset: Initial value for BehindFarTextureOffset.
            behind_near_texture_scale: Initial value for BehindNearTextureScale.
            behind_near_texture_offset: Initial value for BehindNearTextureOffset.
            front_far_texture_scale: Initial value for FrontFarTextureScale.
            front_far_texture_offset: Initial value for FrontFarTextureOffset.
            front_near_texture_scale: Initial value for FrontNearTextureScale.
            front_near_texture_offset: Initial value for FrontNearTextureOffset.
            normal_map: Initial value for NormalMap.
            blend_mode: Initial value for BlendMode.
            sidedness: Initial value for Sidedness.
            zwrite: Initial value for ZWrite.
            render_queue: Initial value for RenderQueue.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            polar_uvmapping: Initial value for PolarUVmapping.
            polar_power: Initial value for PolarPower.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if shader is not None:
            self.shader = shader
        if exponent is not None:
            self.exponent = exponent
        if gamma_curve is not None:
            self.gamma_curve = gamma_curve
        if behind_far_color is not None:
            self.behind_far_color = behind_far_color
        if behind_near_color is not None:
            self.behind_near_color = behind_near_color
        if front_far_color is not None:
            self.front_far_color = front_far_color
        if front_near_color is not None:
            self.front_near_color = front_near_color
        if behind_far_texture is not None:
            self.behind_far_texture = behind_far_texture
        if behind_near_texture is not None:
            self.behind_near_texture = behind_near_texture
        if front_far_texture is not None:
            self.front_far_texture = front_far_texture
        if front_near_texture is not None:
            self.front_near_texture = front_near_texture
        if behind_far_texture_scale is not None:
            self.behind_far_texture_scale = behind_far_texture_scale
        if behind_far_texture_offset is not None:
            self.behind_far_texture_offset = behind_far_texture_offset
        if behind_near_texture_scale is not None:
            self.behind_near_texture_scale = behind_near_texture_scale
        if behind_near_texture_offset is not None:
            self.behind_near_texture_offset = behind_near_texture_offset
        if front_far_texture_scale is not None:
            self.front_far_texture_scale = front_far_texture_scale
        if front_far_texture_offset is not None:
            self.front_far_texture_offset = front_far_texture_offset
        if front_near_texture_scale is not None:
            self.front_near_texture_scale = front_near_texture_scale
        if front_near_texture_offset is not None:
            self.front_near_texture_offset = front_near_texture_offset
        if normal_map is not None:
            self.normal_map = normal_map
        if blend_mode is not None:
            self.blend_mode = blend_mode
        if sidedness is not None:
            self.sidedness = sidedness
        if zwrite is not None:
            self.zwrite = zwrite
        if render_queue is not None:
            self.render_queue = render_queue
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units
        if polar_uvmapping is not None:
            self.polar_uvmapping = polar_uvmapping
        if polar_power is not None:
            self.polar_power = polar_power

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
    def exponent(self) -> primitives.Float | None:
        """The Exponent field value."""
        member = self.get_member("Exponent")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exponent.setter
    def exponent(self, value: primitives.Float) -> None:
        """Set the Exponent field value."""
        member = self.get_member("Exponent")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Exponent", fields.FieldFloat(value=value)
            )

    @property
    def gamma_curve(self) -> primitives.Float | None:
        """The GammaCurve field value."""
        member = self.get_member("GammaCurve")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gamma_curve.setter
    def gamma_curve(self, value: primitives.Float) -> None:
        """Set the GammaCurve field value."""
        member = self.get_member("GammaCurve")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GammaCurve", fields.FieldFloat(value=value)
            )

    @property
    def behind_far_color(self) -> primitives.ColorX | None:
        """The BehindFarColor field value."""
        member = self.get_member("BehindFarColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @behind_far_color.setter
    def behind_far_color(self, value: primitives.ColorX) -> None:
        """Set the BehindFarColor field value."""
        member = self.get_member("BehindFarColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BehindFarColor", fields.FieldColorX(value=value)
            )

    @property
    def behind_near_color(self) -> primitives.ColorX | None:
        """The BehindNearColor field value."""
        member = self.get_member("BehindNearColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @behind_near_color.setter
    def behind_near_color(self, value: primitives.ColorX) -> None:
        """Set the BehindNearColor field value."""
        member = self.get_member("BehindNearColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BehindNearColor", fields.FieldColorX(value=value)
            )

    @property
    def front_far_color(self) -> primitives.ColorX | None:
        """The FrontFarColor field value."""
        member = self.get_member("FrontFarColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @front_far_color.setter
    def front_far_color(self, value: primitives.ColorX) -> None:
        """Set the FrontFarColor field value."""
        member = self.get_member("FrontFarColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FrontFarColor", fields.FieldColorX(value=value)
            )

    @property
    def front_near_color(self) -> primitives.ColorX | None:
        """The FrontNearColor field value."""
        member = self.get_member("FrontNearColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @front_near_color.setter
    def front_near_color(self, value: primitives.ColorX) -> None:
        """Set the FrontNearColor field value."""
        member = self.get_member("FrontNearColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FrontNearColor", fields.FieldColorX(value=value)
            )

    @property
    def behind_far_texture(self) -> str | None:
        """Target ID of the BehindFarTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("BehindFarTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @behind_far_texture.setter
    def behind_far_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the BehindFarTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("BehindFarTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BehindFarTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def behind_near_texture(self) -> str | None:
        """Target ID of the BehindNearTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("BehindNearTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @behind_near_texture.setter
    def behind_near_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the BehindNearTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("BehindNearTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BehindNearTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def front_far_texture(self) -> str | None:
        """Target ID of the FrontFarTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("FrontFarTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @front_far_texture.setter
    def front_far_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the FrontFarTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("FrontFarTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FrontFarTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def front_near_texture(self) -> str | None:
        """Target ID of the FrontNearTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("FrontNearTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @front_near_texture.setter
    def front_near_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the FrontNearTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("FrontNearTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FrontNearTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def behind_far_texture_scale(self) -> primitives.Float2 | None:
        """The BehindFarTextureScale field value."""
        member = self.get_member("BehindFarTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @behind_far_texture_scale.setter
    def behind_far_texture_scale(self, value: primitives.Float2) -> None:
        """Set the BehindFarTextureScale field value."""
        member = self.get_member("BehindFarTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BehindFarTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def behind_far_texture_offset(self) -> primitives.Float2 | None:
        """The BehindFarTextureOffset field value."""
        member = self.get_member("BehindFarTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @behind_far_texture_offset.setter
    def behind_far_texture_offset(self, value: primitives.Float2) -> None:
        """Set the BehindFarTextureOffset field value."""
        member = self.get_member("BehindFarTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BehindFarTextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def behind_near_texture_scale(self) -> primitives.Float2 | None:
        """The BehindNearTextureScale field value."""
        member = self.get_member("BehindNearTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @behind_near_texture_scale.setter
    def behind_near_texture_scale(self, value: primitives.Float2) -> None:
        """Set the BehindNearTextureScale field value."""
        member = self.get_member("BehindNearTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BehindNearTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def behind_near_texture_offset(self) -> primitives.Float2 | None:
        """The BehindNearTextureOffset field value."""
        member = self.get_member("BehindNearTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @behind_near_texture_offset.setter
    def behind_near_texture_offset(self, value: primitives.Float2) -> None:
        """Set the BehindNearTextureOffset field value."""
        member = self.get_member("BehindNearTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BehindNearTextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def front_far_texture_scale(self) -> primitives.Float2 | None:
        """The FrontFarTextureScale field value."""
        member = self.get_member("FrontFarTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @front_far_texture_scale.setter
    def front_far_texture_scale(self, value: primitives.Float2) -> None:
        """Set the FrontFarTextureScale field value."""
        member = self.get_member("FrontFarTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FrontFarTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def front_far_texture_offset(self) -> primitives.Float2 | None:
        """The FrontFarTextureOffset field value."""
        member = self.get_member("FrontFarTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @front_far_texture_offset.setter
    def front_far_texture_offset(self, value: primitives.Float2) -> None:
        """Set the FrontFarTextureOffset field value."""
        member = self.get_member("FrontFarTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FrontFarTextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def front_near_texture_scale(self) -> primitives.Float2 | None:
        """The FrontNearTextureScale field value."""
        member = self.get_member("FrontNearTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @front_near_texture_scale.setter
    def front_near_texture_scale(self, value: primitives.Float2) -> None:
        """Set the FrontNearTextureScale field value."""
        member = self.get_member("FrontNearTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FrontNearTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def front_near_texture_offset(self) -> primitives.Float2 | None:
        """The FrontNearTextureOffset field value."""
        member = self.get_member("FrontNearTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @front_near_texture_offset.setter
    def front_near_texture_offset(self, value: primitives.Float2) -> None:
        """Set the FrontNearTextureOffset field value."""
        member = self.get_member("FrontNearTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FrontNearTextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def normal_map(self) -> str | None:
        """Target ID of the NormalMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("NormalMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @normal_map.setter
    def normal_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the NormalMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("NormalMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NormalMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def blend_mode(self) -> BlendMode | None:
        """The BlendMode enum value."""
        member = self.get_member("BlendMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return BlendMode(member.value)
        return None

    @blend_mode.setter
    def blend_mode(self, value: BlendMode | str) -> None:
        """Set the BlendMode enum value."""
        member = self.get_member("BlendMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "BlendMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def sidedness(self) -> Sidedness | None:
        """The Sidedness enum value."""
        member = self.get_member("Sidedness")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Sidedness(member.value)
        return None

    @sidedness.setter
    def sidedness(self, value: Sidedness | str) -> None:
        """Set the Sidedness enum value."""
        member = self.get_member("Sidedness")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Sidedness",
                members.FieldEnum(value=str(value)),
            )

    @property
    def zwrite(self) -> ZWrite | None:
        """The ZWrite enum value."""
        member = self.get_member("ZWrite")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ZWrite(member.value)
        return None

    @zwrite.setter
    def zwrite(self, value: ZWrite | str) -> None:
        """Set the ZWrite enum value."""
        member = self.get_member("ZWrite")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ZWrite",
                members.FieldEnum(value=str(value)),
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
    def polar_uvmapping(self) -> primitives.Bool | None:
        """The PolarUVmapping field value."""
        member = self.get_member("PolarUVmapping")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @polar_uvmapping.setter
    def polar_uvmapping(self, value: primitives.Bool) -> None:
        """Set the PolarUVmapping field value."""
        member = self.get_member("PolarUVmapping")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PolarUVmapping", fields.FieldBool(value=value)
            )

    @property
    def polar_power(self) -> primitives.Float | None:
        """The PolarPower field value."""
        member = self.get_member("PolarPower")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @polar_power.setter
    def polar_power(self, value: primitives.Float) -> None:
        """Set the PolarPower field value."""
        member = self.get_member("PolarPower")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PolarPower", fields.FieldFloat(value=value)
            )

