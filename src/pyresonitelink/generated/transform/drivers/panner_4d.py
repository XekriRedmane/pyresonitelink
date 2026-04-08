"""Generated component: Panner4D."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Panner4D(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Panner4D.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Panner4D"

    def __init__(self, target: str | IField[primitives.Float4] | None = None, offset: primitives.Float4 | None = None, pre_offset: primitives.Float4 | None = None, speed: primitives.Float4 | None = None, repeat: primitives.Float4 | None = None, ping_pong: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for _target.
            offset: Initial value for _offset.
            pre_offset: Initial value for _preOffset.
            speed: Initial value for _speed.
            repeat: Initial value for _repeat.
            ping_pong: Initial value for PingPong.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if offset is not None:
            self.offset = offset
        if pre_offset is not None:
            self.pre_offset = pre_offset
        if speed is not None:
            self.speed = speed
        if repeat is not None:
            self.repeat = repeat
        if ping_pong is not None:
            self.ping_pong = ping_pong

    @property
    def target(self) -> str | None:
        """Target ID of the _target reference (targets IField[primitives.Float4])."""
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.Float4] | None) -> None:
        """Set the _target reference by target ID or IField[primitives.Float4] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float4>'),
            )

    @property
    def offset(self) -> primitives.Float4 | None:
        """The _offset field value."""
        member = self.get_member("_offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float4) -> None:
        """Set the _offset field value."""
        member = self.get_member("_offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_offset", fields.FieldFloat4(value=value)
            )

    @property
    def pre_offset(self) -> primitives.Float4 | None:
        """The _preOffset field value."""
        member = self.get_member("_preOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pre_offset.setter
    def pre_offset(self, value: primitives.Float4) -> None:
        """Set the _preOffset field value."""
        member = self.get_member("_preOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_preOffset", fields.FieldFloat4(value=value)
            )

    @property
    def speed(self) -> primitives.Float4 | None:
        """The _speed field value."""
        member = self.get_member("_speed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @speed.setter
    def speed(self, value: primitives.Float4) -> None:
        """Set the _speed field value."""
        member = self.get_member("_speed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_speed", fields.FieldFloat4(value=value)
            )

    @property
    def repeat(self) -> primitives.Float4 | None:
        """The _repeat field value."""
        member = self.get_member("_repeat")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @repeat.setter
    def repeat(self, value: primitives.Float4) -> None:
        """Set the _repeat field value."""
        member = self.get_member("_repeat")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_repeat", fields.FieldFloat4(value=value)
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

