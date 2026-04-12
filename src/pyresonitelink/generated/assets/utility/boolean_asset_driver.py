"""Generated component: BooleanAssetDriver."""

from typing import Any

A = Any
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.asset_ref import AssetRef
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BooleanAssetDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """This component is functionally identical to Boolean Reference Driver. Except it only accepts IAssets and acts as a user for assets in ``FalseTarget`` and ``TrueTarget`` meaning assets assigned to this component won't get cleaned up by the asset optimizer world processes.

    Category: Assets/Utility

    Attach this component to a slot, and (optionally) put an asset into the
    False and/or True target fields. Then, put a field which you want to
    change the asset of into ``Target``. now, switching ``State`` will allow
    switching between the values of ``FalseTarget`` and ``TrueTarget``.

    Parameterize with a value type::

        BooleanAssetDriver[primitives.Float]
        BooleanAssetDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BooleanAssetDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.BooleanAssetDriver<>"

    def __init__(self, state: primitives.Bool | None = None, target: str | AssetRef[A] | None = None, false_target: str | IAssetProvider[A] | None = None, true_target: str | IAssetProvider[A] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            state: Initial value for State.
            target: Initial value for Target.
            false_target: Initial value for FalseTarget.
            true_target: Initial value for TrueTarget.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if state is not None:
            self.state = state
        if target is not None:
            self.target = target
        if false_target is not None:
            self.false_target = false_target
        if true_target is not None:
            self.true_target = true_target

    @property
    def state(self) -> primitives.Bool | None:
        """Whether to drive ``Target`` to ``TrueTarget`` or ``FalseTarget``"""
        member = self.get_member("State")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @state.setter
    def state(self, value: primitives.Bool) -> None:
        """Set the State field value."""
        member = self.get_member("State")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "State", fields.FieldBool(value=value)
            )

    @property
    def target(self) -> str | None:
        """The field to drive the value of."""
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
    def false_target(self) -> str | None:
        """The asset to drive ``Target`` to when ``State`` is false."""
        member = self.get_member("FalseTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @false_target.setter
    def false_target(self, target: str | IAssetProvider[A] | None) -> None:
        """Set the FalseTarget reference by target ID or IAssetProvider[A] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("FalseTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FalseTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<A>'),
            )

    @property
    def true_target(self) -> str | None:
        """The asset to drive ``Target`` to when ``State`` is true."""
        member = self.get_member("TrueTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @true_target.setter
    def true_target(self, target: str | IAssetProvider[A] | None) -> None:
        """Set the TrueTarget reference by target ID or IAssetProvider[A] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("TrueTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TrueTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<A>'),
            )

