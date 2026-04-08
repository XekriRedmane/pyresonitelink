"""Generated component: ProceduralAssetMetadata."""

from typing import Any

A = Any
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.procedural_asset_provider import ProceduralAssetProvider
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ProceduralAssetMetadata(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ProceduralAssetMetadata<>.

    Category: Assets/Utility

    Parameterize with a value type::

        ProceduralAssetMetadata[primitives.Float]
        ProceduralAssetMetadata[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProceduralAssetMetadata<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ProceduralAssetMetadata<>"

    def __init__(self, asset: str | ProceduralAssetProvider[A] | None = None, update_count: primitives.Int | None = None, error: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            asset: Initial value for Asset.
            update_count: Initial value for UpdateCount.
            error: Initial value for Error.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if asset is not None:
            self.asset = asset
        if update_count is not None:
            self.update_count = update_count
        if error is not None:
            self.error = error

    @property
    def asset(self) -> str | None:
        """Target ID of the Asset reference (targets ProceduralAssetProvider[A])."""
        member = self.get_member("Asset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @asset.setter
    def asset(self, target: str | ProceduralAssetProvider[A] | None) -> None:
        """Set the Asset reference by target ID or ProceduralAssetProvider[A] instance."""
        target_id: str | None = target.id if isinstance(target, ProceduralAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Asset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Asset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProceduralAssetProvider<A>'),
            )

    @property
    def update_count(self) -> primitives.Int | None:
        """The UpdateCount field value."""
        member = self.get_member("UpdateCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @update_count.setter
    def update_count(self, value: primitives.Int) -> None:
        """Set the UpdateCount field value."""
        member = self.get_member("UpdateCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UpdateCount", fields.FieldInt(value=value)
            )

    @property
    def error(self) -> primitives.Bool | None:
        """The Error field value."""
        member = self.get_member("Error")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @error.setter
    def error(self, value: primitives.Bool) -> None:
        """Set the Error field value."""
        member = self.get_member("Error")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Error", fields.FieldBool(value=value)
            )

