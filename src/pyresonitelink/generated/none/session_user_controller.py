"""Generated component: SessionUserController."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.slider import Slider
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SessionUserController(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SessionUserController.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SessionUserController"

    def __init__(self, name: str | Text | None = None, slider: str | Slider[np.float32] | None = None, mute: str | Button | None = None, jump: str | Button | None = None, respawn: str | Button | None = None, silence: str | Button | None = None, kick: str | Button | None = None, ban: str | Button | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            name: Initial value for _name.
            slider: Initial value for _slider.
            mute: Initial value for _mute.
            jump: Initial value for _jump.
            respawn: Initial value for _respawn.
            silence: Initial value for _silence.
            kick: Initial value for _kick.
            ban: Initial value for _ban.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if name is not None:
            self.name = name
        if slider is not None:
            self.slider = slider
        if mute is not None:
            self.mute = mute
        if jump is not None:
            self.jump = jump
        if respawn is not None:
            self.respawn = respawn
        if silence is not None:
            self.silence = silence
        if kick is not None:
            self.kick = kick
        if ban is not None:
            self.ban = ban

    @property
    def name(self) -> str | None:
        """Target ID of the _name reference (targets Text)."""
        member = self.get_member("_name")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @name.setter
    def name(self, target: str | Text | None) -> None:
        """Set the _name reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_name")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_name",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
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

    @property
    def mute(self) -> str | None:
        """Target ID of the _mute reference (targets Button)."""
        member = self.get_member("_mute")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mute.setter
    def mute(self, target: str | Button | None) -> None:
        """Set the _mute reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_mute")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_mute",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def jump(self) -> str | None:
        """Target ID of the _jump reference (targets Button)."""
        member = self.get_member("_jump")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @jump.setter
    def jump(self, target: str | Button | None) -> None:
        """Set the _jump reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_jump")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_jump",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def respawn(self) -> str | None:
        """Target ID of the _respawn reference (targets Button)."""
        member = self.get_member("_respawn")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @respawn.setter
    def respawn(self, target: str | Button | None) -> None:
        """Set the _respawn reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_respawn")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_respawn",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def silence(self) -> str | None:
        """Target ID of the _silence reference (targets Button)."""
        member = self.get_member("_silence")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @silence.setter
    def silence(self, target: str | Button | None) -> None:
        """Set the _silence reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_silence")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_silence",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def kick(self) -> str | None:
        """Target ID of the _kick reference (targets Button)."""
        member = self.get_member("_kick")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @kick.setter
    def kick(self, target: str | Button | None) -> None:
        """Set the _kick reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_kick")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_kick",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def ban(self) -> str | None:
        """Target ID of the _ban reference (targets Button)."""
        member = self.get_member("_ban")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ban.setter
    def ban(self, target: str | Button | None) -> None:
        """Set the _ban reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_ban")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_ban",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

