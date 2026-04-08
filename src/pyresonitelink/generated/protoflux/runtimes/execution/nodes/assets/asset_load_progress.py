"""Generated component: AssetLoadProgress."""

from typing import Any

A = Any
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.users_asset_load_progress import UsersAssetLoadProgress
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AssetLoadProgress(GenericComponent[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Asset Load Progress is a node that allows for the reading on weither or not a user has loaded an asset. This node takes a UsersAssetLoadProgress`1 component and allows for the extraction of the load progress of a certain User.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Assets

    Parameterize with a value type::

        AssetLoadProgress[primitives.Float]
        AssetLoadProgress[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.AssetLoadProgress<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.AssetLoadProgress<>"

    def __init__(self, tracker: str | INodeObjectOutput[UsersAssetLoadProgress[A]] | None = None, user: str | INodeObjectOutput[User] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tracker: Initial value for Tracker.
            user: Initial value for User.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if tracker is not None:
            self.tracker = tracker
        if user is not None:
            self.user = user

    @property
    def tracker(self) -> str | None:
        """Target ID of the Tracker reference (targets INodeObjectOutput[UsersAssetLoadProgress[A]])."""
        member = self.get_member("Tracker")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tracker.setter
    def tracker(self, target: str | INodeObjectOutput[UsersAssetLoadProgress[A]] | None) -> None:
        """Set the Tracker reference by target ID or INodeObjectOutput[UsersAssetLoadProgress[A]] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Tracker")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Tracker",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.UsersAssetLoadProgress<A>>'),
            )

    @property
    def user(self) -> str | None:
        """Target ID of the User reference (targets INodeObjectOutput[User])."""
        member = self.get_member("User")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user.setter
    def user(self, target: str | INodeObjectOutput[User] | None) -> None:
        """Set the User reference by target ID or INodeObjectOutput[User] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("User")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "User",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.User>'),
            )

    @property
    def download_progress(self) -> members.EmptyElement | None:
        """The DownloadProgress member."""
        member = self.get_member("DownloadProgress")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @download_progress.setter
    def download_progress(self, value: members.EmptyElement) -> None:
        """Set the DownloadProgress member."""
        self.set_member("DownloadProgress", value)

    @property
    def load_state(self) -> members.EmptyElement | None:
        """The LoadState member."""
        member = self.get_member("LoadState")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @load_state.setter
    def load_state(self, value: members.EmptyElement) -> None:
        """Set the LoadState member."""
        self.set_member("LoadState", value)

