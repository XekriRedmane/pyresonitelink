"""Generated component: OnConsumableConsuming."""

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


class OnConsumableConsuming(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.OnConsumableConsuming.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Interaction/Consumable
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.OnConsumableConsuming"

    def __init__(self, consumable: str | IGlobalValueProxy[Consumable] | None = None, on_consuming: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            consumable: Initial value for Consumable.
            on_consuming: Initial value for OnConsuming.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if consumable is not None:
            self.consumable = consumable
        if on_consuming is not None:
            self.on_consuming = on_consuming

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
    def on_consuming(self) -> str | None:
        """Target ID of the OnConsuming reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnConsuming")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_consuming.setter
    def on_consuming(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnConsuming reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnConsuming")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnConsuming",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def stage_index(self) -> members.EmptyElement | None:
        """The StageIndex member."""
        member = self.get_member("StageIndex")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @stage_index.setter
    def stage_index(self, value: members.EmptyElement) -> None:
        """Set the StageIndex member."""
        self.set_member("StageIndex", value)

    @property
    def normalized_consume_progress(self) -> members.EmptyElement | None:
        """The NormalizedConsumeProgress member."""
        member = self.get_member("NormalizedConsumeProgress")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @normalized_consume_progress.setter
    def normalized_consume_progress(self, value: members.EmptyElement) -> None:
        """Set the NormalizedConsumeProgress member."""
        self.set_member("NormalizedConsumeProgress", value)

