"""Generated component: TouchWorldLink."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.world_link import WorldLink
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TouchWorldLink(GeneratedComponent, ITouchable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TouchWorldLink.

    Category: World
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TouchWorldLink"

    def __init__(self, accept_physical_touch: bool | None = None, accept_remote_touch: bool | None = None, accept_out_of_sight_touch: bool | None = None, world_link: str | WorldLink | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            accept_out_of_sight_touch: Initial value for AcceptOutOfSightTouch.
            world_link: Initial value for WorldLink.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch
        if accept_out_of_sight_touch is not None:
            self.accept_out_of_sight_touch = accept_out_of_sight_touch
        if world_link is not None:
            self.world_link = world_link

    @property
    def accept_physical_touch(self) -> bool | None:
        """The AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_physical_touch.setter
    def accept_physical_touch(self, value: bool) -> None:
        """Set the AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptPhysicalTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_remote_touch(self) -> bool | None:
        """The AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_remote_touch.setter
    def accept_remote_touch(self, value: bool) -> None:
        """Set the AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptRemoteTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_out_of_sight_touch(self) -> bool | None:
        """The AcceptOutOfSightTouch field value."""
        member = self.get_member("AcceptOutOfSightTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_out_of_sight_touch.setter
    def accept_out_of_sight_touch(self, value: bool) -> None:
        """Set the AcceptOutOfSightTouch field value."""
        member = self.get_member("AcceptOutOfSightTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptOutOfSightTouch", fields.FieldBool(value=value)
            )

    @property
    def vibrate(self) -> members.FieldEnum | None:
        """The Vibrate member."""
        member = self.get_member("Vibrate")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @vibrate.setter
    def vibrate(self, value: members.FieldEnum) -> None:
        """Set the Vibrate member."""
        self.set_member("Vibrate", value)

    @property
    def world_link(self) -> str | None:
        """Target ID of the WorldLink reference (targets WorldLink)."""
        member = self.get_member("WorldLink")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @world_link.setter
    def world_link(self, target: str | WorldLink | None) -> None:
        """Set the WorldLink reference by target ID or WorldLink instance."""
        target_id: str | None = target.id if isinstance(target, WorldLink) else target  # type: ignore[assignment]
        member = self.get_member("WorldLink")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "WorldLink",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldLink'),
            )

