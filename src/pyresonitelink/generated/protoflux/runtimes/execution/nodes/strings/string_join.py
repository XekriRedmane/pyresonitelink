"""Generated component: StringJoin."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StringJoin(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """String Join is a protoflux node that can take a Separator (String), and a some Inputs (List of String) and combine them, separating each item with Separator (String), or with nothing if Separator (String) is not provided.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.StringJoin"

    def __init__(self, separator: str | INodeObjectOutput[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            separator: Initial value for Separator.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if separator is not None:
            self.separator = separator

    @property
    def inputs(self) -> members.SyncList | None:
        """The items to join together"""
        member = self.get_member("Inputs")
        if isinstance(member, members.SyncList):
            return member
        return None

    @inputs.setter
    def inputs(self, value: members.SyncList) -> None:
        """Set Inputs. The items to join together"""
        self.set_member("Inputs", value)

    @property
    def separator(self) -> str | None:
        """The item to separate the Inputs (List of String) when joined."""
        member = self.get_member("Separator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @separator.setter
    def separator(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Separator reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Separator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Separator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

