"""Generated component: WriteDynamicObjectVariable."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WriteDynamicObjectVariable(GenericComponent[T], IMappableNode, ISyncNodeOperation, IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicObjectVariable<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Variables/Dynamic

    Parameterize with a value type::

        WriteDynamicObjectVariable[np.float32]
        WriteDynamicObjectVariable[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicObjectVariable<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicObjectVariable<>"

    def __init__(self, target: str | INodeObjectOutput[Slot] | None = None, path: str | INodeObjectOutput[str] | None = None, on_not_found: str | INodeOperation | None = None, on_success: str | INodeOperation | None = None, on_failed: str | INodeOperation | None = None, value: str | INodeObjectOutput[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            path: Initial value for Path.
            on_not_found: Initial value for OnNotFound.
            on_success: Initial value for OnSuccess.
            on_failed: Initial value for OnFailed.
            value: Initial value for Value.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if path is not None:
            self.path = path
        if on_not_found is not None:
            self.on_not_found = on_not_found
        if on_success is not None:
            self.on_success = on_success
        if on_failed is not None:
            self.on_failed = on_failed
        if value is not None:
            self.value = value

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the Target reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def path(self) -> str | None:
        """Target ID of the Path reference (targets INodeObjectOutput[str])."""
        member = self.get_member("Path")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @path.setter
    def path(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the Path reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Path")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Path",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def on_not_found(self) -> str | None:
        """Target ID of the OnNotFound reference (targets INodeOperation)."""
        member = self.get_member("OnNotFound")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_not_found.setter
    def on_not_found(self, target: str | INodeOperation | None) -> None:
        """Set the OnNotFound reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnNotFound")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnNotFound",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_success(self) -> str | None:
        """Target ID of the OnSuccess reference (targets INodeOperation)."""
        member = self.get_member("OnSuccess")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_success.setter
    def on_success(self, target: str | INodeOperation | None) -> None:
        """Set the OnSuccess reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnSuccess")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnSuccess",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_failed(self) -> str | None:
        """Target ID of the OnFailed reference (targets INodeOperation)."""
        member = self.get_member("OnFailed")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_failed.setter
    def on_failed(self, target: str | INodeOperation | None) -> None:
        """Set the OnFailed reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnFailed")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnFailed",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
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

