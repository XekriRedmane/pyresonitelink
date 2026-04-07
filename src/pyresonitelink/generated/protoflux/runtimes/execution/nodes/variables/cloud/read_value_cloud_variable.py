"""Generated component: ReadValueCloudVariable."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReadValueCloudVariable(GenericComponent[T], IAsyncNodeOperation, IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Variables/Cloud

    Parameterize with a value type::

        ReadValueCloudVariable[np.float32]
        ReadValueCloudVariable[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<>"

    def __init__(self, path: str | INodeObjectOutput[str] | None = None, variable_owner_id: str | INodeObjectOutput[str] | None = None, on_request: str | INodeOperation | None = None, on_done: str | INodeOperation | None = None, on_fail: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            path: Initial value for Path.
            variable_owner_id: Initial value for VariableOwnerId.
            on_request: Initial value for OnRequest.
            on_done: Initial value for OnDone.
            on_fail: Initial value for OnFail.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if path is not None:
            self.path = path
        if variable_owner_id is not None:
            self.variable_owner_id = variable_owner_id
        if on_request is not None:
            self.on_request = on_request
        if on_done is not None:
            self.on_done = on_done
        if on_fail is not None:
            self.on_fail = on_fail

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
    def variable_owner_id(self) -> str | None:
        """Target ID of the VariableOwnerId reference (targets INodeObjectOutput[str])."""
        member = self.get_member("VariableOwnerId")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @variable_owner_id.setter
    def variable_owner_id(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the VariableOwnerId reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("VariableOwnerId")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "VariableOwnerId",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def on_request(self) -> str | None:
        """Target ID of the OnRequest reference (targets INodeOperation)."""
        member = self.get_member("OnRequest")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_request.setter
    def on_request(self, target: str | INodeOperation | None) -> None:
        """Set the OnRequest reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnRequest")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnRequest",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_done(self) -> str | None:
        """Target ID of the OnDone reference (targets INodeOperation)."""
        member = self.get_member("OnDone")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_done.setter
    def on_done(self, target: str | INodeOperation | None) -> None:
        """Set the OnDone reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnDone")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnDone",
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

    @property
    def value(self) -> members.EmptyElement | None:
        """The Value member."""
        member = self.get_member("Value")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @value.setter
    def value(self, value: members.EmptyElement) -> None:
        """Set the Value member."""
        self.set_member("Value", value)

