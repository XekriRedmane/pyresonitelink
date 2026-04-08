"""Generated component: InteractiveCameraUserItem."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.interactive_camera_control import InteractiveCameraControl
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.slider import Slider
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InteractiveCameraUserItem(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.InteractiveCameraUserItem.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraUserItem"

    def __init__(self, control: str | InteractiveCameraControl | None = None, username: str | Text | None = None, voice_default: str | Button | None = None, voice_mute: str | Button | None = None, voice_shout: str | Button | None = None, voice_broadcast: str | Button | None = None, group_auto: str | Button | None = None, group_exclude: str | Button | None = None, group_include: str | Button | None = None, camera_operator: str | Button | None = None, framing_target: str | Button | None = None, volume_slider: str | Slider[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            control: Initial value for Control.
            username: Initial value for _username.
            voice_default: Initial value for _voiceDefault.
            voice_mute: Initial value for _voiceMute.
            voice_shout: Initial value for _voiceShout.
            voice_broadcast: Initial value for _voiceBroadcast.
            group_auto: Initial value for _groupAuto.
            group_exclude: Initial value for _groupExclude.
            group_include: Initial value for _groupInclude.
            camera_operator: Initial value for _cameraOperator.
            framing_target: Initial value for _framingTarget.
            volume_slider: Initial value for _volumeSlider.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if control is not None:
            self.control = control
        if username is not None:
            self.username = username
        if voice_default is not None:
            self.voice_default = voice_default
        if voice_mute is not None:
            self.voice_mute = voice_mute
        if voice_shout is not None:
            self.voice_shout = voice_shout
        if voice_broadcast is not None:
            self.voice_broadcast = voice_broadcast
        if group_auto is not None:
            self.group_auto = group_auto
        if group_exclude is not None:
            self.group_exclude = group_exclude
        if group_include is not None:
            self.group_include = group_include
        if camera_operator is not None:
            self.camera_operator = camera_operator
        if framing_target is not None:
            self.framing_target = framing_target
        if volume_slider is not None:
            self.volume_slider = volume_slider

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
    def username(self) -> str | None:
        """Target ID of the _username reference (targets Text)."""
        member = self.get_member("_username")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @username.setter
    def username(self, target: str | Text | None) -> None:
        """Set the _username reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_username")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_username",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def voice_default(self) -> str | None:
        """Target ID of the _voiceDefault reference (targets Button)."""
        member = self.get_member("_voiceDefault")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @voice_default.setter
    def voice_default(self, target: str | Button | None) -> None:
        """Set the _voiceDefault reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_voiceDefault")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_voiceDefault",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def voice_mute(self) -> str | None:
        """Target ID of the _voiceMute reference (targets Button)."""
        member = self.get_member("_voiceMute")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @voice_mute.setter
    def voice_mute(self, target: str | Button | None) -> None:
        """Set the _voiceMute reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_voiceMute")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_voiceMute",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def voice_shout(self) -> str | None:
        """Target ID of the _voiceShout reference (targets Button)."""
        member = self.get_member("_voiceShout")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @voice_shout.setter
    def voice_shout(self, target: str | Button | None) -> None:
        """Set the _voiceShout reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_voiceShout")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_voiceShout",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def voice_broadcast(self) -> str | None:
        """Target ID of the _voiceBroadcast reference (targets Button)."""
        member = self.get_member("_voiceBroadcast")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @voice_broadcast.setter
    def voice_broadcast(self, target: str | Button | None) -> None:
        """Set the _voiceBroadcast reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_voiceBroadcast")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_voiceBroadcast",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def group_auto(self) -> str | None:
        """Target ID of the _groupAuto reference (targets Button)."""
        member = self.get_member("_groupAuto")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @group_auto.setter
    def group_auto(self, target: str | Button | None) -> None:
        """Set the _groupAuto reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_groupAuto")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_groupAuto",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def group_exclude(self) -> str | None:
        """Target ID of the _groupExclude reference (targets Button)."""
        member = self.get_member("_groupExclude")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @group_exclude.setter
    def group_exclude(self, target: str | Button | None) -> None:
        """Set the _groupExclude reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_groupExclude")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_groupExclude",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def group_include(self) -> str | None:
        """Target ID of the _groupInclude reference (targets Button)."""
        member = self.get_member("_groupInclude")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @group_include.setter
    def group_include(self, target: str | Button | None) -> None:
        """Set the _groupInclude reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_groupInclude")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_groupInclude",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def camera_operator(self) -> str | None:
        """Target ID of the _cameraOperator reference (targets Button)."""
        member = self.get_member("_cameraOperator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @camera_operator.setter
    def camera_operator(self, target: str | Button | None) -> None:
        """Set the _cameraOperator reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_cameraOperator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cameraOperator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def framing_target(self) -> str | None:
        """Target ID of the _framingTarget reference (targets Button)."""
        member = self.get_member("_framingTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @framing_target.setter
    def framing_target(self, target: str | Button | None) -> None:
        """Set the _framingTarget reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_framingTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_framingTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def volume_slider(self) -> str | None:
        """Target ID of the _volumeSlider reference (targets Slider[np.float32])."""
        member = self.get_member("_volumeSlider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @volume_slider.setter
    def volume_slider(self, target: str | Slider[np.float32] | None) -> None:
        """Set the _volumeSlider reference by target ID or Slider[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, Slider) else target  # type: ignore[assignment]
        member = self.get_member("_volumeSlider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_volumeSlider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Slider<float>'),
            )

