"""Generated component: Link."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Link(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Link node is used to connect two different node groups into one. You can drag an output wire (must be value or object, not call) into the null input to connect it. This can be used to make it easier to pack separated nodes together, due to being part of the same group and selecting one node will select them all.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Core
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Link"

    def __init__(self, a: str | INode | None = None, b: str | INode | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            a: Initial value for A.
            b: Initial value for B.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b

    @property
    def a(self) -> str | None:
        """Target ID of the A reference (targets INode)."""
        member = self.get_member("A")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @a.setter
    def a(self, target: str | INode | None) -> None:
        """Set the A reference by target ID or INode instance."""
        target_id: str | None = target.id if isinstance(target, INode) else target  # type: ignore[assignment]
        member = self.get_member("A")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "A",
                members.Reference(targetId=target_id, targetType='[ProtoFluxBindings]FrooxEngine.ProtoFlux.Core.INode'),
            )

    @property
    def b(self) -> str | None:
        """Target ID of the B reference (targets INode)."""
        member = self.get_member("B")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @b.setter
    def b(self, target: str | INode | None) -> None:
        """Set the B reference by target ID or INode instance."""
        target_id: str | None = target.id if isinstance(target, INode) else target  # type: ignore[assignment]
        member = self.get_member("B")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "B",
                members.Reference(targetId=target_id, targetType='[ProtoFluxBindings]FrooxEngine.ProtoFlux.Core.INode'),
            )

