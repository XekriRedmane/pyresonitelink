"""Generated component: ImpulseMultiplexer."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ImpulseMultiplexer(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ImpulseMultiplexer.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ImpulseMultiplexer"

    def __init__(self, index: str | INodeValueOutput[np.int32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            index: Initial value for Index.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if index is not None:
            self.index = index

    @property
    def index(self) -> str | None:
        """Target ID of the Index reference (targets INodeValueOutput[np.int32])."""
        member = self.get_member("Index")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @index.setter
    def index(self, target: str | INodeValueOutput[np.int32] | None) -> None:
        """Set the Index reference by target ID or INodeValueOutput[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Index")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Index",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def impulses(self) -> members.SyncList | None:
        """The Impulses member."""
        member = self.get_member("Impulses")
        if isinstance(member, members.SyncList):
            return member
        return None

    @impulses.setter
    def impulses(self, value: members.SyncList) -> None:
        """Set the Impulses member."""
        self.set_member("Impulses", value)

