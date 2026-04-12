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
    """Asset Proxy is a component that allows for access to an asset through a slot when being grabbed by the user.

    put this component on a slot and fill the ``AssetReference`` with an
    asset reference to allow access to an asset via holding this slot's
    object root. The asset will then be available when holding onto the
    object root of the slot this component is on, and clicking on a UIX
    field (ex: an inspector field) places the asset type that this component
    has inside of it into the field.

    Parameterize with a value type::

        AssetProxy[primitives.Float]
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
        """The asset to expose to asset ref fields when grabbing the object root of the slot this component is on."""
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

