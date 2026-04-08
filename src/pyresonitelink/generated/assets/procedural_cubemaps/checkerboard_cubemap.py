"""Generated component: CheckerboardCubemap."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itexture_provider import ITextureProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CheckerboardCubemap(GeneratedComponent, ITextureProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CheckerboardCubemap.

    Category: Assets/Procedural Cubemaps
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CheckerboardCubemap"

    def __init__(self, high_priority_integration: bool | None = None, anisotropic_level: np.int32 | None = None, mipmap_bias: np.float32 | None = None, size: np.int32 | None = None, mipmaps: bool | None = None, checker_size: np.int32 | None = None, pos_x_color0: primitives.ColorX | None = None, pos_x_color1: primitives.ColorX | None = None, neg_x_color0: primitives.ColorX | None = None, neg_x_color1: primitives.ColorX | None = None, pos_y_color0: primitives.ColorX | None = None, pos_y_color1: primitives.ColorX | None = None, neg_y_color0: primitives.ColorX | None = None, neg_y_color1: primitives.ColorX | None = None, pos_z_color0: primitives.ColorX | None = None, pos_z_color1: primitives.ColorX | None = None, neg_z_color0: primitives.ColorX | None = None, neg_z_color1: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            anisotropic_level: Initial value for AnisotropicLevel.
            mipmap_bias: Initial value for MipmapBias.
            size: Initial value for Size.
            mipmaps: Initial value for Mipmaps.
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
        if anisotropic_level is not None:
            self.anisotropic_level = anisotropic_level
        if mipmap_bias is not None:
            self.mipmap_bias = mipmap_bias
        if size is not None:
            self.size = size
        if mipmaps is not None:
            self.mipmaps = mipmaps
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
                "AnisotropicLevel", fields.FieldInt(value=value)
            )

    @property
    def mipmap_bias(self) -> np.float32 | None:
        """The MipmapBias field value."""
        member = self.get_member("MipmapBias")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mipmap_bias.setter
    def mipmap_bias(self, value: np.float32) -> None:
        """Set the MipmapBias field value."""
        member = self.get_member("MipmapBias")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MipmapBias", fields.FieldFloat(value=value)
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
    def size(self) -> np.int32 | None:
        """The Size field value."""
        member = self.get_member("Size")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size.setter
    def size(self, value: np.int32) -> None:
        """Set the Size field value."""
        member = self.get_member("Size")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Size", fields.FieldInt(value=value)
            )

    @property
    def mipmaps(self) -> bool | None:
        """The Mipmaps field value."""
        member = self.get_member("Mipmaps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mipmaps.setter
    def mipmaps(self, value: bool) -> None:
        """Set the Mipmaps field value."""
        member = self.get_member("Mipmaps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Mipmaps", fields.FieldBool(value=value)
            )

    @property
    def format_(self) -> members.FieldEnum | None:
        """The Format member."""
        member = self.get_member("Format")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @format_.setter
    def format_(self, value: members.FieldEnum) -> None:
        """Set the Format member."""
        self.set_member("Format", value)

    @property
    def checker_size(self) -> np.int32 | None:
        """The CheckerSize field value."""
        member = self.get_member("CheckerSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @checker_size.setter
    def checker_size(self, value: np.int32) -> None:
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

