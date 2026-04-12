"""Generated component: Texture2DAssetMetadata."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.texture_format import TextureFormat
from pyresonitelink.generated._enums.color_profile import ColorProfile
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Texture2DAssetMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Texture2DAssetMetadata component converts the metadata often seen on texture components in an inspector into data that can be pulled into other systems as actual numbers and values.

    Category: Assets/Utility

    Attach to a slot and provide an asset to ``Texture`` to start getting
    values and using the component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Texture2DAssetMetadata"

    def __init__(self, texture: str | IAssetProvider[Texture2D] | None = None, size: primitives.Int2 | None = None, width: primitives.Int | None = None, height: primitives.Int | None = None, has_mip_maps: primitives.Bool | None = None, mip_map_count: primitives.Int | None = None, memory_bytes: primitives.Long | None = None, formatted_memory_bytes: primitives.String | None = None, format_: TextureFormat | str | None = None, actual_loaded_variant: primitives.String | None = None, profile: ColorProfile | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            texture: Initial value for Texture.
            size: Initial value for Size.
            width: Initial value for Width.
            height: Initial value for Height.
            has_mip_maps: Initial value for HasMipMaps.
            mip_map_count: Initial value for MipMapCount.
            memory_bytes: Initial value for MemoryBytes.
            formatted_memory_bytes: Initial value for FormattedMemoryBytes.
            format_: Initial value for Format.
            actual_loaded_variant: Initial value for ActualLoadedVariant.
            profile: Initial value for Profile.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if texture is not None:
            self.texture = texture
        if size is not None:
            self.size = size
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if has_mip_maps is not None:
            self.has_mip_maps = has_mip_maps
        if mip_map_count is not None:
            self.mip_map_count = mip_map_count
        if memory_bytes is not None:
            self.memory_bytes = memory_bytes
        if formatted_memory_bytes is not None:
            self.formatted_memory_bytes = formatted_memory_bytes
        if format_ is not None:
            self.format_ = format_
        if actual_loaded_variant is not None:
            self.actual_loaded_variant = actual_loaded_variant
        if profile is not None:
            self.profile = profile

    @property
    def texture(self) -> str | None:
        """The texture to get metadata on."""
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture.setter
    def texture(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the Texture reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Texture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

    @property
    def size(self) -> primitives.Int2 | None:
        """How big ``Texture`` is in pixels as a width height pair."""
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
    def width(self) -> primitives.Int | None:
        """How wide ``Texture`` is in pixels."""
        member = self.get_member("Width")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @width.setter
    def width(self, value: primitives.Int) -> None:
        """Set the Width field value."""
        member = self.get_member("Width")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Width", fields.FieldInt(value=value)
            )

    @property
    def height(self) -> primitives.Int | None:
        """How tall ``Texture`` is in pixels."""
        member = self.get_member("Height")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height.setter
    def height(self, value: primitives.Int) -> None:
        """Set the Height field value."""
        member = self.get_member("Height")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Height", fields.FieldInt(value=value)
            )

    @property
    def has_mip_maps(self) -> primitives.Bool | None:
        """Whether ``Texture`` has mipmaps."""
        member = self.get_member("HasMipMaps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @has_mip_maps.setter
    def has_mip_maps(self, value: primitives.Bool) -> None:
        """Set the HasMipMaps field value."""
        member = self.get_member("HasMipMaps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HasMipMaps", fields.FieldBool(value=value)
            )

    @property
    def mip_map_count(self) -> primitives.Int | None:
        """How many mipmap levels ``Texture`` has."""
        member = self.get_member("MipMapCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mip_map_count.setter
    def mip_map_count(self, value: primitives.Int) -> None:
        """Set the MipMapCount field value."""
        member = self.get_member("MipMapCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MipMapCount", fields.FieldInt(value=value)
            )

    @property
    def memory_bytes(self) -> primitives.Long | None:
        """How many bytes of memory ``Texture`` takes up."""
        member = self.get_member("MemoryBytes")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @memory_bytes.setter
    def memory_bytes(self, value: primitives.Long) -> None:
        """Set the MemoryBytes field value."""
        member = self.get_member("MemoryBytes")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MemoryBytes", fields.FieldLong(value=value)
            )

    @property
    def formatted_memory_bytes(self) -> primitives.String | None:
        """The bytes of memory ``Texture`` takes up formatted into an easy to read format."""
        member = self.get_member("FormattedMemoryBytes")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @formatted_memory_bytes.setter
    def formatted_memory_bytes(self, value: primitives.String) -> None:
        """Set the FormattedMemoryBytes field value."""
        member = self.get_member("FormattedMemoryBytes")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FormattedMemoryBytes", fields.FieldString(value=value)
            )

    @property
    def format_(self) -> TextureFormat | None:
        """The format ``Texture`` is encoded in."""
        member = self.get_member("Format")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextureFormat(member.value)
        return None

    @format_.setter
    def format_(self, value: TextureFormat | str) -> None:
        """Set Format. The format ``Texture`` is encoded in."""
        member = self.get_member("Format")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Format",
                members.FieldEnum(value=str(value)),
            )

    @property
    def actual_loaded_variant(self) -> primitives.String | None:
        """The actual variant of ``Texture`` that is loaded on the client."""
        member = self.get_member("ActualLoadedVariant")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @actual_loaded_variant.setter
    def actual_loaded_variant(self, value: primitives.String) -> None:
        """Set the ActualLoadedVariant field value."""
        member = self.get_member("ActualLoadedVariant")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActualLoadedVariant", fields.FieldString(value=value)
            )

    @property
    def profile(self) -> ColorProfile | None:
        """The color profile ``Texture`` is being rendered in."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ColorProfile(member.value)
        return None

    @profile.setter
    def profile(self, value: ColorProfile | str) -> None:
        """Set Profile. The color profile ``Texture`` is being rendered in."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Profile",
                members.FieldEnum(value=str(value)),
            )

