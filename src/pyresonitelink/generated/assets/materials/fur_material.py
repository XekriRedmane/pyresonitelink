"""Generated component: FurMaterial."""

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


class FurMaterial(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The FurMaterial component is used to make multi layered geometry out of a mesh's original geometry that has a specified distance between layers. The number of layers is a constant 20. Combined with a map to create holes in the layers via alpha, this creates the illusion of depth and fur like properties. The geometry layers are instanced on the GPU.

Some players have reported lag when using Fur materials. This is due to either using too large of a texture, or due to an issue called Overdraw.

Overdraw is caused when the GPU generates pixels for a layer for where it appears on the screen in a stage in rendering called "Rasterization" when it is done, it renders the next layer, and has to draw that on top of the already drawn layer pixels. The drawing on top for the next 19 layers is called Overdraw.

This means that if a user looks very closely at a fur shader, or the shader covers their entire screen while all layers are in front of the camera, it will lag intensely. This is because the game is doing 20 drawing cycles on every pixel. Causing significant lag.

    Category: Assets/Materials

    Insert into a MeshRenderer or SkinnedMeshRenderer with a mesh to view
    what the material looks like.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FurMaterial"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, shader: str | IAssetProvider[Shader] | None = None, color: primitives.ColorX | None = None, specular_color: primitives.ColorX | None = None, shininess: primitives.Float | None = None, gloss: primitives.Float | None = None, rim_color: primitives.ColorX | None = None, rim_power: primitives.Float | None = None, fur_length: primitives.Float | None = None, fur_hardness: primitives.Float | None = None, fur_thinness: primitives.Float | None = None, fur_shading: primitives.Float | None = None, fur_coloring: primitives.Float | None = None, base: str | IAssetProvider[ITexture2D] | None = None, normal_map: str | IAssetProvider[ITexture2D] | None = None, noise: str | IAssetProvider[ITexture2D] | None = None, texture_scale: primitives.Float2 | None = None, texture_offset: primitives.Float2 | None = None, alpha_cutoff: primitives.Float | None = None, force_global: primitives.Float4 | None = None, force_local: primitives.Float4 | None = None, render_queue: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            color: Initial value for Color.
            specular_color: Initial value for SpecularColor.
            shininess: Initial value for Shininess.
            gloss: Initial value for Gloss.
            rim_color: Initial value for RimColor.
            rim_power: Initial value for RimPower.
            fur_length: Initial value for FurLength.
            fur_hardness: Initial value for FurHardness.
            fur_thinness: Initial value for FurThinness.
            fur_shading: Initial value for FurShading.
            fur_coloring: Initial value for FurColoring.
            base: Initial value for Base.
            normal_map: Initial value for NormalMap.
            noise: Initial value for Noise.
            texture_scale: Initial value for TextureScale.
            texture_offset: Initial value for TextureOffset.
            alpha_cutoff: Initial value for AlphaCutoff.
            force_global: Initial value for ForceGlobal.
            force_local: Initial value for ForceLocal.
            render_queue: Initial value for RenderQueue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if shader is not None:
            self.shader = shader
        if color is not None:
            self.color = color
        if specular_color is not None:
            self.specular_color = specular_color
        if shininess is not None:
            self.shininess = shininess
        if gloss is not None:
            self.gloss = gloss
        if rim_color is not None:
            self.rim_color = rim_color
        if rim_power is not None:
            self.rim_power = rim_power
        if fur_length is not None:
            self.fur_length = fur_length
        if fur_hardness is not None:
            self.fur_hardness = fur_hardness
        if fur_thinness is not None:
            self.fur_thinness = fur_thinness
        if fur_shading is not None:
            self.fur_shading = fur_shading
        if fur_coloring is not None:
            self.fur_coloring = fur_coloring
        if base is not None:
            self.base = base
        if normal_map is not None:
            self.normal_map = normal_map
        if noise is not None:
            self.noise = noise
        if texture_scale is not None:
            self.texture_scale = texture_scale
        if texture_offset is not None:
            self.texture_offset = texture_offset
        if alpha_cutoff is not None:
            self.alpha_cutoff = alpha_cutoff
        if force_global is not None:
            self.force_global = force_global
        if force_local is not None:
            self.force_local = force_local
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
    def color(self) -> primitives.ColorX | None:
        """The Color field value."""
        member = self.get_member("Color")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color.setter
    def color(self, value: primitives.ColorX) -> None:
        """Set the Color field value."""
        member = self.get_member("Color")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Color", fields.FieldColorX(value=value)
            )

    @property
    def specular_color(self) -> primitives.ColorX | None:
        """The SpecularColor field value."""
        member = self.get_member("SpecularColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @specular_color.setter
    def specular_color(self, value: primitives.ColorX) -> None:
        """Set the SpecularColor field value."""
        member = self.get_member("SpecularColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpecularColor", fields.FieldColorX(value=value)
            )

    @property
    def shininess(self) -> primitives.Float | None:
        """The Shininess field value."""
        member = self.get_member("Shininess")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shininess.setter
    def shininess(self, value: primitives.Float) -> None:
        """Set the Shininess field value."""
        member = self.get_member("Shininess")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Shininess", fields.FieldFloat(value=value)
            )

    @property
    def gloss(self) -> primitives.Float | None:
        """The Gloss field value."""
        member = self.get_member("Gloss")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gloss.setter
    def gloss(self, value: primitives.Float) -> None:
        """Set the Gloss field value."""
        member = self.get_member("Gloss")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Gloss", fields.FieldFloat(value=value)
            )

    @property
    def rim_color(self) -> primitives.ColorX | None:
        """The RimColor field value."""
        member = self.get_member("RimColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rim_color.setter
    def rim_color(self, value: primitives.ColorX) -> None:
        """Set the RimColor field value."""
        member = self.get_member("RimColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RimColor", fields.FieldColorX(value=value)
            )

    @property
    def rim_power(self) -> primitives.Float | None:
        """The RimPower field value."""
        member = self.get_member("RimPower")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rim_power.setter
    def rim_power(self, value: primitives.Float) -> None:
        """Set the RimPower field value."""
        member = self.get_member("RimPower")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RimPower", fields.FieldFloat(value=value)
            )

    @property
    def fur_length(self) -> primitives.Float | None:
        """The FurLength field value."""
        member = self.get_member("FurLength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fur_length.setter
    def fur_length(self, value: primitives.Float) -> None:
        """Set the FurLength field value."""
        member = self.get_member("FurLength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FurLength", fields.FieldFloat(value=value)
            )

    @property
    def fur_hardness(self) -> primitives.Float | None:
        """The FurHardness field value."""
        member = self.get_member("FurHardness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fur_hardness.setter
    def fur_hardness(self, value: primitives.Float) -> None:
        """Set the FurHardness field value."""
        member = self.get_member("FurHardness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FurHardness", fields.FieldFloat(value=value)
            )

    @property
    def fur_thinness(self) -> primitives.Float | None:
        """The FurThinness field value."""
        member = self.get_member("FurThinness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fur_thinness.setter
    def fur_thinness(self, value: primitives.Float) -> None:
        """Set the FurThinness field value."""
        member = self.get_member("FurThinness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FurThinness", fields.FieldFloat(value=value)
            )

    @property
    def fur_shading(self) -> primitives.Float | None:
        """The FurShading field value."""
        member = self.get_member("FurShading")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fur_shading.setter
    def fur_shading(self, value: primitives.Float) -> None:
        """Set the FurShading field value."""
        member = self.get_member("FurShading")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FurShading", fields.FieldFloat(value=value)
            )

    @property
    def fur_coloring(self) -> primitives.Float | None:
        """The FurColoring field value."""
        member = self.get_member("FurColoring")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fur_coloring.setter
    def fur_coloring(self, value: primitives.Float) -> None:
        """Set the FurColoring field value."""
        member = self.get_member("FurColoring")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FurColoring", fields.FieldFloat(value=value)
            )

    @property
    def base(self) -> str | None:
        """Target ID of the Base reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("Base")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @base.setter
    def base(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the Base reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Base")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Base",
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
    def noise(self) -> str | None:
        """Target ID of the Noise reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("Noise")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @noise.setter
    def noise(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the Noise reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Noise")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Noise",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
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
    def force_global(self) -> primitives.Float4 | None:
        """The ForceGlobal field value."""
        member = self.get_member("ForceGlobal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_global.setter
    def force_global(self, value: primitives.Float4) -> None:
        """Set the ForceGlobal field value."""
        member = self.get_member("ForceGlobal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceGlobal", fields.FieldFloat4(value=value)
            )

    @property
    def force_local(self) -> primitives.Float4 | None:
        """The ForceLocal field value."""
        member = self.get_member("ForceLocal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_local.setter
    def force_local(self, value: primitives.Float4) -> None:
        """Set the ForceLocal field value."""
        member = self.get_member("ForceLocal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceLocal", fields.FieldFloat4(value=value)
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

