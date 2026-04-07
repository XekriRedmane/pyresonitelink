"""Generated component: Substring."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Substring(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.Substring.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.Substring"

    def __init__(self, str_: str | INodeObjectOutput[str] | None = None, start_index: str | INodeValueOutput[np.int32] | None = None, length: str | INodeValueOutput[np.int32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            str_: Initial value for Str.
            start_index: Initial value for StartIndex.
            length: Initial value for Length.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if str_ is not None:
            self.str_ = str_
        if start_index is not None:
            self.start_index = start_index
        if length is not None:
            self.length = length

    @property
    def str_(self) -> str | None:
        """Target ID of the Str reference (targets INodeObjectOutput[str])."""
        member = self.get_member("Str")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @str_.setter
    def str_(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the Str reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Str")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Str",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def start_index(self) -> str | None:
        """Target ID of the StartIndex reference (targets INodeValueOutput[np.int32])."""
        member = self.get_member("StartIndex")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @start_index.setter
    def start_index(self, target: str | INodeValueOutput[np.int32] | None) -> None:
        """Set the StartIndex reference by target ID or INodeValueOutput[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("StartIndex")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "StartIndex",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def length(self) -> str | None:
        """Target ID of the Length reference (targets INodeValueOutput[np.int32])."""
        member = self.get_member("Length")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @length.setter
    def length(self, target: str | INodeValueOutput[np.int32] | None) -> None:
        """Set the Length reference by target ID or INodeValueOutput[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Length")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Length",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

