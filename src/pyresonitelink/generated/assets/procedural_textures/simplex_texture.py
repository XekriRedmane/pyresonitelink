"""Generated component: SimplexTexture."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itexture_2d_provider import ITexture2DProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SimplexTexture(GeneratedComponent, ITexture2DProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SimplexTexture.

    Category: Assets/Procedural Textures
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SimplexTexture"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, anisotropic_level: primitives.Int | None = None, mipmap_bias: primitives.Float | None = None, size: primitives.Int2 | None = None, mipmaps: primitives.Bool | None = None, offset: primitives.Float2 | None = None, scale: primitives.Float2 | None = None, background: primitives.ColorX | None = None, foreground: primitives.ColorX | None = None, use_3d: primitives.Bool | None = None, zoffset: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            anisotropic_level: Initial value for AnisotropicLevel.
            mipmap_bias: Initial value for MipmapBias.
            size: Initial value for Size.
            mipmaps: Initial value for Mipmaps.
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
        if anisotropic_level is not None:
            self.anisotropic_level = anisotropic_level
        if mipmap_bias is not None:
            self.mipmap_bias = mipmap_bias
        if size is not None:
            self.size = size
        if mipmaps is not None:
            self.mipmaps = mipmaps
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
    def offset(self) -> primitives.Float2 | None:
        """The Offset field value."""
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
        """The Scale field value."""
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
        """The Background field value."""
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
        """The Foreground field value."""
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
        """The Use3D field value."""
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
        """The ZOffset field value."""
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

