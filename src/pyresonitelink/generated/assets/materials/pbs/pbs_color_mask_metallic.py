"""Generated component: PBS_ColorMaskMetallic."""

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


class PBS_ColorMaskMetallic(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The PBS_ColorMaskMetallic material is a metallic material that allows for four distinct colors to be used separately or mixed in on different areas of the surface based on an image map.

    Category: Assets/Materials/PBS

    The ``ColorMask`` texture is a color mask that gets mapped to the four
    albedo/emissive channels to change individual tints for certain parts of
    the material. Other fields work as described on the PBS_Metallic
    material.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PBS_ColorMaskMetallic"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, shader: str | IAssetProvider[Shader] | None = None, texture_scale: primitives.Float2 | None = None, texture_offset: primitives.Float2 | None = None, color_mask_scale: primitives.Float2 | None = None, color_mask_offset: primitives.Float2 | None = None, color_mask: str | IAssetProvider[ITexture2D] | None = None, albedo_color0: primitives.ColorX | None = None, albedo_color1: primitives.ColorX | None = None, albedo_color2: primitives.ColorX | None = None, albedo_color3: primitives.ColorX | None = None, albedo_texture: str | IAssetProvider[ITexture2D] | None = None, emissive_color0: primitives.ColorX | None = None, emissive_color1: primitives.ColorX | None = None, emissive_color2: primitives.ColorX | None = None, emissive_color3: primitives.ColorX | None = None, emissive_map: str | IAssetProvider[ITexture2D] | None = None, normal_map: str | IAssetProvider[ITexture2D] | None = None, normal_scale: primitives.Float | None = None, occlusion_map: str | IAssetProvider[ITexture2D] | None = None, transparent_field: primitives.Bool | None = None, force_zwrite: primitives.Bool | None = None, offset_factor: primitives.Float | None = None, offset_units: primitives.Float | None = None, render_queue: primitives.Int | None = None, metallic: primitives.Float | None = None, smoothness: primitives.Float | None = None, metallic_map: str | IAssetProvider[ITexture2D] | None = None, regular: str | IAssetProvider[Shader] | None = None, transparent_ref: str | IAssetProvider[Shader] | None = None, zwrite: str | IAssetProvider[Shader] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            texture_scale: Initial value for TextureScale.
            texture_offset: Initial value for TextureOffset.
            color_mask_scale: Initial value for ColorMaskScale.
            color_mask_offset: Initial value for ColorMaskOffset.
            color_mask: Initial value for ColorMask.
            albedo_color0: Initial value for AlbedoColor0.
            albedo_color1: Initial value for AlbedoColor1.
            albedo_color2: Initial value for AlbedoColor2.
            albedo_color3: Initial value for AlbedoColor3.
            albedo_texture: Initial value for AlbedoTexture.
            emissive_color0: Initial value for EmissiveColor0.
            emissive_color1: Initial value for EmissiveColor1.
            emissive_color2: Initial value for EmissiveColor2.
            emissive_color3: Initial value for EmissiveColor3.
            emissive_map: Initial value for EmissiveMap.
            normal_map: Initial value for NormalMap.
            normal_scale: Initial value for NormalScale.
            occlusion_map: Initial value for OcclusionMap.
            transparent_field: Initial value for Transparent.
            force_zwrite: Initial value for ForceZWrite.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            render_queue: Initial value for RenderQueue.
            metallic: Initial value for Metallic.
            smoothness: Initial value for Smoothness.
            metallic_map: Initial value for MetallicMap.
            regular: Initial value for _regular.
            transparent_ref: Initial value for _transparent.
            zwrite: Initial value for _zwrite.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if shader is not None:
            self.shader = shader
        if texture_scale is not None:
            self.texture_scale = texture_scale
        if texture_offset is not None:
            self.texture_offset = texture_offset
        if color_mask_scale is not None:
            self.color_mask_scale = color_mask_scale
        if color_mask_offset is not None:
            self.color_mask_offset = color_mask_offset
        if color_mask is not None:
            self.color_mask = color_mask
        if albedo_color0 is not None:
            self.albedo_color0 = albedo_color0
        if albedo_color1 is not None:
            self.albedo_color1 = albedo_color1
        if albedo_color2 is not None:
            self.albedo_color2 = albedo_color2
        if albedo_color3 is not None:
            self.albedo_color3 = albedo_color3
        if albedo_texture is not None:
            self.albedo_texture = albedo_texture
        if emissive_color0 is not None:
            self.emissive_color0 = emissive_color0
        if emissive_color1 is not None:
            self.emissive_color1 = emissive_color1
        if emissive_color2 is not None:
            self.emissive_color2 = emissive_color2
        if emissive_color3 is not None:
            self.emissive_color3 = emissive_color3
        if emissive_map is not None:
            self.emissive_map = emissive_map
        if normal_map is not None:
            self.normal_map = normal_map
        if normal_scale is not None:
            self.normal_scale = normal_scale
        if occlusion_map is not None:
            self.occlusion_map = occlusion_map
        if transparent_field is not None:
            self.transparent_field = transparent_field
        if force_zwrite is not None:
            self.force_zwrite = force_zwrite
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units
        if render_queue is not None:
            self.render_queue = render_queue
        if metallic is not None:
            self.metallic = metallic
        if smoothness is not None:
            self.smoothness = smoothness
        if metallic_map is not None:
            self.metallic_map = metallic_map
        if regular is not None:
            self.regular = regular
        if transparent_ref is not None:
            self.transparent_ref = transparent_ref
        if zwrite is not None:
            self.zwrite = zwrite

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
    def texture_scale(self) -> primitives.Float2 | None:
        """The TextureScale field value."""
        member = self.get_member("TextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @texture_scale.setter
    def texture_scale(self, value: primitives.Float2) -> None:
        """Set the TextureScale field value."""
        member = self.get_member("TextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def texture_offset(self) -> primitives.Float2 | None:
        """The TextureOffset field value."""
        member = self.get_member("TextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @texture_offset.setter
    def texture_offset(self, value: primitives.Float2) -> None:
        """Set the TextureOffset field value."""
        member = self.get_member("TextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def color_mask_scale(self) -> primitives.Float2 | None:
        """The ColorMaskScale field value."""
        member = self.get_member("ColorMaskScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color_mask_scale.setter
    def color_mask_scale(self, value: primitives.Float2) -> None:
        """Set the ColorMaskScale field value."""
        member = self.get_member("ColorMaskScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ColorMaskScale", fields.FieldFloat2(value=value)
            )

    @property
    def color_mask_offset(self) -> primitives.Float2 | None:
        """The ColorMaskOffset field value."""
        member = self.get_member("ColorMaskOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color_mask_offset.setter
    def color_mask_offset(self, value: primitives.Float2) -> None:
        """Set the ColorMaskOffset field value."""
        member = self.get_member("ColorMaskOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ColorMaskOffset", fields.FieldFloat2(value=value)
            )

    @property
    def color_mask(self) -> str | None:
        """Target ID of the ColorMask reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("ColorMask")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color_mask.setter
    def color_mask(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the ColorMask reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("ColorMask")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ColorMask",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def albedo_color0(self) -> primitives.ColorX | None:
        """The AlbedoColor0 field value."""
        member = self.get_member("AlbedoColor0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @albedo_color0.setter
    def albedo_color0(self, value: primitives.ColorX) -> None:
        """Set the AlbedoColor0 field value."""
        member = self.get_member("AlbedoColor0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlbedoColor0", fields.FieldColorX(value=value)
            )

    @property
    def albedo_color1(self) -> primitives.ColorX | None:
        """The AlbedoColor1 field value."""
        member = self.get_member("AlbedoColor1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @albedo_color1.setter
    def albedo_color1(self, value: primitives.ColorX) -> None:
        """Set the AlbedoColor1 field value."""
        member = self.get_member("AlbedoColor1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlbedoColor1", fields.FieldColorX(value=value)
            )

    @property
    def albedo_color2(self) -> primitives.ColorX | None:
        """The AlbedoColor2 field value."""
        member = self.get_member("AlbedoColor2")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @albedo_color2.setter
    def albedo_color2(self, value: primitives.ColorX) -> None:
        """Set the AlbedoColor2 field value."""
        member = self.get_member("AlbedoColor2")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlbedoColor2", fields.FieldColorX(value=value)
            )

    @property
    def albedo_color3(self) -> primitives.ColorX | None:
        """The AlbedoColor3 field value."""
        member = self.get_member("AlbedoColor3")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @albedo_color3.setter
    def albedo_color3(self, value: primitives.ColorX) -> None:
        """Set the AlbedoColor3 field value."""
        member = self.get_member("AlbedoColor3")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlbedoColor3", fields.FieldColorX(value=value)
            )

    @property
    def albedo_texture(self) -> str | None:
        """Target ID of the AlbedoTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("AlbedoTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @albedo_texture.setter
    def albedo_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the AlbedoTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("AlbedoTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AlbedoTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def emissive_color0(self) -> primitives.ColorX | None:
        """The EmissiveColor0 field value."""
        member = self.get_member("EmissiveColor0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emissive_color0.setter
    def emissive_color0(self, value: primitives.ColorX) -> None:
        """Set the EmissiveColor0 field value."""
        member = self.get_member("EmissiveColor0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissiveColor0", fields.FieldColorX(value=value)
            )

    @property
    def emissive_color1(self) -> primitives.ColorX | None:
        """The EmissiveColor1 field value."""
        member = self.get_member("EmissiveColor1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emissive_color1.setter
    def emissive_color1(self, value: primitives.ColorX) -> None:
        """Set the EmissiveColor1 field value."""
        member = self.get_member("EmissiveColor1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissiveColor1", fields.FieldColorX(value=value)
            )

    @property
    def emissive_color2(self) -> primitives.ColorX | None:
        """The EmissiveColor2 field value."""
        member = self.get_member("EmissiveColor2")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emissive_color2.setter
    def emissive_color2(self, value: primitives.ColorX) -> None:
        """Set the EmissiveColor2 field value."""
        member = self.get_member("EmissiveColor2")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissiveColor2", fields.FieldColorX(value=value)
            )

    @property
    def emissive_color3(self) -> primitives.ColorX | None:
        """The EmissiveColor3 field value."""
        member = self.get_member("EmissiveColor3")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emissive_color3.setter
    def emissive_color3(self, value: primitives.ColorX) -> None:
        """Set the EmissiveColor3 field value."""
        member = self.get_member("EmissiveColor3")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissiveColor3", fields.FieldColorX(value=value)
            )

    @property
    def emissive_map(self) -> str | None:
        """Target ID of the EmissiveMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("EmissiveMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @emissive_map.setter
    def emissive_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the EmissiveMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("EmissiveMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EmissiveMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
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
    def normal_scale(self) -> primitives.Float | None:
        """The NormalScale field value."""
        member = self.get_member("NormalScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_scale.setter
    def normal_scale(self, value: primitives.Float) -> None:
        """Set the NormalScale field value."""
        member = self.get_member("NormalScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalScale", fields.FieldFloat(value=value)
            )

    @property
    def occlusion_map(self) -> str | None:
        """Target ID of the OcclusionMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("OcclusionMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @occlusion_map.setter
    def occlusion_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the OcclusionMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("OcclusionMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OcclusionMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def transparent_field(self) -> primitives.Bool | None:
        """The Transparent field value."""
        member = self.get_member("Transparent")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @transparent_field.setter
    def transparent_field(self, value: primitives.Bool) -> None:
        """Set the Transparent field value."""
        member = self.get_member("Transparent")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Transparent", fields.FieldBool(value=value)
            )

    @property
    def force_zwrite(self) -> primitives.Bool | None:
        """The ForceZWrite field value."""
        member = self.get_member("ForceZWrite")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_zwrite.setter
    def force_zwrite(self, value: primitives.Bool) -> None:
        """Set the ForceZWrite field value."""
        member = self.get_member("ForceZWrite")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceZWrite", fields.FieldBool(value=value)
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
    def metallic(self) -> primitives.Float | None:
        """The Metallic field value."""
        member = self.get_member("Metallic")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @metallic.setter
    def metallic(self, value: primitives.Float) -> None:
        """Set the Metallic field value."""
        member = self.get_member("Metallic")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Metallic", fields.FieldFloat(value=value)
            )

    @property
    def smoothness(self) -> primitives.Float | None:
        """The Smoothness field value."""
        member = self.get_member("Smoothness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smoothness.setter
    def smoothness(self, value: primitives.Float) -> None:
        """Set the Smoothness field value."""
        member = self.get_member("Smoothness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Smoothness", fields.FieldFloat(value=value)
            )

    @property
    def metallic_map(self) -> str | None:
        """Target ID of the MetallicMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("MetallicMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @metallic_map.setter
    def metallic_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the MetallicMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("MetallicMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MetallicMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def regular(self) -> str | None:
        """Target ID of the _regular reference (targets IAssetProvider[Shader])."""
        member = self.get_member("_regular")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @regular.setter
    def regular(self, target: str | IAssetProvider[Shader] | None) -> None:
        """Set the _regular reference by target ID or IAssetProvider[Shader] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_regular")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_regular",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Shader>'),
            )

    @property
    def transparent_ref(self) -> str | None:
        """Target ID of the _transparent reference (targets IAssetProvider[Shader])."""
        member = self.get_member("_transparent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @transparent_ref.setter
    def transparent_ref(self, target: str | IAssetProvider[Shader] | None) -> None:
        """Set the _transparent reference by target ID or IAssetProvider[Shader] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_transparent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_transparent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Shader>'),
            )

    @property
    def zwrite(self) -> str | None:
        """Target ID of the _zwrite reference (targets IAssetProvider[Shader])."""
        member = self.get_member("_zwrite")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @zwrite.setter
    def zwrite(self, target: str | IAssetProvider[Shader] | None) -> None:
        """Set the _zwrite reference by target ID or IAssetProvider[Shader] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_zwrite")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_zwrite",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Shader>'),
            )

