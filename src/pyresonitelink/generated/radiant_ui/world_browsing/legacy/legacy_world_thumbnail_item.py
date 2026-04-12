"""Generated component: LegacyWorldThumbnailItem."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.raw_graphic import RawGraphic
from pyresonitelink.generated._types.static_texture_2d import StaticTexture2D
from pyresonitelink.generated._types.rect_transform import RectTransform
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.image import Image
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.ibutton_hover_receiver import IButtonHoverReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyWorldThumbnailItem(GeneratedComponent, IButtonPressReceiver, IButtonHoverReceiver, IWorldEventReceiver):
    """The LegacyWorldThumbnailItem component is used to show worlds in the list of the legacy world facet.

    Category: Radiant UI/World Browsing/Legacy

    Don't use.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyWorldThumbnailItem"

    def __init__(self, world_or_session_id: primitives.String | None = None, visited: primitives.Bool | None = None, total_active_users: primitives.Int | None = None, total_contacts: primitives.Int | None = None, thumbnail_graphic: str | RawGraphic | None = None, thumbnail_texture: str | StaticTexture2D | None = None, name_root: str | RectTransform | None = None, detail_root: str | RectTransform | None = None, visited_root: str | RectTransform | None = None, counter_root: str | RectTransform | None = None, icons_root: str | RectTransform | None = None, close_button: str | RectTransform | None = None, name_text: str | Text | None = None, detail_text: str | Text | None = None, counter_text: str | Text | None = None, border_overlay: str | Image | None = None, border_color: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            world_or_session_id: Initial value for WorldOrSessionId.
            visited: Initial value for _visited.
            total_active_users: Initial value for _totalActiveUsers.
            total_contacts: Initial value for _totalContacts.
            thumbnail_graphic: Initial value for _thumbnailGraphic.
            thumbnail_texture: Initial value for _thumbnailTexture.
            name_root: Initial value for _nameRoot.
            detail_root: Initial value for _detailRoot.
            visited_root: Initial value for _visitedRoot.
            counter_root: Initial value for _counterRoot.
            icons_root: Initial value for _iconsRoot.
            close_button: Initial value for _closeButton.
            name_text: Initial value for _nameText.
            detail_text: Initial value for _detailText.
            counter_text: Initial value for _counterText.
            border_overlay: Initial value for _borderOverlay.
            border_color: Initial value for _borderColor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if world_or_session_id is not None:
            self.world_or_session_id = world_or_session_id
        if visited is not None:
            self.visited = visited
        if total_active_users is not None:
            self.total_active_users = total_active_users
        if total_contacts is not None:
            self.total_contacts = total_contacts
        if thumbnail_graphic is not None:
            self.thumbnail_graphic = thumbnail_graphic
        if thumbnail_texture is not None:
            self.thumbnail_texture = thumbnail_texture
        if name_root is not None:
            self.name_root = name_root
        if detail_root is not None:
            self.detail_root = detail_root
        if visited_root is not None:
            self.visited_root = visited_root
        if counter_root is not None:
            self.counter_root = counter_root
        if icons_root is not None:
            self.icons_root = icons_root
        if close_button is not None:
            self.close_button = close_button
        if name_text is not None:
            self.name_text = name_text
        if detail_text is not None:
            self.detail_text = detail_text
        if counter_text is not None:
            self.counter_text = counter_text
        if border_overlay is not None:
            self.border_overlay = border_overlay
        if border_color is not None:
            self.border_color = border_color

    @property
    def updating_user(self) -> members.SyncObject | None:
        """The user managing updating this component's functionality."""
        member = self.get_member("UpdatingUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @updating_user.setter
    def updating_user(self, value: members.SyncObject) -> None:
        """Set UpdatingUser. The user managing updating this component's functionality."""
        self.set_member("UpdatingUser", value)

    @property
    def world_or_session_id(self) -> primitives.String | None:
        """The world or session ID this component is providing information on."""
        member = self.get_member("WorldOrSessionId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @world_or_session_id.setter
    def world_or_session_id(self, value: primitives.String) -> None:
        """Set the WorldOrSessionId field value."""
        member = self.get_member("WorldOrSessionId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WorldOrSessionId", fields.FieldString(value=value)
            )

    @property
    def visited(self) -> primitives.Bool | None:
        """Whether the World has been visited by ``UpdatingUser``."""
        member = self.get_member("_visited")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @visited.setter
    def visited(self, value: primitives.Bool) -> None:
        """Set the _visited field value."""
        member = self.get_member("_visited")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_visited", fields.FieldBool(value=value)
            )

    @property
    def total_active_users(self) -> primitives.Int | None:
        """The total focused and active users in the world."""
        member = self.get_member("_totalActiveUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_active_users.setter
    def total_active_users(self, value: primitives.Int) -> None:
        """Set the _totalActiveUsers field value."""
        member = self.get_member("_totalActiveUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_totalActiveUsers", fields.FieldInt(value=value)
            )

    @property
    def total_contacts(self) -> primitives.Int | None:
        """The total amount of users on the world that are contacts of ``UpdatingUser``."""
        member = self.get_member("_totalContacts")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_contacts.setter
    def total_contacts(self, value: primitives.Int) -> None:
        """Set the _totalContacts field value."""
        member = self.get_member("_totalContacts")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_totalContacts", fields.FieldInt(value=value)
            )

    @property
    def thumbnail_graphic(self) -> str | None:
        """The component handling the Thumbnail graphic."""
        member = self.get_member("_thumbnailGraphic")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @thumbnail_graphic.setter
    def thumbnail_graphic(self, target: str | RawGraphic | None) -> None:
        """Set the _thumbnailGraphic reference by target ID or RawGraphic instance."""
        target_id: str | None = target.id if isinstance(target, RawGraphic) else target  # type: ignore[assignment]
        member = self.get_member("_thumbnailGraphic")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_thumbnailGraphic",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RawGraphic'),
            )

    @property
    def thumbnail_texture(self) -> str | None:
        """The component handling the Thumbnail texture."""
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
    def name_root(self) -> str | None:
        """The component that is the graphic rectangle handler for the world name."""
        member = self.get_member("_nameRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @name_root.setter
    def name_root(self, target: str | RectTransform | None) -> None:
        """Set the _nameRoot reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("_nameRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_nameRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def detail_root(self) -> str | None:
        """The component that is the graphic rectangle handler for the world details."""
        member = self.get_member("_detailRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @detail_root.setter
    def detail_root(self, target: str | RectTransform | None) -> None:
        """Set the _detailRoot reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("_detailRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_detailRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def visited_root(self) -> str | None:
        """The component that is the graphic rectangle handler for the world visited status."""
        member = self.get_member("_visitedRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visited_root.setter
    def visited_root(self, target: str | RectTransform | None) -> None:
        """Set the _visitedRoot reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("_visitedRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visitedRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def counter_root(self) -> str | None:
        """The component that is the graphic rectangle handler for the world active users and contacts amount."""
        member = self.get_member("_counterRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @counter_root.setter
    def counter_root(self, target: str | RectTransform | None) -> None:
        """Set the _counterRoot reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("_counterRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_counterRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def icons_root(self) -> str | None:
        """The component that is the graphic rectangle handler for the world icons."""
        member = self.get_member("_iconsRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @icons_root.setter
    def icons_root(self, target: str | RectTransform | None) -> None:
        """Set the _iconsRoot reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("_iconsRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_iconsRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def close_button(self) -> str | None:
        """The component that is the graphic rectangle handler for the world close button."""
        member = self.get_member("_closeButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @close_button.setter
    def close_button(self, target: str | RectTransform | None) -> None:
        """Set the _closeButton reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("_closeButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_closeButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def name_text(self) -> str | None:
        """The text showing the world name."""
        member = self.get_member("_nameText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @name_text.setter
    def name_text(self, target: str | Text | None) -> None:
        """Set the _nameText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_nameText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_nameText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def detail_text(self) -> str | None:
        """The text showing the world details."""
        member = self.get_member("_detailText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @detail_text.setter
    def detail_text(self, target: str | Text | None) -> None:
        """Set the _detailText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_detailText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_detailText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def counter_text(self) -> str | None:
        """The text showing the world active user/contacts."""
        member = self.get_member("_counterText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @counter_text.setter
    def counter_text(self, target: str | Text | None) -> None:
        """Set the _counterText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_counterText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_counterText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def border_overlay(self) -> str | None:
        """The image UIX component handling the border graphic"""
        member = self.get_member("_borderOverlay")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @border_overlay.setter
    def border_overlay(self, target: str | Image | None) -> None:
        """Set the _borderOverlay reference by target ID or Image instance."""
        target_id: str | None = target.id if isinstance(target, Image) else target  # type: ignore[assignment]
        member = self.get_member("_borderOverlay")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_borderOverlay",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Image'),
            )

    @property
    def border_color(self) -> primitives.ColorX | None:
        """The color the border should be."""
        member = self.get_member("_borderColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @border_color.setter
    def border_color(self, value: primitives.ColorX) -> None:
        """Set the _borderColor field value."""
        member = self.get_member("_borderColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_borderColor", fields.FieldColorX(value=value)
            )

