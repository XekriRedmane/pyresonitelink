"""Generated component: InteractiveCameraControlAnchors."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.canvas import Canvas
from pyresonitelink.generated._types.legacy_panel import LegacyPanel
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.interactive_camera_control import InteractiveCameraControl
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InteractiveCameraControlAnchors(GeneratedComponent, IComponent, IWorldEventReceiver):
    """See Camera.

    See Camera.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraControlAnchors"

    def __init__(self, canvas: str | Canvas | None = None, panel: str | LegacyPanel | None = None, ui_root: str | Slot | None = None, camera_control: str | InteractiveCameraControl | None = None, no_anchor_message: str | Text | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            canvas: Initial value for _canvas.
            panel: Initial value for _panel.
            ui_root: Initial value for _uiRoot.
            camera_control: Initial value for _cameraControl.
            no_anchor_message: Initial value for _noAnchorMessage.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if canvas is not None:
            self.canvas = canvas
        if panel is not None:
            self.panel = panel
        if ui_root is not None:
            self.ui_root = ui_root
        if camera_control is not None:
            self.camera_control = camera_control
        if no_anchor_message is not None:
            self.no_anchor_message = no_anchor_message

    @property
    def canvas(self) -> str | None:
        """The canvas being used to show settings."""
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
        """The legacy panel being used as a base to interact with the settings."""
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
    def ui_root(self) -> str | None:
        """The slot to put UI elements for anchors."""
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

    @property
    def camera_control(self) -> str | None:
        """See Interactive Camera Control."""
        member = self.get_member("_cameraControl")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @camera_control.setter
    def camera_control(self, target: str | InteractiveCameraControl | None) -> None:
        """Set the _cameraControl reference by target ID or InteractiveCameraControl instance."""
        target_id: str | None = target.id if isinstance(target, InteractiveCameraControl) else target  # type: ignore[assignment]
        member = self.get_member("_cameraControl")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cameraControl",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InteractiveCameraControl'),
            )

    @property
    def no_anchor_message(self) -> str | None:
        """The text to fill with the no anchors message."""
        member = self.get_member("_noAnchorMessage")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @no_anchor_message.setter
    def no_anchor_message(self, target: str | Text | None) -> None:
        """Set the _noAnchorMessage reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_noAnchorMessage")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_noAnchorMessage",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

