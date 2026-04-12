"""Generated component: RootContextMenuItem."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.context_menu_item_source import ContextMenuItemSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RootContextMenuItem(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Root context menu item is a component that makes a new context menu item appear for the active user for when they open their context menu.

    Category: Radiant UI/Context Menu

    **Related Components**: ContextMenuItemSource
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RootContextMenuItem"

    def __init__(self, exclude_on_tools: primitives.Bool | None = None, exclude_primary_hand: primitives.Bool | None = None, exclude_secondary_hand: primitives.Bool | None = None, item: str | ContextMenuItemSource | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            exclude_on_tools: Initial value for ExcludeOnTools.
            exclude_primary_hand: Initial value for ExcludePrimaryHand.
            exclude_secondary_hand: Initial value for ExcludeSecondaryHand.
            item: Initial value for Item.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if exclude_on_tools is not None:
            self.exclude_on_tools = exclude_on_tools
        if exclude_primary_hand is not None:
            self.exclude_primary_hand = exclude_primary_hand
        if exclude_secondary_hand is not None:
            self.exclude_secondary_hand = exclude_secondary_hand
        if item is not None:
            self.item = item

    @property
    def only_for_side(self) -> members.FieldEnum | None:
        """When set, the item will only be inserted when the context menu is opened on the specified hand."""
        member = self.get_member("OnlyForSide")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @only_for_side.setter
    def only_for_side(self, value: members.FieldEnum) -> None:
        """Set OnlyForSide. When set, the item will only be inserted when the context menu is opened on the specified hand."""
        self.set_member("OnlyForSide", value)

    @property
    def exclude_on_tools(self) -> primitives.Bool | None:
        """Determines whether or not the item shows up when opening the context menu while having a tool equipped on the same hand."""
        member = self.get_member("ExcludeOnTools")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exclude_on_tools.setter
    def exclude_on_tools(self, value: primitives.Bool) -> None:
        """Set the ExcludeOnTools field value."""
        member = self.get_member("ExcludeOnTools")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ExcludeOnTools", fields.FieldBool(value=value)
            )

    @property
    def exclude_primary_hand(self) -> primitives.Bool | None:
        """Makes the item not show up when the context menu is open on the user's primary hand."""
        member = self.get_member("ExcludePrimaryHand")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exclude_primary_hand.setter
    def exclude_primary_hand(self, value: primitives.Bool) -> None:
        """Set the ExcludePrimaryHand field value."""
        member = self.get_member("ExcludePrimaryHand")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ExcludePrimaryHand", fields.FieldBool(value=value)
            )

    @property
    def exclude_secondary_hand(self) -> primitives.Bool | None:
        """Makes the item not show up when the context menu is open on the user's secondary hand."""
        member = self.get_member("ExcludeSecondaryHand")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exclude_secondary_hand.setter
    def exclude_secondary_hand(self, value: primitives.Bool) -> None:
        """Set the ExcludeSecondaryHand field value."""
        member = self.get_member("ExcludeSecondaryHand")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ExcludeSecondaryHand", fields.FieldBool(value=value)
            )

    @property
    def item(self) -> str | None:
        """The ContextMenuItemSource that will be inserted into the context menu."""
        member = self.get_member("Item")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item.setter
    def item(self, target: str | ContextMenuItemSource | None) -> None:
        """Set the Item reference by target ID or ContextMenuItemSource instance."""
        target_id: str | None = target.id if isinstance(target, ContextMenuItemSource) else target  # type: ignore[assignment]
        member = self.get_member("Item")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Item",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ContextMenuItemSource'),
            )

