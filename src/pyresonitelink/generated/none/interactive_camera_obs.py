"""Generated component: InteractiveCameraOBS."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.canvas import Canvas
from pyresonitelink.generated._types.legacy_panel import LegacyPanel
from pyresonitelink.generated._types.rect_transform import RectTransform
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.interactive_camera_control import InteractiveCameraControl
from pyresonitelink.generated._types.text_field import TextField
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.checkbox import Checkbox
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InteractiveCameraOBS(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.InteractiveCameraOBS.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraOBS"

    def __init__(self, canvas: str | Canvas | None = None, panel: str | LegacyPanel | None = None, current_panel: str | RectTransform | None = None, container: str | Slot | None = None, camera_control: str | InteractiveCameraControl | None = None, connect_address: str | TextField | None = None, connect_password: str | TextField | None = None, status: str | Text | None = None, active: primitives.Bool | None = None, stream_time: str | Text | None = None, bytes_per_sec: str | Text | None = None, fps: str | Text | None = None, dropped_frames: str | Text | None = None, stream_button: str | Button | None = None, record_button: str | Button | None = None, launch_ob_sbutton: str | Button | None = None, auto_mirror: str | Checkbox | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            canvas: Initial value for _canvas.
            panel: Initial value for _panel.
            current_panel: Initial value for _currentPanel.
            container: Initial value for _container.
            camera_control: Initial value for CameraControl.
            connect_address: Initial value for _connectAddress.
            connect_password: Initial value for _connectPassword.
            status: Initial value for _status.
            active: Initial value for _active.
            stream_time: Initial value for _streamTime.
            bytes_per_sec: Initial value for _bytesPerSec.
            fps: Initial value for _fps.
            dropped_frames: Initial value for _droppedFrames.
            stream_button: Initial value for _streamButton.
            record_button: Initial value for _recordButton.
            launch_ob_sbutton: Initial value for _launchOBSbutton.
            auto_mirror: Initial value for _autoMirror.
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
        if camera_control is not None:
            self.camera_control = camera_control
        if connect_address is not None:
            self.connect_address = connect_address
        if connect_password is not None:
            self.connect_password = connect_password
        if status is not None:
            self.status = status
        if active is not None:
            self.active = active
        if stream_time is not None:
            self.stream_time = stream_time
        if bytes_per_sec is not None:
            self.bytes_per_sec = bytes_per_sec
        if fps is not None:
            self.fps = fps
        if dropped_frames is not None:
            self.dropped_frames = dropped_frames
        if stream_button is not None:
            self.stream_button = stream_button
        if record_button is not None:
            self.record_button = record_button
        if launch_ob_sbutton is not None:
            self.launch_ob_sbutton = launch_ob_sbutton
        if auto_mirror is not None:
            self.auto_mirror = auto_mirror

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

    @property
    def camera_control(self) -> str | None:
        """Target ID of the CameraControl reference (targets InteractiveCameraControl)."""
        member = self.get_member("CameraControl")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @camera_control.setter
    def camera_control(self, target: str | InteractiveCameraControl | None) -> None:
        """Set the CameraControl reference by target ID or InteractiveCameraControl instance."""
        target_id: str | None = target.id if isinstance(target, InteractiveCameraControl) else target  # type: ignore[assignment]
        member = self.get_member("CameraControl")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CameraControl",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InteractiveCameraControl'),
            )

    @property
    def connect_address(self) -> str | None:
        """Target ID of the _connectAddress reference (targets TextField)."""
        member = self.get_member("_connectAddress")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @connect_address.setter
    def connect_address(self, target: str | TextField | None) -> None:
        """Set the _connectAddress reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_connectAddress")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_connectAddress",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def connect_password(self) -> str | None:
        """Target ID of the _connectPassword reference (targets TextField)."""
        member = self.get_member("_connectPassword")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @connect_password.setter
    def connect_password(self, target: str | TextField | None) -> None:
        """Set the _connectPassword reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_connectPassword")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_connectPassword",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def status(self) -> str | None:
        """Target ID of the _status reference (targets Text)."""
        member = self.get_member("_status")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @status.setter
    def status(self, target: str | Text | None) -> None:
        """Set the _status reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_status")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_status",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def active(self) -> primitives.Bool | None:
        """The _active field value."""
        member = self.get_member("_active")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @active.setter
    def active(self, value: primitives.Bool) -> None:
        """Set the _active field value."""
        member = self.get_member("_active")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_active", fields.FieldBool(value=value)
            )

    @property
    def stream_time(self) -> str | None:
        """Target ID of the _streamTime reference (targets Text)."""
        member = self.get_member("_streamTime")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stream_time.setter
    def stream_time(self, target: str | Text | None) -> None:
        """Set the _streamTime reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_streamTime")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_streamTime",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def bytes_per_sec(self) -> str | None:
        """Target ID of the _bytesPerSec reference (targets Text)."""
        member = self.get_member("_bytesPerSec")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bytes_per_sec.setter
    def bytes_per_sec(self, target: str | Text | None) -> None:
        """Set the _bytesPerSec reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_bytesPerSec")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_bytesPerSec",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def fps(self) -> str | None:
        """Target ID of the _fps reference (targets Text)."""
        member = self.get_member("_fps")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @fps.setter
    def fps(self, target: str | Text | None) -> None:
        """Set the _fps reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_fps")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_fps",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def dropped_frames(self) -> str | None:
        """Target ID of the _droppedFrames reference (targets Text)."""
        member = self.get_member("_droppedFrames")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @dropped_frames.setter
    def dropped_frames(self, target: str | Text | None) -> None:
        """Set the _droppedFrames reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_droppedFrames")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_droppedFrames",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def stream_button(self) -> str | None:
        """Target ID of the _streamButton reference (targets Button)."""
        member = self.get_member("_streamButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stream_button.setter
    def stream_button(self, target: str | Button | None) -> None:
        """Set the _streamButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_streamButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_streamButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def record_button(self) -> str | None:
        """Target ID of the _recordButton reference (targets Button)."""
        member = self.get_member("_recordButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @record_button.setter
    def record_button(self, target: str | Button | None) -> None:
        """Set the _recordButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_recordButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_recordButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def launch_ob_sbutton(self) -> str | None:
        """Target ID of the _launchOBSbutton reference (targets Button)."""
        member = self.get_member("_launchOBSbutton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @launch_ob_sbutton.setter
    def launch_ob_sbutton(self, target: str | Button | None) -> None:
        """Set the _launchOBSbutton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_launchOBSbutton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_launchOBSbutton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def auto_mirror(self) -> str | None:
        """Target ID of the _autoMirror reference (targets Checkbox)."""
        member = self.get_member("_autoMirror")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @auto_mirror.setter
    def auto_mirror(self, target: str | Checkbox | None) -> None:
        """Set the _autoMirror reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_autoMirror")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_autoMirror",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

