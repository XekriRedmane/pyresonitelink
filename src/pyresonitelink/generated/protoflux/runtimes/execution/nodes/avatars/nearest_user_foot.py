"""Generated component: NearestUserFoot."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NearestUserFoot(GeneratedComponent, IMappableNode, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Nearest User Foot is a protoflux node that returns the closest user foot to a slot and the foot's user, or closest to the root if not provided a slot. This will also ignore the user provided to IgnoreUser (User).

    Category: ProtoFlux/Runtimes/Execution/Nodes/Avatars
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.NearestUserFoot"

    def __init__(self, reference: str | INodeObjectOutput[Slot] | None = None, ignore_user: str | INodeObjectOutput[User] | None = None, ignore_afk: str | INodeValueOutput[primitives.Bool] | None = None, get_left: str | INodeValueOutput[primitives.Bool] | None = None, get_right: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            reference: Initial value for Reference.
            ignore_user: Initial value for IgnoreUser.
            ignore_afk: Initial value for IgnoreAFK.
            get_left: Initial value for GetLeft.
            get_right: Initial value for GetRight.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if reference is not None:
            self.reference = reference
        if ignore_user is not None:
            self.ignore_user = ignore_user
        if ignore_afk is not None:
            self.ignore_afk = ignore_afk
        if get_left is not None:
            self.get_left = get_left
        if get_right is not None:
            self.get_right = get_right

    @property
    def reference(self) -> str | None:
        """The slot which to use as a point to find the closest foot to."""
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
    def ignore_user(self) -> str | None:
        """The user to ignore when looking for the nearest foot."""
        member = self.get_member("IgnoreUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ignore_user.setter
    def ignore_user(self, target: str | INodeObjectOutput[User] | None) -> None:
        """Set the IgnoreUser reference by target ID or INodeObjectOutput[User] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("IgnoreUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IgnoreUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.User>'),
            )

    @property
    def ignore_afk(self) -> str | None:
        """Will not return a foot position from a user that is not currently focused into the world."""
        member = self.get_member("IgnoreAFK")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ignore_afk.setter
    def ignore_afk(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the IgnoreAFK reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("IgnoreAFK")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IgnoreAFK",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def slot(self) -> members.EmptyElement | None:
        """The slot of the foot when found."""
        member = self.get_member("Slot")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @slot.setter
    def slot(self, value: members.EmptyElement) -> None:
        """Set Slot. The slot of the foot when found."""
        self.set_member("Slot", value)

    @property
    def user(self) -> members.EmptyElement | None:
        """The user of the foot that was found."""
        member = self.get_member("User")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @user.setter
    def user(self, value: members.EmptyElement) -> None:
        """Set User. The user of the foot that was found."""
        self.set_member("User", value)

    @property
    def distance(self) -> members.EmptyElement | None:
        """How far away the found foot was."""
        member = self.get_member("Distance")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @distance.setter
    def distance(self, value: members.EmptyElement) -> None:
        """Set Distance. How far away the found foot was."""
        self.set_member("Distance", value)

    @property
    def get_left(self) -> str | None:
        """Whether to get the left foot if closest, true by default."""
        member = self.get_member("GetLeft")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @get_left.setter
    def get_left(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the GetLeft reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("GetLeft")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "GetLeft",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def get_right(self) -> str | None:
        """Whether to get the right foot if closest, true by default."""
        member = self.get_member("GetRight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @get_right.setter
    def get_right(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the GetRight reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("GetRight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "GetRight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def chirality(self) -> members.EmptyElement | None:
        """The side of the foot that was found. Left or Right or -1."""
        member = self.get_member("Chirality")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @chirality.setter
    def chirality(self, value: members.EmptyElement) -> None:
        """Set Chirality. The side of the foot that was found. Left or Right or -1."""
        self.set_member("Chirality", value)

