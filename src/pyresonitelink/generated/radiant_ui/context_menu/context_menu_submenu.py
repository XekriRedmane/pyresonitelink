"""Generated component: ContextMenuSubmenu."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ContextMenuSubmenu(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """The ContextMenuSubmenu component can be used in combination with any button component to make said button open a custom context menu when clicked.

    Category: Radiant UI/Context Menu

    Attach this component to a slot and attach a Context Menu Item Source
    along side it.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ContextMenuSubmenu"

    def __init__(self, items_root: str | Slot | None = None, search_whole_hierarchy: primitives.Bool | None = None, disable_flick: primitives.Bool | None = None, speed_override: primitives.Float | None = None, counter_clockwise: primitives.Bool | None = None, keep_position: primitives.Bool | None = None, hidden: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            items_root: Initial value for ItemsRoot.
            search_whole_hierarchy: Initial value for SearchWholeHierarchy.
            disable_flick: Initial value for DisableFlick.
            speed_override: Initial value for SpeedOverride.
            counter_clockwise: Initial value for CounterClockwise.
            keep_position: Initial value for KeepPosition.
            hidden: Initial value for Hidden.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if items_root is not None:
            self.items_root = items_root
        if search_whole_hierarchy is not None:
            self.search_whole_hierarchy = search_whole_hierarchy
        if disable_flick is not None:
            self.disable_flick = disable_flick
        if speed_override is not None:
            self.speed_override = speed_override
        if counter_clockwise is not None:
            self.counter_clockwise = counter_clockwise
        if keep_position is not None:
            self.keep_position = keep_position
        if hidden is not None:
            self.hidden = hidden

    @property
    def items_root(self) -> str | None:
        """All Context Menu Item Sources on slots immediately under this one will be included in the submenu."""
        member = self.get_member("ItemsRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @items_root.setter
    def items_root(self, target: str | Slot | None) -> None:
        """Set the ItemsRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ItemsRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ItemsRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def search_whole_hierarchy(self) -> primitives.Bool | None:
        """Display all items under ItemsRoot including sub slots, not just ones immediately under."""
        member = self.get_member("SearchWholeHierarchy")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @search_whole_hierarchy.setter
    def search_whole_hierarchy(self, value: primitives.Bool) -> None:
        """Set the SearchWholeHierarchy field value."""
        member = self.get_member("SearchWholeHierarchy")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SearchWholeHierarchy", fields.FieldBool(value=value)
            )

    @property
    def disable_flick(self) -> primitives.Bool | None:
        """Whether to allow opening of the sub menu by clicking on the context menu center and moving it to this component's Context Menu Item Source on the same slot."""
        member = self.get_member("DisableFlick")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @disable_flick.setter
    def disable_flick(self, value: primitives.Bool) -> None:
        """Set the DisableFlick field value."""
        member = self.get_member("DisableFlick")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisableFlick", fields.FieldBool(value=value)
            )

    @property
    def speed_override(self) -> primitives.Float | None:
        """Override the speed at which the new context menu will open."""
        member = self.get_member("SpeedOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @speed_override.setter
    def speed_override(self, value: primitives.Float) -> None:
        """Set the SpeedOverride field value."""
        member = self.get_member("SpeedOverride")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpeedOverride", fields.FieldNullableFloat(value=value)
            )

    @property
    def counter_clockwise(self) -> primitives.Bool | None:
        """Whether the items should be arranged clockwise or counter-clockwise in the submenu."""
        member = self.get_member("CounterClockwise")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @counter_clockwise.setter
    def counter_clockwise(self, value: primitives.Bool) -> None:
        """Set the CounterClockwise field value."""
        member = self.get_member("CounterClockwise")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CounterClockwise", fields.FieldBool(value=value)
            )

    @property
    def keep_position(self) -> primitives.Bool | None:
        """When set, the context menu will stay in the same place as the submenu opens. Otherwise, the context menu will recenter on the user's laser."""
        member = self.get_member("KeepPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @keep_position.setter
    def keep_position(self, value: primitives.Bool) -> None:
        """Set the KeepPosition field value."""
        member = self.get_member("KeepPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "KeepPosition", fields.FieldBool(value=value)
            )

    @property
    def hidden(self) -> primitives.Bool | None:
        """If set, the submenu is only visible to the user that opened it."""
        member = self.get_member("Hidden")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hidden.setter
    def hidden(self, value: primitives.Bool) -> None:
        """Set the Hidden field value."""
        member = self.get_member("Hidden")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Hidden", fields.FieldBool(value=value)
            )

