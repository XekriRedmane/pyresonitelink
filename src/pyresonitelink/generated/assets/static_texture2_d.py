"""Generated component: StaticTexture2D."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itexture2_dprovider import ITexture2DProvider
from pyresonitelink.generated._types.istatic_asset_provider import IStaticAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StaticTexture2D(GeneratedComponent, ITexture2DProvider, IStaticAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.StaticTexture2D.

    Category: Assets
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.StaticTexture2D"

    @property
    def url(self) -> str | None:
        """The URL field value."""
        member = self.get_member("URL")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @url.setter
    def url(self, value: str) -> None:
        """Set the URL field value."""
        member = self.get_member("URL")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "URL", fields.FieldUri(value=value)
            )

    @property
    def filter_mode(self) -> members.FieldEnum | None:
        """The FilterMode member."""
        member = self.get_member("FilterMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @filter_mode.setter
    def filter_mode(self, value: members.FieldEnum) -> None:
        """Set the FilterMode member."""
        self.set_member("FilterMode", value)

    @property
    def anisotropic_level(self) -> np.int32 | None:
        """The AnisotropicLevel field value."""
        member = self.get_member("AnisotropicLevel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anisotropic_level.setter
    def anisotropic_level(self, value: np.int32) -> None:
        """Set the AnisotropicLevel field value."""
        member = self.get_member("AnisotropicLevel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnisotropicLevel", fields.FieldNullableInt(value=value)
            )

    @property
    def uncompressed(self) -> bool | None:
        """The Uncompressed field value."""
        member = self.get_member("Uncompressed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uncompressed.setter
    def uncompressed(self, value: bool) -> None:
        """Set the Uncompressed field value."""
        member = self.get_member("Uncompressed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Uncompressed", fields.FieldBool(value=value)
            )

    @property
    def direct_load(self) -> bool | None:
        """The DirectLoad field value."""
        member = self.get_member("DirectLoad")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @direct_load.setter
    def direct_load(self, value: bool) -> None:
        """Set the DirectLoad field value."""
        member = self.get_member("DirectLoad")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DirectLoad", fields.FieldBool(value=value)
            )

    @property
    def force_exact_variant(self) -> bool | None:
        """The ForceExactVariant field value."""
        member = self.get_member("ForceExactVariant")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_exact_variant.setter
    def force_exact_variant(self, value: bool) -> None:
        """Set the ForceExactVariant field value."""
        member = self.get_member("ForceExactVariant")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceExactVariant", fields.FieldBool(value=value)
            )

    @property
    def preferred_format(self) -> members.FieldEnum | None:
        """The PreferredFormat member."""
        member = self.get_member("PreferredFormat")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @preferred_format.setter
    def preferred_format(self, value: members.FieldEnum) -> None:
        """Set the PreferredFormat member."""
        self.set_member("PreferredFormat", value)

    @property
    def preferred_profile(self) -> members.FieldEnum | None:
        """The PreferredProfile member."""
        member = self.get_member("PreferredProfile")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @preferred_profile.setter
    def preferred_profile(self, value: members.FieldEnum) -> None:
        """Set the PreferredProfile member."""
        self.set_member("PreferredProfile", value)

    @property
    def mip_map_bias(self) -> np.float32 | None:
        """The MipMapBias field value."""
        member = self.get_member("MipMapBias")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mip_map_bias.setter
    def mip_map_bias(self, value: np.float32) -> None:
        """Set the MipMapBias field value."""
        member = self.get_member("MipMapBias")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MipMapBias", fields.FieldFloat(value=value)
            )

    @property
    def is_normal_map(self) -> bool | None:
        """The IsNormalMap field value."""
        member = self.get_member("IsNormalMap")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_normal_map.setter
    def is_normal_map(self, value: bool) -> None:
        """Set the IsNormalMap field value."""
        member = self.get_member("IsNormalMap")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsNormalMap", fields.FieldBool(value=value)
            )

    @property
    def wrap_mode_u(self) -> members.FieldEnum | None:
        """The WrapModeU member."""
        member = self.get_member("WrapModeU")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @wrap_mode_u.setter
    def wrap_mode_u(self, value: members.FieldEnum) -> None:
        """Set the WrapModeU member."""
        self.set_member("WrapModeU", value)

    @property
    def wrap_mode_v(self) -> members.FieldEnum | None:
        """The WrapModeV member."""
        member = self.get_member("WrapModeV")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @wrap_mode_v.setter
    def wrap_mode_v(self, value: members.FieldEnum) -> None:
        """Set the WrapModeV member."""
        self.set_member("WrapModeV", value)

    @property
    def power_of_two_align_threshold(self) -> np.float32 | None:
        """The PowerOfTwoAlignThreshold field value."""
        member = self.get_member("PowerOfTwoAlignThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @power_of_two_align_threshold.setter
    def power_of_two_align_threshold(self, value: np.float32) -> None:
        """Set the PowerOfTwoAlignThreshold field value."""
        member = self.get_member("PowerOfTwoAlignThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PowerOfTwoAlignThreshold", fields.FieldFloat(value=value)
            )

    @property
    def crunch_compressed(self) -> bool | None:
        """The CrunchCompressed field value."""
        member = self.get_member("CrunchCompressed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @crunch_compressed.setter
    def crunch_compressed(self, value: bool) -> None:
        """Set the CrunchCompressed field value."""
        member = self.get_member("CrunchCompressed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CrunchCompressed", fields.FieldBool(value=value)
            )

    @property
    def min_size(self) -> np.int32 | None:
        """The MinSize field value."""
        member = self.get_member("MinSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_size.setter
    def min_size(self, value: np.int32) -> None:
        """Set the MinSize field value."""
        member = self.get_member("MinSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinSize", fields.FieldNullableInt(value=value)
            )

    @property
    def max_size(self) -> np.int32 | None:
        """The MaxSize field value."""
        member = self.get_member("MaxSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_size.setter
    def max_size(self, value: np.int32) -> None:
        """Set the MaxSize field value."""
        member = self.get_member("MaxSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSize", fields.FieldNullableInt(value=value)
            )

    @property
    def mip_maps(self) -> bool | None:
        """The MipMaps field value."""
        member = self.get_member("MipMaps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mip_maps.setter
    def mip_maps(self, value: bool) -> None:
        """Set the MipMaps field value."""
        member = self.get_member("MipMaps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MipMaps", fields.FieldBool(value=value)
            )

    @property
    def keep_original_mip_maps(self) -> bool | None:
        """The KeepOriginalMipMaps field value."""
        member = self.get_member("KeepOriginalMipMaps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @keep_original_mip_maps.setter
    def keep_original_mip_maps(self, value: bool) -> None:
        """Set the KeepOriginalMipMaps field value."""
        member = self.get_member("KeepOriginalMipMaps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "KeepOriginalMipMaps", fields.FieldBool(value=value)
            )

    @property
    def mip_map_filter(self) -> members.FieldEnum | None:
        """The MipMapFilter member."""
        member = self.get_member("MipMapFilter")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @mip_map_filter.setter
    def mip_map_filter(self, value: members.FieldEnum) -> None:
        """Set the MipMapFilter member."""
        self.set_member("MipMapFilter", value)

    @property
    def readable(self) -> bool | None:
        """The Readable field value."""
        member = self.get_member("Readable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @readable.setter
    def readable(self, value: bool) -> None:
        """Set the Readable field value."""
        member = self.get_member("Readable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Readable", fields.FieldBool(value=value)
            )

