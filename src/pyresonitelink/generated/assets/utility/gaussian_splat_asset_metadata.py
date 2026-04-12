"""Generated component: GaussianSplatAssetMetadata."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.gaussian_splat import GaussianSplat
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GaussianSplatAssetMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Gaussian Splat Asset Metadata component gives statistics on Gaussian Splats seen in inspectors for components that generate or provide such data.

    Category: Assets/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GaussianSplatAssetMetadata"

    def __init__(self, splat: str | IAssetProvider[GaussianSplat] | None = None, splat_count: primitives.Int | None = None, memory_bytes: primitives.Long | None = None, formatted_memory_bytes: primitives.String | None = None, actual_loaded_variant: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            splat: Initial value for Splat.
            splat_count: Initial value for SplatCount.
            memory_bytes: Initial value for MemoryBytes.
            formatted_memory_bytes: Initial value for FormattedMemoryBytes.
            actual_loaded_variant: Initial value for ActualLoadedVariant.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if splat is not None:
            self.splat = splat
        if splat_count is not None:
            self.splat_count = splat_count
        if memory_bytes is not None:
            self.memory_bytes = memory_bytes
        if formatted_memory_bytes is not None:
            self.formatted_memory_bytes = formatted_memory_bytes
        if actual_loaded_variant is not None:
            self.actual_loaded_variant = actual_loaded_variant

    @property
    def splat(self) -> str | None:
        """The splat to get data on."""
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
    def splat_count(self) -> primitives.Int | None:
        """The number of splats in the Gaussian splat."""
        member = self.get_member("SplatCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @splat_count.setter
    def splat_count(self, value: primitives.Int) -> None:
        """Set the SplatCount field value."""
        member = self.get_member("SplatCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SplatCount", fields.FieldInt(value=value)
            )

    @property
    def memory_bytes(self) -> primitives.Long | None:
        """The amount of memory in bytes the Gaussian splat takes up."""
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
        """The amount of memory in bytes the Gaussian splat takes up when formatted."""
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
    def actual_loaded_variant(self) -> primitives.String | None:
        """The variant of the Gaussian splat that is loaded from the cloud."""
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

