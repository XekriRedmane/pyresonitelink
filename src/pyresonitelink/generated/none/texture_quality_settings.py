"""Generated component: TextureQualitySettings."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class TextureQualitySettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.TextureQualitySettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TextureQualitySettings"

    def __init__(self, minimum_texture_size: np.int32 | None = None, anisotropic_level: np.int32 | None = None, use_anisotropic_level: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            minimum_texture_size: Initial value for MinimumTextureSize.
            anisotropic_level: Initial value for AnisotropicLevel.
            use_anisotropic_level: Initial value for UseAnisotropicLevel.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if minimum_texture_size is not None:
            self.minimum_texture_size = minimum_texture_size
        if anisotropic_level is not None:
            self.anisotropic_level = anisotropic_level
        if use_anisotropic_level is not None:
            self.use_anisotropic_level = use_anisotropic_level

    @property
    def texture_size_ratio(self) -> members.FieldEnum | None:
        """The TextureSizeRatio member."""
        member = self.get_member("TextureSizeRatio")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @texture_size_ratio.setter
    def texture_size_ratio(self, value: members.FieldEnum) -> None:
        """Set the TextureSizeRatio member."""
        self.set_member("TextureSizeRatio", value)

    @property
    def texture_size_limit(self) -> members.FieldEnum | None:
        """The TextureSizeLimit member."""
        member = self.get_member("TextureSizeLimit")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @texture_size_limit.setter
    def texture_size_limit(self, value: members.FieldEnum) -> None:
        """Set the TextureSizeLimit member."""
        self.set_member("TextureSizeLimit", value)

    @property
    def minimum_texture_size(self) -> np.int32 | None:
        """The MinimumTextureSize field value."""
        member = self.get_member("MinimumTextureSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @minimum_texture_size.setter
    def minimum_texture_size(self, value: np.int32) -> None:
        """Set the MinimumTextureSize field value."""
        member = self.get_member("MinimumTextureSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinimumTextureSize", fields.FieldInt(value=value)
            )

    @property
    def default_filter_mode(self) -> members.FieldEnum | None:
        """The DefaultFilterMode member."""
        member = self.get_member("DefaultFilterMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @default_filter_mode.setter
    def default_filter_mode(self, value: members.FieldEnum) -> None:
        """Set the DefaultFilterMode member."""
        self.set_member("DefaultFilterMode", value)

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
                "AnisotropicLevel", fields.FieldInt(value=value)
            )

    @property
    def use_anisotropic_level(self) -> bool | None:
        """The UseAnisotropicLevel field value."""
        member = self.get_member("UseAnisotropicLevel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_anisotropic_level.setter
    def use_anisotropic_level(self, value: bool) -> None:
        """Set the UseAnisotropicLevel field value."""
        member = self.get_member("UseAnisotropicLevel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseAnisotropicLevel", fields.FieldBool(value=value)
            )

    async def reload_all_textures(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ReloadAllTextures sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ReloadAllTextures", {}, debug,
        )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

