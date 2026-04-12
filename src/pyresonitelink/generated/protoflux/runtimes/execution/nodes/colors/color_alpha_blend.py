"""Generated component: ColorAlphaBlend."""

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


class ColorAlphaBlend(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Color Alpha Blend does an alpha blend of its two input colors. The source is blended "onto" the destination, and the higher the source alpha, the more of the "source" color and less of the "destination" color comes through.

Alpha values are summed and clamped to a maximum of 1.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Colors
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorAlphaBlend"

    def __init__(self, source: str | INodeValueOutput[primitives.Color] | None = None, destination: str | INodeValueOutput[primitives.Color] | None = None, *, component: workers.Component | None = None) -> None:
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
        """The color that is blended "onto" the destination."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | INodeValueOutput[primitives.Color] | None) -> None:
        """Set the Source reference by target ID or INodeValueOutput[primitives.Color] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<color>'),
            )

    @property
    def destination(self) -> str | None:
        """The destination color that the source is blended "onto"."""
        member = self.get_member("Destination")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @destination.setter
    def destination(self, target: str | INodeValueOutput[primitives.Color] | None) -> None:
        """Set the Destination reference by target ID or INodeValueOutput[primitives.Color] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Destination")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Destination",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<color>'),
            )

