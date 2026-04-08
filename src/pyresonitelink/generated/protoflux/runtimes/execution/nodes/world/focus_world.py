"""Generated component: FocusWorld."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iworld_link import IWorldLink
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FocusWorld(GeneratedComponent, IAsyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Worlds.FocusWorld.

    Category: ProtoFlux/Runtimes/Execution/Nodes/World
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Worlds.FocusWorld"

    def __init__(self, url: str | INodeObjectOutput[str] | None = None, world_link: str | INodeObjectOutput[IWorldLink] | None = None, close_current: str | INodeValueOutput[primitives.Bool] | None = None, on_not_found: str | INodeOperation | None = None, on_focused: str | INodeOperation | None = None, on_fail: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            world_link: Initial value for WorldLink.
            close_current: Initial value for CloseCurrent.
            on_not_found: Initial value for OnNotFound.
            on_focused: Initial value for OnFocused.
            on_fail: Initial value for OnFail.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if url is not None:
            self.url = url
        if world_link is not None:
            self.world_link = world_link
        if close_current is not None:
            self.close_current = close_current
        if on_not_found is not None:
            self.on_not_found = on_not_found
        if on_focused is not None:
            self.on_focused = on_focused
        if on_fail is not None:
            self.on_fail = on_fail

    @property
    def url(self) -> str | None:
        """Target ID of the URL reference (targets INodeObjectOutput[str])."""
        member = self.get_member("URL")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @url.setter
    def url(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the URL reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("URL")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "URL",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<Uri>'),
            )

    @property
    def world_link(self) -> str | None:
        """Target ID of the WorldLink reference (targets INodeObjectOutput[IWorldLink])."""
        member = self.get_member("WorldLink")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @world_link.setter
    def world_link(self, target: str | INodeObjectOutput[IWorldLink] | None) -> None:
        """Set the WorldLink reference by target ID or INodeObjectOutput[IWorldLink] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("WorldLink")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "WorldLink",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.IWorldLink>'),
            )

    @property
    def close_current(self) -> str | None:
        """Target ID of the CloseCurrent reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("CloseCurrent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @close_current.setter
    def close_current(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the CloseCurrent reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("CloseCurrent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CloseCurrent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def on_not_found(self) -> str | None:
        """Target ID of the OnNotFound reference (targets INodeOperation)."""
        member = self.get_member("OnNotFound")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_not_found.setter
    def on_not_found(self, target: str | INodeOperation | None) -> None:
        """Set the OnNotFound reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnNotFound")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnNotFound",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_focused(self) -> str | None:
        """Target ID of the OnFocused reference (targets INodeOperation)."""
        member = self.get_member("OnFocused")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_focused.setter
    def on_focused(self, target: str | INodeOperation | None) -> None:
        """Set the OnFocused reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnFocused")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnFocused",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_fail(self) -> str | None:
        """Target ID of the OnFail reference (targets INodeOperation)."""
        member = self.get_member("OnFail")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_fail.setter
    def on_fail(self, target: str | INodeOperation | None) -> None:
        """Set the OnFail reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnFail")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnFail",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

