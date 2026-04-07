"""Generated component: SampleColorX."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SampleColorX(GeneratedComponent, IAsyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Rendering.SampleColorX.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Rendering
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Rendering.SampleColorX"

    def __init__(self, point: str | INodeValueOutput[primitives.Float3] | None = None, direction: str | INodeValueOutput[primitives.Float3] | None = None, reference: str | INodeObjectOutput[Slot] | None = None, near_clip: str | INodeValueOutput[np.float32] | None = None, far_clip: str | INodeValueOutput[np.float32] | None = None, on_sample_start: str | INodeOperation | None = None, on_sampled: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            point: Initial value for Point.
            direction: Initial value for Direction.
            reference: Initial value for Reference.
            near_clip: Initial value for NearClip.
            far_clip: Initial value for FarClip.
            on_sample_start: Initial value for OnSampleStart.
            on_sampled: Initial value for OnSampled.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if point is not None:
            self.point = point
        if direction is not None:
            self.direction = direction
        if reference is not None:
            self.reference = reference
        if near_clip is not None:
            self.near_clip = near_clip
        if far_clip is not None:
            self.far_clip = far_clip
        if on_sample_start is not None:
            self.on_sample_start = on_sample_start
        if on_sampled is not None:
            self.on_sampled = on_sampled

    @property
    def point(self) -> str | None:
        """Target ID of the Point reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Point")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @point.setter
    def point(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Point reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Point")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Point",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def direction(self) -> str | None:
        """Target ID of the Direction reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Direction")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @direction.setter
    def direction(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Direction reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Direction")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Direction",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def reference(self) -> str | None:
        """Target ID of the Reference reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference.setter
    def reference(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the Reference reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Reference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def near_clip(self) -> str | None:
        """Target ID of the NearClip reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("NearClip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @near_clip.setter
    def near_clip(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the NearClip reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("NearClip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NearClip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def far_clip(self) -> str | None:
        """Target ID of the FarClip reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("FarClip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @far_clip.setter
    def far_clip(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the FarClip reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("FarClip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FarClip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def on_sample_start(self) -> str | None:
        """Target ID of the OnSampleStart reference (targets INodeOperation)."""
        member = self.get_member("OnSampleStart")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_sample_start.setter
    def on_sample_start(self, target: str | INodeOperation | None) -> None:
        """Set the OnSampleStart reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnSampleStart")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnSampleStart",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_sampled(self) -> str | None:
        """Target ID of the OnSampled reference (targets INodeOperation)."""
        member = self.get_member("OnSampled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_sampled.setter
    def on_sampled(self, target: str | INodeOperation | None) -> None:
        """Set the OnSampled reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnSampled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnSampled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def sampled_color(self) -> members.EmptyElement | None:
        """The SampledColor member."""
        member = self.get_member("SampledColor")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sampled_color.setter
    def sampled_color(self, value: members.EmptyElement) -> None:
        """Set the SampledColor member."""
        self.set_member("SampledColor", value)

