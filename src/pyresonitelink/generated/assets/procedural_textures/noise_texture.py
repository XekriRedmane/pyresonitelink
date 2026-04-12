"""Generated component: NoiseTexture."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.texture_filter_mode import TextureFilterMode
from pyresonitelink.generated._enums.texture_wrap_mode import TextureWrapMode
from pyresonitelink.generated._enums.color_profile import ColorProfile
from pyresonitelink.generated._enums.texture_format import TextureFormat
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itexture_2d_provider import ITexture2DProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NoiseTexture(GeneratedComponent, ITexture2DProvider, ICustomInspector, IWorldEventReceiver):
    """Noise texture is a component that procedurally generates a 2D texture with a random noise pattern like TV static.

    Category: Assets/Procedural Textures
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.NoiseTexture"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, filter_mode: TextureFilterMode | str | None = None, anisotropic_level: primitives.Int | None = None, wrap_mode_u: TextureWrapMode | str | None = None, wrap_mode_v: TextureWrapMode | str | None = None, mipmap_bias: primitives.Float | None = None, profile: ColorProfile | str | None = None, size: primitives.Int2 | None = None, mipmaps: primitives.Bool | None = None, format_: TextureFormat | str | None = None, seed: primitives.Int | None = None, monochrome: primitives.Bool | None = None, monochrome_max: primitives.ColorX | None = None, monochrome_min: primitives.ColorX | None = None, bias: primitives.Float | None = None, gain: primitives.Float | None = None, clamp: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            filter_mode: Initial value for FilterMode.
            anisotropic_level: Initial value for AnisotropicLevel.
            wrap_mode_u: Initial value for WrapModeU.
            wrap_mode_v: Initial value for WrapModeV.
            mipmap_bias: Initial value for MipmapBias.
            profile: Initial value for Profile.
            size: Initial value for Size.
            mipmaps: Initial value for Mipmaps.
            format_: Initial value for Format.
            seed: Initial value for Seed.
            monochrome: Initial value for Monochrome.
            monochrome_max: Initial value for MonochromeMax.
            monochrome_min: Initial value for MonochromeMin.
            bias: Initial value for Bias.
            gain: Initial value for Gain.
            clamp: Initial value for Clamp.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if filter_mode is not None:
            self.filter_mode = filter_mode
        if anisotropic_level is not None:
            self.anisotropic_level = anisotropic_level
        if wrap_mode_u is not None:
            self.wrap_mode_u = wrap_mode_u
        if wrap_mode_v is not None:
            self.wrap_mode_v = wrap_mode_v
        if mipmap_bias is not None:
            self.mipmap_bias = mipmap_bias
        if profile is not None:
            self.profile = profile
        if size is not None:
            self.size = size
        if mipmaps is not None:
            self.mipmaps = mipmaps
        if format_ is not None:
            self.format_ = format_
        if seed is not None:
            self.seed = seed
        if monochrome is not None:
            self.monochrome = monochrome
        if monochrome_max is not None:
            self.monochrome_max = monochrome_max
        if monochrome_min is not None:
            self.monochrome_min = monochrome_min
        if bias is not None:
            self.bias = bias
        if gain is not None:
            self.gain = gain
        if clamp is not None:
            self.clamp = clamp

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
    def filter_mode(self) -> TextureFilterMode | None:
        """The FilterMode enum value."""
        member = self.get_member("FilterMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextureFilterMode(member.value)
        return None

    @filter_mode.setter
    def filter_mode(self, value: TextureFilterMode | str) -> None:
        """Set the FilterMode enum value."""
        member = self.get_member("FilterMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "FilterMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def anisotropic_level(self) -> primitives.Int | None:
        """The AnisotropicLevel field value."""
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
    def wrap_mode_u(self) -> TextureWrapMode | None:
        """The WrapModeU enum value."""
        member = self.get_member("WrapModeU")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextureWrapMode(member.value)
        return None

    @wrap_mode_u.setter
    def wrap_mode_u(self, value: TextureWrapMode | str) -> None:
        """Set the WrapModeU enum value."""
        member = self.get_member("WrapModeU")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "WrapModeU",
                members.FieldEnum(value=str(value)),
            )

    @property
    def wrap_mode_v(self) -> TextureWrapMode | None:
        """The WrapModeV enum value."""
        member = self.get_member("WrapModeV")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextureWrapMode(member.value)
        return None

    @wrap_mode_v.setter
    def wrap_mode_v(self, value: TextureWrapMode | str) -> None:
        """Set the WrapModeV enum value."""
        member = self.get_member("WrapModeV")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "WrapModeV",
                members.FieldEnum(value=str(value)),
            )

    @property
    def mipmap_bias(self) -> primitives.Float | None:
        """The MipmapBias field value."""
        member = self.get_member("MipmapBias")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mipmap_bias.setter
    def mipmap_bias(self, value: primitives.Float) -> None:
        """Set the MipmapBias field value."""
        member = self.get_member("MipmapBias")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MipmapBias", fields.FieldFloat(value=value)
            )

    @property
    def profile(self) -> ColorProfile | None:
        """The Profile enum value."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ColorProfile(member.value)
        return None

    @profile.setter
    def profile(self, value: ColorProfile | str) -> None:
        """Set the Profile enum value."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Profile",
                members.FieldEnum(value=str(value)),
            )

    @property
    def size(self) -> primitives.Int2 | None:
        """The Size field value."""
        member = self.get_member("Size")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size.setter
    def size(self, value: primitives.Int2) -> None:
        """Set the Size field value."""
        member = self.get_member("Size")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Size", fields.FieldInt2(value=value)
            )

    @property
    def mipmaps(self) -> primitives.Bool | None:
        """The Mipmaps field value."""
        member = self.get_member("Mipmaps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mipmaps.setter
    def mipmaps(self, value: primitives.Bool) -> None:
        """Set the Mipmaps field value."""
        member = self.get_member("Mipmaps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Mipmaps", fields.FieldBool(value=value)
            )

    @property
    def format_(self) -> TextureFormat | None:
        """The Format enum value."""
        member = self.get_member("Format")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextureFormat(member.value)
        return None

    @format_.setter
    def format_(self, value: TextureFormat | str) -> None:
        """Set the Format enum value."""
        member = self.get_member("Format")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Format",
                members.FieldEnum(value=str(value)),
            )

    @property
    def seed(self) -> primitives.Int | None:
        """The number to use to seed the generation of the noise for the texture."""
        member = self.get_member("Seed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @seed.setter
    def seed(self, value: primitives.Int) -> None:
        """Set the Seed field value."""
        member = self.get_member("Seed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Seed", fields.FieldInt(value=value)
            )

    @property
    def monochrome(self) -> primitives.Bool | None:
        """Whether to make the noise generation use a mix of 2 colors rather than random colors."""
        member = self.get_member("Monochrome")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @monochrome.setter
    def monochrome(self, value: primitives.Bool) -> None:
        """Set the Monochrome field value."""
        member = self.get_member("Monochrome")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Monochrome", fields.FieldBool(value=value)
            )

    @property
    def monochrome_max(self) -> primitives.ColorX | None:
        """Color 1 to use for the noise texture when ``Monochrome`` is enabled."""
        member = self.get_member("MonochromeMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @monochrome_max.setter
    def monochrome_max(self, value: primitives.ColorX) -> None:
        """Set the MonochromeMax field value."""
        member = self.get_member("MonochromeMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MonochromeMax", fields.FieldColorX(value=value)
            )

    @property
    def monochrome_min(self) -> primitives.ColorX | None:
        """Color 2 to use for the noise texture when ``Monochrome`` is enabled."""
        member = self.get_member("MonochromeMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @monochrome_min.setter
    def monochrome_min(self, value: primitives.ColorX) -> None:
        """Set the MonochromeMin field value."""
        member = self.get_member("MonochromeMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MonochromeMin", fields.FieldColorX(value=value)
            )

    @property
    def bias(self) -> primitives.Float | None:
        """The bias to use more of ``MonochromeMax`` or ``MonochromeMin``"""
        member = self.get_member("Bias")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bias.setter
    def bias(self, value: primitives.Float) -> None:
        """Set the Bias field value."""
        member = self.get_member("Bias")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Bias", fields.FieldFloat(value=value)
            )

    @property
    def gain(self) -> primitives.Float | None:
        """How much to brighten the entire texture."""
        member = self.get_member("Gain")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gain.setter
    def gain(self, value: primitives.Float) -> None:
        """Set the Gain field value."""
        member = self.get_member("Gain")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Gain", fields.FieldFloat(value=value)
            )

    @property
    def clamp(self) -> primitives.Bool | None:
        """Whether to keep color ranges for the output from going beyond 1 and causing bloom."""
        member = self.get_member("Clamp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @clamp.setter
    def clamp(self, value: primitives.Bool) -> None:
        """Set the Clamp field value."""
        member = self.get_member("Clamp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Clamp", fields.FieldBool(value=value)
            )

    async def bake_texture(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeTexture sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeTexture", {}, debug,
        )

