"""Generated component: RenderTextureProvider."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.texture_filter_mode import TextureFilterMode
from pyresonitelink.generated._enums.texture_wrap_mode import TextureWrapMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itexture_2d_provider import ITexture2DProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RenderTextureProvider(GeneratedComponent, ITexture2DProvider, ICustomInspector, IWorldEventReceiver):
    """The RenderTextureProvider component is used as a target for rendering Camera or CameraPortal data onto. This component can be used as a texture for any material.

    Category: Assets

    Attach to a slot and use as a render texture for any component that
    accepts it. The texture color data will now exist. Insert into any
    material to view.

    **See also**: * Camera
* CameraPortal
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RenderTextureProvider"

    def __init__(self, size: primitives.Int2 | None = None, depth: primitives.Int | None = None, filter_mode: TextureFilterMode | str | None = None, anisotropic_level: primitives.Int | None = None, wrap_mode_u: TextureWrapMode | str | None = None, wrap_mode_v: TextureWrapMode | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            size: Initial value for Size.
            depth: Initial value for Depth.
            filter_mode: Initial value for FilterMode.
            anisotropic_level: Initial value for AnisotropicLevel.
            wrap_mode_u: Initial value for WrapModeU.
            wrap_mode_v: Initial value for WrapModeV.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if size is not None:
            self.size = size
        if depth is not None:
            self.depth = depth
        if filter_mode is not None:
            self.filter_mode = filter_mode
        if anisotropic_level is not None:
            self.anisotropic_level = anisotropic_level
        if wrap_mode_u is not None:
            self.wrap_mode_u = wrap_mode_u
        if wrap_mode_v is not None:
            self.wrap_mode_v = wrap_mode_v

    @property
    def size(self) -> primitives.Int2 | None:
        """The size the camera renders in ``width`` and ``height``"""
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
    def depth(self) -> primitives.Int | None:
        """Precision, in bits, of the depth buffer used for rendering. Possibly values are 0, 16, 24 and 32."""
        member = self.get_member("Depth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @depth.setter
    def depth(self, value: primitives.Int) -> None:
        """Set the Depth field value."""
        member = self.get_member("Depth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Depth", fields.FieldInt(value=value)
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

