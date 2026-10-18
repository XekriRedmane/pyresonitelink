"""Generated component: SplitString."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SplitString(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Split String node takes in a string and a separator, along with options on how you want to handle empty entries. The node then returns a Collection of that string.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.SplitString"

    def __init__(self, string: str | INodeObjectOutput[primitives.String] | None = None, separator: str | INodeObjectOutput[primitives.String] | None = None, remove_empty_entries: str | INodeValueOutput[primitives.Bool] | None = None, trim_entries: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            string: Initial value for String.
            separator: Initial value for Separator.
            remove_empty_entries: Initial value for RemoveEmptyEntries.
            trim_entries: Initial value for TrimEntries.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if string is not None:
            self.string = string
        if separator is not None:
            self.separator = separator
        if remove_empty_entries is not None:
            self.remove_empty_entries = remove_empty_entries
        if trim_entries is not None:
            self.trim_entries = trim_entries

    @property
    def string(self) -> str | None:
        """The provided string used to turn into a collection."""
        member = self.get_member("String")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @string.setter
    def string(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the String reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("String")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "String",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def separator(self) -> str | None:
        """The string separator used to chop up the provided string for the array."""
        member = self.get_member("Separator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @separator.setter
    def separator(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Separator reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Separator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Separator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def remove_empty_entries(self) -> str | None:
        """If true, will remove any empty entries found in the provided string."""
        member = self.get_member("RemoveEmptyEntries")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @remove_empty_entries.setter
    def remove_empty_entries(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the RemoveEmptyEntries reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("RemoveEmptyEntries")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RemoveEmptyEntries",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def trim_entries(self) -> str | None:
        """If true, will remove any empty entries found around the start and end of the provided string."""
        member = self.get_member("TrimEntries")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @trim_entries.setter
    def trim_entries(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the TrimEntries reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("TrimEntries")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TrimEntries",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

