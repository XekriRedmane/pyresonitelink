"""Generated component: TestFakeViveTracker."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TestFakeViveTracker(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TestFakeViveTracker.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TestFakeViveTracker"

    def __init__(self, id_: str | None = None, is_tracking: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            id_: Initial value for Id.
            is_tracking: Initial value for IsTracking.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if id_ is not None:
            self.id_ = id_
        if is_tracking is not None:
            self.is_tracking = is_tracking

    @property
    def id_(self) -> str | None:
        """The Id field value."""
        member = self.get_member("Id")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @id_.setter
    def id_(self, value: str) -> None:
        """Set the Id field value."""
        member = self.get_member("Id")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Id", fields.FieldString(value=value)
            )

    @property
    def is_tracking(self) -> bool | None:
        """The IsTracking field value."""
        member = self.get_member("IsTracking")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_tracking.setter
    def is_tracking(self, value: bool) -> None:
        """Set the IsTracking field value."""
        member = self.get_member("IsTracking")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsTracking", fields.FieldBool(value=value)
            )

    @property
    def user(self) -> members.SyncObject | None:
        """The User member."""
        member = self.get_member("User")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @user.setter
    def user(self, value: members.SyncObject) -> None:
        """Set the User member."""
        self.set_member("User", value)

