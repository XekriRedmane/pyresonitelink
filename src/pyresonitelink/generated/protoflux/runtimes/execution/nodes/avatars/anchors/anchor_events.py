"""Generated component: AnchorEvents."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.avatar_anchor import AvatarAnchor
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AnchorEvents(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.Anchors.AnchorEvents.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Avatars/Anchors
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.Anchors.AnchorEvents"

    def __init__(self, anchor: str | IGlobalValueProxy[AvatarAnchor] | None = None, on_anchored: str | ISyncNodeOperation | None = None, on_released: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            anchor: Initial value for Anchor.
            on_anchored: Initial value for OnAnchored.
            on_released: Initial value for OnReleased.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if anchor is not None:
            self.anchor = anchor
        if on_anchored is not None:
            self.on_anchored = on_anchored
        if on_released is not None:
            self.on_released = on_released

    @property
    def anchor(self) -> str | None:
        """Target ID of the Anchor reference (targets IGlobalValueProxy[AvatarAnchor])."""
        member = self.get_member("Anchor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @anchor.setter
    def anchor(self, target: str | IGlobalValueProxy[AvatarAnchor] | None) -> None:
        """Set the Anchor reference by target ID or IGlobalValueProxy[AvatarAnchor] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Anchor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Anchor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.CommonAvatar.AvatarAnchor>'),
            )

    @property
    def on_anchored(self) -> str | None:
        """Target ID of the OnAnchored reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnAnchored")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_anchored.setter
    def on_anchored(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnAnchored reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnAnchored")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnAnchored",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def on_released(self) -> str | None:
        """Target ID of the OnReleased reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnReleased")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_released.setter
    def on_released(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnReleased reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnReleased")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnReleased",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def user(self) -> members.EmptyElement | None:
        """The User member."""
        member = self.get_member("User")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @user.setter
    def user(self, value: members.EmptyElement) -> None:
        """Set the User member."""
        self.set_member("User", value)

