"""Generated component: LineEmitter."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.particle_system import ParticleSystem
from pyresonitelink.generated._types.iparticle_system_emitter import IParticleSystemEmitter


class LineEmitter(GeneratedComponent, IParticleSystemEmitter):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.LineEmitter.

    Category: Rendering/Particle System/Emitters
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.LineEmitter"

    def __init__(self, system: str | ParticleSystem | None = None, rate: np.float32 | None = None, burst_on_activated_min: np.float32 | None = None, burst_on_activated_max: np.float32 | None = None, burst_on_start: bool | None = None, point0: primitives.Float3 | None = None, point1: primitives.Float3 | None = None, color0: primitives.ColorX | None = None, color1: primitives.ColorX | None = None, direction0: primitives.Float3 | None = None, direction1: primitives.Float3 | None = None, up_direction: primitives.Float3 | None = None, random_direction_weight: np.float32 | None = None, direction_post_transform: primitives.Float3x3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            system: Initial value for System.
            rate: Initial value for Rate.
            burst_on_activated_min: Initial value for BurstOnActivatedMin.
            burst_on_activated_max: Initial value for BurstOnActivatedMax.
            burst_on_start: Initial value for BurstOnStart.
            point0: Initial value for Point0.
            point1: Initial value for Point1.
            color0: Initial value for Color0.
            color1: Initial value for Color1.
            direction0: Initial value for Direction0.
            direction1: Initial value for Direction1.
            up_direction: Initial value for UpDirection.
            random_direction_weight: Initial value for RandomDirectionWeight.
            direction_post_transform: Initial value for DirectionPostTransform.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if system is not None:
            self.system = system
        if rate is not None:
            self.rate = rate
        if burst_on_activated_min is not None:
            self.burst_on_activated_min = burst_on_activated_min
        if burst_on_activated_max is not None:
            self.burst_on_activated_max = burst_on_activated_max
        if burst_on_start is not None:
            self.burst_on_start = burst_on_start
        if point0 is not None:
            self.point0 = point0
        if point1 is not None:
            self.point1 = point1
        if color0 is not None:
            self.color0 = color0
        if color1 is not None:
            self.color1 = color1
        if direction0 is not None:
            self.direction0 = direction0
        if direction1 is not None:
            self.direction1 = direction1
        if up_direction is not None:
            self.up_direction = up_direction
        if random_direction_weight is not None:
            self.random_direction_weight = random_direction_weight
        if direction_post_transform is not None:
            self.direction_post_transform = direction_post_transform

    @property
    def system(self) -> str | None:
        """Target ID of the System reference (targets ParticleSystem)."""
        member = self.get_member("System")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @system.setter
    def system(self, target: str | ParticleSystem | None) -> None:
        """Set the System reference by target ID or ParticleSystem instance."""
        target_id: str | None = target.id if isinstance(target, ParticleSystem) else target  # type: ignore[assignment]
        member = self.get_member("System")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "System",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PhotonDust.ParticleSystem'),
            )

    @property
    def rate(self) -> np.float32 | None:
        """The Rate field value."""
        member = self.get_member("Rate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rate.setter
    def rate(self, value: np.float32) -> None:
        """Set the Rate field value."""
        member = self.get_member("Rate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Rate", fields.FieldFloat(value=value)
            )

    @property
    def burst_on_activated_min(self) -> np.float32 | None:
        """The BurstOnActivatedMin field value."""
        member = self.get_member("BurstOnActivatedMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @burst_on_activated_min.setter
    def burst_on_activated_min(self, value: np.float32) -> None:
        """Set the BurstOnActivatedMin field value."""
        member = self.get_member("BurstOnActivatedMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BurstOnActivatedMin", fields.FieldFloat(value=value)
            )

    @property
    def burst_on_activated_max(self) -> np.float32 | None:
        """The BurstOnActivatedMax field value."""
        member = self.get_member("BurstOnActivatedMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @burst_on_activated_max.setter
    def burst_on_activated_max(self, value: np.float32) -> None:
        """Set the BurstOnActivatedMax field value."""
        member = self.get_member("BurstOnActivatedMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BurstOnActivatedMax", fields.FieldFloat(value=value)
            )

    @property
    def burst_on_start(self) -> bool | None:
        """The BurstOnStart field value."""
        member = self.get_member("BurstOnStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @burst_on_start.setter
    def burst_on_start(self, value: bool) -> None:
        """Set the BurstOnStart field value."""
        member = self.get_member("BurstOnStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BurstOnStart", fields.FieldBool(value=value)
            )

    @property
    def point0(self) -> primitives.Float3 | None:
        """The Point0 field value."""
        member = self.get_member("Point0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @point0.setter
    def point0(self, value: primitives.Float3) -> None:
        """Set the Point0 field value."""
        member = self.get_member("Point0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Point0", fields.FieldFloat3(value=value)
            )

    @property
    def point1(self) -> primitives.Float3 | None:
        """The Point1 field value."""
        member = self.get_member("Point1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @point1.setter
    def point1(self, value: primitives.Float3) -> None:
        """Set the Point1 field value."""
        member = self.get_member("Point1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Point1", fields.FieldFloat3(value=value)
            )

    @property
    def color0(self) -> primitives.ColorX | None:
        """The Color0 field value."""
        member = self.get_member("Color0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color0.setter
    def color0(self, value: primitives.ColorX) -> None:
        """Set the Color0 field value."""
        member = self.get_member("Color0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Color0", fields.FieldColorX(value=value)
            )

    @property
    def color1(self) -> primitives.ColorX | None:
        """The Color1 field value."""
        member = self.get_member("Color1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color1.setter
    def color1(self, value: primitives.ColorX) -> None:
        """Set the Color1 field value."""
        member = self.get_member("Color1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Color1", fields.FieldColorX(value=value)
            )

    @property
    def direction_mode(self) -> members.FieldEnum | None:
        """The DirectionMode member."""
        member = self.get_member("DirectionMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @direction_mode.setter
    def direction_mode(self, value: members.FieldEnum) -> None:
        """Set the DirectionMode member."""
        self.set_member("DirectionMode", value)

    @property
    def direction0(self) -> primitives.Float3 | None:
        """The Direction0 field value."""
        member = self.get_member("Direction0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @direction0.setter
    def direction0(self, value: primitives.Float3) -> None:
        """Set the Direction0 field value."""
        member = self.get_member("Direction0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Direction0", fields.FieldFloat3(value=value)
            )

    @property
    def direction1(self) -> primitives.Float3 | None:
        """The Direction1 field value."""
        member = self.get_member("Direction1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @direction1.setter
    def direction1(self, value: primitives.Float3) -> None:
        """Set the Direction1 field value."""
        member = self.get_member("Direction1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Direction1", fields.FieldFloat3(value=value)
            )

    @property
    def up_direction(self) -> primitives.Float3 | None:
        """The UpDirection field value."""
        member = self.get_member("UpDirection")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @up_direction.setter
    def up_direction(self, value: primitives.Float3) -> None:
        """Set the UpDirection field value."""
        member = self.get_member("UpDirection")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UpDirection", fields.FieldFloat3(value=value)
            )

    @property
    def random_direction_weight(self) -> np.float32 | None:
        """The RandomDirectionWeight field value."""
        member = self.get_member("RandomDirectionWeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @random_direction_weight.setter
    def random_direction_weight(self, value: np.float32) -> None:
        """Set the RandomDirectionWeight field value."""
        member = self.get_member("RandomDirectionWeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RandomDirectionWeight", fields.FieldFloat(value=value)
            )

    @property
    def direction_post_transform(self) -> primitives.Float3x3 | None:
        """The DirectionPostTransform field value."""
        member = self.get_member("DirectionPostTransform")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @direction_post_transform.setter
    def direction_post_transform(self, value: primitives.Float3x3) -> None:
        """Set the DirectionPostTransform field value."""
        member = self.get_member("DirectionPostTransform")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DirectionPostTransform", fields.FieldFloat3x3(value=value)
            )

