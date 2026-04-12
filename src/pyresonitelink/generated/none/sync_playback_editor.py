"""Generated component: SyncPlaybackEditor."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync_playback import SyncPlayback
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.float_text_editor_parser import FloatTextEditorParser
from pyresonitelink.generated._types.slider import Slider
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SyncPlaybackEditor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The SyncPlaybackEditor component is used to interact with and modify the playback of a Sync playback like a video, animation, or a sound player.

    Used commonly in inspectors and video players to allow interaction with
    playback fields directly.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SyncPlaybackEditor"

    def __init__(self, playback: str | SyncPlayback | None = None, slider_value: str | IField[primitives.Float] | None = None, loop_toggle_sprite: str | IField[str] | None = None, speed_field: str | FloatTextEditorParser | None = None, slider: str | Slider[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
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
        """The playback to edit and influence with this component."""
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
        """The field to drive with the current playback of ``_playback``"""
        member = self.get_member("_sliderValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @slider_value.setter
    def slider_value(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _sliderValue reference by target ID or IField[primitives.Float] instance."""
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
        """The sprite URI field of the toggle loop button. Used to switch between a loop and a play once icon URI."""
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
        """The field used to change the speed of the playback of ``_playback``"""
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
        """The slider used to change the play head/position of ``_playback``."""
        member = self.get_member("_slider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @slider.setter
    def slider(self, target: str | Slider[primitives.Float] | None) -> None:
        """Set the _slider reference by target ID or Slider[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, Slider) else target  # type: ignore[assignment]
        member = self.get_member("_slider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_slider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Slider<float>'),
            )

