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
    """AssetLoader is a Component that is used to tell the game that an Asset is still being used. This is helpful for when an asset is referenced in a way that deletes it during asset cleanup and saving.

    Category: Assets/Utility

    Set the ``Asset`` field to the asset that should be kept around,
    afterwards the asset should not be cleaned up as long as it continues to
    be referenced by the AssetLoader.

    Parameterize with a value type::

        AssetLoader[primitives.Float]
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
        """The Asset to keep loaded."""
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

