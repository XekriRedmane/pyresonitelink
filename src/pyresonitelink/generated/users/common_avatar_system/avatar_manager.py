"""Generated component: AvatarManager."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.avatar_anchor import AvatarAnchor
from pyresonitelink.generated._types.iempty_avatar_slot_handler import IEmptyAvatarSlotHandler
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """For detailed information on how this functions for mix and match body parts. Please also see Equipping Multiple Avatars.

The AvatarManager component is found on User root slots and is used to manage avatars equipped to a particular user. It also keeps track of and sets the equipped parameters of AvatarObjectSlots under an avatar, It manages the setting of fields on the AvatarRoot and AvatarGroup components.

    Category: Users/Common Avatar System

    Should not be used directly by the player, since this is used by the
    game instead to manage avatars on a user.

    **EquippedGroup**: Equipped group is internally handled as a type to hold data from a Dictionary&lt;AvatarRoot, &gt;
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarManager"

    def __init__(self, current_anchor: str | AvatarAnchor | None = None, auto_add_name_badge: primitives.Bool | None = None, auto_add_icon_badge: primitives.Bool | None = None, auto_add_live_indicator: primitives.Bool | None = None, empty_slot_handler: str | IEmptyAvatarSlotHandler | None = None, default_scale: primitives.Float | None = None, name_tag_text: primitives.String | None = None, name_tag_color: primitives.ColorX | None = None, name_tag_outline: primitives.ColorX | None = None, name_tag_background: primitives.ColorX | None = None, badge_templates: str | Slot | None = None, auto_name_badge: str | Slot | None = None, auto_icon_badge: str | Slot | None = None, auto_live_indicator: str | Slot | None = None, update_version: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            current_anchor: Initial value for _currentAnchor.
            auto_add_name_badge: Initial value for AutoAddNameBadge.
            auto_add_icon_badge: Initial value for AutoAddIconBadge.
            auto_add_live_indicator: Initial value for AutoAddLiveIndicator.
            empty_slot_handler: Initial value for EmptySlotHandler.
            default_scale: Initial value for DefaultScale.
            name_tag_text: Initial value for NameTagText.
            name_tag_color: Initial value for NameTagColor.
            name_tag_outline: Initial value for NameTagOutline.
            name_tag_background: Initial value for NameTagBackground.
            badge_templates: Initial value for _badgeTemplates.
            auto_name_badge: Initial value for _autoNameBadge.
            auto_icon_badge: Initial value for _autoIconBadge.
            auto_live_indicator: Initial value for _autoLiveIndicator.
            update_version: Initial value for _updateVersion.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if current_anchor is not None:
            self.current_anchor = current_anchor
        if auto_add_name_badge is not None:
            self.auto_add_name_badge = auto_add_name_badge
        if auto_add_icon_badge is not None:
            self.auto_add_icon_badge = auto_add_icon_badge
        if auto_add_live_indicator is not None:
            self.auto_add_live_indicator = auto_add_live_indicator
        if empty_slot_handler is not None:
            self.empty_slot_handler = empty_slot_handler
        if default_scale is not None:
            self.default_scale = default_scale
        if name_tag_text is not None:
            self.name_tag_text = name_tag_text
        if name_tag_color is not None:
            self.name_tag_color = name_tag_color
        if name_tag_outline is not None:
            self.name_tag_outline = name_tag_outline
        if name_tag_background is not None:
            self.name_tag_background = name_tag_background
        if badge_templates is not None:
            self.badge_templates = badge_templates
        if auto_name_badge is not None:
            self.auto_name_badge = auto_name_badge
        if auto_icon_badge is not None:
            self.auto_icon_badge = auto_icon_badge
        if auto_live_indicator is not None:
            self.auto_live_indicator = auto_live_indicator
        if update_version is not None:
            self.update_version = update_version

    @property
    def object_groups(self) -> members.SyncList | None:
        """A list of objects currently equipped by the user as part of an avatar."""
        member = self.get_member("_objectGroups")
        if isinstance(member, members.SyncList):
            return member
        return None

    @object_groups.setter
    def object_groups(self, value: members.SyncList) -> None:
        """Set _objectGroups. A list of objects currently equipped by the user as part of an avatar."""
        self.set_member("_objectGroups", value)

    @property
    def current_anchor(self) -> str | None:
        """The anchor the user associated with this component is currently sitting in."""
        member = self.get_member("_currentAnchor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_anchor.setter
    def current_anchor(self, target: str | AvatarAnchor | None) -> None:
        """Set the _currentAnchor reference by target ID or AvatarAnchor instance."""
        target_id: str | None = target.id if isinstance(target, AvatarAnchor) else target  # type: ignore[assignment]
        member = self.get_member("_currentAnchor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentAnchor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarAnchor'),
            )

    @property
    def auto_add_name_badge(self) -> primitives.Bool | None:
        """Whether to auto add the name badge component if it doesn't exist on an avatar when equipping it. Usually managed by the world through the Component:CommonAvatarBuilder"""
        member = self.get_member("AutoAddNameBadge")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_add_name_badge.setter
    def auto_add_name_badge(self, value: primitives.Bool) -> None:
        """Set the AutoAddNameBadge field value."""
        member = self.get_member("AutoAddNameBadge")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoAddNameBadge", fields.FieldBool(value=value)
            )

    @property
    def auto_add_icon_badge(self) -> primitives.Bool | None:
        """Whether to auto add the icon badges if it doesn't exist on an avatar when equipping it. Usually managed by the world through the Component:CommonAvatarBuilder"""
        member = self.get_member("AutoAddIconBadge")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_add_icon_badge.setter
    def auto_add_icon_badge(self, value: primitives.Bool) -> None:
        """Set the AutoAddIconBadge field value."""
        member = self.get_member("AutoAddIconBadge")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoAddIconBadge", fields.FieldBool(value=value)
            )

    @property
    def auto_add_live_indicator(self) -> primitives.Bool | None:
        """Whether to auto add the live indicator component if it doesn't exist on an avatar when equipping it. Usually managed by the world through the Component:CommonAvatarBuilder"""
        member = self.get_member("AutoAddLiveIndicator")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_add_live_indicator.setter
    def auto_add_live_indicator(self, value: primitives.Bool) -> None:
        """Set the AutoAddLiveIndicator field value."""
        member = self.get_member("AutoAddLiveIndicator")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoAddLiveIndicator", fields.FieldBool(value=value)
            )

    @property
    def empty_slot_handler(self) -> str | None:
        """The object to handle empty avatar slots. Usually defined by the world through the Component:CommonAvatarBuilder."""
        member = self.get_member("EmptySlotHandler")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @empty_slot_handler.setter
    def empty_slot_handler(self, target: str | IEmptyAvatarSlotHandler | None) -> None:
        """Set the EmptySlotHandler reference by target ID or IEmptyAvatarSlotHandler instance."""
        target_id: str | None = target.id if isinstance(target, IEmptyAvatarSlotHandler) else target  # type: ignore[assignment]
        member = self.get_member("EmptySlotHandler")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EmptySlotHandler",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.IEmptyAvatarSlotHandler'),
            )

    @property
    def default_scale(self) -> primitives.Float | None:
        """The default scale multiplier of the avatar currently equipped"""
        member = self.get_member("DefaultScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_scale.setter
    def default_scale(self, value: primitives.Float) -> None:
        """Set the DefaultScale field value."""
        member = self.get_member("DefaultScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DefaultScale", fields.FieldFloat(value=value)
            )

    @property
    def name_tag_text(self) -> primitives.String | None:
        """The text that should be assigned to the avatar nametag's text field list"""
        member = self.get_member("NameTagText")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @name_tag_text.setter
    def name_tag_text(self, value: primitives.String) -> None:
        """Set the NameTagText field value."""
        member = self.get_member("NameTagText")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NameTagText", fields.FieldString(value=value)
            )

    @property
    def name_tag_color(self) -> primitives.ColorX | None:
        """The color that should be assigned to the avatar nametag's color list."""
        member = self.get_member("NameTagColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @name_tag_color.setter
    def name_tag_color(self, value: primitives.ColorX) -> None:
        """Set the NameTagColor field value."""
        member = self.get_member("NameTagColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NameTagColor", fields.FieldColorX(value=value)
            )

    @property
    def name_tag_outline(self) -> primitives.ColorX | None:
        """The color that should be assigned to the avatar nametag's color1 list."""
        member = self.get_member("NameTagOutline")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @name_tag_outline.setter
    def name_tag_outline(self, value: primitives.ColorX) -> None:
        """Set the NameTagOutline field value."""
        member = self.get_member("NameTagOutline")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NameTagOutline", fields.FieldColorX(value=value)
            )

    @property
    def name_tag_background(self) -> primitives.ColorX | None:
        """The color.that should be assigned to the avatar nametag's color background list."""
        member = self.get_member("NameTagBackground")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @name_tag_background.setter
    def name_tag_background(self, value: primitives.ColorX) -> None:
        """Set the NameTagBackground field value."""
        member = self.get_member("NameTagBackground")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NameTagBackground", fields.FieldColorX(value=value)
            )

    @property
    def badge_templates(self) -> str | None:
        """the slot that was made for the user for storage of their badges."""
        member = self.get_member("_badgeTemplates")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @badge_templates.setter
    def badge_templates(self, target: str | Slot | None) -> None:
        """Set the _badgeTemplates reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_badgeTemplates")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_badgeTemplates",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def auto_name_badge(self) -> str | None:
        """the slot that was made for the user for their name badge."""
        member = self.get_member("_autoNameBadge")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @auto_name_badge.setter
    def auto_name_badge(self, target: str | Slot | None) -> None:
        """Set the _autoNameBadge reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_autoNameBadge")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_autoNameBadge",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def auto_icon_badge(self) -> str | None:
        """the slot that was made for the user for their Icon."""
        member = self.get_member("_autoIconBadge")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @auto_icon_badge.setter
    def auto_icon_badge(self, target: str | Slot | None) -> None:
        """Set the _autoIconBadge reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_autoIconBadge")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_autoIconBadge",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def auto_live_indicator(self) -> str | None:
        """The slot that was made for the user for their live indicator"""
        member = self.get_member("_autoLiveIndicator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @auto_live_indicator.setter
    def auto_live_indicator(self, target: str | Slot | None) -> None:
        """Set the _autoLiveIndicator reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_autoLiveIndicator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_autoLiveIndicator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def update_version(self) -> primitives.Int | None:
        """Internal."""
        member = self.get_member("_updateVersion")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @update_version.setter
    def update_version(self, value: primitives.Int) -> None:
        """Set the _updateVersion field value."""
        member = self.get_member("_updateVersion")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_updateVersion", fields.FieldInt(value=value)
            )

