"""Generated component: SessionItem."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.image import Image
from pyresonitelink.generated._types.static_texture_2d import StaticTexture2D
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SessionItem(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The SessionItem component is used to handle the session items in a world menu.

    not to be used directly by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SessionItem"

    def __init__(self, background: str | Image | None = None, status_indicator: str | Image | None = None, thumbnail: str | Image | None = None, thumbnail_texture: str | StaticTexture2D | None = None, session_name: str | Text | None = None, session_host: str | Text | None = None, user_count: str | Text | None = None, join_button: str | Button | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            background: Initial value for _background.
            status_indicator: Initial value for _statusIndicator.
            thumbnail: Initial value for _thumbnail.
            thumbnail_texture: Initial value for _thumbnailTexture.
            session_name: Initial value for _sessionName.
            session_host: Initial value for _sessionHost.
            user_count: Initial value for _userCount.
            join_button: Initial value for _joinButton.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if background is not None:
            self.background = background
        if status_indicator is not None:
            self.status_indicator = status_indicator
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if thumbnail_texture is not None:
            self.thumbnail_texture = thumbnail_texture
        if session_name is not None:
            self.session_name = session_name
        if session_host is not None:
            self.session_host = session_host
        if user_count is not None:
            self.user_count = user_count
        if join_button is not None:
            self.join_button = join_button

    @property
    def background(self) -> str | None:
        """The UIX image handling the background for this session item."""
        member = self.get_member("_background")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @background.setter
    def background(self, target: str | Image | None) -> None:
        """Set the _background reference by target ID or Image instance."""
        target_id: str | None = target.id if isinstance(target, Image) else target  # type: ignore[assignment]
        member = self.get_member("_background")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_background",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Image'),
            )

    @property
    def status_indicator(self) -> str | None:
        """The UIX image used to handle showing the status for this world like access level."""
        member = self.get_member("_statusIndicator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @status_indicator.setter
    def status_indicator(self, target: str | Image | None) -> None:
        """Set the _statusIndicator reference by target ID or Image instance."""
        target_id: str | None = target.id if isinstance(target, Image) else target  # type: ignore[assignment]
        member = self.get_member("_statusIndicator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_statusIndicator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Image'),
            )

    @property
    def thumbnail(self) -> str | None:
        """The UIX image handling the session preview thumbnail."""
        member = self.get_member("_thumbnail")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @thumbnail.setter
    def thumbnail(self, target: str | Image | None) -> None:
        """Set the _thumbnail reference by target ID or Image instance."""
        target_id: str | None = target.id if isinstance(target, Image) else target  # type: ignore[assignment]
        member = self.get_member("_thumbnail")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_thumbnail",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Image'),
            )

    @property
    def thumbnail_texture(self) -> str | None:
        """The image handling the session preview thumbnail image data."""
        member = self.get_member("_thumbnailTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @thumbnail_texture.setter
    def thumbnail_texture(self, target: str | StaticTexture2D | None) -> None:
        """Set the _thumbnailTexture reference by target ID or StaticTexture2D instance."""
        target_id: str | None = target.id if isinstance(target, StaticTexture2D) else target  # type: ignore[assignment]
        member = self.get_member("_thumbnailTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_thumbnailTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.StaticTexture2D'),
            )

    @property
    def session_name(self) -> str | None:
        """The text visual being used to show the session name."""
        member = self.get_member("_sessionName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @session_name.setter
    def session_name(self, target: str | Text | None) -> None:
        """Set the _sessionName reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_sessionName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sessionName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def session_host(self) -> str | None:
        """The text visual being used to show the session host's name."""
        member = self.get_member("_sessionHost")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @session_host.setter
    def session_host(self, target: str | Text | None) -> None:
        """Set the _sessionHost reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_sessionHost")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sessionHost",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def user_count(self) -> str | None:
        """The text visual being used to show the session user count."""
        member = self.get_member("_userCount")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user_count.setter
    def user_count(self, target: str | Text | None) -> None:
        """Set the _userCount reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_userCount")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_userCount",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def join_button(self) -> str | None:
        """The button that can be used to join the specified session."""
        member = self.get_member("_joinButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @join_button.setter
    def join_button(self, target: str | Button | None) -> None:
        """Set the _joinButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_joinButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_joinButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    async def on_join(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, debug: bool = False) -> dict:
        """Called when the join button is touched.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "OnJoin", {"button": button, "eventData": event_data}, debug,
        )

