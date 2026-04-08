"""Generated component: FireOnLocalTrue."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation


class FireOnLocalTrue(GeneratedComponent):
    """The FireOnLocalTrue node will listen for changes on its input bool and fire an impulse whenever the input turns from False to True across updates.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow

    **See also**: * FireOnTrue for the non-local equivalent of this node where a user to fire the impulse on can be specified.
* FireOnLocalChange
* FireOnLocalFalse

ProtoFlux:Flow
Listener nodes
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalTrue"

    def __init__(self, condition: str | INodeValueOutput[primitives.Bool] | None = None, on_change: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            condition: Initial value for Condition.
            on_change: Initial value for OnChange.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if condition is not None:
            self.condition = condition
        if on_change is not None:
            self.on_change = on_change

    @property
    def condition(self) -> str | None:
        """Target ID of the Condition reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Condition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @condition.setter
    def condition(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Condition reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Condition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Condition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def on_change(self) -> str | None:
        """Target ID of the OnChange reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnChange")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_change.setter
    def on_change(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnChange reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnChange")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnChange",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

