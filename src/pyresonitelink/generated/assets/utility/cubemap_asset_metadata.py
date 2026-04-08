"""Generated component: CubemapAssetMetadata."""

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

    def __init__(self, cubemap: str | IAssetProvider[Cubemap] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            cubemap: Initial value for Cubemap.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if cubemap is not None:
            self.cubemap = cubemap

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
    def size(self) -> members.EmptyElement | None:
        """The Size member."""
        member = self.get_member("Size")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @size.setter
    def size(self, value: members.EmptyElement) -> None:
        """Set the Size member."""
        self.set_member("Size", value)

    @property
    def has_mip_maps(self) -> members.EmptyElement | None:
        """The HasMipMaps member."""
        member = self.get_member("HasMipMaps")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @has_mip_maps.setter
    def has_mip_maps(self, value: members.EmptyElement) -> None:
        """Set the HasMipMaps member."""
        self.set_member("HasMipMaps", value)

    @property
    def mip_map_count(self) -> members.EmptyElement | None:
        """The MipMapCount member."""
        member = self.get_member("MipMapCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @mip_map_count.setter
    def mip_map_count(self, value: members.EmptyElement) -> None:
        """Set the MipMapCount member."""
        self.set_member("MipMapCount", value)

    @property
    def memory_bytes(self) -> members.EmptyElement | None:
        """The MemoryBytes member."""
        member = self.get_member("MemoryBytes")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @memory_bytes.setter
    def memory_bytes(self, value: members.EmptyElement) -> None:
        """Set the MemoryBytes member."""
        self.set_member("MemoryBytes", value)

    @property
    def formatted_memory_bytes(self) -> members.EmptyElement | None:
        """The FormattedMemoryBytes member."""
        member = self.get_member("FormattedMemoryBytes")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @formatted_memory_bytes.setter
    def formatted_memory_bytes(self, value: members.EmptyElement) -> None:
        """Set the FormattedMemoryBytes member."""
        self.set_member("FormattedMemoryBytes", value)

    @property
    def format_(self) -> members.EmptyElement | None:
        """The Format member."""
        member = self.get_member("Format")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @format_.setter
    def format_(self, value: members.EmptyElement) -> None:
        """Set the Format member."""
        self.set_member("Format", value)

    @property
    def actual_loaded_variant(self) -> members.EmptyElement | None:
        """The ActualLoadedVariant member."""
        member = self.get_member("ActualLoadedVariant")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @actual_loaded_variant.setter
    def actual_loaded_variant(self, value: members.EmptyElement) -> None:
        """Set the ActualLoadedVariant member."""
        self.set_member("ActualLoadedVariant", value)

    @property
    def profile(self) -> members.EmptyElement | None:
        """The Profile member."""
        member = self.get_member("Profile")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @profile.setter
    def profile(self, value: members.EmptyElement) -> None:
        """Set the Profile member."""
        self.set_member("Profile", value)

