"""Generated component: SetUserScale."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.user_root import UserRoot
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SetUserScale(GeneratedComponent, IAsyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.SetUserScale.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Users
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.SetUserScale"

    def __init__(self, user_root: str | INodeObjectOutput[UserRoot] | None = None, scale: str | INodeValueOutput[np.float32] | None = None, animation_time: str | INodeValueOutput[np.float32] | None = None, on_scale_change_start: str | INodeOperation | None = None, on_animation_finished: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user_root: Initial value for UserRoot.
            scale: Initial value for Scale.
            animation_time: Initial value for AnimationTime.
            on_scale_change_start: Initial value for OnScaleChangeStart.
            on_animation_finished: Initial value for OnAnimationFinished.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user_root is not None:
            self.user_root = user_root
        if scale is not None:
            self.scale = scale
        if animation_time is not None:
            self.animation_time = animation_time
        if on_scale_change_start is not None:
            self.on_scale_change_start = on_scale_change_start
        if on_animation_finished is not None:
            self.on_animation_finished = on_animation_finished

    @property
    def user_root(self) -> str | None:
        """Target ID of the UserRoot reference (targets INodeObjectOutput[UserRoot])."""
        member = self.get_member("UserRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user_root.setter
    def user_root(self, target: str | INodeObjectOutput[UserRoot] | None) -> None:
        """Set the UserRoot reference by target ID or INodeObjectOutput[UserRoot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("UserRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UserRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.UserRoot>'),
            )

    @property
    def scale(self) -> str | None:
        """Target ID of the Scale reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("Scale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale.setter
    def scale(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the Scale reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Scale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Scale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def animation_time(self) -> str | None:
        """Target ID of the AnimationTime reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("AnimationTime")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @animation_time.setter
    def animation_time(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the AnimationTime reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("AnimationTime")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AnimationTime",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def on_scale_change_start(self) -> str | None:
        """Target ID of the OnScaleChangeStart reference (targets INodeOperation)."""
        member = self.get_member("OnScaleChangeStart")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_scale_change_start.setter
    def on_scale_change_start(self, target: str | INodeOperation | None) -> None:
        """Set the OnScaleChangeStart reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnScaleChangeStart")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnScaleChangeStart",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_animation_finished(self) -> str | None:
        """Target ID of the OnAnimationFinished reference (targets INodeOperation)."""
        member = self.get_member("OnAnimationFinished")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_animation_finished.setter
    def on_animation_finished(self, target: str | INodeOperation | None) -> None:
        """Set the OnAnimationFinished reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnAnimationFinished")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnAnimationFinished",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

