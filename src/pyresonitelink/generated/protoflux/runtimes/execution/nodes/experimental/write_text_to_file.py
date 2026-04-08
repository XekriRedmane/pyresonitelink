"""Generated component: WriteTextToFile."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WriteTextToFile(GeneratedComponent, IAsyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Write Text To File node allows you to write files to your device, given if there is a path and proper permissions.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Experimental
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Experimental.WriteTextToFile"

    def __init__(self, string: str | INodeObjectOutput[primitives.String] | None = None, file_path: str | INodeObjectOutput[primitives.String] | None = None, append: str | INodeValueOutput[primitives.Bool] | None = None, new_line: str | INodeValueOutput[primitives.Bool] | None = None, on_write_started: str | INodeOperation | None = None, on_write_finished: str | INodeOperation | None = None, on_write_fail: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            string: Initial value for String.
            file_path: Initial value for FilePath.
            append: Initial value for Append.
            new_line: Initial value for NewLine.
            on_write_started: Initial value for OnWriteStarted.
            on_write_finished: Initial value for OnWriteFinished.
            on_write_fail: Initial value for OnWriteFail.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if string is not None:
            self.string = string
        if file_path is not None:
            self.file_path = file_path
        if append is not None:
            self.append = append
        if new_line is not None:
            self.new_line = new_line
        if on_write_started is not None:
            self.on_write_started = on_write_started
        if on_write_finished is not None:
            self.on_write_finished = on_write_finished
        if on_write_fail is not None:
            self.on_write_fail = on_write_fail

    @property
    def string(self) -> str | None:
        """Target ID of the String reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("String")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @string.setter
    def string(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the String reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("String")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "String",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def file_path(self) -> str | None:
        """Target ID of the FilePath reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("FilePath")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @file_path.setter
    def file_path(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the FilePath reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("FilePath")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FilePath",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def append(self) -> str | None:
        """Target ID of the Append reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Append")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @append.setter
    def append(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Append reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Append")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Append",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def new_line(self) -> str | None:
        """Target ID of the NewLine reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("NewLine")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @new_line.setter
    def new_line(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the NewLine reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("NewLine")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NewLine",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def on_write_started(self) -> str | None:
        """Target ID of the OnWriteStarted reference (targets INodeOperation)."""
        member = self.get_member("OnWriteStarted")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_write_started.setter
    def on_write_started(self, target: str | INodeOperation | None) -> None:
        """Set the OnWriteStarted reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnWriteStarted")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnWriteStarted",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_write_finished(self) -> str | None:
        """Target ID of the OnWriteFinished reference (targets INodeOperation)."""
        member = self.get_member("OnWriteFinished")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_write_finished.setter
    def on_write_finished(self, target: str | INodeOperation | None) -> None:
        """Set the OnWriteFinished reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnWriteFinished")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnWriteFinished",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_write_fail(self) -> str | None:
        """Target ID of the OnWriteFail reference (targets INodeOperation)."""
        member = self.get_member("OnWriteFail")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_write_fail.setter
    def on_write_fail(self, target: str | INodeOperation | None) -> None:
        """Set the OnWriteFail reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnWriteFail")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnWriteFail",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

