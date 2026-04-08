"""Generated component: UserspaceRadiantDash."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.radiant_dash import RadiantDash
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.user_interface_positioner import UserInterfacePositioner
from pyresonitelink.generated._types.modal_overlay_manager import ModalOverlayManager
from pyresonitelink.generated._types.legacy_canvas_panel import LegacyCanvasPanel
from pyresonitelink.generated._types.inventory_browser import InventoryBrowser
from pyresonitelink.generated._types.slider import Slider
from pyresonitelink.generated._types.look_at import LookAt
from pyresonitelink.generated._types.workspace import Workspace
from pyresonitelink.generated._types.notification_panel import NotificationPanel
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserspaceRadiantDash(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UserspaceRadiantDash.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserspaceRadiantDash"

    def __init__(self, block_open_close: bool | None = None, freeform: bool | None = None, dash: str | RadiantDash | None = None, dash_visual_root: str | Slot | None = None, positioner: str | UserInterfacePositioner | None = None, modal_overlay: str | ModalOverlayManager | None = None, legacy_inventory_panel: str | LegacyCanvasPanel | None = None, legacy_inventory: str | InventoryBrowser | None = None, slider: str | Slider | None = None, lookat: str | LookAt | None = None, ui_edit_mode_toggle: str | Slot | None = None, always_on_facet_root: str | Slot | None = None, screens_workspace: str | Workspace | None = None, top_workspace: str | Workspace | None = None, notifications: str | NotificationPanel | None = None, notifications_root: str | Slot | None = None, notifications_holder: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            block_open_close: Initial value for BlockOpenClose.
            freeform: Initial value for Freeform.
            dash: Initial value for _dash.
            dash_visual_root: Initial value for _dashVisualRoot.
            positioner: Initial value for _positioner.
            modal_overlay: Initial value for _modalOverlay.
            legacy_inventory_panel: Initial value for _legacyInventoryPanel.
            legacy_inventory: Initial value for _legacyInventory.
            slider: Initial value for _slider.
            lookat: Initial value for _lookat.
            ui_edit_mode_toggle: Initial value for _uiEditModeToggle.
            always_on_facet_root: Initial value for _alwaysOnFacetRoot.
            screens_workspace: Initial value for _screensWorkspace.
            top_workspace: Initial value for _topWorkspace.
            notifications: Initial value for _notifications.
            notifications_root: Initial value for _notificationsRoot.
            notifications_holder: Initial value for _notificationsHolder.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if block_open_close is not None:
            self.block_open_close = block_open_close
        if freeform is not None:
            self.freeform = freeform
        if dash is not None:
            self.dash = dash
        if dash_visual_root is not None:
            self.dash_visual_root = dash_visual_root
        if positioner is not None:
            self.positioner = positioner
        if modal_overlay is not None:
            self.modal_overlay = modal_overlay
        if legacy_inventory_panel is not None:
            self.legacy_inventory_panel = legacy_inventory_panel
        if legacy_inventory is not None:
            self.legacy_inventory = legacy_inventory
        if slider is not None:
            self.slider = slider
        if lookat is not None:
            self.lookat = lookat
        if ui_edit_mode_toggle is not None:
            self.ui_edit_mode_toggle = ui_edit_mode_toggle
        if always_on_facet_root is not None:
            self.always_on_facet_root = always_on_facet_root
        if screens_workspace is not None:
            self.screens_workspace = screens_workspace
        if top_workspace is not None:
            self.top_workspace = top_workspace
        if notifications is not None:
            self.notifications = notifications
        if notifications_root is not None:
            self.notifications_root = notifications_root
        if notifications_holder is not None:
            self.notifications_holder = notifications_holder

    @property
    def block_open_close(self) -> bool | None:
        """The BlockOpenClose field value."""
        member = self.get_member("BlockOpenClose")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @block_open_close.setter
    def block_open_close(self, value: bool) -> None:
        """Set the BlockOpenClose field value."""
        member = self.get_member("BlockOpenClose")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlockOpenClose", fields.FieldBool(value=value)
            )

    @property
    def freeform(self) -> bool | None:
        """The Freeform field value."""
        member = self.get_member("Freeform")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @freeform.setter
    def freeform(self, value: bool) -> None:
        """Set the Freeform field value."""
        member = self.get_member("Freeform")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Freeform", fields.FieldBool(value=value)
            )

    @property
    def dash(self) -> str | None:
        """Target ID of the _dash reference (targets RadiantDash)."""
        member = self.get_member("_dash")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @dash.setter
    def dash(self, target: str | RadiantDash | None) -> None:
        """Set the _dash reference by target ID or RadiantDash instance."""
        target_id: str | None = target.id if isinstance(target, RadiantDash) else target  # type: ignore[assignment]
        member = self.get_member("_dash")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_dash",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RadiantDash'),
            )

    @property
    def dash_visual_root(self) -> str | None:
        """Target ID of the _dashVisualRoot reference (targets Slot)."""
        member = self.get_member("_dashVisualRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @dash_visual_root.setter
    def dash_visual_root(self, target: str | Slot | None) -> None:
        """Set the _dashVisualRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_dashVisualRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_dashVisualRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def positioner(self) -> str | None:
        """Target ID of the _positioner reference (targets UserInterfacePositioner)."""
        member = self.get_member("_positioner")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @positioner.setter
    def positioner(self, target: str | UserInterfacePositioner | None) -> None:
        """Set the _positioner reference by target ID or UserInterfacePositioner instance."""
        target_id: str | None = target.id if isinstance(target, UserInterfacePositioner) else target  # type: ignore[assignment]
        member = self.get_member("_positioner")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_positioner",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UserInterfacePositioner'),
            )

    @property
    def modal_overlay(self) -> str | None:
        """Target ID of the _modalOverlay reference (targets ModalOverlayManager)."""
        member = self.get_member("_modalOverlay")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @modal_overlay.setter
    def modal_overlay(self, target: str | ModalOverlayManager | None) -> None:
        """Set the _modalOverlay reference by target ID or ModalOverlayManager instance."""
        target_id: str | None = target.id if isinstance(target, ModalOverlayManager) else target  # type: ignore[assignment]
        member = self.get_member("_modalOverlay")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_modalOverlay",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ModalOverlayManager'),
            )

    @property
    def legacy_inventory_panel(self) -> str | None:
        """Target ID of the _legacyInventoryPanel reference (targets LegacyCanvasPanel)."""
        member = self.get_member("_legacyInventoryPanel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @legacy_inventory_panel.setter
    def legacy_inventory_panel(self, target: str | LegacyCanvasPanel | None) -> None:
        """Set the _legacyInventoryPanel reference by target ID or LegacyCanvasPanel instance."""
        target_id: str | None = target.id if isinstance(target, LegacyCanvasPanel) else target  # type: ignore[assignment]
        member = self.get_member("_legacyInventoryPanel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_legacyInventoryPanel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyCanvasPanel'),
            )

    @property
    def legacy_inventory(self) -> str | None:
        """Target ID of the _legacyInventory reference (targets InventoryBrowser)."""
        member = self.get_member("_legacyInventory")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @legacy_inventory.setter
    def legacy_inventory(self, target: str | InventoryBrowser | None) -> None:
        """Set the _legacyInventory reference by target ID or InventoryBrowser instance."""
        target_id: str | None = target.id if isinstance(target, InventoryBrowser) else target  # type: ignore[assignment]
        member = self.get_member("_legacyInventory")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_legacyInventory",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InventoryBrowser'),
            )

    @property
    def slider(self) -> str | None:
        """Target ID of the _slider reference (targets Slider)."""
        member = self.get_member("_slider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @slider.setter
    def slider(self, target: str | Slider | None) -> None:
        """Set the _slider reference by target ID or Slider instance."""
        target_id: str | None = target.id if isinstance(target, Slider) else target  # type: ignore[assignment]
        member = self.get_member("_slider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_slider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slider'),
            )

    @property
    def lookat(self) -> str | None:
        """Target ID of the _lookat reference (targets LookAt)."""
        member = self.get_member("_lookat")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lookat.setter
    def lookat(self, target: str | LookAt | None) -> None:
        """Set the _lookat reference by target ID or LookAt instance."""
        target_id: str | None = target.id if isinstance(target, LookAt) else target  # type: ignore[assignment]
        member = self.get_member("_lookat")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_lookat",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LookAt'),
            )

    @property
    def ui_edit_mode_toggle(self) -> str | None:
        """Target ID of the _uiEditModeToggle reference (targets Slot)."""
        member = self.get_member("_uiEditModeToggle")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ui_edit_mode_toggle.setter
    def ui_edit_mode_toggle(self, target: str | Slot | None) -> None:
        """Set the _uiEditModeToggle reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_uiEditModeToggle")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_uiEditModeToggle",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def always_on_facet_root(self) -> str | None:
        """Target ID of the _alwaysOnFacetRoot reference (targets Slot)."""
        member = self.get_member("_alwaysOnFacetRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @always_on_facet_root.setter
    def always_on_facet_root(self, target: str | Slot | None) -> None:
        """Set the _alwaysOnFacetRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_alwaysOnFacetRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_alwaysOnFacetRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def screens_workspace(self) -> str | None:
        """Target ID of the _screensWorkspace reference (targets Workspace)."""
        member = self.get_member("_screensWorkspace")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @screens_workspace.setter
    def screens_workspace(self, target: str | Workspace | None) -> None:
        """Set the _screensWorkspace reference by target ID or Workspace instance."""
        target_id: str | None = target.id if isinstance(target, Workspace) else target  # type: ignore[assignment]
        member = self.get_member("_screensWorkspace")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_screensWorkspace",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Workspace'),
            )

    @property
    def top_workspace(self) -> str | None:
        """Target ID of the _topWorkspace reference (targets Workspace)."""
        member = self.get_member("_topWorkspace")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @top_workspace.setter
    def top_workspace(self, target: str | Workspace | None) -> None:
        """Set the _topWorkspace reference by target ID or Workspace instance."""
        target_id: str | None = target.id if isinstance(target, Workspace) else target  # type: ignore[assignment]
        member = self.get_member("_topWorkspace")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_topWorkspace",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Workspace'),
            )

    @property
    def notifications(self) -> str | None:
        """Target ID of the _notifications reference (targets NotificationPanel)."""
        member = self.get_member("_notifications")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @notifications.setter
    def notifications(self, target: str | NotificationPanel | None) -> None:
        """Set the _notifications reference by target ID or NotificationPanel instance."""
        target_id: str | None = target.id if isinstance(target, NotificationPanel) else target  # type: ignore[assignment]
        member = self.get_member("_notifications")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_notifications",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.NotificationPanel'),
            )

    @property
    def notifications_root(self) -> str | None:
        """Target ID of the _notificationsRoot reference (targets Slot)."""
        member = self.get_member("_notificationsRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @notifications_root.setter
    def notifications_root(self, target: str | Slot | None) -> None:
        """Set the _notificationsRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_notificationsRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_notificationsRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def notifications_holder(self) -> str | None:
        """Target ID of the _notificationsHolder reference (targets Slot)."""
        member = self.get_member("_notificationsHolder")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @notifications_holder.setter
    def notifications_holder(self, target: str | Slot | None) -> None:
        """Set the _notificationsHolder reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_notificationsHolder")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_notificationsHolder",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    async def setup_default_screens(self, resolink: protocols.ResoniteLinkClient, root: str, debug: bool = False) -> dict:
        """Call the SetupDefaultScreens sync method.

        Args:
            resolink: Connected ResoniteLink client.
            root: The root parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetupDefaultScreens", {"root": root}, debug,
        )

