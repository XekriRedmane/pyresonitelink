"""Generated component: InteractiveCameraUserControl."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.canvas import Canvas
from pyresonitelink.generated._types.legacy_panel import LegacyPanel
from pyresonitelink.generated._types.interactive_camera_control import InteractiveCameraControl
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InteractiveCameraUserControl(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.InteractiveCameraUserControl.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraUserControl"

    def __init__(self, canvas: str | Canvas | None = None, panel: str | LegacyPanel | None = None, control: str | InteractiveCameraControl | None = None, ui_root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            canvas: Initial value for _canvas.
            panel: Initial value for _panel.
            control: Initial value for Control.
            ui_root: Initial value for _uiRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if canvas is not None:
            self.canvas = canvas
        if panel is not None:
            self.panel = panel
        if control is not None:
            self.control = control
        if ui_root is not None:
            self.ui_root = ui_root

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
    def control(self) -> str | None:
        """Target ID of the Control reference (targets InteractiveCameraControl)."""
        member = self.get_member("Control")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @control.setter
    def control(self, target: str | InteractiveCameraControl | None) -> None:
        """Set the Control reference by target ID or InteractiveCameraControl instance."""
        target_id: str | None = target.id if isinstance(target, InteractiveCameraControl) else target  # type: ignore[assignment]
        member = self.get_member("Control")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Control",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InteractiveCameraControl'),
            )

    @property
    def ui_root(self) -> str | None:
        """Target ID of the _uiRoot reference (targets Slot)."""
        member = self.get_member("_uiRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ui_root.setter
    def ui_root(self, target: str | Slot | None) -> None:
        """Set the _uiRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_uiRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_uiRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

