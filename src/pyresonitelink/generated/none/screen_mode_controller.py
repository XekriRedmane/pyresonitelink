"""Generated component: ScreenModeController."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.userspace_radiant_dash import UserspaceRadiantDash
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.audio_clip import AudioClip
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ScreenModeController(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ScreenModeController.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ScreenModeController"

    def __init__(self, dash: str | UserspaceRadiantDash | None = None, mute_sound: str | IAssetProvider[AudioClip] | None = None, unmute_sound: str | IAssetProvider[AudioClip] | None = None, start_talk_sound: str | IAssetProvider[AudioClip] | None = None, stop_talk_sound: str | IAssetProvider[AudioClip] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            dash: Initial value for _dash.
            mute_sound: Initial value for _muteSound.
            unmute_sound: Initial value for _unmuteSound.
            start_talk_sound: Initial value for _startTalkSound.
            stop_talk_sound: Initial value for _stopTalkSound.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if dash is not None:
            self.dash = dash
        if mute_sound is not None:
            self.mute_sound = mute_sound
        if unmute_sound is not None:
            self.unmute_sound = unmute_sound
        if start_talk_sound is not None:
            self.start_talk_sound = start_talk_sound
        if stop_talk_sound is not None:
            self.stop_talk_sound = stop_talk_sound

    @property
    def dash(self) -> str | None:
        """Target ID of the _dash reference (targets UserspaceRadiantDash)."""
        member = self.get_member("_dash")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @dash.setter
    def dash(self, target: str | UserspaceRadiantDash | None) -> None:
        """Set the _dash reference by target ID or UserspaceRadiantDash instance."""
        target_id: str | None = target.id if isinstance(target, UserspaceRadiantDash) else target  # type: ignore[assignment]
        member = self.get_member("_dash")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_dash",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UserspaceRadiantDash'),
            )

    @property
    def mute_sound(self) -> str | None:
        """Target ID of the _muteSound reference (targets IAssetProvider[AudioClip])."""
        member = self.get_member("_muteSound")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mute_sound.setter
    def mute_sound(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the _muteSound reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_muteSound")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_muteSound",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

    @property
    def unmute_sound(self) -> str | None:
        """Target ID of the _unmuteSound reference (targets IAssetProvider[AudioClip])."""
        member = self.get_member("_unmuteSound")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @unmute_sound.setter
    def unmute_sound(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the _unmuteSound reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_unmuteSound")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_unmuteSound",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

    @property
    def start_talk_sound(self) -> str | None:
        """Target ID of the _startTalkSound reference (targets IAssetProvider[AudioClip])."""
        member = self.get_member("_startTalkSound")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @start_talk_sound.setter
    def start_talk_sound(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the _startTalkSound reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_startTalkSound")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_startTalkSound",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

    @property
    def stop_talk_sound(self) -> str | None:
        """Target ID of the _stopTalkSound reference (targets IAssetProvider[AudioClip])."""
        member = self.get_member("_stopTalkSound")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stop_talk_sound.setter
    def stop_talk_sound(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the _stopTalkSound reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_stopTalkSound")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_stopTalkSound",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

