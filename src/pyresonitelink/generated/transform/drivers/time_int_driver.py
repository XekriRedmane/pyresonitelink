"""Generated component: TimeIntDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TimeIntDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The TimeIntDriver Component drives the Int value specified in ``Target`` based on the current time, modified by the specified parameters.

    Category: Transform/Drivers

    **Related Components**: * AtlasInfo
* TimeIntDriver
* UVAtlasAnimator
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TimeIntDriver"

    def __init__(self, scale: primitives.Float | None = None, repeat: primitives.Int | None = None, ping_pong: primitives.Bool | None = None, target: str | IField[primitives.Int] | None = None, *, component: workers.Component | None = None) -> None:
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
    def scale(self) -> primitives.Float | None:
        """Time scale in relation to time in seconds, where 1.0 means ``Target`` will increment once per second."""
        member = self.get_member("Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale.setter
    def scale(self, value: primitives.Float) -> None:
        """Set the Scale field value."""
        member = self.get_member("Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Scale", fields.FieldFloat(value=value)
            )

    @property
    def repeat(self) -> primitives.Int | None:
        """Once ``Target`` reaches this value, it will reset to 0 and restart."""
        member = self.get_member("Repeat")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @repeat.setter
    def repeat(self, value: primitives.Int) -> None:
        """Set the Repeat field value."""
        member = self.get_member("Repeat")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Repeat", fields.FieldInt(value=value)
            )

    @property
    def ping_pong(self) -> primitives.Bool | None:
        """Causes ``Target`` to reverse direction when it reaches 0 or the value in ``Repeat``, instead of restarting."""
        member = self.get_member("PingPong")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ping_pong.setter
    def ping_pong(self, value: primitives.Bool) -> None:
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
        """The value to be driven."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

