"""Generated component: CreateUndoBatch."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CreateUndoBatch(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Undo.CreateUndoBatch.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Undo
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Undo.CreateUndoBatch"

    def __init__(self, description: str | INodeObjectOutput[primitives.String] | None = None, create: str | ISyncNodeOperation | None = None, on_created: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            description: Initial value for Description.
            create: Initial value for Create.
            on_created: Initial value for OnCreated.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if description is not None:
            self.description = description
        if create is not None:
            self.create = create
        if on_created is not None:
            self.on_created = on_created

    @property
    def description(self) -> str | None:
        """Target ID of the Description reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("Description")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @description.setter
    def description(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Description reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Description")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Description",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def create(self) -> str | None:
        """Target ID of the Create reference (targets ISyncNodeOperation)."""
        member = self.get_member("Create")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @create.setter
    def create(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the Create reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Create")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Create",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
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

