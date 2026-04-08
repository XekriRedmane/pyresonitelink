"""Generated component: FundingStatistics."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FundingStatistics(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FundingStatistics.

    Category: Cloud/Indicators
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FundingStatistics"

    def __init__(self, timestamp: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            timestamp: Initial value for Timestamp.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def timestamp(self) -> str | None:
        """The Timestamp field value."""
        member = self.get_member("Timestamp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @timestamp.setter
    def timestamp(self, value: str) -> None:
        """Set the Timestamp field value."""
        member = self.get_member("Timestamp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Timestamp", fields.FieldDateTime(value=value)
            )

    @property
    def aggregate(self) -> members.SyncObject | None:
        """The Aggregate member."""
        member = self.get_member("Aggregate")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @aggregate.setter
    def aggregate(self, value: members.SyncObject) -> None:
        """Set the Aggregate member."""
        self.set_member("Aggregate", value)

    @property
    def patreon(self) -> members.SyncObject | None:
        """The Patreon member."""
        member = self.get_member("Patreon")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @patreon.setter
    def patreon(self, value: members.SyncObject) -> None:
        """Set the Patreon member."""
        self.set_member("Patreon", value)

    @property
    def stripe(self) -> members.SyncObject | None:
        """The Stripe member."""
        member = self.get_member("Stripe")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @stripe.setter
    def stripe(self, value: members.SyncObject) -> None:
        """Set the Stripe member."""
        self.set_member("Stripe", value)

