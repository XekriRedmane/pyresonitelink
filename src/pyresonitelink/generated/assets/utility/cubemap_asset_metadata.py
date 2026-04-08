"""Generated component: CubemapAssetMetadata."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.cubemap import Cubemap
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CubemapAssetMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CubemapAssetMetadata.

    Category: Assets/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CubemapAssetMetadata"

    def __init__(self, cubemap: str | IAssetProvider[Cubemap] | None = None, size: np.int32 | None = None, has_mip_maps: bool | None = None, mip_map_count: np.int32 | None = None, memory_bytes: np.int64 | None = None, formatted_memory_bytes: str | None = None, actual_loaded_variant: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            cubemap: Initial value for Cubemap.
            size: Initial value for Size.
            has_mip_maps: Initial value for HasMipMaps.
            mip_map_count: Initial value for MipMapCount.
            memory_bytes: Initial value for MemoryBytes.
            formatted_memory_bytes: Initial value for FormattedMemoryBytes.
            actual_loaded_variant: Initial value for ActualLoadedVariant.
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
        if actual_loaded_variant is not None:
            self.actual_loaded_variant = actual_loaded_variant

    @property
    def cubemap(self) -> str | None:
        """Target ID of the Cubemap reference (targets IAssetProvider[Cubemap])."""
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
    def has_mip_maps(self) -> bool | None:
        """The HasMipMaps field value."""
        member = self.get_member("HasMipMaps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @has_mip_maps.setter
    def has_mip_maps(self, value: bool) -> None:
        """Set the HasMipMaps field value."""
        member = self.get_member("HasMipMaps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HasMipMaps", fields.FieldBool(value=value)
            )

    @property
    def mip_map_count(self) -> np.int32 | None:
        """The MipMapCount field value."""
        member = self.get_member("MipMapCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mip_map_count.setter
    def mip_map_count(self, value: np.int32) -> None:
        """Set the MipMapCount field value."""
        member = self.get_member("MipMapCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MipMapCount", fields.FieldInt(value=value)
            )

    @property
    def memory_bytes(self) -> np.int64 | None:
        """The MemoryBytes field value."""
        member = self.get_member("MemoryBytes")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @memory_bytes.setter
    def memory_bytes(self, value: np.int64) -> None:
        """Set the MemoryBytes field value."""
        member = self.get_member("MemoryBytes")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MemoryBytes", fields.FieldLong(value=value)
            )

    @property
    def formatted_memory_bytes(self) -> str | None:
        """The FormattedMemoryBytes field value."""
        member = self.get_member("FormattedMemoryBytes")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @formatted_memory_bytes.setter
    def formatted_memory_bytes(self, value: str) -> None:
        """Set the FormattedMemoryBytes field value."""
        member = self.get_member("FormattedMemoryBytes")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FormattedMemoryBytes", fields.FieldString(value=value)
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
    def actual_loaded_variant(self) -> str | None:
        """The ActualLoadedVariant field value."""
        member = self.get_member("ActualLoadedVariant")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @actual_loaded_variant.setter
    def actual_loaded_variant(self, value: str) -> None:
        """Set the ActualLoadedVariant field value."""
        member = self.get_member("ActualLoadedVariant")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActualLoadedVariant", fields.FieldString(value=value)
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

