"""Generated component: GetRawDataToolHit."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.raw_data_tool import RawDataTool
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GetRawDataToolHit(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``Get Raw Data Tool Hit`` node creates a raycast from the origin (tip reference slot position and direction?) looking and retrieving for valid hits. This node acts similarly to the Raycaster and Raycast One nodes in functionality.

This node returns data per frame, and is very useful for debugging and testing hit detection due to its constant updates.

This node can be combined with the Hit UV Coordinate node to get further data from this hit, such as a 2D location point on the collider for example.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Tools
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.Tools.GetRawDataToolHit"

    def __init__(self, tool: str | INodeObjectOutput[RawDataTool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tool: Initial value for Tool.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if tool is not None:
            self.tool = tool

    @property
    def tool(self) -> str | None:
        """Target ID of the Tool reference (targets INodeObjectOutput[RawDataTool])."""
        member = self.get_member("Tool")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tool.setter
    def tool(self, target: str | INodeObjectOutput[RawDataTool] | None) -> None:
        """Set the Tool reference by target ID or INodeObjectOutput[RawDataTool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Tool")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Tool",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.RawDataTool>'),
            )

    @property
    def hit_collider(self) -> members.EmptyElement | None:
        """The HitCollider member."""
        member = self.get_member("HitCollider")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hit_collider.setter
    def hit_collider(self, value: members.EmptyElement) -> None:
        """Set the HitCollider member."""
        self.set_member("HitCollider", value)

    @property
    def hit_point(self) -> members.EmptyElement | None:
        """The point in 3D space of where we hit."""
        member = self.get_member("HitPoint")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hit_point.setter
    def hit_point(self, value: members.EmptyElement) -> None:
        """Set HitPoint. The point in 3D space of where we hit."""
        self.set_member("HitPoint", value)

    @property
    def hit_normal(self) -> members.EmptyElement | None:
        """The normal of the collider facing direction."""
        member = self.get_member("HitNormal")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hit_normal.setter
    def hit_normal(self, value: members.EmptyElement) -> None:
        """Set HitNormal. The normal of the collider facing direction."""
        self.set_member("HitNormal", value)

    @property
    def hit_distance(self) -> members.EmptyElement | None:
        """The distance of how far this hit was from the origin of this raycast."""
        member = self.get_member("HitDistance")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hit_distance.setter
    def hit_distance(self, value: members.EmptyElement) -> None:
        """Set HitDistance. The distance of how far this hit was from the origin of this raycast."""
        self.set_member("HitDistance", value)

    @property
    def hit_triangle_index(self) -> members.EmptyElement | None:
        """The mesh data number of our hit."""
        member = self.get_member("HitTriangleIndex")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hit_triangle_index.setter
    def hit_triangle_index(self, value: members.EmptyElement) -> None:
        """Set HitTriangleIndex. The mesh data number of our hit."""
        self.set_member("HitTriangleIndex", value)

