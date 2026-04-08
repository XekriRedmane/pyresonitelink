"""Generated component: LegacyWorldDetail."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.raw_graphic import RawGraphic
from pyresonitelink.generated._types.static_texture_2d import StaticTexture2D
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.scroll_rect import ScrollRect
from pyresonitelink.generated._types.image import Image
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.sprite import Sprite
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyWorldDetail(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacyWorldDetail.

    Category: Radiant UI/World Browsing/Legacy
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyWorldDetail"

    def __init__(self, world_or_session_id: primitives.String | None = None, visited: primitives.Bool | None = None, total_active_users: primitives.Int | None = None, total_contacts: primitives.Int | None = None, expanded: primitives.Bool | None = None, compact_detail_expanded: primitives.Bool | None = None, modal_compact_size: primitives.Float2 | None = None, modal_expanded_size: primitives.Float2 | None = None, host_text: str | Text | None = None, session_items_root: str | Slot | None = None, thumbnail_graphic: str | RawGraphic | None = None, thumbnail_texture: str | StaticTexture2D | None = None, detail_image_root: str | Slot | None = None, compact_root: str | Slot | None = None, compact_header_root: str | Slot | None = None, detail_header_root: str | Slot | None = None, compact_mask_enabled: str | IField[primitives.Bool] | None = None, compact_mask_root_enabled: str | IField[primitives.Bool] | None = None, open_button: str | Button | None = None, scroll_rect: str | ScrollRect | None = None, expand_button: str | Button | None = None, expand_icon: str | Image | None = None, expand_sprite: str | IAssetProvider[Sprite] | None = None, compact_sprite: str | IAssetProvider[Sprite] | None = None, description: str | Text | None = None, left_details_root: str | Slot | None = None, right_details_root: str | Slot | None = None, details_text: str | Text | None = None, cycle_left_button: str | Button | None = None, cycle_right_button: str | Button | None = None, compact_parent: str | SyncRef[Slot] | None = None, compact_header_parent: str | SyncRef[Slot] | None = None, sidebar_active: str | IField[primitives.Bool] | None = None, sidebar_anchor_min: str | IField[primitives.Float2] | None = None, sidebar_anchor_max: str | IField[primitives.Float2] | None = None, content_anchor_min: str | IField[primitives.Float2] | None = None, content_anchor_max: str | IField[primitives.Float2] | None = None, rect_transform_lerp: str | IField[primitives.Float] | None = None, modal_anchor_min: str | IField[primitives.Float2] | None = None, modal_anchor_max: str | IField[primitives.Float2] | None = None, compact_buttons_active: str | IField[primitives.Bool] | None = None, compact_buttons_anchor_min: str | IField[primitives.Float2] | None = None, compact_buttons_anchor_max: str | IField[primitives.Float2] | None = None, compact_detail_rect: str | IField[primitives.Rect] | None = None, compact_detail_button_rect: str | IField[primitives.Rect] | None = None, compact_detail_text: str | Text | None = None, compact_detail_expand_button: str | Button | None = None, new_session_item_root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            world_or_session_id: Initial value for WorldOrSessionId.
            visited: Initial value for _visited.
            total_active_users: Initial value for _totalActiveUsers.
            total_contacts: Initial value for _totalContacts.
            expanded: Initial value for Expanded.
            compact_detail_expanded: Initial value for CompactDetailExpanded.
            modal_compact_size: Initial value for ModalCompactSize.
            modal_expanded_size: Initial value for ModalExpandedSize.
            host_text: Initial value for _hostText.
            session_items_root: Initial value for _sessionItemsRoot.
            thumbnail_graphic: Initial value for _thumbnailGraphic.
            thumbnail_texture: Initial value for _thumbnailTexture.
            detail_image_root: Initial value for _detailImageRoot.
            compact_root: Initial value for _compactRoot.
            compact_header_root: Initial value for _compactHeaderRoot.
            detail_header_root: Initial value for _detailHeaderRoot.
            compact_mask_enabled: Initial value for _compactMaskEnabled.
            compact_mask_root_enabled: Initial value for _compactMaskRootEnabled.
            open_button: Initial value for _openButton.
            scroll_rect: Initial value for _scrollRect.
            expand_button: Initial value for _expandButton.
            expand_icon: Initial value for _expandIcon.
            expand_sprite: Initial value for _expandSprite.
            compact_sprite: Initial value for _compactSprite.
            description: Initial value for _description.
            left_details_root: Initial value for _leftDetailsRoot.
            right_details_root: Initial value for _rightDetailsRoot.
            details_text: Initial value for _detailsText.
            cycle_left_button: Initial value for _cycleLeftButton.
            cycle_right_button: Initial value for _cycleRightButton.
            compact_parent: Initial value for _compactParent.
            compact_header_parent: Initial value for _compactHeaderParent.
            sidebar_active: Initial value for _sidebarActive.
            sidebar_anchor_min: Initial value for _sidebarAnchorMin.
            sidebar_anchor_max: Initial value for _sidebarAnchorMax.
            content_anchor_min: Initial value for _contentAnchorMin.
            content_anchor_max: Initial value for _contentAnchorMax.
            rect_transform_lerp: Initial value for _rectTransformLerp.
            modal_anchor_min: Initial value for _modalAnchorMin.
            modal_anchor_max: Initial value for _modalAnchorMax.
            compact_buttons_active: Initial value for _compactButtonsActive.
            compact_buttons_anchor_min: Initial value for _compactButtonsAnchorMin.
            compact_buttons_anchor_max: Initial value for _compactButtonsAnchorMax.
            compact_detail_rect: Initial value for _compactDetailRect.
            compact_detail_button_rect: Initial value for _compactDetailButtonRect.
            compact_detail_text: Initial value for _compactDetailText.
            compact_detail_expand_button: Initial value for _compactDetailExpandButton.
            new_session_item_root: Initial value for _newSessionItemRoot.
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
        if expanded is not None:
            self.expanded = expanded
        if compact_detail_expanded is not None:
            self.compact_detail_expanded = compact_detail_expanded
        if modal_compact_size is not None:
            self.modal_compact_size = modal_compact_size
        if modal_expanded_size is not None:
            self.modal_expanded_size = modal_expanded_size
        if host_text is not None:
            self.host_text = host_text
        if session_items_root is not None:
            self.session_items_root = session_items_root
        if thumbnail_graphic is not None:
            self.thumbnail_graphic = thumbnail_graphic
        if thumbnail_texture is not None:
            self.thumbnail_texture = thumbnail_texture
        if detail_image_root is not None:
            self.detail_image_root = detail_image_root
        if compact_root is not None:
            self.compact_root = compact_root
        if compact_header_root is not None:
            self.compact_header_root = compact_header_root
        if detail_header_root is not None:
            self.detail_header_root = detail_header_root
        if compact_mask_enabled is not None:
            self.compact_mask_enabled = compact_mask_enabled
        if compact_mask_root_enabled is not None:
            self.compact_mask_root_enabled = compact_mask_root_enabled
        if open_button is not None:
            self.open_button = open_button
        if scroll_rect is not None:
            self.scroll_rect = scroll_rect
        if expand_button is not None:
            self.expand_button = expand_button
        if expand_icon is not None:
            self.expand_icon = expand_icon
        if expand_sprite is not None:
            self.expand_sprite = expand_sprite
        if compact_sprite is not None:
            self.compact_sprite = compact_sprite
        if description is not None:
            self.description = description
        if left_details_root is not None:
            self.left_details_root = left_details_root
        if right_details_root is not None:
            self.right_details_root = right_details_root
        if details_text is not None:
            self.details_text = details_text
        if cycle_left_button is not None:
            self.cycle_left_button = cycle_left_button
        if cycle_right_button is not None:
            self.cycle_right_button = cycle_right_button
        if compact_parent is not None:
            self.compact_parent = compact_parent
        if compact_header_parent is not None:
            self.compact_header_parent = compact_header_parent
        if sidebar_active is not None:
            self.sidebar_active = sidebar_active
        if sidebar_anchor_min is not None:
            self.sidebar_anchor_min = sidebar_anchor_min
        if sidebar_anchor_max is not None:
            self.sidebar_anchor_max = sidebar_anchor_max
        if content_anchor_min is not None:
            self.content_anchor_min = content_anchor_min
        if content_anchor_max is not None:
            self.content_anchor_max = content_anchor_max
        if rect_transform_lerp is not None:
            self.rect_transform_lerp = rect_transform_lerp
        if modal_anchor_min is not None:
            self.modal_anchor_min = modal_anchor_min
        if modal_anchor_max is not None:
            self.modal_anchor_max = modal_anchor_max
        if compact_buttons_active is not None:
            self.compact_buttons_active = compact_buttons_active
        if compact_buttons_anchor_min is not None:
            self.compact_buttons_anchor_min = compact_buttons_anchor_min
        if compact_buttons_anchor_max is not None:
            self.compact_buttons_anchor_max = compact_buttons_anchor_max
        if compact_detail_rect is not None:
            self.compact_detail_rect = compact_detail_rect
        if compact_detail_button_rect is not None:
            self.compact_detail_button_rect = compact_detail_button_rect
        if compact_detail_text is not None:
            self.compact_detail_text = compact_detail_text
        if compact_detail_expand_button is not None:
            self.compact_detail_expand_button = compact_detail_expand_button
        if new_session_item_root is not None:
            self.new_session_item_root = new_session_item_root

    @property
    def updating_user(self) -> members.SyncObject | None:
        """The UpdatingUser member."""
        member = self.get_member("UpdatingUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @updating_user.setter
    def updating_user(self, value: members.SyncObject) -> None:
        """Set the UpdatingUser member."""
        self.set_member("UpdatingUser", value)

    @property
    def world_or_session_id(self) -> primitives.String | None:
        """The WorldOrSessionId field value."""
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
        """The _visited field value."""
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
        """The _totalActiveUsers field value."""
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
        """The _totalContacts field value."""
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
    def expanded(self) -> primitives.Bool | None:
        """The Expanded field value."""
        member = self.get_member("Expanded")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @expanded.setter
    def expanded(self, value: primitives.Bool) -> None:
        """Set the Expanded field value."""
        member = self.get_member("Expanded")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Expanded", fields.FieldBool(value=value)
            )

    @property
    def compact_detail_expanded(self) -> primitives.Bool | None:
        """The CompactDetailExpanded field value."""
        member = self.get_member("CompactDetailExpanded")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @compact_detail_expanded.setter
    def compact_detail_expanded(self, value: primitives.Bool) -> None:
        """Set the CompactDetailExpanded field value."""
        member = self.get_member("CompactDetailExpanded")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CompactDetailExpanded", fields.FieldBool(value=value)
            )

    @property
    def compact_detail_category(self) -> members.FieldEnum | None:
        """The CompactDetailCategory member."""
        member = self.get_member("CompactDetailCategory")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @compact_detail_category.setter
    def compact_detail_category(self, value: members.FieldEnum) -> None:
        """Set the CompactDetailCategory member."""
        self.set_member("CompactDetailCategory", value)

    @property
    def modal_compact_size(self) -> primitives.Float2 | None:
        """The ModalCompactSize field value."""
        member = self.get_member("ModalCompactSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @modal_compact_size.setter
    def modal_compact_size(self, value: primitives.Float2) -> None:
        """Set the ModalCompactSize field value."""
        member = self.get_member("ModalCompactSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ModalCompactSize", fields.FieldFloat2(value=value)
            )

    @property
    def modal_expanded_size(self) -> primitives.Float2 | None:
        """The ModalExpandedSize field value."""
        member = self.get_member("ModalExpandedSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @modal_expanded_size.setter
    def modal_expanded_size(self, value: primitives.Float2) -> None:
        """Set the ModalExpandedSize field value."""
        member = self.get_member("ModalExpandedSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ModalExpandedSize", fields.FieldFloat2(value=value)
            )

    @property
    def host_text(self) -> str | None:
        """Target ID of the _hostText reference (targets Text)."""
        member = self.get_member("_hostText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @host_text.setter
    def host_text(self, target: str | Text | None) -> None:
        """Set the _hostText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_hostText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_hostText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def session_items_root(self) -> str | None:
        """Target ID of the _sessionItemsRoot reference (targets Slot)."""
        member = self.get_member("_sessionItemsRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @session_items_root.setter
    def session_items_root(self, target: str | Slot | None) -> None:
        """Set the _sessionItemsRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_sessionItemsRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sessionItemsRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def thumbnail_graphic(self) -> str | None:
        """Target ID of the _thumbnailGraphic reference (targets RawGraphic)."""
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
    def detail_image_root(self) -> str | None:
        """Target ID of the _detailImageRoot reference (targets Slot)."""
        member = self.get_member("_detailImageRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @detail_image_root.setter
    def detail_image_root(self, target: str | Slot | None) -> None:
        """Set the _detailImageRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_detailImageRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_detailImageRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def compact_root(self) -> str | None:
        """Target ID of the _compactRoot reference (targets Slot)."""
        member = self.get_member("_compactRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @compact_root.setter
    def compact_root(self, target: str | Slot | None) -> None:
        """Set the _compactRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_compactRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_compactRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def compact_header_root(self) -> str | None:
        """Target ID of the _compactHeaderRoot reference (targets Slot)."""
        member = self.get_member("_compactHeaderRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @compact_header_root.setter
    def compact_header_root(self, target: str | Slot | None) -> None:
        """Set the _compactHeaderRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_compactHeaderRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_compactHeaderRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def detail_header_root(self) -> str | None:
        """Target ID of the _detailHeaderRoot reference (targets Slot)."""
        member = self.get_member("_detailHeaderRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @detail_header_root.setter
    def detail_header_root(self, target: str | Slot | None) -> None:
        """Set the _detailHeaderRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_detailHeaderRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_detailHeaderRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def compact_mask_enabled(self) -> str | None:
        """Target ID of the _compactMaskEnabled reference (targets IField[primitives.Bool])."""
        member = self.get_member("_compactMaskEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @compact_mask_enabled.setter
    def compact_mask_enabled(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _compactMaskEnabled reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_compactMaskEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_compactMaskEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def compact_mask_root_enabled(self) -> str | None:
        """Target ID of the _compactMaskRootEnabled reference (targets IField[primitives.Bool])."""
        member = self.get_member("_compactMaskRootEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @compact_mask_root_enabled.setter
    def compact_mask_root_enabled(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _compactMaskRootEnabled reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_compactMaskRootEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_compactMaskRootEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def open_button(self) -> str | None:
        """Target ID of the _openButton reference (targets Button)."""
        member = self.get_member("_openButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @open_button.setter
    def open_button(self, target: str | Button | None) -> None:
        """Set the _openButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_openButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_openButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def scroll_rect(self) -> str | None:
        """Target ID of the _scrollRect reference (targets ScrollRect)."""
        member = self.get_member("_scrollRect")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scroll_rect.setter
    def scroll_rect(self, target: str | ScrollRect | None) -> None:
        """Set the _scrollRect reference by target ID or ScrollRect instance."""
        target_id: str | None = target.id if isinstance(target, ScrollRect) else target  # type: ignore[assignment]
        member = self.get_member("_scrollRect")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_scrollRect",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.ScrollRect'),
            )

    @property
    def expand_button(self) -> str | None:
        """Target ID of the _expandButton reference (targets Button)."""
        member = self.get_member("_expandButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @expand_button.setter
    def expand_button(self, target: str | Button | None) -> None:
        """Set the _expandButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_expandButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_expandButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def expand_icon(self) -> str | None:
        """Target ID of the _expandIcon reference (targets Image)."""
        member = self.get_member("_expandIcon")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @expand_icon.setter
    def expand_icon(self, target: str | Image | None) -> None:
        """Set the _expandIcon reference by target ID or Image instance."""
        target_id: str | None = target.id if isinstance(target, Image) else target  # type: ignore[assignment]
        member = self.get_member("_expandIcon")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_expandIcon",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Image'),
            )

    @property
    def expand_sprite(self) -> str | None:
        """Target ID of the _expandSprite reference (targets IAssetProvider[Sprite])."""
        member = self.get_member("_expandSprite")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @expand_sprite.setter
    def expand_sprite(self, target: str | IAssetProvider[Sprite] | None) -> None:
        """Set the _expandSprite reference by target ID or IAssetProvider[Sprite] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_expandSprite")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_expandSprite",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Sprite>'),
            )

    @property
    def compact_sprite(self) -> str | None:
        """Target ID of the _compactSprite reference (targets IAssetProvider[Sprite])."""
        member = self.get_member("_compactSprite")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @compact_sprite.setter
    def compact_sprite(self, target: str | IAssetProvider[Sprite] | None) -> None:
        """Set the _compactSprite reference by target ID or IAssetProvider[Sprite] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_compactSprite")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_compactSprite",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Sprite>'),
            )

    @property
    def description(self) -> str | None:
        """Target ID of the _description reference (targets Text)."""
        member = self.get_member("_description")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @description.setter
    def description(self, target: str | Text | None) -> None:
        """Set the _description reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_description")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_description",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def left_details_root(self) -> str | None:
        """Target ID of the _leftDetailsRoot reference (targets Slot)."""
        member = self.get_member("_leftDetailsRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_details_root.setter
    def left_details_root(self, target: str | Slot | None) -> None:
        """Set the _leftDetailsRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_leftDetailsRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftDetailsRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def right_details_root(self) -> str | None:
        """Target ID of the _rightDetailsRoot reference (targets Slot)."""
        member = self.get_member("_rightDetailsRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_details_root.setter
    def right_details_root(self, target: str | Slot | None) -> None:
        """Set the _rightDetailsRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_rightDetailsRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightDetailsRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def details_text(self) -> str | None:
        """Target ID of the _detailsText reference (targets Text)."""
        member = self.get_member("_detailsText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @details_text.setter
    def details_text(self, target: str | Text | None) -> None:
        """Set the _detailsText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_detailsText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_detailsText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def cycle_left_button(self) -> str | None:
        """Target ID of the _cycleLeftButton reference (targets Button)."""
        member = self.get_member("_cycleLeftButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cycle_left_button.setter
    def cycle_left_button(self, target: str | Button | None) -> None:
        """Set the _cycleLeftButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_cycleLeftButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cycleLeftButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def cycle_right_button(self) -> str | None:
        """Target ID of the _cycleRightButton reference (targets Button)."""
        member = self.get_member("_cycleRightButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cycle_right_button.setter
    def cycle_right_button(self, target: str | Button | None) -> None:
        """Set the _cycleRightButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_cycleRightButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cycleRightButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def compact_parent(self) -> str | None:
        """Target ID of the _compactParent reference (targets SyncRef[Slot])."""
        member = self.get_member("_compactParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @compact_parent.setter
    def compact_parent(self, target: str | SyncRef[Slot] | None) -> None:
        """Set the _compactParent reference by target ID or SyncRef[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("_compactParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_compactParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def compact_header_parent(self) -> str | None:
        """Target ID of the _compactHeaderParent reference (targets SyncRef[Slot])."""
        member = self.get_member("_compactHeaderParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @compact_header_parent.setter
    def compact_header_parent(self, target: str | SyncRef[Slot] | None) -> None:
        """Set the _compactHeaderParent reference by target ID or SyncRef[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("_compactHeaderParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_compactHeaderParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def sidebar_active(self) -> str | None:
        """Target ID of the _sidebarActive reference (targets IField[primitives.Bool])."""
        member = self.get_member("_sidebarActive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sidebar_active.setter
    def sidebar_active(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _sidebarActive reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_sidebarActive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sidebarActive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def sidebar_anchor_min(self) -> str | None:
        """Target ID of the _sidebarAnchorMin reference (targets IField[primitives.Float2])."""
        member = self.get_member("_sidebarAnchorMin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sidebar_anchor_min.setter
    def sidebar_anchor_min(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _sidebarAnchorMin reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_sidebarAnchorMin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sidebarAnchorMin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def sidebar_anchor_max(self) -> str | None:
        """Target ID of the _sidebarAnchorMax reference (targets IField[primitives.Float2])."""
        member = self.get_member("_sidebarAnchorMax")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sidebar_anchor_max.setter
    def sidebar_anchor_max(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _sidebarAnchorMax reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_sidebarAnchorMax")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sidebarAnchorMax",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def content_anchor_min(self) -> str | None:
        """Target ID of the _contentAnchorMin reference (targets IField[primitives.Float2])."""
        member = self.get_member("_contentAnchorMin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @content_anchor_min.setter
    def content_anchor_min(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _contentAnchorMin reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_contentAnchorMin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_contentAnchorMin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def content_anchor_max(self) -> str | None:
        """Target ID of the _contentAnchorMax reference (targets IField[primitives.Float2])."""
        member = self.get_member("_contentAnchorMax")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @content_anchor_max.setter
    def content_anchor_max(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _contentAnchorMax reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_contentAnchorMax")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_contentAnchorMax",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def rect_transform_lerp(self) -> str | None:
        """Target ID of the _rectTransformLerp reference (targets IField[primitives.Float])."""
        member = self.get_member("_rectTransformLerp")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rect_transform_lerp.setter
    def rect_transform_lerp(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _rectTransformLerp reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rectTransformLerp")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rectTransformLerp",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def modal_anchor_min(self) -> str | None:
        """Target ID of the _modalAnchorMin reference (targets IField[primitives.Float2])."""
        member = self.get_member("_modalAnchorMin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @modal_anchor_min.setter
    def modal_anchor_min(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _modalAnchorMin reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_modalAnchorMin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_modalAnchorMin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def modal_anchor_max(self) -> str | None:
        """Target ID of the _modalAnchorMax reference (targets IField[primitives.Float2])."""
        member = self.get_member("_modalAnchorMax")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @modal_anchor_max.setter
    def modal_anchor_max(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _modalAnchorMax reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_modalAnchorMax")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_modalAnchorMax",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def compact_buttons_active(self) -> str | None:
        """Target ID of the _compactButtonsActive reference (targets IField[primitives.Bool])."""
        member = self.get_member("_compactButtonsActive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @compact_buttons_active.setter
    def compact_buttons_active(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _compactButtonsActive reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_compactButtonsActive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_compactButtonsActive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def compact_buttons_anchor_min(self) -> str | None:
        """Target ID of the _compactButtonsAnchorMin reference (targets IField[primitives.Float2])."""
        member = self.get_member("_compactButtonsAnchorMin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @compact_buttons_anchor_min.setter
    def compact_buttons_anchor_min(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _compactButtonsAnchorMin reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_compactButtonsAnchorMin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_compactButtonsAnchorMin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def compact_buttons_anchor_max(self) -> str | None:
        """Target ID of the _compactButtonsAnchorMax reference (targets IField[primitives.Float2])."""
        member = self.get_member("_compactButtonsAnchorMax")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @compact_buttons_anchor_max.setter
    def compact_buttons_anchor_max(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _compactButtonsAnchorMax reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_compactButtonsAnchorMax")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_compactButtonsAnchorMax",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def compact_detail_rect(self) -> str | None:
        """Target ID of the _compactDetailRect reference (targets IField[primitives.Rect])."""
        member = self.get_member("_compactDetailRect")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @compact_detail_rect.setter
    def compact_detail_rect(self, target: str | IField[primitives.Rect] | None) -> None:
        """Set the _compactDetailRect reference by target ID or IField[primitives.Rect] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_compactDetailRect")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_compactDetailRect",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Rect>'),
            )

    @property
    def compact_detail_button_rect(self) -> str | None:
        """Target ID of the _compactDetailButtonRect reference (targets IField[primitives.Rect])."""
        member = self.get_member("_compactDetailButtonRect")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @compact_detail_button_rect.setter
    def compact_detail_button_rect(self, target: str | IField[primitives.Rect] | None) -> None:
        """Set the _compactDetailButtonRect reference by target ID or IField[primitives.Rect] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_compactDetailButtonRect")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_compactDetailButtonRect",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Rect>'),
            )

    @property
    def compact_detail_text(self) -> str | None:
        """Target ID of the _compactDetailText reference (targets Text)."""
        member = self.get_member("_compactDetailText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @compact_detail_text.setter
    def compact_detail_text(self, target: str | Text | None) -> None:
        """Set the _compactDetailText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_compactDetailText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_compactDetailText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def compact_detail_expand_button(self) -> str | None:
        """Target ID of the _compactDetailExpandButton reference (targets Button)."""
        member = self.get_member("_compactDetailExpandButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @compact_detail_expand_button.setter
    def compact_detail_expand_button(self, target: str | Button | None) -> None:
        """Set the _compactDetailExpandButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_compactDetailExpandButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_compactDetailExpandButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def new_session_item_root(self) -> str | None:
        """Target ID of the _newSessionItemRoot reference (targets Slot)."""
        member = self.get_member("_newSessionItemRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @new_session_item_root.setter
    def new_session_item_root(self, target: str | Slot | None) -> None:
        """Set the _newSessionItemRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_newSessionItemRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_newSessionItemRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    async def open_world_detail(self, resolink: protocols.ResoniteLinkClient, item: str, debug: bool = False) -> dict:
        """Call the OpenWorldDetail sync method.

        Args:
            resolink: Connected ResoniteLink client.
            item: The item parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "OpenWorldDetail", {"item": item}, debug,
        )

