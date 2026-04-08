"""Generated component: TimeIntDriver."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TimeIntDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TimeIntDriver.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TimeIntDriver"

    def __init__(self, scale: np.float32 | None = None, repeat: np.int32 | None = None, ping_pong: bool | None = None, target: str | IField[np.int32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            scale: Initial value for Scale.
            repeat: Initial value for Repeat.
            ping_pong: Initial value for PingPong.
            target: Initial value for Target.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if scale is not None:
            self.scale = scale
        if repeat is not None:
            self.repeat = repeat
        if ping_pong is not None:
            self.ping_pong = ping_pong
        if target is not None:
            self.target = target

    @property
    def scale(self) -> np.float32 | None:
        """The Scale field value."""
        member = self.get_member("Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale.setter
    def scale(self, value: np.float32) -> None:
        """Set the Scale field value."""
        member = self.get_member("Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Scale", fields.FieldFloat(value=value)
            )

    @property
    def repeat(self) -> np.int32 | None:
        """The Repeat field value."""
        member = self.get_member("Repeat")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @repeat.setter
    def repeat(self, value: np.int32) -> None:
        """Set the Repeat field value."""
        member = self.get_member("Repeat")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Repeat", fields.FieldInt(value=value)
            )

    @property
    def ping_pong(self) -> bool | None:
        """The PingPong field value."""
        member = self.get_member("PingPong")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ping_pong.setter
    def ping_pong(self, value: bool) -> None:
        """Set the PingPong field value."""
        member = self.get_member("PingPong")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PingPong", fields.FieldBool(value=value)
            )

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[np.int32])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[np.int32] | None) -> None:
        """Set the Target reference by target ID or IField[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

