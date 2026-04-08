"""Generated component: CharacterColliderWorldLink."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.world_link import WorldLink
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CharacterColliderWorldLink(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CharacterColliderWorldLink.

    Category: World
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CharacterColliderWorldLink"

    def __init__(self, triggers_only: bool | None = None, open_on_contact_start: bool | None = None, open_on_contact_stay: bool | None = None, open_on_contact_end: bool | None = None, world_link: str | WorldLink | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            triggers_only: Initial value for TriggersOnly.
            open_on_contact_start: Initial value for OpenOnContactStart.
            open_on_contact_stay: Initial value for OpenOnContactStay.
            open_on_contact_end: Initial value for OpenOnContactEnd.
            world_link: Initial value for WorldLink.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if triggers_only is not None:
            self.triggers_only = triggers_only
        if open_on_contact_start is not None:
            self.open_on_contact_start = open_on_contact_start
        if open_on_contact_stay is not None:
            self.open_on_contact_stay = open_on_contact_stay
        if open_on_contact_end is not None:
            self.open_on_contact_end = open_on_contact_end
        if world_link is not None:
            self.world_link = world_link

    @property
    def triggers_only(self) -> bool | None:
        """The TriggersOnly field value."""
        member = self.get_member("TriggersOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @triggers_only.setter
    def triggers_only(self, value: bool) -> None:
        """Set the TriggersOnly field value."""
        member = self.get_member("TriggersOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TriggersOnly", fields.FieldBool(value=value)
            )

    @property
    def open_on_contact_start(self) -> bool | None:
        """The OpenOnContactStart field value."""
        member = self.get_member("OpenOnContactStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @open_on_contact_start.setter
    def open_on_contact_start(self, value: bool) -> None:
        """Set the OpenOnContactStart field value."""
        member = self.get_member("OpenOnContactStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OpenOnContactStart", fields.FieldBool(value=value)
            )

    @property
    def open_on_contact_stay(self) -> bool | None:
        """The OpenOnContactStay field value."""
        member = self.get_member("OpenOnContactStay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @open_on_contact_stay.setter
    def open_on_contact_stay(self, value: bool) -> None:
        """Set the OpenOnContactStay field value."""
        member = self.get_member("OpenOnContactStay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OpenOnContactStay", fields.FieldBool(value=value)
            )

    @property
    def open_on_contact_end(self) -> bool | None:
        """The OpenOnContactEnd field value."""
        member = self.get_member("OpenOnContactEnd")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @open_on_contact_end.setter
    def open_on_contact_end(self, value: bool) -> None:
        """Set the OpenOnContactEnd field value."""
        member = self.get_member("OpenOnContactEnd")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OpenOnContactEnd", fields.FieldBool(value=value)
            )

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

