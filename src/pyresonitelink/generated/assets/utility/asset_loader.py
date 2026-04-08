"""Generated component: AssetLoader."""

from typing import Any

A = Any
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AssetLoader(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AssetLoader<>.

    Category: Assets/Utility

    Parameterize with a value type::

        AssetLoader[np.float32]
        AssetLoader[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AssetLoader<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.AssetLoader<>"

    def __init__(self, asset: str | IAssetProvider[A] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            asset: Initial value for Asset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if asset is not None:
            self.asset = asset

    @property
    def asset(self) -> str | None:
        """Target ID of the Asset reference (targets IAssetProvider[A])."""
        member = self.get_member("Asset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @asset.setter
    def asset(self, target: str | IAssetProvider[A] | None) -> None:
        """Set the Asset reference by target ID or IAssetProvider[A] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Asset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Asset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<A>'),
            )

