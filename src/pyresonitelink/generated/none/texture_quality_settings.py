"""Generated component: TextureQualitySettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.texture_size_ratio import TextureSizeRatio
from pyresonitelink.generated._enums.texture_size_limit import TextureSizeLimit
from pyresonitelink.generated._enums.texture_filter_mode import TextureFilterMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class TextureQualitySettings(GeneratedComponent, ICustomInspector):
    """The TextureQualitySettings component is part of the Settings menu and should be interacted with via such menu instead of through this component.

    See Settings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TextureQualitySettings"

    def __init__(self, texture_size_ratio: TextureSizeRatio | str | None = None, texture_size_limit: TextureSizeLimit | str | None = None, minimum_texture_size: primitives.Int | None = None, default_filter_mode: TextureFilterMode | str | None = None, anisotropic_level: primitives.Int | None = None, use_anisotropic_level: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            texture_size_ratio: Initial value for TextureSizeRatio.
            texture_size_limit: Initial value for TextureSizeLimit.
            minimum_texture_size: Initial value for MinimumTextureSize.
            default_filter_mode: Initial value for DefaultFilterMode.
            anisotropic_level: Initial value for AnisotropicLevel.
            use_anisotropic_level: Initial value for UseAnisotropicLevel.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if texture_size_ratio is not None:
            self.texture_size_ratio = texture_size_ratio
        if texture_size_limit is not None:
            self.texture_size_limit = texture_size_limit
        if minimum_texture_size is not None:
            self.minimum_texture_size = minimum_texture_size
        if default_filter_mode is not None:
            self.default_filter_mode = default_filter_mode
        if anisotropic_level is not None:
            self.anisotropic_level = anisotropic_level
        if use_anisotropic_level is not None:
            self.use_anisotropic_level = use_anisotropic_level

    @property
    def texture_size_ratio(self) -> TextureSizeRatio | None:
        """The ratio at which textures should be loaded locally versus their original size on the cloud."""
        member = self.get_member("TextureSizeRatio")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextureSizeRatio(member.value)
        return None

    @texture_size_ratio.setter
    def texture_size_ratio(self, value: TextureSizeRatio | str) -> None:
        """Set TextureSizeRatio. The ratio at which textures should be loaded locally versus their original size on the cloud."""
        member = self.get_member("TextureSizeRatio")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "TextureSizeRatio",
                members.FieldEnum(value=str(value)),
            )

    @property
    def texture_size_limit(self) -> TextureSizeLimit | None:
        """The maximum Texture Size that textures should be loaded at."""
        member = self.get_member("TextureSizeLimit")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextureSizeLimit(member.value)
        return None

    @texture_size_limit.setter
    def texture_size_limit(self, value: TextureSizeLimit | str) -> None:
        """Set TextureSizeLimit. The maximum Texture Size that textures should be loaded at."""
        member = self.get_member("TextureSizeLimit")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "TextureSizeLimit",
                members.FieldEnum(value=str(value)),
            )

    @property
    def minimum_texture_size(self) -> primitives.Int | None:
        """The minimum size textures loaded can be locally."""
        member = self.get_member("MinimumTextureSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @minimum_texture_size.setter
    def minimum_texture_size(self, value: primitives.Int) -> None:
        """Set the MinimumTextureSize field value."""
        member = self.get_member("MinimumTextureSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinimumTextureSize", fields.FieldInt(value=value)
            )

    @property
    def default_filter_mode(self) -> TextureFilterMode | None:
        """The default Texture mode that textures will be if they don't manually specify their Texture mode."""
        member = self.get_member("DefaultFilterMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextureFilterMode(member.value)
        return None

    @default_filter_mode.setter
    def default_filter_mode(self, value: TextureFilterMode | str) -> None:
        """Set DefaultFilterMode. The default Texture mode that textures will be if they don't manually specify their Texture mode."""
        member = self.get_member("DefaultFilterMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "DefaultFilterMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def anisotropic_level(self) -> primitives.Int | None:
        """The Anisotropic levels textures should have."""
        member = self.get_member("AnisotropicLevel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anisotropic_level.setter
    def anisotropic_level(self, value: primitives.Int) -> None:
        """Set the AnisotropicLevel field value."""
        member = self.get_member("AnisotropicLevel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnisotropicLevel", fields.FieldInt(value=value)
            )

    @property
    def use_anisotropic_level(self) -> primitives.Bool | None:
        """Whether the Anisotropic levels should be used."""
        member = self.get_member("UseAnisotropicLevel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_anisotropic_level.setter
    def use_anisotropic_level(self, value: primitives.Bool) -> None:
        """Set the UseAnisotropicLevel field value."""
        member = self.get_member("UseAnisotropicLevel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseAnisotropicLevel", fields.FieldBool(value=value)
            )

    async def reload_all_textures(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Forces a reload of all loaded textures to use curre t Settings (LAGGY)

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

