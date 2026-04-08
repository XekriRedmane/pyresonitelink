"""Generated component: FromUnixMilliseconds."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FromUnixMilliseconds(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The From Unix Milliseconds node takes in the Unix milliseconds and then converts it into a DateTime, along with an option to offset it to make it a local DateTime (based on your time zone). The amount of milliseconds given will count up from the Unix epoch.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Time
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.TimeAndDate.FromUnixMilliseconds"

    def __init__(self, unix_miliseconds: str | INodeValueOutput[primitives.Long] | None = None, is_local: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            unix_miliseconds: Initial value for UnixMiliseconds.
            is_local: Initial value for IsLocal.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if unix_miliseconds is not None:
            self.unix_miliseconds = unix_miliseconds
        if is_local is not None:
            self.is_local = is_local

    @property
    def unix_miliseconds(self) -> str | None:
        """Target ID of the UnixMiliseconds reference (targets INodeValueOutput[primitives.Long])."""
        member = self.get_member("UnixMiliseconds")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @unix_miliseconds.setter
    def unix_miliseconds(self, target: str | INodeValueOutput[primitives.Long] | None) -> None:
        """Set the UnixMiliseconds reference by target ID or INodeValueOutput[primitives.Long] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("UnixMiliseconds")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UnixMiliseconds",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<long>'),
            )

    @property
    def is_local(self) -> str | None:
        """Target ID of the IsLocal reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("IsLocal")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @is_local.setter
    def is_local(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the IsLocal reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("IsLocal")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IsLocal",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

