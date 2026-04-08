"""Generated component: LegacySwapCanvasPanel."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.canvas import Canvas
from pyresonitelink.generated._types.legacy_panel import LegacyPanel
from pyresonitelink.generated._types.rect_transform import RectTransform
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacySwapCanvasPanel(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacySwapCanvasPanel.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacySwapCanvasPanel"

    def __init__(self, canvas: str | Canvas | None = None, panel: str | LegacyPanel | None = None, current_panel: str | RectTransform | None = None, container: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            canvas: Initial value for _canvas.
            panel: Initial value for _panel.
            current_panel: Initial value for _currentPanel.
            container: Initial value for _container.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if canvas is not None:
            self.canvas = canvas
        if panel is not None:
            self.panel = panel
        if current_panel is not None:
            self.current_panel = current_panel
        if container is not None:
            self.container = container

    @property
    def canvas(self) -> str | None:
        """Target ID of the _canvas reference (targets Canvas)."""
        member = self.get_member("_canvas")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @canvas.setter
    def canvas(self, target: str | Canvas | None) -> None:
        """Set the _canvas reference by target ID or Canvas instance."""
        target_id: str | None = target.id if isinstance(target, Canvas) else target  # type: ignore[assignment]
        member = self.get_member("_canvas")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_canvas",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Canvas'),
            )

    @property
    def panel(self) -> str | None:
        """Target ID of the _panel reference (targets LegacyPanel)."""
        member = self.get_member("_panel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @panel.setter
    def panel(self, target: str | LegacyPanel | None) -> None:
        """Set the _panel reference by target ID or LegacyPanel instance."""
        target_id: str | None = target.id if isinstance(target, LegacyPanel) else target  # type: ignore[assignment]
        member = self.get_member("_panel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_panel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyPanel'),
            )

    @property
    def current_panel(self) -> str | None:
        """Target ID of the _currentPanel reference (targets RectTransform)."""
        member = self.get_member("_currentPanel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_panel.setter
    def current_panel(self, target: str | RectTransform | None) -> None:
        """Set the _currentPanel reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("_currentPanel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentPanel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def container(self) -> str | None:
        """Target ID of the _container reference (targets Slot)."""
        member = self.get_member("_container")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @container.setter
    def container(self, target: str | Slot | None) -> None:
        """Set the _container reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_container")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_container",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

