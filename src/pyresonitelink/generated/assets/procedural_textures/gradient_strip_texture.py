"""Generated component: GradientStripTexture."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.texture_filter_mode import TextureFilterMode
from pyresonitelink.generated._enums.texture_wrap_mode import TextureWrapMode
from pyresonitelink.generated._enums.color_profile import ColorProfile
from pyresonitelink.generated._enums.texture_format import TextureFormat
from pyresonitelink.generated._enums.strip_orientation import StripOrientation
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itexture_2d_provider import ITexture2DProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GradientStripTexture(GeneratedComponent, ITexture2DProvider, ICustomInspector, IWorldEventReceiver):
    """The GradientStripTexture is a component that generates a texture with a gradient defined by ``Gradient``

    Category: Assets/Procedural Textures

    Attach to a slot and then insert into a material to view the data. This
    component currently cannot be used properly until collections are
    implemented or the user installs Mods.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GradientStripTexture"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, filter_mode: TextureFilterMode | str | None = None, anisotropic_level: primitives.Int | None = None, wrap_mode_u: TextureWrapMode | str | None = None, wrap_mode_v: TextureWrapMode | str | None = None, mipmap_bias: primitives.Float | None = None, profile: ColorProfile | str | None = None, size: primitives.Int2 | None = None, mipmaps: primitives.Bool | None = None, format_: TextureFormat | str | None = None, exp: primitives.Float | None = None, orientation: StripOrientation | str | None = None, *, component: workers.Component | None = None) -> None:
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
            exp: Initial value for Exp.
            orientation: Initial value for _orientation.
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
        if exp is not None:
            self.exp = exp
        if orientation is not None:
            self.orientation = orientation

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
    def gradient(self) -> members.Member | None:
        """A list of gradients that this texture uses to generate the final result. This requires Mods to edit."""
        member = self.get_member("Gradient")
        if isinstance(member, members.Member):
            return member
        return None

    @gradient.setter
    def gradient(self, value: members.Member) -> None:
        """Set Gradient. A list of gradients that this texture uses to generate the final result. This requires Mods to edit."""
        self.set_member("Gradient", value)

    @property
    def exp(self) -> primitives.Float | None:
        """The sharpness of the transition between each ``Gradient``"""
        member = self.get_member("Exp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exp.setter
    def exp(self, value: primitives.Float) -> None:
        """Set the Exp field value."""
        member = self.get_member("Exp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Exp", fields.FieldFloat(value=value)
            )

    @property
    def orientation(self) -> StripOrientation | None:
        """The direction to generate the gradient strip towards"""
        member = self.get_member("_orientation")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return StripOrientation(member.value)
        return None

    @orientation.setter
    def orientation(self, value: StripOrientation | str) -> None:
        """Set _orientation. The direction to generate the gradient strip towards"""
        member = self.get_member("_orientation")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "_orientation",
                members.FieldEnum(value=str(value)),
            )

    async def bake_texture(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeTexture sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeTexture", {}, debug,
        )

