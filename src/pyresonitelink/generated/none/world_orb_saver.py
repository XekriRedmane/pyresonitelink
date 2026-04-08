"""Generated component: WorldOrbSaver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.world_orb import WorldOrb
from pyresonitelink.generated._types.context_menu_item import ContextMenuItem
from pyresonitelink.generated._types.context_menu import ContextMenu
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldOrbSaver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.WorldOrbSaver.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldOrbSaver"

    def __init__(self, orb: str | WorldOrb | None = None, save_here_item: str | ContextMenuItem | None = None, save_to_inventory_item: str | ContextMenuItem | None = None, cancel_item: str | ContextMenuItem | None = None, menu: str | ContextMenu | None = None, interactive: primitives.Bool | None = None, saving: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            orb: Initial value for Orb.
            save_here_item: Initial value for saveHereItem.
            save_to_inventory_item: Initial value for saveToInventoryItem.
            cancel_item: Initial value for cancelItem.
            menu: Initial value for menu.
            interactive: Initial value for interactive.
            saving: Initial value for saving.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if orb is not None:
            self.orb = orb
        if save_here_item is not None:
            self.save_here_item = save_here_item
        if save_to_inventory_item is not None:
            self.save_to_inventory_item = save_to_inventory_item
        if cancel_item is not None:
            self.cancel_item = cancel_item
        if menu is not None:
            self.menu = menu
        if interactive is not None:
            self.interactive = interactive
        if saving is not None:
            self.saving = saving

    @property
    def orb(self) -> str | None:
        """Target ID of the Orb reference (targets WorldOrb)."""
        member = self.get_member("Orb")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @orb.setter
    def orb(self, target: str | WorldOrb | None) -> None:
        """Set the Orb reference by target ID or WorldOrb instance."""
        target_id: str | None = target.id if isinstance(target, WorldOrb) else target  # type: ignore[assignment]
        member = self.get_member("Orb")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Orb",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldOrb'),
            )

    @property
    def save_here_item(self) -> str | None:
        """Target ID of the saveHereItem reference (targets ContextMenuItem)."""
        member = self.get_member("saveHereItem")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @save_here_item.setter
    def save_here_item(self, target: str | ContextMenuItem | None) -> None:
        """Set the saveHereItem reference by target ID or ContextMenuItem instance."""
        target_id: str | None = target.id if isinstance(target, ContextMenuItem) else target  # type: ignore[assignment]
        member = self.get_member("saveHereItem")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "saveHereItem",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ContextMenuItem'),
            )

    @property
    def save_to_inventory_item(self) -> str | None:
        """Target ID of the saveToInventoryItem reference (targets ContextMenuItem)."""
        member = self.get_member("saveToInventoryItem")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @save_to_inventory_item.setter
    def save_to_inventory_item(self, target: str | ContextMenuItem | None) -> None:
        """Set the saveToInventoryItem reference by target ID or ContextMenuItem instance."""
        target_id: str | None = target.id if isinstance(target, ContextMenuItem) else target  # type: ignore[assignment]
        member = self.get_member("saveToInventoryItem")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "saveToInventoryItem",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ContextMenuItem'),
            )

    @property
    def cancel_item(self) -> str | None:
        """Target ID of the cancelItem reference (targets ContextMenuItem)."""
        member = self.get_member("cancelItem")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cancel_item.setter
    def cancel_item(self, target: str | ContextMenuItem | None) -> None:
        """Set the cancelItem reference by target ID or ContextMenuItem instance."""
        target_id: str | None = target.id if isinstance(target, ContextMenuItem) else target  # type: ignore[assignment]
        member = self.get_member("cancelItem")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "cancelItem",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ContextMenuItem'),
            )

    @property
    def menu(self) -> str | None:
        """Target ID of the menu reference (targets ContextMenu)."""
        member = self.get_member("menu")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @menu.setter
    def menu(self, target: str | ContextMenu | None) -> None:
        """Set the menu reference by target ID or ContextMenu instance."""
        target_id: str | None = target.id if isinstance(target, ContextMenu) else target  # type: ignore[assignment]
        member = self.get_member("menu")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "menu",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ContextMenu'),
            )

    @property
    def interactive(self) -> primitives.Bool | None:
        """The interactive field value."""
        member = self.get_member("interactive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @interactive.setter
    def interactive(self, value: primitives.Bool) -> None:
        """Set the interactive field value."""
        member = self.get_member("interactive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "interactive", fields.FieldBool(value=value)
            )

    @property
    def saving(self) -> primitives.Bool | None:
        """The saving field value."""
        member = self.get_member("saving")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @saving.setter
    def saving(self, value: primitives.Bool) -> None:
        """Set the saving field value."""
        member = self.get_member("saving")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "saving", fields.FieldBool(value=value)
            )

