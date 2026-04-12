"""Generated component: SimplexTexture."""

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


class SimplexTexture(GeneratedComponent, ITexture2DProvider, ICustomInspector, IWorldEventReceiver):
    """The SimplexTexture component is used to generate procedural noise to use in any material.

    Category: Assets/Procedural Textures

    Insert into any material to view what this texture looks like.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SimplexTexture"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, filter_mode: TextureFilterMode | str | None = None, anisotropic_level: primitives.Int | None = None, wrap_mode_u: TextureWrapMode | str | None = None, wrap_mode_v: TextureWrapMode | str | None = None, mipmap_bias: primitives.Float | None = None, profile: ColorProfile | str | None = None, size: primitives.Int2 | None = None, mipmaps: primitives.Bool | None = None, format_: TextureFormat | str | None = None, offset: primitives.Float2 | None = None, scale: primitives.Float2 | None = None, background: primitives.ColorX | None = None, foreground: primitives.ColorX | None = None, use_3d: primitives.Bool | None = None, zoffset: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
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
            offset: Initial value for Offset.
            scale: Initial value for Scale.
            background: Initial value for Background.
            foreground: Initial value for Foreground.
            use_3d: Initial value for Use3D.
            zoffset: Initial value for ZOffset.
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
        if offset is not None:
            self.offset = offset
        if scale is not None:
            self.scale = scale
        if background is not None:
            self.background = background
        if foreground is not None:
            self.foreground = foreground
        if use_3d is not None:
            self.use_3d = use_3d
        if zoffset is not None:
            self.zoffset = zoffset

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
    def offset(self) -> primitives.Float2 | None:
        """How much to shift the procedural noise."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float2) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat2(value=value)
            )

    @property
    def scale(self) -> primitives.Float2 | None:
        """scales the pattern up or down inside the image."""
        member = self.get_member("Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale.setter
    def scale(self, value: primitives.Float2) -> None:
        """Set the Scale field value."""
        member = self.get_member("Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Scale", fields.FieldFloat2(value=value)
            )

    @property
    def background(self) -> primitives.ColorX | None:
        """The background color of the noise."""
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
        """The color of the noise itself."""
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
    def use_3d(self) -> primitives.Bool | None:
        """Whether to allow ``ZOffset`` to affect the texture, and generates 3D noise."""
        member = self.get_member("Use3D")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_3d.setter
    def use_3d(self, value: primitives.Bool) -> None:
        """Set the Use3D field value."""
        member = self.get_member("Use3D")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Use3D", fields.FieldBool(value=value)
            )

    @property
    def zoffset(self) -> primitives.Float | None:
        """The offset in the 3D noise, which takes a slice of the 3D noise for the texture."""
        member = self.get_member("ZOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @zoffset.setter
    def zoffset(self, value: primitives.Float) -> None:
        """Set the ZOffset field value."""
        member = self.get_member("ZOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ZOffset", fields.FieldFloat(value=value)
            )

    async def bake_texture(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeTexture sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeTexture", {}, debug,
        )

