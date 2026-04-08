"""Generated component: CreateDynamicValueVariable."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
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


class CreateDynamicValueVariable(GenericComponent[T], IMappableNode, ISyncNodeOperation, IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Variables/Dynamic

    Parameterize with a value type::

        CreateDynamicValueVariable[primitives.Float]
        CreateDynamicValueVariable[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<>"

    def __init__(self, target: str | INodeObjectOutput[Slot] | None = None, path: str | INodeObjectOutput[primitives.String] | None = None, on_not_found: str | INodeOperation | None = None, on_created: str | INodeOperation | None = None, on_already_exists: str | INodeOperation | None = None, on_failed: str | INodeOperation | None = None, create_directly_on_target: str | INodeValueOutput[primitives.Bool] | None = None, create_non_persistent: str | INodeValueOutput[primitives.Bool] | None = None, initial_value: str | INodeValueOutput[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            path: Initial value for Path.
            on_not_found: Initial value for OnNotFound.
            on_created: Initial value for OnCreated.
            on_already_exists: Initial value for OnAlreadyExists.
            on_failed: Initial value for OnFailed.
            create_directly_on_target: Initial value for CreateDirectlyOnTarget.
            create_non_persistent: Initial value for CreateNonPersistent.
            initial_value: Initial value for InitialValue.
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
        if on_already_exists is not None:
            self.on_already_exists = on_already_exists
        if on_failed is not None:
            self.on_failed = on_failed
        if create_directly_on_target is not None:
            self.create_directly_on_target = create_directly_on_target
        if create_non_persistent is not None:
            self.create_non_persistent = create_non_persistent
        if initial_value is not None:
            self.initial_value = initial_value

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
        """Target ID of the Path reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("Path")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @path.setter
    def path(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Path reference by target ID or INodeObjectOutput[primitives.String] instance."""
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
    def on_already_exists(self) -> str | None:
        """Target ID of the OnAlreadyExists reference (targets INodeOperation)."""
        member = self.get_member("OnAlreadyExists")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_already_exists.setter
    def on_already_exists(self, target: str | INodeOperation | None) -> None:
        """Set the OnAlreadyExists reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnAlreadyExists")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnAlreadyExists",
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
        """Target ID of the CreateDirectlyOnTarget reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("CreateDirectlyOnTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @create_directly_on_target.setter
    def create_directly_on_target(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the CreateDirectlyOnTarget reference by target ID or INodeValueOutput[primitives.Bool] instance."""
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
        """Target ID of the CreateNonPersistent reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("CreateNonPersistent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @create_non_persistent.setter
    def create_non_persistent(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the CreateNonPersistent reference by target ID or INodeValueOutput[primitives.Bool] instance."""
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
    def initial_value(self) -> str | None:
        """Target ID of the InitialValue reference (targets INodeValueOutput[T])."""
        member = self.get_member("InitialValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @initial_value.setter
    def initial_value(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the InitialValue reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("InitialValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "InitialValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

