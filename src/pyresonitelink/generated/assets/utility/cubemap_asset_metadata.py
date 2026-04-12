"""Generated component: CubemapAssetMetadata."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.texture_format import TextureFormat
from pyresonitelink.generated._enums.color_profile import ColorProfile
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.cubemap import Cubemap
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CubemapAssetMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The CubemapAssetMetadata component is used to display info about any particular cube map provided.

    Category: Assets/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CubemapAssetMetadata"

    def __init__(self, cubemap: str | IAssetProvider[Cubemap] | None = None, size: primitives.Int | None = None, has_mip_maps: primitives.Bool | None = None, mip_map_count: primitives.Int | None = None, memory_bytes: primitives.Long | None = None, formatted_memory_bytes: primitives.String | None = None, format_: TextureFormat | str | None = None, actual_loaded_variant: primitives.String | None = None, profile: ColorProfile | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            cubemap: Initial value for Cubemap.
            size: Initial value for Size.
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
        if cubemap is not None:
            self.cubemap = cubemap
        if size is not None:
            self.size = size
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
    def cubemap(self) -> str | None:
        """The cubemap to analyse."""
        member = self.get_member("Cubemap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cubemap.setter
    def cubemap(self, target: str | IAssetProvider[Cubemap] | None) -> None:
        """Set the Cubemap reference by target ID or IAssetProvider[Cubemap] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Cubemap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Cubemap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Cubemap>'),
            )

    @property
    def size(self) -> primitives.Int | None:
        """The size in pixels of the width or height of any 1 of the 6 sides. (The sides are the same size)"""
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
    def has_mip_maps(self) -> primitives.Bool | None:
        """Whether the cubemap has mipmap data."""
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
        """How many mip map resolution variants the cubemap has."""
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
        """How much memory the cubemap takes up."""
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
        """The bytes formatted into a readable string."""
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
        """The texture format of the cube map."""
        member = self.get_member("Format")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextureFormat(member.value)
        return None

    @format_.setter
    def format_(self, value: TextureFormat | str) -> None:
        """Set Format. The texture format of the cube map."""
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
        """The Asset variant Type currently loaded."""
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
        """The color profile being used for this texture when rendering it."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ColorProfile(member.value)
        return None

    @profile.setter
    def profile(self, value: ColorProfile | str) -> None:
        """Set Profile. The color profile being used for this texture when rendering it."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Profile",
                members.FieldEnum(value=str(value)),
            )

