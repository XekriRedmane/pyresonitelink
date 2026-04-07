"""Generated component: WriteOrCreateDynamicValueVariable."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WriteOrCreateDynamicValueVariable(GenericComponent[T], IMappableNode, ISyncNodeOperation, IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Variables/Dynamic

    Parameterize with a value type::

        WriteOrCreateDynamicValueVariable[np.float32]
        WriteOrCreateDynamicValueVariable[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<>"

    def __init__(self, target: str | INodeObjectOutput[Slot] | None = None, path: str | INodeObjectOutput[str] | None = None, on_not_found: str | INodeOperation | None = None, on_created: str | INodeOperation | None = None, on_written: str | INodeOperation | None = None, on_failed: str | INodeOperation | None = None, create_directly_on_target: str | INodeValueOutput[bool] | None = None, create_non_persistent: str | INodeValueOutput[bool] | None = None, value: str | INodeValueOutput[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            path: Initial value for Path.
            on_not_found: Initial value for OnNotFound.
            on_created: Initial value for OnCreated.
            on_written: Initial value for OnWritten.
            on_failed: Initial value for OnFailed.
            create_directly_on_target: Initial value for CreateDirectlyOnTarget.
            create_non_persistent: Initial value for CreateNonPersistent.
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
        if on_created is not None:
            self.on_created = on_created
        if on_written is not None:
            self.on_written = on_written
        if on_failed is not None:
            self.on_failed = on_failed
        if create_directly_on_target is not None:
            self.create_directly_on_target = create_directly_on_target
        if create_non_persistent is not None:
            self.create_non_persistent = create_non_persistent
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
    def on_created(self) -> str | None:
        """Target ID of the OnCreated reference (targets INodeOperation)."""
        member = self.get_member("OnCreated")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_created.setter
    def on_created(self, target: str | INodeOperation | None) -> None:
        """Set the OnCreated reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnCreated")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnCreated",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
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
    def create_directly_on_target(self) -> str | None:
        """Target ID of the CreateDirectlyOnTarget reference (targets INodeValueOutput[bool])."""
        member = self.get_member("CreateDirectlyOnTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @create_directly_on_target.setter
    def create_directly_on_target(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the CreateDirectlyOnTarget reference by target ID or INodeValueOutput[bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("CreateDirectlyOnTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CreateDirectlyOnTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def create_non_persistent(self) -> str | None:
        """Target ID of the CreateNonPersistent reference (targets INodeValueOutput[bool])."""
        member = self.get_member("CreateNonPersistent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @create_non_persistent.setter
    def create_non_persistent(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the CreateNonPersistent reference by target ID or INodeValueOutput[bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("CreateNonPersistent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CreateNonPersistent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def value(self) -> str | None:
        """Target ID of the Value reference (targets INodeValueOutput[T])."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the Value reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

