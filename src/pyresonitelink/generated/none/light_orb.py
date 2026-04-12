"""Generated component: LightOrb."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.light import Light
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LightOrb(GeneratedComponent, ITouchable, IWorldEventReceiver):
    """The Light Orb component is used as a visual for lights created by the Light Tool.

    Not used directly by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LightOrb"

    def __init__(self, flip_on_touch: primitives.Bool | None = None, light: str | Light | None = None, emission_color: str | IField[primitives.ColorX] | None = None, accept_physical_touch: primitives.Bool | None = None, accept_remote_touch: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            flip_on_touch: Initial value for FlipOnTouch.
            light: Initial value for Light.
            emission_color: Initial value for EmissionColor.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if flip_on_touch is not None:
            self.flip_on_touch = flip_on_touch
        if light is not None:
            self.light = light
        if emission_color is not None:
            self.emission_color = emission_color
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch

    @property
    def flip_on_touch(self) -> primitives.Bool | None:
        """Whether this can be toggled by touching a collider on the same slot."""
        member = self.get_member("FlipOnTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flip_on_touch.setter
    def flip_on_touch(self, value: primitives.Bool) -> None:
        """Set the FlipOnTouch field value."""
        member = self.get_member("FlipOnTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FlipOnTouch", fields.FieldBool(value=value)
            )

    @property
    def light(self) -> str | None:
        """The light to control."""
        member = self.get_member("Light")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @light.setter
    def light(self, target: str | Light | None) -> None:
        """Set the Light reference by target ID or Light instance."""
        target_id: str | None = target.id if isinstance(target, Light) else target  # type: ignore[assignment]
        member = self.get_member("Light")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Light",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Light'),
            )

    @property
    def emission_color(self) -> str | None:
        """The field to drive to control the emission color of the light."""
        member = self.get_member("EmissionColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @emission_color.setter
    def emission_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the EmissionColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("EmissionColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EmissionColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def accept_physical_touch(self) -> primitives.Bool | None:
        """The AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_physical_touch.setter
    def accept_physical_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptPhysicalTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_remote_touch(self) -> primitives.Bool | None:
        """The AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_remote_touch.setter
    def accept_remote_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptRemoteTouch", fields.FieldBool(value=value)
            )

