"""Generated component: ColorXMultiplicativeBlend."""

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


class ColorXMultiplicativeBlend(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """ColorX Multiplicative Blend does a multiplicative blend of its two input colors. The result is the product of each component between the target and destination.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Colors
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorXMultiplicativeBlend"

    def __init__(self, source: str | INodeValueOutput[primitives.ColorX] | None = None, destination: str | INodeValueOutput[primitives.ColorX] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            destination: Initial value for Destination.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if destination is not None:
            self.destination = destination

    @property
    def source(self) -> str | None:
        """Target ID of the Source reference (targets INodeValueOutput[primitives.ColorX])."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | INodeValueOutput[primitives.ColorX] | None) -> None:
        """Set the Source reference by target ID or INodeValueOutput[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<colorX>'),
            )

    @property
    def destination(self) -> str | None:
        """Target ID of the Destination reference (targets INodeValueOutput[primitives.ColorX])."""
        member = self.get_member("Destination")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @destination.setter
    def destination(self, target: str | INodeValueOutput[primitives.ColorX] | None) -> None:
        """Set the Destination reference by target ID or INodeValueOutput[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Destination")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Destination",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<colorX>'),
            )

