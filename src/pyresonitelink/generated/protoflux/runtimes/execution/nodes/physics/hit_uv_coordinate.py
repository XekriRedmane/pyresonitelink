"""Generated component: HitUVCoordinate."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.icollider import ICollider
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HitUVCoordinate(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.HitUVCoordinate.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Physics
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.HitUVCoordinate"

    def __init__(self, hit_collider: str | INodeObjectOutput[ICollider] | None = None, hit_triangle_index: str | INodeValueOutput[np.int32] | None = None, hit_point: str | INodeValueOutput[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            hit_collider: Initial value for HitCollider.
            hit_triangle_index: Initial value for HitTriangleIndex.
            hit_point: Initial value for HitPoint.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if hit_collider is not None:
            self.hit_collider = hit_collider
        if hit_triangle_index is not None:
            self.hit_triangle_index = hit_triangle_index
        if hit_point is not None:
            self.hit_point = hit_point

    @property
    def hit_collider(self) -> str | None:
        """Target ID of the HitCollider reference (targets INodeObjectOutput[ICollider])."""
        member = self.get_member("HitCollider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hit_collider.setter
    def hit_collider(self, target: str | INodeObjectOutput[ICollider] | None) -> None:
        """Set the HitCollider reference by target ID or INodeObjectOutput[ICollider] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("HitCollider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HitCollider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.ICollider>'),
            )

    @property
    def hit_triangle_index(self) -> str | None:
        """Target ID of the HitTriangleIndex reference (targets INodeValueOutput[np.int32])."""
        member = self.get_member("HitTriangleIndex")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hit_triangle_index.setter
    def hit_triangle_index(self, target: str | INodeValueOutput[np.int32] | None) -> None:
        """Set the HitTriangleIndex reference by target ID or INodeValueOutput[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("HitTriangleIndex")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HitTriangleIndex",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def hit_point(self) -> str | None:
        """Target ID of the HitPoint reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("HitPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hit_point.setter
    def hit_point(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the HitPoint reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("HitPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HitPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def uv(self) -> members.EmptyElement | None:
        """The UV member."""
        member = self.get_member("UV")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @uv.setter
    def uv(self, value: members.EmptyElement) -> None:
        """Set the UV member."""
        self.set_member("UV", value)

    @property
    def is_valid_uv(self) -> members.EmptyElement | None:
        """The IsValidUV member."""
        member = self.get_member("IsValidUV")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_valid_uv.setter
    def is_valid_uv(self, value: members.EmptyElement) -> None:
        """Set the IsValidUV member."""
        self.set_member("IsValidUV", value)

