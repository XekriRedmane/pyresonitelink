"""Generated component: FeedOrderedItemInterface."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.idata_feed_view import IDataFeedView
from pyresonitelink.generated._types.feed_item_interface import FeedItemInterface
from pyresonitelink.generated._types.sync_delegate import SyncDelegate
from pyresonitelink.generated._types.action import Action
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FeedOrderedItemInterface(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FeedOrderedItemInterface<>.

    Category: Radiant UI/Data Feeds/Interfaces

    Parameterize with a value type::

        FeedOrderedItemInterface[primitives.Float]
        FeedOrderedItemInterface[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FeedOrderedItemInterface<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.FeedOrderedItemInterface<>"

    def __init__(self, has_data: primitives.Bool | None = None, item_name: str | IField[primitives.String] | None = None, item_key: str | IField[primitives.String] | None = None, item_description: str | IField[primitives.String] | None = None, has_description: str | IField[primitives.Bool] | None = None, description_cleanup: str | Slot | None = None, item_icon: str | IField[str] | None = None, has_icon: str | IField[primitives.Bool] | None = None, icon_cleanup: str | Slot | None = None, view: str | SyncRef[IDataFeedView] | None = None, parent_container: str | FeedItemInterface | None = None, child_container: str | Slot | None = None, enabled_state: str | IField[primitives.Bool] | None = None, value: str | IField[T] | None = None, formatting: str | IField[primitives.String] | None = None, is_first: str | IField[primitives.Bool] | None = None, is_last: str | IField[primitives.Bool] | None = None, move_up_label: str | IField[primitives.String] | None = None, move_down_label: str | IField[primitives.String] | None = None, make_first_label: str | IField[primitives.String] | None = None, make_last_label: str | IField[primitives.String] | None = None, move_up: str | SyncDelegate[Action] | None = None, move_down: str | SyncDelegate[Action] | None = None, make_first: str | SyncDelegate[Action] | None = None, make_last: str | SyncDelegate[Action] | None = None, has_move_up: str | IField[primitives.Bool] | None = None, has_move_down: str | IField[primitives.Bool] | None = None, has_make_first: str | IField[primitives.Bool] | None = None, has_make_last: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            has_data: Initial value for HasData.
            item_name: Initial value for ItemName.
            item_key: Initial value for ItemKey.
            item_description: Initial value for ItemDescription.
            has_description: Initial value for HasDescription.
            description_cleanup: Initial value for DescriptionCleanup.
            item_icon: Initial value for ItemIcon.
            has_icon: Initial value for HasIcon.
            icon_cleanup: Initial value for IconCleanup.
            view: Initial value for View.
            parent_container: Initial value for ParentContainer.
            child_container: Initial value for ChildContainer.
            enabled_state: Initial value for EnabledState.
            value: Initial value for Value.
            formatting: Initial value for Formatting.
            is_first: Initial value for IsFirst.
            is_last: Initial value for IsLast.
            move_up_label: Initial value for MoveUpLabel.
            move_down_label: Initial value for MoveDownLabel.
            make_first_label: Initial value for MakeFirstLabel.
            make_last_label: Initial value for MakeLastLabel.
            move_up: Initial value for MoveUp.
            move_down: Initial value for MoveDown.
            make_first: Initial value for MakeFirst.
            make_last: Initial value for MakeLast.
            has_move_up: Initial value for HasMoveUp.
            has_move_down: Initial value for HasMoveDown.
            has_make_first: Initial value for HasMakeFirst.
            has_make_last: Initial value for HasMakeLast.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if has_data is not None:
            self.has_data = has_data
        if item_name is not None:
            self.item_name = item_name
        if item_key is not None:
            self.item_key = item_key
        if item_description is not None:
            self.item_description = item_description
        if has_description is not None:
            self.has_description = has_description
        if description_cleanup is not None:
            self.description_cleanup = description_cleanup
        if item_icon is not None:
            self.item_icon = item_icon
        if has_icon is not None:
            self.has_icon = has_icon
        if icon_cleanup is not None:
            self.icon_cleanup = icon_cleanup
        if view is not None:
            self.view = view
        if parent_container is not None:
            self.parent_container = parent_container
        if child_container is not None:
            self.child_container = child_container
        if enabled_state is not None:
            self.enabled_state = enabled_state
        if value is not None:
            self.value = value
        if formatting is not None:
            self.formatting = formatting
        if is_first is not None:
            self.is_first = is_first
        if is_last is not None:
            self.is_last = is_last
        if move_up_label is not None:
            self.move_up_label = move_up_label
        if move_down_label is not None:
            self.move_down_label = move_down_label
        if make_first_label is not None:
            self.make_first_label = make_first_label
        if make_last_label is not None:
            self.make_last_label = make_last_label
        if move_up is not None:
            self.move_up = move_up
        if move_down is not None:
            self.move_down = move_down
        if make_first is not None:
            self.make_first = make_first
        if make_last is not None:
            self.make_last = make_last
        if has_move_up is not None:
            self.has_move_up = has_move_up
        if has_move_down is not None:
            self.has_move_down = has_move_down
        if has_make_first is not None:
            self.has_make_first = has_make_first
        if has_make_last is not None:
            self.has_make_last = has_make_last

    @property
    def has_data(self) -> primitives.Bool | None:
        """The HasData field value."""
        member = self.get_member("HasData")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @has_data.setter
    def has_data(self, value: primitives.Bool) -> None:
        """Set the HasData field value."""
        member = self.get_member("HasData")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HasData", fields.FieldBool(value=value)
            )

    @property
    def item_name(self) -> str | None:
        """Target ID of the ItemName reference (targets IField[primitives.String])."""
        member = self.get_member("ItemName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_name.setter
    def item_name(self, target: str | IField[primitives.String] | None) -> None:
        """Set the ItemName reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ItemName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ItemName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def item_key(self) -> str | None:
        """Target ID of the ItemKey reference (targets IField[primitives.String])."""
        member = self.get_member("ItemKey")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_key.setter
    def item_key(self, target: str | IField[primitives.String] | None) -> None:
        """Set the ItemKey reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ItemKey")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ItemKey",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def item_description(self) -> str | None:
        """Target ID of the ItemDescription reference (targets IField[primitives.String])."""
        member = self.get_member("ItemDescription")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_description.setter
    def item_description(self, target: str | IField[primitives.String] | None) -> None:
        """Set the ItemDescription reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ItemDescription")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ItemDescription",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def has_description(self) -> str | None:
        """Target ID of the HasDescription reference (targets IField[primitives.Bool])."""
        member = self.get_member("HasDescription")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @has_description.setter
    def has_description(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the HasDescription reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("HasDescription")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HasDescription",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def description_cleanup(self) -> str | None:
        """Target ID of the DescriptionCleanup reference (targets Slot)."""
        member = self.get_member("DescriptionCleanup")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @description_cleanup.setter
    def description_cleanup(self, target: str | Slot | None) -> None:
        """Set the DescriptionCleanup reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("DescriptionCleanup")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DescriptionCleanup",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def item_icon(self) -> str | None:
        """Target ID of the ItemIcon reference (targets IField[str])."""
        member = self.get_member("ItemIcon")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_icon.setter
    def item_icon(self, target: str | IField[str] | None) -> None:
        """Set the ItemIcon reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ItemIcon")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ItemIcon",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Uri>'),
            )

    @property
    def has_icon(self) -> str | None:
        """Target ID of the HasIcon reference (targets IField[primitives.Bool])."""
        member = self.get_member("HasIcon")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @has_icon.setter
    def has_icon(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the HasIcon reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("HasIcon")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HasIcon",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def icon_cleanup(self) -> str | None:
        """Target ID of the IconCleanup reference (targets Slot)."""
        member = self.get_member("IconCleanup")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @icon_cleanup.setter
    def icon_cleanup(self, target: str | Slot | None) -> None:
        """Set the IconCleanup reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("IconCleanup")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IconCleanup",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def view(self) -> str | None:
        """Target ID of the View reference (targets SyncRef[IDataFeedView])."""
        member = self.get_member("View")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @view.setter
    def view(self, target: str | SyncRef[IDataFeedView] | None) -> None:
        """Set the View reference by target ID or SyncRef[IDataFeedView] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("View")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "View",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<[FrooxEngine]FrooxEngine.IDataFeedView>'),
            )

    @property
    def parent_container(self) -> str | None:
        """Target ID of the ParentContainer reference (targets FeedItemInterface)."""
        member = self.get_member("ParentContainer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @parent_container.setter
    def parent_container(self, target: str | FeedItemInterface | None) -> None:
        """Set the ParentContainer reference by target ID or FeedItemInterface instance."""
        target_id: str | None = target.id if isinstance(target, FeedItemInterface) else target  # type: ignore[assignment]
        member = self.get_member("ParentContainer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ParentContainer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FeedItemInterface'),
            )

    @property
    def child_container(self) -> str | None:
        """Target ID of the ChildContainer reference (targets Slot)."""
        member = self.get_member("ChildContainer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @child_container.setter
    def child_container(self, target: str | Slot | None) -> None:
        """Set the ChildContainer reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ChildContainer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ChildContainer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def nested_items(self) -> members.SyncList | None:
        """The NestedItems member."""
        member = self.get_member("NestedItems")
        if isinstance(member, members.SyncList):
            return member
        return None

    @nested_items.setter
    def nested_items(self, value: members.SyncList) -> None:
        """Set the NestedItems member."""
        self.set_member("NestedItems", value)

    @property
    def enabled_state(self) -> str | None:
        """Target ID of the EnabledState reference (targets IField[primitives.Bool])."""
        member = self.get_member("EnabledState")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @enabled_state.setter
    def enabled_state(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the EnabledState reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("EnabledState")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EnabledState",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def value(self) -> str | None:
        """Target ID of the Value reference (targets IField[T])."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | IField[T] | None) -> None:
        """Set the Value reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def formatting(self) -> str | None:
        """Target ID of the Formatting reference (targets IField[primitives.String])."""
        member = self.get_member("Formatting")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @formatting.setter
    def formatting(self, target: str | IField[primitives.String] | None) -> None:
        """Set the Formatting reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Formatting")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Formatting",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def is_first(self) -> str | None:
        """Target ID of the IsFirst reference (targets IField[primitives.Bool])."""
        member = self.get_member("IsFirst")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @is_first.setter
    def is_first(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the IsFirst reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("IsFirst")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IsFirst",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def is_last(self) -> str | None:
        """Target ID of the IsLast reference (targets IField[primitives.Bool])."""
        member = self.get_member("IsLast")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @is_last.setter
    def is_last(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the IsLast reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("IsLast")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IsLast",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def move_up_label(self) -> str | None:
        """Target ID of the MoveUpLabel reference (targets IField[primitives.String])."""
        member = self.get_member("MoveUpLabel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @move_up_label.setter
    def move_up_label(self, target: str | IField[primitives.String] | None) -> None:
        """Set the MoveUpLabel reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("MoveUpLabel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MoveUpLabel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def move_down_label(self) -> str | None:
        """Target ID of the MoveDownLabel reference (targets IField[primitives.String])."""
        member = self.get_member("MoveDownLabel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @move_down_label.setter
    def move_down_label(self, target: str | IField[primitives.String] | None) -> None:
        """Set the MoveDownLabel reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("MoveDownLabel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MoveDownLabel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def make_first_label(self) -> str | None:
        """Target ID of the MakeFirstLabel reference (targets IField[primitives.String])."""
        member = self.get_member("MakeFirstLabel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @make_first_label.setter
    def make_first_label(self, target: str | IField[primitives.String] | None) -> None:
        """Set the MakeFirstLabel reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("MakeFirstLabel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MakeFirstLabel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def make_last_label(self) -> str | None:
        """Target ID of the MakeLastLabel reference (targets IField[primitives.String])."""
        member = self.get_member("MakeLastLabel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @make_last_label.setter
    def make_last_label(self, target: str | IField[primitives.String] | None) -> None:
        """Set the MakeLastLabel reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("MakeLastLabel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MakeLastLabel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def move_up(self) -> str | None:
        """Target ID of the MoveUp reference (targets SyncDelegate[Action])."""
        member = self.get_member("MoveUp")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @move_up.setter
    def move_up(self, target: str | SyncDelegate[Action] | None) -> None:
        """Set the MoveUp reference by target ID or SyncDelegate[Action] instance."""
        target_id: str | None = target.id if isinstance(target, SyncDelegate) else target  # type: ignore[assignment]
        member = self.get_member("MoveUp")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MoveUp",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncDelegate<Action>'),
            )

    @property
    def move_down(self) -> str | None:
        """Target ID of the MoveDown reference (targets SyncDelegate[Action])."""
        member = self.get_member("MoveDown")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @move_down.setter
    def move_down(self, target: str | SyncDelegate[Action] | None) -> None:
        """Set the MoveDown reference by target ID or SyncDelegate[Action] instance."""
        target_id: str | None = target.id if isinstance(target, SyncDelegate) else target  # type: ignore[assignment]
        member = self.get_member("MoveDown")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MoveDown",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncDelegate<Action>'),
            )

    @property
    def make_first(self) -> str | None:
        """Target ID of the MakeFirst reference (targets SyncDelegate[Action])."""
        member = self.get_member("MakeFirst")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @make_first.setter
    def make_first(self, target: str | SyncDelegate[Action] | None) -> None:
        """Set the MakeFirst reference by target ID or SyncDelegate[Action] instance."""
        target_id: str | None = target.id if isinstance(target, SyncDelegate) else target  # type: ignore[assignment]
        member = self.get_member("MakeFirst")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MakeFirst",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncDelegate<Action>'),
            )

    @property
    def make_last(self) -> str | None:
        """Target ID of the MakeLast reference (targets SyncDelegate[Action])."""
        member = self.get_member("MakeLast")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @make_last.setter
    def make_last(self, target: str | SyncDelegate[Action] | None) -> None:
        """Set the MakeLast reference by target ID or SyncDelegate[Action] instance."""
        target_id: str | None = target.id if isinstance(target, SyncDelegate) else target  # type: ignore[assignment]
        member = self.get_member("MakeLast")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MakeLast",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncDelegate<Action>'),
            )

    @property
    def has_move_up(self) -> str | None:
        """Target ID of the HasMoveUp reference (targets IField[primitives.Bool])."""
        member = self.get_member("HasMoveUp")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @has_move_up.setter
    def has_move_up(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the HasMoveUp reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("HasMoveUp")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HasMoveUp",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def has_move_down(self) -> str | None:
        """Target ID of the HasMoveDown reference (targets IField[primitives.Bool])."""
        member = self.get_member("HasMoveDown")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @has_move_down.setter
    def has_move_down(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the HasMoveDown reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("HasMoveDown")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HasMoveDown",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def has_make_first(self) -> str | None:
        """Target ID of the HasMakeFirst reference (targets IField[primitives.Bool])."""
        member = self.get_member("HasMakeFirst")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @has_make_first.setter
    def has_make_first(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the HasMakeFirst reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("HasMakeFirst")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HasMakeFirst",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def has_make_last(self) -> str | None:
        """Target ID of the HasMakeLast reference (targets IField[primitives.Bool])."""
        member = self.get_member("HasMakeLast")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @has_make_last.setter
    def has_make_last(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the HasMakeLast reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("HasMakeLast")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HasMakeLast",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

