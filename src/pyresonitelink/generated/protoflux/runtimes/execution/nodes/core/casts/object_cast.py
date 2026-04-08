"""Generated component: ObjectCast."""

from typing import Any

I = Any
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.icast import ICast
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ObjectCast(GeneratedComponent, ICast, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """alt=A picture of an object cast. Looks like a square object with one side a different color than the other, with a split down the middle that has a beveled edge. Though it's just an image so you can't actually feel such bevel in game even with detailed haptics.|thumb|An object cast from Type:IWorldElement|IWorldElement to IFieldint.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Core/Casts
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.ObjectCast<,>"

    def __init__(self, input_: str | INodeObjectOutput[I] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            input_: Initial value for Input.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if input_ is not None:
            self.input_ = input_

    @property
    def input_(self) -> str | None:
        """Target ID of the Input reference (targets INodeObjectOutput[I])."""
        member = self.get_member("Input")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @input_.setter
    def input_(self, target: str | INodeObjectOutput[I] | None) -> None:
        """Set the Input reference by target ID or INodeObjectOutput[I] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Input")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Input",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<I>'),
            )

