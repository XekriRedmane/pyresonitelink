"""Generated component: ColorBySpeedMinMaxHSV."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorBySpeedMinMaxHSV(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The Color By Speed Min Max HSV component changes the HSV values of particles in a particle system depending on their speed.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ColorBySpeedMinMaxHSV"

    def __init__(self, min_speed: primitives.Float | None = None, max_speed: primitives.Float | None = None, min_hue: primitives.Float | None = None, max_hue: primitives.Float | None = None, min_saturation: primitives.Float | None = None, max_saturation: primitives.Float | None = None, min_value: primitives.Float | None = None, max_value: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            min_speed: Initial value for MinSpeed.
            max_speed: Initial value for MaxSpeed.
            min_hue: Initial value for MinHue.
            max_hue: Initial value for MaxHue.
            min_saturation: Initial value for MinSaturation.
            max_saturation: Initial value for MaxSaturation.
            min_value: Initial value for MinValue.
            max_value: Initial value for MaxValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if min_speed is not None:
            self.min_speed = min_speed
        if max_speed is not None:
            self.max_speed = max_speed
        if min_hue is not None:
            self.min_hue = min_hue
        if max_hue is not None:
            self.max_hue = max_hue
        if min_saturation is not None:
            self.min_saturation = min_saturation
        if max_saturation is not None:
            self.max_saturation = max_saturation
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value

    @property
    def min_speed(self) -> primitives.Float | None:
        """The speed the particle has to be be traveling at or under to be considered minimum speed."""
        member = self.get_member("MinSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_speed.setter
    def min_speed(self, value: primitives.Float) -> None:
        """Set the MinSpeed field value."""
        member = self.get_member("MinSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinSpeed", fields.FieldFloat(value=value)
            )

    @property
    def max_speed(self) -> primitives.Float | None:
        """The speed the particle has to be be traveling at or above to be considered maximum speed."""
        member = self.get_member("MaxSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_speed.setter
    def max_speed(self, value: primitives.Float) -> None:
        """Set the MaxSpeed field value."""
        member = self.get_member("MaxSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSpeed", fields.FieldFloat(value=value)
            )

    @property
    def min_hue(self) -> primitives.Float | None:
        """The Hue to display when traveling at or below ``MinSpeed``."""
        member = self.get_member("MinHue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_hue.setter
    def min_hue(self, value: primitives.Float) -> None:
        """Set the MinHue field value."""
        member = self.get_member("MinHue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinHue", fields.FieldFloat(value=value)
            )

    @property
    def max_hue(self) -> primitives.Float | None:
        """The Hue to display when traveling at or above ``MaxSpeed``"""
        member = self.get_member("MaxHue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_hue.setter
    def max_hue(self, value: primitives.Float) -> None:
        """Set the MaxHue field value."""
        member = self.get_member("MaxHue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxHue", fields.FieldFloat(value=value)
            )

    @property
    def min_saturation(self) -> primitives.Float | None:
        """The Saturation to display when traveling at or below ``MinSpeed``."""
        member = self.get_member("MinSaturation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_saturation.setter
    def min_saturation(self, value: primitives.Float) -> None:
        """Set the MinSaturation field value."""
        member = self.get_member("MinSaturation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinSaturation", fields.FieldFloat(value=value)
            )

    @property
    def max_saturation(self) -> primitives.Float | None:
        """The Saturation to display when traveling at or above ``MaxSpeed``"""
        member = self.get_member("MaxSaturation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_saturation.setter
    def max_saturation(self, value: primitives.Float) -> None:
        """Set the MaxSaturation field value."""
        member = self.get_member("MaxSaturation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSaturation", fields.FieldFloat(value=value)
            )

    @property
    def min_value(self) -> primitives.Float | None:
        """The Value to display when traveling at or below ``MinSpeed``."""
        member = self.get_member("MinValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_value.setter
    def min_value(self, value: primitives.Float) -> None:
        """Set the MinValue field value."""
        member = self.get_member("MinValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinValue", fields.FieldFloat(value=value)
            )

    @property
    def max_value(self) -> primitives.Float | None:
        """The Value to display when traveling at or above ``MaxSpeed``"""
        member = self.get_member("MaxValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_value.setter
    def max_value(self, value: primitives.Float) -> None:
        """Set the MaxValue field value."""
        member = self.get_member("MaxValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxValue", fields.FieldFloat(value=value)
            )

