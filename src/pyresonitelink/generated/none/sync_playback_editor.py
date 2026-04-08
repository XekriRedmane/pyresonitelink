"""Generated component: SyncPlaybackEditor."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync_playback import SyncPlayback
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.float_text_editor_parser import FloatTextEditorParser
from pyresonitelink.generated._types.slider import Slider
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SyncPlaybackEditor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SyncPlaybackEditor.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SyncPlaybackEditor"

    def __init__(self, playback: str | SyncPlayback | None = None, slider_value: str | IField[np.float32] | None = None, loop_toggle_sprite: str | IField[str] | None = None, speed_field: str | FloatTextEditorParser | None = None, slider: str | Slider[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            playback: Initial value for _playback.
            slider_value: Initial value for _sliderValue.
            loop_toggle_sprite: Initial value for _loopToggleSprite.
            speed_field: Initial value for _speedField.
            slider: Initial value for _slider.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if playback is not None:
            self.playback = playback
        if slider_value is not None:
            self.slider_value = slider_value
        if loop_toggle_sprite is not None:
            self.loop_toggle_sprite = loop_toggle_sprite
        if speed_field is not None:
            self.speed_field = speed_field
        if slider is not None:
            self.slider = slider

    @property
    def playback(self) -> str | None:
        """Target ID of the _playback reference (targets SyncPlayback)."""
        member = self.get_member("_playback")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @playback.setter
    def playback(self, target: str | SyncPlayback | None) -> None:
        """Set the _playback reference by target ID or SyncPlayback instance."""
        target_id: str | None = target.id if isinstance(target, SyncPlayback) else target  # type: ignore[assignment]
        member = self.get_member("_playback")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_playback",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncPlayback'),
            )

    @property
    def slider_value(self) -> str | None:
        """Target ID of the _sliderValue reference (targets IField[np.float32])."""
        member = self.get_member("_sliderValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @slider_value.setter
    def slider_value(self, target: str | IField[np.float32] | None) -> None:
        """Set the _sliderValue reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_sliderValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sliderValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def loop_toggle_sprite(self) -> str | None:
        """Target ID of the _loopToggleSprite reference (targets IField[str])."""
        member = self.get_member("_loopToggleSprite")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loop_toggle_sprite.setter
    def loop_toggle_sprite(self, target: str | IField[str] | None) -> None:
        """Set the _loopToggleSprite reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_loopToggleSprite")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_loopToggleSprite",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Uri>'),
            )

    @property
    def speed_field(self) -> str | None:
        """Target ID of the _speedField reference (targets FloatTextEditorParser)."""
        member = self.get_member("_speedField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @speed_field.setter
    def speed_field(self, target: str | FloatTextEditorParser | None) -> None:
        """Set the _speedField reference by target ID or FloatTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, FloatTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("_speedField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_speedField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FloatTextEditorParser'),
            )

    @property
    def slider(self) -> str | None:
        """Target ID of the _slider reference (targets Slider[np.float32])."""
        member = self.get_member("_slider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @slider.setter
    def slider(self, target: str | Slider[np.float32] | None) -> None:
        """Set the _slider reference by target ID or Slider[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, Slider) else target  # type: ignore[assignment]
        member = self.get_member("_slider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_slider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Slider<float>'),
            )

