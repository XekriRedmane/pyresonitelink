"""Generated component: BooleanAssetDriver."""

from typing import Any

A = Any
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.asset_ref import AssetRef
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BooleanAssetDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BooleanAssetDriver<>.

    Category: Assets/Utility

    Parameterize with a value type::

        BooleanAssetDriver[np.float32]
        BooleanAssetDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BooleanAssetDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.BooleanAssetDriver<>"

    def __init__(self, state: bool | None = None, target: str | AssetRef[A] | None = None, false_target: str | IAssetProvider[A] | None = None, true_target: str | IAssetProvider[A] | None = None, *, component: workers.Component | None = None) -> None:
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
    def state(self) -> bool | None:
        """The State field value."""
        member = self.get_member("State")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @state.setter
    def state(self, value: bool) -> None:
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
        """Target ID of the Target reference (targets AssetRef[A])."""
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
        """Target ID of the FalseTarget reference (targets IAssetProvider[A])."""
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
        """Target ID of the TrueTarget reference (targets IAssetProvider[A])."""
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

