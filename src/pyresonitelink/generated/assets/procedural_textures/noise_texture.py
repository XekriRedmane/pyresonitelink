"""Generated component: NoiseTexture."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itexture_2d_provider import ITexture2DProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NoiseTexture(GeneratedComponent, ITexture2DProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.NoiseTexture.

    Category: Assets/Procedural Textures
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.NoiseTexture"

    def __init__(self, high_priority_integration: bool | None = None, anisotropic_level: np.int32 | None = None, mipmap_bias: np.float32 | None = None, size: primitives.Int2 | None = None, mipmaps: bool | None = None, seed: np.int32 | None = None, monochrome: bool | None = None, monochrome_max: primitives.ColorX | None = None, monochrome_min: primitives.ColorX | None = None, bias: np.float32 | None = None, gain: np.float32 | None = None, clamp: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            anisotropic_level: Initial value for AnisotropicLevel.
            mipmap_bias: Initial value for MipmapBias.
            size: Initial value for Size.
            mipmaps: Initial value for Mipmaps.
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
        if anisotropic_level is not None:
            self.anisotropic_level = anisotropic_level
        if mipmap_bias is not None:
            self.mipmap_bias = mipmap_bias
        if size is not None:
            self.size = size
        if mipmaps is not None:
            self.mipmaps = mipmaps
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
    def seed(self) -> np.int32 | None:
        """The Seed field value."""
        member = self.get_member("Seed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @seed.setter
    def seed(self, value: np.int32) -> None:
        """Set the Seed field value."""
        member = self.get_member("Seed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Seed", fields.FieldInt(value=value)
            )

    @property
    def monochrome(self) -> bool | None:
        """The Monochrome field value."""
        member = self.get_member("Monochrome")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @monochrome.setter
    def monochrome(self, value: bool) -> None:
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
        """The MonochromeMax field value."""
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
        """The MonochromeMin field value."""
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
    def bias(self) -> np.float32 | None:
        """The Bias field value."""
        member = self.get_member("Bias")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bias.setter
    def bias(self, value: np.float32) -> None:
        """Set the Bias field value."""
        member = self.get_member("Bias")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Bias", fields.FieldFloat(value=value)
            )

    @property
    def gain(self) -> np.float32 | None:
        """The Gain field value."""
        member = self.get_member("Gain")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gain.setter
    def gain(self, value: np.float32) -> None:
        """Set the Gain field value."""
        member = self.get_member("Gain")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Gain", fields.FieldFloat(value=value)
            )

    @property
    def clamp(self) -> bool | None:
        """The Clamp field value."""
        member = self.get_member("Clamp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @clamp.setter
    def clamp(self, value: bool) -> None:
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

