"""Generated component: Update."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_update_receiver import IExecutionUpdateReceiver
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Update(GeneratedComponent, IExecutionUpdateReceiver, IMappableNode, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Update node sends a pulse at every engine update from the UpdatingUser.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.Update"

    def __init__(self, updating_user: str | IGlobalValueProxy[User] | None = None, skip_if_null: str | IGlobalValueProxy[primitives.Bool] | None = None, on_update: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            updating_user: Initial value for UpdatingUser.
            skip_if_null: Initial value for SkipIfNull.
            on_update: Initial value for OnUpdate.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if updating_user is not None:
            self.updating_user = updating_user
        if skip_if_null is not None:
            self.skip_if_null = skip_if_null
        if on_update is not None:
            self.on_update = on_update

    @property
    def updating_user(self) -> str | None:
        """Target ID of the UpdatingUser reference (targets IGlobalValueProxy[User])."""
        member = self.get_member("UpdatingUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @updating_user.setter
    def updating_user(self, target: str | IGlobalValueProxy[User] | None) -> None:
        """Set the UpdatingUser reference by target ID or IGlobalValueProxy[User] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("UpdatingUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UpdatingUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.User>'),
            )

    @property
    def skip_if_null(self) -> str | None:
        """Target ID of the SkipIfNull reference (targets IGlobalValueProxy[primitives.Bool])."""
        member = self.get_member("SkipIfNull")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @skip_if_null.setter
    def skip_if_null(self, target: str | IGlobalValueProxy[primitives.Bool] | None) -> None:
        """Set the SkipIfNull reference by target ID or IGlobalValueProxy[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("SkipIfNull")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SkipIfNull",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<bool>'),
            )

    @property
    def on_update(self) -> str | None:
        """Target ID of the OnUpdate reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnUpdate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_update.setter
    def on_update(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnUpdate reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnUpdate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnUpdate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

