"""Generated component: WriteObjectToGlobal."""

from typing import Any

T = Any
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iglobal_ref_write import IGlobalRefWrite
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WriteObjectToGlobal(GeneratedComponent, IGlobalRefWrite, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.WriteObjectToGlobal<,>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Core
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.WriteObjectToGlobal<,>"

    def __init__(self, global_: str | IGlobalValueProxy[T] | None = None, value: str | INodeObjectOutput[T] | None = None, on_written: str | INodeOperation | None = None, on_fail: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            global_: Initial value for Global.
            value: Initial value for Value.
            on_written: Initial value for OnWritten.
            on_fail: Initial value for OnFail.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if global_ is not None:
            self.global_ = global_
        if value is not None:
            self.value = value
        if on_written is not None:
            self.on_written = on_written
        if on_fail is not None:
            self.on_fail = on_fail

    @property
    def global_(self) -> str | None:
        """Target ID of the Global reference (targets IGlobalValueProxy[T])."""
        member = self.get_member("Global")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @global_.setter
    def global_(self, target: str | IGlobalValueProxy[T] | None) -> None:
        """Set the Global reference by target ID or IGlobalValueProxy[T] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Global")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Global",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<T>'),
            )

    @property
    def value(self) -> str | None:
        """Target ID of the Value reference (targets INodeObjectOutput[T])."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | INodeObjectOutput[T] | None) -> None:
        """Set the Value reference by target ID or INodeObjectOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<T>'),
            )

    @property
    def on_written(self) -> str | None:
        """Target ID of the OnWritten reference (targets INodeOperation)."""
        member = self.get_member("OnWritten")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_written.setter
    def on_written(self, target: str | INodeOperation | None) -> None:
        """Set the OnWritten reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnWritten")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnWritten",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_fail(self) -> str | None:
        """Target ID of the OnFail reference (targets INodeOperation)."""
        member = self.get_member("OnFail")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_fail.setter
    def on_fail(self, target: str | INodeOperation | None) -> None:
        """Set the OnFail reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnFail")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnFail",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

