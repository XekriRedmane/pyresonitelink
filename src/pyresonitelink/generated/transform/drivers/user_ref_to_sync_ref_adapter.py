"""Generated component: UserRefToSyncRefAdapter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserRefToSyncRefAdapter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The UserRefToSyncRefAdapter component takes a UserRef type and drives a user ref field with what it has inside of it.

    Category: Transform/Drivers

    Attach to a slot and provide values for all fields in order for this
    component to work.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserRefToSyncRefAdapter"

    def __init__(self, target_reference: str | SyncRef[User] | None = None, write_back: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_reference: Initial value for TargetReference.
            write_back: Initial value for WriteBack.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_reference is not None:
            self.target_reference = target_reference
        if write_back is not None:
            self.write_back = write_back

    @property
    def user(self) -> members.SyncObject | None:
        """The ref to get a user from."""
        member = self.get_member("User")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @user.setter
    def user(self, value: members.SyncObject) -> None:
        """Set User. The ref to get a user from."""
        self.set_member("User", value)

    @property
    def target_reference(self) -> str | None:
        """The field to drive with what user ``User`` refers to."""
        member = self.get_member("TargetReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_reference.setter
    def target_reference(self, target: str | SyncRef[User] | None) -> None:
        """Set the TargetReference reference by target ID or SyncRef[User] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("TargetReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<[FrooxEngine]FrooxEngine.User>'),
            )

    @property
    def write_back(self) -> primitives.Bool | None:
        """Whether changes to the field ``TargetReference`` will update the value of ``User``. See write backs."""
        member = self.get_member("WriteBack")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @write_back.setter
    def write_back(self, value: primitives.Bool) -> None:
        """Set the WriteBack field value."""
        member = self.get_member("WriteBack")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WriteBack", fields.FieldBool(value=value)
            )

