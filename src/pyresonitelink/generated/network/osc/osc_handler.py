"""Generated component: OSC_Handler."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OSC_Handler(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.OSC_Handler.

    Category: Network/OSC
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.OSC_Handler"

    def __init__(self, access_reason: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            access_reason: Initial value for AccessReason.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if access_reason is not None:
            self.access_reason = access_reason

    @property
    def handling_user(self) -> members.SyncObject | None:
        """The HandlingUser member."""
        member = self.get_member("HandlingUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @handling_user.setter
    def handling_user(self, value: members.SyncObject) -> None:
        """Set the HandlingUser member."""
        self.set_member("HandlingUser", value)

    @property
    def access_reason(self) -> str | None:
        """The AccessReason field value."""
        member = self.get_member("AccessReason")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @access_reason.setter
    def access_reason(self, value: str) -> None:
        """Set the AccessReason field value."""
        member = self.get_member("AccessReason")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AccessReason", fields.FieldString(value=value)
            )

