"""Generated component: ContactItem."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.image import Image
from pyresonitelink.generated._types.static_texture_2d import StaticTexture2D
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ContactItem(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ContactItem.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ContactItem"

    def __init__(self, background: str | Image | None = None, status_indicator: str | Image | None = None, thumbnail: str | Image | None = None, thumbnail_texture: str | StaticTexture2D | None = None, username: str | Text | None = None, status: str | Text | None = None, unread_count: str | Text | None = None, join_button: str | Button | None = None, raw_username: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            background: Initial value for _background.
            status_indicator: Initial value for _statusIndicator.
            thumbnail: Initial value for _thumbnail.
            thumbnail_texture: Initial value for _thumbnailTexture.
            username: Initial value for _username.
            status: Initial value for _status.
            unread_count: Initial value for _unreadCount.
            join_button: Initial value for _joinButton.
            raw_username: Initial value for _rawUsername.
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
        if username is not None:
            self.username = username
        if status is not None:
            self.status = status
        if unread_count is not None:
            self.unread_count = unread_count
        if join_button is not None:
            self.join_button = join_button
        if raw_username is not None:
            self.raw_username = raw_username

    @property
    def background(self) -> str | None:
        """Target ID of the _background reference (targets Image)."""
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
        """Target ID of the _statusIndicator reference (targets Image)."""
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
        """Target ID of the _thumbnail reference (targets Image)."""
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
        """Target ID of the _thumbnailTexture reference (targets StaticTexture2D)."""
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
    def username(self) -> str | None:
        """Target ID of the _username reference (targets Text)."""
        member = self.get_member("_username")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @username.setter
    def username(self, target: str | Text | None) -> None:
        """Set the _username reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_username")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_username",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def status(self) -> str | None:
        """Target ID of the _status reference (targets Text)."""
        member = self.get_member("_status")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @status.setter
    def status(self, target: str | Text | None) -> None:
        """Set the _status reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_status")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_status",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def unread_count(self) -> str | None:
        """Target ID of the _unreadCount reference (targets Text)."""
        member = self.get_member("_unreadCount")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @unread_count.setter
    def unread_count(self, target: str | Text | None) -> None:
        """Set the _unreadCount reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_unreadCount")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_unreadCount",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def join_button(self) -> str | None:
        """Target ID of the _joinButton reference (targets Button)."""
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

    @property
    def raw_username(self) -> str | None:
        """The _rawUsername field value."""
        member = self.get_member("_rawUsername")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @raw_username.setter
    def raw_username(self, value: str) -> None:
        """Set the _rawUsername field value."""
        member = self.get_member("_rawUsername")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_rawUsername", fields.FieldString(value=value)
            )

    @property
    def alternate_names(self) -> members.SyncList | None:
        """The _alternateNames member."""
        member = self.get_member("_alternateNames")
        if isinstance(member, members.SyncList):
            return member
        return None

    @alternate_names.setter
    def alternate_names(self, value: members.SyncList) -> None:
        """Set the _alternateNames member."""
        self.set_member("_alternateNames", value)

