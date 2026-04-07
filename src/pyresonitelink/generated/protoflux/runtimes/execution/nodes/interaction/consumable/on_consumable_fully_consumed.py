"""Generated component: OnConsumableFullyConsumed."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.consumable import Consumable
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OnConsumableFullyConsumed(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.OnConsumableFullyConsumed.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Interaction/Consumable
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.OnConsumableFullyConsumed"

    def __init__(self, consumable: str | IGlobalValueProxy[Consumable] | None = None, on_consumed: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            consumable: Initial value for Consumable.
            on_consumed: Initial value for OnConsumed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if consumable is not None:
            self.consumable = consumable
        if on_consumed is not None:
            self.on_consumed = on_consumed

    @property
    def consumable(self) -> str | None:
        """Target ID of the Consumable reference (targets IGlobalValueProxy[Consumable])."""
        member = self.get_member("Consumable")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @consumable.setter
    def consumable(self, target: str | IGlobalValueProxy[Consumable] | None) -> None:
        """Set the Consumable reference by target ID or IGlobalValueProxy[Consumable] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Consumable")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Consumable",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.Consumable>'),
            )

    @property
    def on_consumed(self) -> str | None:
        """Target ID of the OnConsumed reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnConsumed")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_consumed.setter
    def on_consumed(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnConsumed reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnConsumed")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnConsumed",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

