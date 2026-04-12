"""Generated component: TestFakeViveTracker."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TestFakeViveTracker(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The TestFakeViveTracker component simulates a vive Tracker for ``User`` that has the position and rotation of the slot this component is on. This allows for making fake trackers that can be used to control the ``User``'s IK as a real Tracker would. It even """tricks""" the input system into fully seeing this as a Tracker, even generating a visual for the user. The tracker device's position/rotation is based on its position/rotation in global space compared to ``User``'s root slot global position/rotation.

    Category: Debug

    Attach to a slot and preferably parent it under the ``User`` to create a
    new tracker for the targeted ``User``. a user is needed for this
    component to work.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TestFakeViveTracker"

    def __init__(self, id_: primitives.String | None = None, is_tracking: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
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
    def id_(self) -> primitives.String | None:
        """Upon attaching is a random GUID. Can be changed which makes a new Tracker object. If identical to another older tracker the user has used before, will take on the old tracker's identity and settings."""
        member = self.get_member("Id")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @id_.setter
    def id_(self, value: primitives.String) -> None:
        """Set the Id field value."""
        member = self.get_member("Id")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Id", fields.FieldString(value=value)
            )

    @property
    def is_tracking(self) -> primitives.Bool | None:
        """Controls whether the tracker has lost tracking."""
        member = self.get_member("IsTracking")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_tracking.setter
    def is_tracking(self, value: primitives.Bool) -> None:
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
        """The user this tracker shoul"""
        member = self.get_member("User")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @user.setter
    def user(self, value: members.SyncObject) -> None:
        """Set User. The user this tracker shoul"""
        self.set_member("User", value)

