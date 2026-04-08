"""Generated component: SetComponentEnabled."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SetComponentEnabled(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Get Component Enabled is a ProtoFlux node Takes an IComponent and gets if it's enabled or not.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Components
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Components.SetComponentEnabled"

    def __init__(self, next: str | INodeOperation | None = None, component_: str | INodeObjectOutput[IComponent] | None = None, state: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            component_: Initial value for Component.
            state: Initial value for State.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if component_ is not None:
            self.component_ = component_
        if state is not None:
            self.state = state

    @property
    def next(self) -> str | None:
        """Target ID of the Next reference (targets INodeOperation)."""
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @next.setter
    def next(self, target: str | INodeOperation | None) -> None:
        """Set the Next reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Next",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def component_(self) -> str | None:
        """Target ID of the Component reference (targets INodeObjectOutput[IComponent])."""
        member = self.get_member("Component")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @component_.setter
    def component_(self, target: str | INodeObjectOutput[IComponent] | None) -> None:
        """Set the Component reference by target ID or INodeObjectOutput[IComponent] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Component")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Component",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.IComponent>'),
            )

    @property
    def state(self) -> str | None:
        """Target ID of the State reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("State")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @state.setter
    def state(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the State reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("State")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "State",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

