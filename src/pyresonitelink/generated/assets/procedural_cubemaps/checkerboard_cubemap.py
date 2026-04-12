"""Generated component: CheckerboardCubemap."""

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


class CheckerboardCubemap(GeneratedComponent, ITextureProvider, ICustomInspector, IWorldEventReceiver):
    """The CheckerboardCubemap component procedurally generates a cubemap for Projection 360 Materials that is a checkerboard with different pairs of colors for each of the 6 sides.

    Category: Assets/Procedural Cubemaps

    Put into the ``CubeMap`` field of a Projection 360 Materials to view
    what the skybox would look like.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CheckerboardCubemap"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, filter_mode: TextureFilterMode | str | None = None, anisotropic_level: primitives.Int | None = None, mipmap_bias: primitives.Float | None = None, profile: ColorProfile | str | None = None, size: primitives.Int | None = None, mipmaps: primitives.Bool | None = None, format_: TextureFormat | str | None = None, checker_size: primitives.Int | None = None, pos_x_color0: primitives.ColorX | None = None, pos_x_color1: primitives.ColorX | None = None, neg_x_color0: primitives.ColorX | None = None, neg_x_color1: primitives.ColorX | None = None, pos_y_color0: primitives.ColorX | None = None, pos_y_color1: primitives.ColorX | None = None, neg_y_color0: primitives.ColorX | None = None, neg_y_color1: primitives.ColorX | None = None, pos_z_color0: primitives.ColorX | None = None, pos_z_color1: primitives.ColorX | None = None, neg_z_color0: primitives.ColorX | None = None, neg_z_color1: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
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
            checker_size: Initial value for CheckerSize.
            pos_x_color0: Initial value for PosX_Color0.
            pos_x_color1: Initial value for PosX_Color1.
            neg_x_color0: Initial value for NegX_Color0.
            neg_x_color1: Initial value for NegX_Color1.
            pos_y_color0: Initial value for PosY_Color0.
            pos_y_color1: Initial value for PosY_Color1.
            neg_y_color0: Initial value for NegY_Color0.
            neg_y_color1: Initial value for NegY_Color1.
            pos_z_color0: Initial value for PosZ_Color0.
            pos_z_color1: Initial value for PosZ_Color1.
            neg_z_color0: Initial value for NegZ_Color0.
            neg_z_color1: Initial value for NegZ_Color1.
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
        if checker_size is not None:
            self.checker_size = checker_size
        if pos_x_color0 is not None:
            self.pos_x_color0 = pos_x_color0
        if pos_x_color1 is not None:
            self.pos_x_color1 = pos_x_color1
        if neg_x_color0 is not None:
            self.neg_x_color0 = neg_x_color0
        if neg_x_color1 is not None:
            self.neg_x_color1 = neg_x_color1
        if pos_y_color0 is not None:
            self.pos_y_color0 = pos_y_color0
        if pos_y_color1 is not None:
            self.pos_y_color1 = pos_y_color1
        if neg_y_color0 is not None:
            self.neg_y_color0 = neg_y_color0
        if neg_y_color1 is not None:
            self.neg_y_color1 = neg_y_color1
        if pos_z_color0 is not None:
            self.pos_z_color0 = pos_z_color0
        if pos_z_color1 is not None:
            self.pos_z_color1 = pos_z_color1
        if neg_z_color0 is not None:
            self.neg_z_color0 = neg_z_color0
        if neg_z_color1 is not None:
            self.neg_z_color1 = neg_z_color1

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
        """The size of each side of the cubemap in pixels."""
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
    def checker_size(self) -> primitives.Int | None:
        """The size in pixels for 1 square of the checkerboard pattern."""
        member = self.get_member("CheckerSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @checker_size.setter
    def checker_size(self, value: primitives.Int) -> None:
        """Set the CheckerSize field value."""
        member = self.get_member("CheckerSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CheckerSize", fields.FieldInt(value=value)
            )

    @property
    def pos_x_color0(self) -> primitives.ColorX | None:
        """The PosX_Color0 field value."""
        member = self.get_member("PosX_Color0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pos_x_color0.setter
    def pos_x_color0(self, value: primitives.ColorX) -> None:
        """Set the PosX_Color0 field value."""
        member = self.get_member("PosX_Color0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PosX_Color0", fields.FieldColorX(value=value)
            )

    @property
    def pos_x_color1(self) -> primitives.ColorX | None:
        """The PosX_Color1 field value."""
        member = self.get_member("PosX_Color1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pos_x_color1.setter
    def pos_x_color1(self, value: primitives.ColorX) -> None:
        """Set the PosX_Color1 field value."""
        member = self.get_member("PosX_Color1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PosX_Color1", fields.FieldColorX(value=value)
            )

    @property
    def neg_x_color0(self) -> primitives.ColorX | None:
        """The NegX_Color0 field value."""
        member = self.get_member("NegX_Color0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @neg_x_color0.setter
    def neg_x_color0(self, value: primitives.ColorX) -> None:
        """Set the NegX_Color0 field value."""
        member = self.get_member("NegX_Color0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NegX_Color0", fields.FieldColorX(value=value)
            )

    @property
    def neg_x_color1(self) -> primitives.ColorX | None:
        """The NegX_Color1 field value."""
        member = self.get_member("NegX_Color1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @neg_x_color1.setter
    def neg_x_color1(self, value: primitives.ColorX) -> None:
        """Set the NegX_Color1 field value."""
        member = self.get_member("NegX_Color1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NegX_Color1", fields.FieldColorX(value=value)
            )

    @property
    def pos_y_color0(self) -> primitives.ColorX | None:
        """The PosY_Color0 field value."""
        member = self.get_member("PosY_Color0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pos_y_color0.setter
    def pos_y_color0(self, value: primitives.ColorX) -> None:
        """Set the PosY_Color0 field value."""
        member = self.get_member("PosY_Color0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PosY_Color0", fields.FieldColorX(value=value)
            )

    @property
    def pos_y_color1(self) -> primitives.ColorX | None:
        """The PosY_Color1 field value."""
        member = self.get_member("PosY_Color1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pos_y_color1.setter
    def pos_y_color1(self, value: primitives.ColorX) -> None:
        """Set the PosY_Color1 field value."""
        member = self.get_member("PosY_Color1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PosY_Color1", fields.FieldColorX(value=value)
            )

    @property
    def neg_y_color0(self) -> primitives.ColorX | None:
        """The NegY_Color0 field value."""
        member = self.get_member("NegY_Color0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @neg_y_color0.setter
    def neg_y_color0(self, value: primitives.ColorX) -> None:
        """Set the NegY_Color0 field value."""
        member = self.get_member("NegY_Color0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NegY_Color0", fields.FieldColorX(value=value)
            )

    @property
    def neg_y_color1(self) -> primitives.ColorX | None:
        """The NegY_Color1 field value."""
        member = self.get_member("NegY_Color1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @neg_y_color1.setter
    def neg_y_color1(self, value: primitives.ColorX) -> None:
        """Set the NegY_Color1 field value."""
        member = self.get_member("NegY_Color1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NegY_Color1", fields.FieldColorX(value=value)
            )

    @property
    def pos_z_color0(self) -> primitives.ColorX | None:
        """The PosZ_Color0 field value."""
        member = self.get_member("PosZ_Color0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pos_z_color0.setter
    def pos_z_color0(self, value: primitives.ColorX) -> None:
        """Set the PosZ_Color0 field value."""
        member = self.get_member("PosZ_Color0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PosZ_Color0", fields.FieldColorX(value=value)
            )

    @property
    def pos_z_color1(self) -> primitives.ColorX | None:
        """The PosZ_Color1 field value."""
        member = self.get_member("PosZ_Color1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pos_z_color1.setter
    def pos_z_color1(self, value: primitives.ColorX) -> None:
        """Set the PosZ_Color1 field value."""
        member = self.get_member("PosZ_Color1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PosZ_Color1", fields.FieldColorX(value=value)
            )

    @property
    def neg_z_color0(self) -> primitives.ColorX | None:
        """The NegZ_Color0 field value."""
        member = self.get_member("NegZ_Color0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @neg_z_color0.setter
    def neg_z_color0(self, value: primitives.ColorX) -> None:
        """Set the NegZ_Color0 field value."""
        member = self.get_member("NegZ_Color0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NegZ_Color0", fields.FieldColorX(value=value)
            )

    @property
    def neg_z_color1(self) -> primitives.ColorX | None:
        """The NegZ_Color1 field value."""
        member = self.get_member("NegZ_Color1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @neg_z_color1.setter
    def neg_z_color1(self, value: primitives.ColorX) -> None:
        """Set the NegZ_Color1 field value."""
        member = self.get_member("NegZ_Color1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NegZ_Color1", fields.FieldColorX(value=value)
            )

