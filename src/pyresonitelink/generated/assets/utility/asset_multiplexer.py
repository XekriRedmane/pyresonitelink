"""Generated component: AssetMultiplexer."""

from typing import Any

A = Any
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.asset_ref import AssetRef
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AssetMultiplexer(GenericComponent[T], IComponent, IWorldEventReceiver):
    """The AssetMultiplexer component is used to drive an asset field from a list of assets and an index within the list.

    Category: Assets/Utility

    Add the list of assets you want to use through the SyncAssetList area,
    then add in your assets into the items. Then you can specify the field
    through the Target you wanna switch between different assets for.
    Changing the Index will change which asset the Target has in it. Ensure
    you can set the Target field on this component before making any other
    components reference the Index field on this component if you don't
    wanna waste your time.

    Parameterize with a value type::

        AssetMultiplexer[primitives.Float]
        AssetMultiplexer[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AssetMultiplexer<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.AssetMultiplexer<>"

    def __init__(self, target: str | AssetRef[A] | None = None, index_: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            index_: Initial value for Index.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if index_ is not None:
            self.index_ = index_

    @property
    def target(self) -> str | None:
        """The field to drive."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | AssetRef[A] | None) -> None:
        """Set the Target reference by target ID or AssetRef[A] instance."""
        target_id: str | None = target.id if isinstance(target, AssetRef) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AssetRef<A>'),
            )

    @property
    def index_(self) -> primitives.Int | None:
        """Which element in ``Assets`` to drive to ``Target``"""
        member = self.get_member("Index")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @index_.setter
    def index_(self, value: primitives.Int) -> None:
        """Set the Index field value."""
        member = self.get_member("Index")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Index", fields.FieldInt(value=value)
            )

    @property
    def assets(self) -> members.SyncList | None:
        """The list of assets to multiplex between."""
        member = self.get_member("Assets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @assets.setter
    def assets(self, value: members.SyncList) -> None:
        """Set Assets. The list of assets to multiplex between."""
        self.set_member("Assets", value)

