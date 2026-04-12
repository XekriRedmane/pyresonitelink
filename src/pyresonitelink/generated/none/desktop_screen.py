"""Generated component: DesktopScreen."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.canvas import Canvas
from pyresonitelink.generated._types.modal_overlay_manager import ModalOverlayManager
from pyresonitelink.generated._types.radiant_dash_button import RadiantDashButton
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DesktopScreen(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DesktopScreen component is used to make the behavior of the desktop tab on the Dash Menu.

    Used in the dash menu. Not used by the user directly.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DesktopScreen"

    def __init__(self, icon: str | None = None, active_color: primitives.ColorX | None = None, label: primitives.String | None = None, screen_enabled: primitives.Bool | None = None, base_resolution: primitives.Float2 | None = None, screen_root: str | Slot | None = None, screen_canvas: str | Canvas | None = None, modal_overlay_manager: str | ModalOverlayManager | None = None, button: str | RadiantDashButton | None = None, icon_texture: str | IAssetProvider[Texture2D] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            icon: Initial value for Icon.
            active_color: Initial value for ActiveColor.
            label: Initial value for Label.
            screen_enabled: Initial value for ScreenEnabled.
            base_resolution: Initial value for BaseResolution.
            screen_root: Initial value for _screenRoot.
            screen_canvas: Initial value for _screenCanvas.
            modal_overlay_manager: Initial value for _modalOverlayManager.
            button: Initial value for _button.
            icon_texture: Initial value for _iconTexture.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if icon is not None:
            self.icon = icon
        if active_color is not None:
            self.active_color = active_color
        if label is not None:
            self.label = label
        if screen_enabled is not None:
            self.screen_enabled = screen_enabled
        if base_resolution is not None:
            self.base_resolution = base_resolution
        if screen_root is not None:
            self.screen_root = screen_root
        if screen_canvas is not None:
            self.screen_canvas = screen_canvas
        if modal_overlay_manager is not None:
            self.modal_overlay_manager = modal_overlay_manager
        if button is not None:
            self.button = button
        if icon_texture is not None:
            self.icon_texture = icon_texture

    @property
    def icon(self) -> str | None:
        """The icon of the dash menu tab."""
        member = self.get_member("Icon")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @icon.setter
    def icon(self, value: str) -> None:
        """Set the Icon field value."""
        member = self.get_member("Icon")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Icon", fields.FieldUri(value=value)
            )

    @property
    def active_color(self) -> primitives.ColorX | None:
        """The color when this dash menu screen tab is selected."""
        member = self.get_member("ActiveColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @active_color.setter
    def active_color(self, value: primitives.ColorX) -> None:
        """Set the ActiveColor field value."""
        member = self.get_member("ActiveColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActiveColor", fields.FieldNullableColorX(value=value)
            )

    @property
    def label(self) -> primitives.String | None:
        """The text for this dash menu Screen tab."""
        member = self.get_member("Label")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @label.setter
    def label(self, value: primitives.String) -> None:
        """Set the Label field value."""
        member = self.get_member("Label")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Label", fields.FieldString(value=value)
            )

    @property
    def screen_enabled(self) -> primitives.Bool | None:
        """Whether the screen is enabled for viewing."""
        member = self.get_member("ScreenEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @screen_enabled.setter
    def screen_enabled(self, value: primitives.Bool) -> None:
        """Set the ScreenEnabled field value."""
        member = self.get_member("ScreenEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScreenEnabled", fields.FieldBool(value=value)
            )

    @property
    def base_resolution(self) -> primitives.Float2 | None:
        """The default resolution of the tab screen."""
        member = self.get_member("BaseResolution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_resolution.setter
    def base_resolution(self, value: primitives.Float2) -> None:
        """Set the BaseResolution field value."""
        member = self.get_member("BaseResolution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseResolution", fields.FieldFloat2(value=value)
            )

    @property
    def screen_root(self) -> str | None:
        """The root slot of the desktop screen view."""
        member = self.get_member("_screenRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @screen_root.setter
    def screen_root(self, target: str | Slot | None) -> None:
        """Set the _screenRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_screenRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_screenRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def screen_canvas(self) -> str | None:
        """The canvas being used for the tab view."""
        member = self.get_member("_screenCanvas")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @screen_canvas.setter
    def screen_canvas(self, target: str | Canvas | None) -> None:
        """Set the _screenCanvas reference by target ID or Canvas instance."""
        target_id: str | None = target.id if isinstance(target, Canvas) else target  # type: ignore[assignment]
        member = self.get_member("_screenCanvas")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_screenCanvas",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Canvas'),
            )

    @property
    def modal_overlay_manager(self) -> str | None:
        """The Overlay manager being used for handling edit mode."""
        member = self.get_member("_modalOverlayManager")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @modal_overlay_manager.setter
    def modal_overlay_manager(self, target: str | ModalOverlayManager | None) -> None:
        """Set the _modalOverlayManager reference by target ID or ModalOverlayManager instance."""
        target_id: str | None = target.id if isinstance(target, ModalOverlayManager) else target  # type: ignore[assignment]
        member = self.get_member("_modalOverlayManager")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_modalOverlayManager",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ModalOverlayManager'),
            )

    @property
    def button(self) -> str | None:
        """The button to select this dash menu screen tab."""
        member = self.get_member("_button")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @button.setter
    def button(self, target: str | RadiantDashButton | None) -> None:
        """Set the _button reference by target ID or RadiantDashButton instance."""
        target_id: str | None = target.id if isinstance(target, RadiantDashButton) else target  # type: ignore[assignment]
        member = self.get_member("_button")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_button",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RadiantDashButton'),
            )

    @property
    def icon_texture(self) -> str | None:
        """The texture being used for the icon of this dash menu tab."""
        member = self.get_member("_iconTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @icon_texture.setter
    def icon_texture(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the _iconTexture reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_iconTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_iconTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

