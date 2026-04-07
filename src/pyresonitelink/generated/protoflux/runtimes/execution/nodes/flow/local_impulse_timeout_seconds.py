"""Generated component: LocalImpulseTimeoutSeconds."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocalImpulseTimeoutSeconds(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.LocalImpulseTimeoutSeconds.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.LocalImpulseTimeoutSeconds"

    def __init__(self, next: str | INodeOperation | None = None, timeout: str | INodeValueOutput[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            timeout: Initial value for Timeout.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if timeout is not None:
            self.timeout = timeout

    @property
    def trigger(self) -> members.EmptyElement | None:
        """The Trigger member."""
        member = self.get_member("Trigger")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @trigger.setter
    def trigger(self, value: members.EmptyElement) -> None:
        """Set the Trigger member."""
        self.set_member("Trigger", value)

    @property
    def reset(self) -> members.EmptyElement | None:
        """The Reset member."""
        member = self.get_member("Reset")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @reset.setter
    def reset(self, value: members.EmptyElement) -> None:
        """Set the Reset member."""
        self.set_member("Reset", value)

    @property
    def next(self) -> str | None:
        """Target ID of the Next reference (targets INodeOperation)."""
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @next.setter
    def next(self, target: str | INodeOperation | None) -> None:
        """Set the Next reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Next",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def timeout(self) -> str | None:
        """Target ID of the Timeout reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("Timeout")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timeout.setter
    def timeout(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the Timeout reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Timeout")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Timeout",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

