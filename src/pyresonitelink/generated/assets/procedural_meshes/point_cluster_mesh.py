"""Generated component: PointClusterMesh."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture import ITexture
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.atlas_info import AtlasInfo
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PointClusterMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PointClusterMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PointClusterMesh"

    def __init__(self, high_priority_integration: bool | None = None, override_bounding_box: bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, texture_color_source: str | IAssetProvider[ITexture] | None = None, height_scale_source: str | IAssetProvider[Texture2D] | None = None, texture_intensity_clip: np.float32 | None = None, texture_alpha_clip: np.float32 | None = None, max_clip_attempts: np.int32 | None = None, heightmap_exp: np.float32 | None = None, seed: np.int32 | None = None, points: np.int32 | None = None, atlas: str | AtlasInfo | None = None, scale: primitives.Float3 | None = None, range_exp: np.float32 | None = None, jitter_range: primitives.Float3 | None = None, color0: primitives.ColorX | None = None, color1: primitives.ColorX | None = None, color_lerp_scale: np.float32 | None = None, color_gap: np.float32 | None = None, simplex_noise_scale: primitives.Float3 | None = None, simplex_noise_offset: primitives.Float3 | None = None, uniform_size: bool | None = None, min_size: primitives.Float2 | None = None, max_size: primitives.Float2 | None = None, min_rotation: np.float32 | None = None, max_rotation: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            texture_color_source: Initial value for TextureColorSource.
            height_scale_source: Initial value for HeightScaleSource.
            texture_intensity_clip: Initial value for TextureIntensityClip.
            texture_alpha_clip: Initial value for TextureAlphaClip.
            max_clip_attempts: Initial value for MaxClipAttempts.
            heightmap_exp: Initial value for HeightmapExp.
            seed: Initial value for Seed.
            points: Initial value for Points.
            atlas: Initial value for Atlas.
            scale: Initial value for Scale.
            range_exp: Initial value for RangeExp.
            jitter_range: Initial value for JitterRange.
            color0: Initial value for Color0.
            color1: Initial value for Color1.
            color_lerp_scale: Initial value for ColorLerpScale.
            color_gap: Initial value for ColorGap.
            simplex_noise_scale: Initial value for SimplexNoiseScale.
            simplex_noise_offset: Initial value for SimplexNoiseOffset.
            uniform_size: Initial value for UniformSize.
            min_size: Initial value for MinSize.
            max_size: Initial value for MaxSize.
            min_rotation: Initial value for MinRotation.
            max_rotation: Initial value for MaxRotation.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if texture_color_source is not None:
            self.texture_color_source = texture_color_source
        if height_scale_source is not None:
            self.height_scale_source = height_scale_source
        if texture_intensity_clip is not None:
            self.texture_intensity_clip = texture_intensity_clip
        if texture_alpha_clip is not None:
            self.texture_alpha_clip = texture_alpha_clip
        if max_clip_attempts is not None:
            self.max_clip_attempts = max_clip_attempts
        if heightmap_exp is not None:
            self.heightmap_exp = heightmap_exp
        if seed is not None:
            self.seed = seed
        if points is not None:
            self.points = points
        if atlas is not None:
            self.atlas = atlas
        if scale is not None:
            self.scale = scale
        if range_exp is not None:
            self.range_exp = range_exp
        if jitter_range is not None:
            self.jitter_range = jitter_range
        if color0 is not None:
            self.color0 = color0
        if color1 is not None:
            self.color1 = color1
        if color_lerp_scale is not None:
            self.color_lerp_scale = color_lerp_scale
        if color_gap is not None:
            self.color_gap = color_gap
        if simplex_noise_scale is not None:
            self.simplex_noise_scale = simplex_noise_scale
        if simplex_noise_offset is not None:
            self.simplex_noise_offset = simplex_noise_offset
        if uniform_size is not None:
            self.uniform_size = uniform_size
        if min_size is not None:
            self.min_size = min_size
        if max_size is not None:
            self.max_size = max_size
        if min_rotation is not None:
            self.min_rotation = min_rotation
        if max_rotation is not None:
            self.max_rotation = max_rotation

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
    def distribution(self) -> members.FieldEnum | None:
        """The Distribution member."""
        member = self.get_member("Distribution")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @distribution.setter
    def distribution(self, value: members.FieldEnum) -> None:
        """Set the Distribution member."""
        self.set_member("Distribution", value)

    @property
    def colors(self) -> members.FieldEnum | None:
        """The Colors member."""
        member = self.get_member("Colors")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @colors.setter
    def colors(self, value: members.FieldEnum) -> None:
        """Set the Colors member."""
        self.set_member("Colors", value)

    @property
    def texture_color_source(self) -> str | None:
        """Target ID of the TextureColorSource reference (targets IAssetProvider[ITexture])."""
        member = self.get_member("TextureColorSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture_color_source.setter
    def texture_color_source(self, target: str | IAssetProvider[ITexture] | None) -> None:
        """Set the TextureColorSource reference by target ID or IAssetProvider[ITexture] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("TextureColorSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TextureColorSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture>'),
            )

    @property
    def height_scale_source(self) -> str | None:
        """Target ID of the HeightScaleSource reference (targets IAssetProvider[Texture2D])."""
        member = self.get_member("HeightScaleSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @height_scale_source.setter
    def height_scale_source(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the HeightScaleSource reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("HeightScaleSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HeightScaleSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

    @property
    def texture_intensity_clip(self) -> np.float32 | None:
        """The TextureIntensityClip field value."""
        member = self.get_member("TextureIntensityClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @texture_intensity_clip.setter
    def texture_intensity_clip(self, value: np.float32) -> None:
        """Set the TextureIntensityClip field value."""
        member = self.get_member("TextureIntensityClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TextureIntensityClip", fields.FieldFloat(value=value)
            )

    @property
    def texture_alpha_clip(self) -> np.float32 | None:
        """The TextureAlphaClip field value."""
        member = self.get_member("TextureAlphaClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @texture_alpha_clip.setter
    def texture_alpha_clip(self, value: np.float32) -> None:
        """Set the TextureAlphaClip field value."""
        member = self.get_member("TextureAlphaClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TextureAlphaClip", fields.FieldFloat(value=value)
            )

    @property
    def max_clip_attempts(self) -> np.int32 | None:
        """The MaxClipAttempts field value."""
        member = self.get_member("MaxClipAttempts")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_clip_attempts.setter
    def max_clip_attempts(self, value: np.int32) -> None:
        """Set the MaxClipAttempts field value."""
        member = self.get_member("MaxClipAttempts")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxClipAttempts", fields.FieldInt(value=value)
            )

    @property
    def heightmap_exp(self) -> np.float32 | None:
        """The HeightmapExp field value."""
        member = self.get_member("HeightmapExp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @heightmap_exp.setter
    def heightmap_exp(self, value: np.float32) -> None:
        """Set the HeightmapExp field value."""
        member = self.get_member("HeightmapExp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeightmapExp", fields.FieldFloat(value=value)
            )

    @property
    def seed(self) -> np.int32 | None:
        """The Seed field value."""
        member = self.get_member("Seed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @seed.setter
    def seed(self, value: np.int32) -> None:
        """Set the Seed field value."""
        member = self.get_member("Seed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Seed", fields.FieldInt(value=value)
            )

    @property
    def points(self) -> np.int32 | None:
        """The Points field value."""
        member = self.get_member("Points")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @points.setter
    def points(self, value: np.int32) -> None:
        """Set the Points field value."""
        member = self.get_member("Points")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Points", fields.FieldInt(value=value)
            )

    @property
    def atlas(self) -> str | None:
        """Target ID of the Atlas reference (targets AtlasInfo)."""
        member = self.get_member("Atlas")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @atlas.setter
    def atlas(self, target: str | AtlasInfo | None) -> None:
        """Set the Atlas reference by target ID or AtlasInfo instance."""
        target_id: str | None = target.id if isinstance(target, AtlasInfo) else target  # type: ignore[assignment]
        member = self.get_member("Atlas")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Atlas",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AtlasInfo'),
            )

    @property
    def scale(self) -> primitives.Float3 | None:
        """The Scale field value."""
        member = self.get_member("Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale.setter
    def scale(self, value: primitives.Float3) -> None:
        """Set the Scale field value."""
        member = self.get_member("Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Scale", fields.FieldFloat3(value=value)
            )

    @property
    def range_exp(self) -> np.float32 | None:
        """The RangeExp field value."""
        member = self.get_member("RangeExp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @range_exp.setter
    def range_exp(self, value: np.float32) -> None:
        """Set the RangeExp field value."""
        member = self.get_member("RangeExp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RangeExp", fields.FieldFloat(value=value)
            )

    @property
    def jitter_range(self) -> primitives.Float3 | None:
        """The JitterRange field value."""
        member = self.get_member("JitterRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @jitter_range.setter
    def jitter_range(self, value: primitives.Float3) -> None:
        """Set the JitterRange field value."""
        member = self.get_member("JitterRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "JitterRange", fields.FieldFloat3(value=value)
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
    def color_lerp_scale(self) -> np.float32 | None:
        """The ColorLerpScale field value."""
        member = self.get_member("ColorLerpScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color_lerp_scale.setter
    def color_lerp_scale(self, value: np.float32) -> None:
        """Set the ColorLerpScale field value."""
        member = self.get_member("ColorLerpScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ColorLerpScale", fields.FieldFloat(value=value)
            )

    @property
    def color_gap(self) -> np.float32 | None:
        """The ColorGap field value."""
        member = self.get_member("ColorGap")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color_gap.setter
    def color_gap(self, value: np.float32) -> None:
        """Set the ColorGap field value."""
        member = self.get_member("ColorGap")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ColorGap", fields.FieldFloat(value=value)
            )

    @property
    def simplex_noise_scale(self) -> primitives.Float3 | None:
        """The SimplexNoiseScale field value."""
        member = self.get_member("SimplexNoiseScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @simplex_noise_scale.setter
    def simplex_noise_scale(self, value: primitives.Float3) -> None:
        """Set the SimplexNoiseScale field value."""
        member = self.get_member("SimplexNoiseScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SimplexNoiseScale", fields.FieldFloat3(value=value)
            )

    @property
    def simplex_noise_offset(self) -> primitives.Float3 | None:
        """The SimplexNoiseOffset field value."""
        member = self.get_member("SimplexNoiseOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @simplex_noise_offset.setter
    def simplex_noise_offset(self, value: primitives.Float3) -> None:
        """Set the SimplexNoiseOffset field value."""
        member = self.get_member("SimplexNoiseOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SimplexNoiseOffset", fields.FieldFloat3(value=value)
            )

    @property
    def uniform_size(self) -> bool | None:
        """The UniformSize field value."""
        member = self.get_member("UniformSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uniform_size.setter
    def uniform_size(self, value: bool) -> None:
        """Set the UniformSize field value."""
        member = self.get_member("UniformSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UniformSize", fields.FieldBool(value=value)
            )

    @property
    def min_size(self) -> primitives.Float2 | None:
        """The MinSize field value."""
        member = self.get_member("MinSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_size.setter
    def min_size(self, value: primitives.Float2) -> None:
        """Set the MinSize field value."""
        member = self.get_member("MinSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinSize", fields.FieldFloat2(value=value)
            )

    @property
    def max_size(self) -> primitives.Float2 | None:
        """The MaxSize field value."""
        member = self.get_member("MaxSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_size.setter
    def max_size(self, value: primitives.Float2) -> None:
        """Set the MaxSize field value."""
        member = self.get_member("MaxSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSize", fields.FieldFloat2(value=value)
            )

    @property
    def min_rotation(self) -> np.float32 | None:
        """The MinRotation field value."""
        member = self.get_member("MinRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_rotation.setter
    def min_rotation(self, value: np.float32) -> None:
        """Set the MinRotation field value."""
        member = self.get_member("MinRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinRotation", fields.FieldFloat(value=value)
            )

    @property
    def max_rotation(self) -> np.float32 | None:
        """The MaxRotation field value."""
        member = self.get_member("MaxRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_rotation.setter
    def max_rotation(self, value: np.float32) -> None:
        """Set the MaxRotation field value."""
        member = self.get_member("MaxRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxRotation", fields.FieldFloat(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

