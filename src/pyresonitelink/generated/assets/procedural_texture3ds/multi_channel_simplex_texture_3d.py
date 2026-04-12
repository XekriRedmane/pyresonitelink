"""Generated component: MultiChannelSimplexTexture3D."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.texture_filter_mode import TextureFilterMode
from pyresonitelink.generated._enums.texture_wrap_mode import TextureWrapMode
from pyresonitelink.generated._enums.color_profile import ColorProfile
from pyresonitelink.generated._enums.texture_format import TextureFormat
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itexture_provider import ITextureProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MultiChannelSimplexTexture3D(GeneratedComponent, ITextureProvider, ICustomInspector, IWorldEventReceiver):
    """The MultiChannelSimplexTexture3D component creates a monochrome noise channel for each RGBA channel with their own settings. It is also considered a ITexture3D element.

    Category: Assets/Procedural Texture3Ds

    Can be used to make procedural noise 4D textures for use with LUT, and
    volume.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MultiChannelSimplexTexture3D"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, filter_mode: TextureFilterMode | str | None = None, anisotropic_level: primitives.Int | None = None, wrap_mode_u: TextureWrapMode | str | None = None, wrap_mode_v: TextureWrapMode | str | None = None, wrap_mode_w: TextureWrapMode | str | None = None, profile: ColorProfile | str | None = None, size: primitives.Int3 | None = None, format_: TextureFormat | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            filter_mode: Initial value for FilterMode.
            anisotropic_level: Initial value for AnisotropicLevel.
            wrap_mode_u: Initial value for WrapModeU.
            wrap_mode_v: Initial value for WrapModeV.
            wrap_mode_w: Initial value for WrapModeW.
            profile: Initial value for Profile.
            size: Initial value for Size.
            format_: Initial value for Format.
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
        if wrap_mode_w is not None:
            self.wrap_mode_w = wrap_mode_w
        if profile is not None:
            self.profile = profile
        if size is not None:
            self.size = size
        if format_ is not None:
            self.format_ = format_

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
        """How to interpolate enlarged pixels when rendering the texture."""
        member = self.get_member("FilterMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextureFilterMode(member.value)
        return None

    @filter_mode.setter
    def filter_mode(self, value: TextureFilterMode | str) -> None:
        """Set FilterMode. How to interpolate enlarged pixels when rendering the texture."""
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
        """Used when the texture is using the Anisotropic filtering render algorithm."""
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
        """How to handle wrapping for UVW sampling positions beyond the 0 to 1 range for U."""
        member = self.get_member("WrapModeU")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextureWrapMode(member.value)
        return None

    @wrap_mode_u.setter
    def wrap_mode_u(self, value: TextureWrapMode | str) -> None:
        """Set WrapModeU. How to handle wrapping for UVW sampling positions beyond the 0 to 1 range for U."""
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
        """How to handle wrapping for UVW sampling positions beyond the 0 to 1 range for V."""
        member = self.get_member("WrapModeV")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextureWrapMode(member.value)
        return None

    @wrap_mode_v.setter
    def wrap_mode_v(self, value: TextureWrapMode | str) -> None:
        """Set WrapModeV. How to handle wrapping for UVW sampling positions beyond the 0 to 1 range for V."""
        member = self.get_member("WrapModeV")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "WrapModeV",
                members.FieldEnum(value=str(value)),
            )

    @property
    def wrap_mode_w(self) -> TextureWrapMode | None:
        """How to handle wrapping for UVW sampling positions beyond the 0 to 1 range for W."""
        member = self.get_member("WrapModeW")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextureWrapMode(member.value)
        return None

    @wrap_mode_w.setter
    def wrap_mode_w(self, value: TextureWrapMode | str) -> None:
        """Set WrapModeW. How to handle wrapping for UVW sampling positions beyond the 0 to 1 range for W."""
        member = self.get_member("WrapModeW")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "WrapModeW",
                members.FieldEnum(value=str(value)),
            )

    @property
    def profile(self) -> ColorProfile | None:
        """The color space to render the image in."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ColorProfile(member.value)
        return None

    @profile.setter
    def profile(self, value: ColorProfile | str) -> None:
        """Set Profile. The color space to render the image in."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Profile",
                members.FieldEnum(value=str(value)),
            )

    @property
    def size(self) -> primitives.Int3 | None:
        """How big the texture is in pixels."""
        member = self.get_member("Size")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size.setter
    def size(self, value: primitives.Int3) -> None:
        """Set the Size field value."""
        member = self.get_member("Size")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Size", fields.FieldInt3(value=value)
            )

    @property
    def format_(self) -> TextureFormat | None:
        """What format to show the texture in."""
        member = self.get_member("Format")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextureFormat(member.value)
        return None

    @format_.setter
    def format_(self, value: TextureFormat | str) -> None:
        """Set Format. What format to show the texture in."""
        member = self.get_member("Format")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Format",
                members.FieldEnum(value=str(value)),
            )

    @property
    def r(self) -> members.SyncObject | None:
        """The settings to use when generating the noise for the red channel."""
        member = self.get_member("R")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @r.setter
    def r(self, value: members.SyncObject) -> None:
        """Set R. The settings to use when generating the noise for the red channel."""
        self.set_member("R", value)

    @property
    def g(self) -> members.SyncObject | None:
        """The settings to use when generating the noise for the green channel."""
        member = self.get_member("G")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @g.setter
    def g(self, value: members.SyncObject) -> None:
        """Set G. The settings to use when generating the noise for the green channel."""
        self.set_member("G", value)

    @property
    def b(self) -> members.SyncObject | None:
        """The settings to use when generating the noise for the blue channel."""
        member = self.get_member("B")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @b.setter
    def b(self, value: members.SyncObject) -> None:
        """Set B. The settings to use when generating the noise for the blue channel."""
        self.set_member("B", value)

    @property
    def a(self) -> members.SyncObject | None:
        """The settings to use when generating the noise for the alpha channel."""
        member = self.get_member("A")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @a.setter
    def a(self, value: members.SyncObject) -> None:
        """Set A. The settings to use when generating the noise for the alpha channel."""
        self.set_member("A", value)

