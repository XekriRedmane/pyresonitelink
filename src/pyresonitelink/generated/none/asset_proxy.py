"""Generated component: AssetProxy."""

from typing import Any

A = Any
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.ireference_source import IReferenceSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AssetProxy(GenericComponent[T], IReferenceSource[T], IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AssetProxy<>.

    Parameterize with a value type::

        AssetProxy[np.float32]
        AssetProxy[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AssetProxy<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.AssetProxy<>"

    def __init__(self, asset_reference: str | IAssetProvider[A] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            asset_reference: Initial value for AssetReference.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if asset_reference is not None:
            self.asset_reference = asset_reference

    @property
    def asset_reference(self) -> str | None:
        """Target ID of the AssetReference reference (targets IAssetProvider[A])."""
        member = self.get_member("AssetReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @asset_reference.setter
    def asset_reference(self, target: str | IAssetProvider[A] | None) -> None:
        """Set the AssetReference reference by target ID or IAssetProvider[A] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("AssetReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AssetReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<A>'),
            )

