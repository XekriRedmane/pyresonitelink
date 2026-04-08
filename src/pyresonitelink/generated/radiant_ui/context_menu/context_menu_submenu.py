"""Generated component: ContextMenuSubmenu."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ContextMenuSubmenu(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ContextMenuSubmenu.

    Category: Radiant UI/Context Menu
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ContextMenuSubmenu"

    def __init__(self, items_root: str | Slot | None = None, search_whole_hierarchy: bool | None = None, disable_flick: bool | None = None, speed_override: np.float32 | None = None, counter_clockwise: bool | None = None, keep_position: bool | None = None, hidden: bool | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the ItemsRoot reference (targets Slot)."""
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
    def search_whole_hierarchy(self) -> bool | None:
        """The SearchWholeHierarchy field value."""
        member = self.get_member("SearchWholeHierarchy")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @search_whole_hierarchy.setter
    def search_whole_hierarchy(self, value: bool) -> None:
        """Set the SearchWholeHierarchy field value."""
        member = self.get_member("SearchWholeHierarchy")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SearchWholeHierarchy", fields.FieldBool(value=value)
            )

    @property
    def disable_flick(self) -> bool | None:
        """The DisableFlick field value."""
        member = self.get_member("DisableFlick")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @disable_flick.setter
    def disable_flick(self, value: bool) -> None:
        """Set the DisableFlick field value."""
        member = self.get_member("DisableFlick")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisableFlick", fields.FieldBool(value=value)
            )

    @property
    def speed_override(self) -> np.float32 | None:
        """The SpeedOverride field value."""
        member = self.get_member("SpeedOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @speed_override.setter
    def speed_override(self, value: np.float32) -> None:
        """Set the SpeedOverride field value."""
        member = self.get_member("SpeedOverride")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpeedOverride", fields.FieldNullableFloat(value=value)
            )

    @property
    def counter_clockwise(self) -> bool | None:
        """The CounterClockwise field value."""
        member = self.get_member("CounterClockwise")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @counter_clockwise.setter
    def counter_clockwise(self, value: bool) -> None:
        """Set the CounterClockwise field value."""
        member = self.get_member("CounterClockwise")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CounterClockwise", fields.FieldBool(value=value)
            )

    @property
    def keep_position(self) -> bool | None:
        """The KeepPosition field value."""
        member = self.get_member("KeepPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @keep_position.setter
    def keep_position(self, value: bool) -> None:
        """Set the KeepPosition field value."""
        member = self.get_member("KeepPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "KeepPosition", fields.FieldBool(value=value)
            )

    @property
    def hidden(self) -> bool | None:
        """The Hidden field value."""
        member = self.get_member("Hidden")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hidden.setter
    def hidden(self, value: bool) -> None:
        """Set the Hidden field value."""
        member = self.get_member("Hidden")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Hidden", fields.FieldBool(value=value)
            )

