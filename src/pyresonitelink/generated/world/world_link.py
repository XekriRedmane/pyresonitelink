"""Generated component: WorldLink."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.world_relation import WorldRelation
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_link import IWorldLink
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldLink(GeneratedComponent, IWorldLink, IWorldEventReceiver):
    """The WorldLink component is used to set the world information, either to use as a way to jump to different worlds or to pre-load worlds.

}}

    Category: World

    * This can be combined with the ButtonWorldLink component to setup a
    button for loading a world for a user. * This can be hooked up into
    ProtoFlux with the Open World or Focus World nodes to open or jump to
    another world.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldLink"

    def __init__(self, url: str | None = None, world_relation: WorldRelation | str | None = None, auto_focus: primitives.Bool | None = None, get_existing: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            world_relation: Initial value for WorldRelation.
            auto_focus: Initial value for AutoFocus.
            get_existing: Initial value for GetExisting.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if url is not None:
            self.url = url
        if world_relation is not None:
            self.world_relation = world_relation
        if auto_focus is not None:
            self.auto_focus = auto_focus
        if get_existing is not None:
            self.get_existing = get_existing

    @property
    def url(self) -> str | None:
        """The world to link."""
        member = self.get_member("URL")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @url.setter
    def url(self, value: str) -> None:
        """Set the URL field value."""
        member = self.get_member("URL")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "URL", fields.FieldUri(value=value)
            )

    @property
    def active_session_urls(self) -> members.SyncList | None:
        """Used for session orbs."""
        member = self.get_member("ActiveSessionURLs")
        if isinstance(member, members.SyncList):
            return member
        return None

    @active_session_urls.setter
    def active_session_urls(self, value: members.SyncList) -> None:
        """Set ActiveSessionURLs. Used for session orbs."""
        self.set_member("ActiveSessionURLs", value)

    @property
    def world_relation(self) -> WorldRelation | None:
        """The relation of the world."""
        member = self.get_member("WorldRelation")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return WorldRelation(member.value)
        return None

    @world_relation.setter
    def world_relation(self, value: WorldRelation | str) -> None:
        """Set WorldRelation. The relation of the world."""
        member = self.get_member("WorldRelation")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "WorldRelation",
                members.FieldEnum(value=str(value)),
            )

    @property
    def auto_focus(self) -> primitives.Bool | None:
        """After the world loads, focus to this world automatically."""
        member = self.get_member("AutoFocus")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_focus.setter
    def auto_focus(self, value: primitives.Bool) -> None:
        """Set the AutoFocus field value."""
        member = self.get_member("AutoFocus")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoFocus", fields.FieldBool(value=value)
            )

    @property
    def get_existing(self) -> primitives.Bool | None:
        """If a world we are looking for already exists, then don't make a new one and then optionally focus onto it."""
        member = self.get_member("GetExisting")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @get_existing.setter
    def get_existing(self, value: primitives.Bool) -> None:
        """Set the GetExisting field value."""
        member = self.get_member("GetExisting")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GetExisting", fields.FieldBool(value=value)
            )

