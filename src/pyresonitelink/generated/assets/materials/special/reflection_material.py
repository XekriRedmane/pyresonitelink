"""Generated component: ReflectionMaterial."""

import numpy as np

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


class ReflectionMaterial(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ReflectionMaterial.

    Category: Assets/Materials/Special
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReflectionMaterial"

    def __init__(self, high_priority_integration: bool | None = None, shader: str | IAssetProvider[Shader] | None = None, reflection_texture: str | IAssetProvider[ITexture2D] | None = None, normal_map: str | IAssetProvider[ITexture2D] | None = None, normal_map_scale: primitives.Float2 | None = None, normal_map_offset: primitives.Float2 | None = None, distort: np.float32 | None = None, tint_color: primitives.ColorX | None = None, alpha_cutoff: np.float32 | None = None, offset_factor: np.float32 | None = None, offset_units: np.float32 | None = None, render_queue: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            reflection_texture: Initial value for ReflectionTexture.
            normal_map: Initial value for NormalMap.
            normal_map_scale: Initial value for NormalMapScale.
            normal_map_offset: Initial value for NormalMapOffset.
            distort: Initial value for Distort.
            tint_color: Initial value for TintColor.
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
        if reflection_texture is not None:
            self.reflection_texture = reflection_texture
        if normal_map is not None:
            self.normal_map = normal_map
        if normal_map_scale is not None:
            self.normal_map_scale = normal_map_scale
        if normal_map_offset is not None:
            self.normal_map_offset = normal_map_offset
        if distort is not None:
            self.distort = distort
        if tint_color is not None:
            self.tint_color = tint_color
        if alpha_cutoff is not None:
            self.alpha_cutoff = alpha_cutoff
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units
        if render_queue is not None:
            self.render_queue = render_queue

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
    def reflection_texture(self) -> str | None:
        """Target ID of the ReflectionTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("ReflectionTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reflection_texture.setter
    def reflection_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the ReflectionTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("ReflectionTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ReflectionTexture",
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
    def normal_map_scale(self) -> primitives.Float2 | None:
        """The NormalMapScale field value."""
        member = self.get_member("NormalMapScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_map_scale.setter
    def normal_map_scale(self, value: primitives.Float2) -> None:
        """Set the NormalMapScale field value."""
        member = self.get_member("NormalMapScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalMapScale", fields.FieldFloat2(value=value)
            )

    @property
    def normal_map_offset(self) -> primitives.Float2 | None:
        """The NormalMapOffset field value."""
        member = self.get_member("NormalMapOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_map_offset.setter
    def normal_map_offset(self, value: primitives.Float2) -> None:
        """Set the NormalMapOffset field value."""
        member = self.get_member("NormalMapOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalMapOffset", fields.FieldFloat2(value=value)
            )

    @property
    def distort(self) -> np.float32 | None:
        """The Distort field value."""
        member = self.get_member("Distort")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distort.setter
    def distort(self, value: np.float32) -> None:
        """Set the Distort field value."""
        member = self.get_member("Distort")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Distort", fields.FieldFloat(value=value)
            )

    @property
    def tint_color(self) -> primitives.ColorX | None:
        """The TintColor field value."""
        member = self.get_member("TintColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tint_color.setter
    def tint_color(self, value: primitives.ColorX) -> None:
        """Set the TintColor field value."""
        member = self.get_member("TintColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TintColor", fields.FieldColorX(value=value)
            )

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
    def alpha_cutoff(self) -> np.float32 | None:
        """The AlphaCutoff field value."""
        member = self.get_member("AlphaCutoff")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @alpha_cutoff.setter
    def alpha_cutoff(self, value: np.float32) -> None:
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
    def offset_factor(self) -> np.float32 | None:
        """The OffsetFactor field value."""
        member = self.get_member("OffsetFactor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset_factor.setter
    def offset_factor(self, value: np.float32) -> None:
        """Set the OffsetFactor field value."""
        member = self.get_member("OffsetFactor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OffsetFactor", fields.FieldFloat(value=value)
            )

    @property
    def offset_units(self) -> np.float32 | None:
        """The OffsetUnits field value."""
        member = self.get_member("OffsetUnits")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset_units.setter
    def offset_units(self, value: np.float32) -> None:
        """Set the OffsetUnits field value."""
        member = self.get_member("OffsetUnits")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OffsetUnits", fields.FieldFloat(value=value)
            )

    @property
    def render_queue(self) -> np.int32 | None:
        """The RenderQueue field value."""
        member = self.get_member("RenderQueue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @render_queue.setter
    def render_queue(self, value: np.int32) -> None:
        """Set the RenderQueue field value."""
        member = self.get_member("RenderQueue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RenderQueue", fields.FieldInt(value=value)
            )

