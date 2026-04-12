"""Generated component: SimplexCubemap."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.texture_filter_mode import TextureFilterMode
from pyresonitelink.generated._enums.color_profile import ColorProfile
from pyresonitelink.generated._enums.texture_format import TextureFormat
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itexture_provider import ITextureProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SimplexCubemap(GeneratedComponent, ITextureProvider, ICustomInspector, IWorldEventReceiver):
    """The Simplex Cubemap component creates a cubemap data that looks like a simplex noise texture in 3D.

    Category: Assets/Procedural Cubemaps
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SimplexCubemap"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, filter_mode: TextureFilterMode | str | None = None, anisotropic_level: primitives.Int | None = None, mipmap_bias: primitives.Float | None = None, profile: ColorProfile | str | None = None, size: primitives.Int | None = None, mipmaps: primitives.Bool | None = None, format_: TextureFormat | str | None = None, background: primitives.ColorX | None = None, foreground: primitives.ColorX | None = None, scale: primitives.Float | None = None, use_4d: primitives.Bool | None = None, woffset: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            filter_mode: Initial value for FilterMode.
            anisotropic_level: Initial value for AnisotropicLevel.
            mipmap_bias: Initial value for MipmapBias.
            profile: Initial value for Profile.
            size: Initial value for Size.
            mipmaps: Initial value for Mipmaps.
            format_: Initial value for Format.
            background: Initial value for Background.
            foreground: Initial value for Foreground.
            scale: Initial value for Scale.
            use_4d: Initial value for Use4D.
            woffset: Initial value for WOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if filter_mode is not None:
            self.filter_mode = filter_mode
        if anisotropic_level is not None:
            self.anisotropic_level = anisotropic_level
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
        if background is not None:
            self.background = background
        if foreground is not None:
            self.foreground = foreground
        if scale is not None:
            self.scale = scale
        if use_4d is not None:
            self.use_4d = use_4d
        if woffset is not None:
            self.woffset = woffset

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
    def size(self) -> primitives.Int | None:
        """The Size field value."""
        member = self.get_member("Size")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size.setter
    def size(self, value: primitives.Int) -> None:
        """Set the Size field value."""
        member = self.get_member("Size")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Size", fields.FieldInt(value=value)
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
    def background(self) -> primitives.ColorX | None:
        """The color for the simplex's background."""
        member = self.get_member("Background")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @background.setter
    def background(self, value: primitives.ColorX) -> None:
        """Set the Background field value."""
        member = self.get_member("Background")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Background", fields.FieldColorX(value=value)
            )

    @property
    def foreground(self) -> primitives.ColorX | None:
        """The color for the simplex's foreground."""
        member = self.get_member("Foreground")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @foreground.setter
    def foreground(self, value: primitives.ColorX) -> None:
        """Set the Foreground field value."""
        member = self.get_member("Foreground")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Foreground", fields.FieldColorX(value=value)
            )

    @property
    def scale(self) -> primitives.Float | None:
        """The scale of the simplex algorithm."""
        member = self.get_member("Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale.setter
    def scale(self, value: primitives.Float) -> None:
        """Set the Scale field value."""
        member = self.get_member("Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Scale", fields.FieldFloat(value=value)
            )

    @property
    def use_4d(self) -> primitives.Bool | None:
        """whether to use 4D to allow animation or shifting of the texture."""
        member = self.get_member("Use4D")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_4d.setter
    def use_4d(self, value: primitives.Bool) -> None:
        """Set the Use4D field value."""
        member = self.get_member("Use4D")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Use4D", fields.FieldBool(value=value)
            )

    @property
    def woffset(self) -> primitives.Float | None:
        """The offset of the texture in 4D."""
        member = self.get_member("WOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @woffset.setter
    def woffset(self, value: primitives.Float) -> None:
        """Set the WOffset field value."""
        member = self.get_member("WOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WOffset", fields.FieldFloat(value=value)
            )

