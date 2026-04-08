"""Generated component: GaussianSplatAssetMetadata."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.gaussian_splat import GaussianSplat
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GaussianSplatAssetMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GaussianSplatAssetMetadata.

    Category: Assets/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GaussianSplatAssetMetadata"

    def __init__(self, splat: str | IAssetProvider[GaussianSplat] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            splat: Initial value for Splat.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if splat is not None:
            self.splat = splat

    @property
    def splat(self) -> str | None:
        """Target ID of the Splat reference (targets IAssetProvider[GaussianSplat])."""
        member = self.get_member("Splat")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @splat.setter
    def splat(self, target: str | IAssetProvider[GaussianSplat] | None) -> None:
        """Set the Splat reference by target ID or IAssetProvider[GaussianSplat] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Splat")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Splat",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.GaussianSplat>'),
            )

    @property
    def splat_count(self) -> members.EmptyElement | None:
        """The SplatCount member."""
        member = self.get_member("SplatCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @splat_count.setter
    def splat_count(self, value: members.EmptyElement) -> None:
        """Set the SplatCount member."""
        self.set_member("SplatCount", value)

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

