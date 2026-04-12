"""Generated component: SimplexTurbulentForce."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.force_mode import ForceMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SimplexTurbulentForce(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The SimplexTurbulentForce component is used to make random noise throughout an entire particle system that affects particles moving through it by changing their movement.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.SimplexTurbulentForce"

    def __init__(self, mode: ForceMode | str | None = None, strength: primitives.Float | None = None, global_noise_offset: primitives.Float | None = None, scale: primitives.Float3 | None = None, offset: primitives.Float3 | None = None, x_noise_offset: primitives.Float | None = None, y_noise_offset: primitives.Float | None = None, z_noise_offset: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            mode: Initial value for Mode.
            strength: Initial value for Strength.
            global_noise_offset: Initial value for GlobalNoiseOffset.
            scale: Initial value for Scale.
            offset: Initial value for Offset.
            x_noise_offset: Initial value for X_NoiseOffset.
            y_noise_offset: Initial value for Y_NoiseOffset.
            z_noise_offset: Initial value for Z_NoiseOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if mode is not None:
            self.mode = mode
        if strength is not None:
            self.strength = strength
        if global_noise_offset is not None:
            self.global_noise_offset = global_noise_offset
        if scale is not None:
            self.scale = scale
        if offset is not None:
            self.offset = offset
        if x_noise_offset is not None:
            self.x_noise_offset = x_noise_offset
        if y_noise_offset is not None:
            self.y_noise_offset = y_noise_offset
        if z_noise_offset is not None:
            self.z_noise_offset = z_noise_offset

    @property
    def mode(self) -> ForceMode | None:
        """How to affect Particles in terms of force."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ForceMode(member.value)
        return None

    @mode.setter
    def mode(self, value: ForceMode | str) -> None:
        """Set Mode. How to affect Particles in terms of force."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Mode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def strength(self) -> primitives.Float | None:
        """How strong is the force effect."""
        member = self.get_member("Strength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @strength.setter
    def strength(self, value: primitives.Float) -> None:
        """Set the Strength field value."""
        member = self.get_member("Strength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Strength", fields.FieldFloat(value=value)
            )

    @property
    def global_noise_offset(self) -> primitives.Float | None:
        """The 4th dimensional offset of the noise. Essentially a seed."""
        member = self.get_member("GlobalNoiseOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @global_noise_offset.setter
    def global_noise_offset(self, value: primitives.Float) -> None:
        """Set the GlobalNoiseOffset field value."""
        member = self.get_member("GlobalNoiseOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GlobalNoiseOffset", fields.FieldFloat(value=value)
            )

    @property
    def scale(self) -> primitives.Float3 | None:
        """How much to scale up or down the noise from it's center."""
        member = self.get_member("Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale.setter
    def scale(self, value: primitives.Float3) -> None:
        """Set the Scale field value."""
        member = self.get_member("Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Scale", fields.FieldFloat3(value=value)
            )

    @property
    def offset(self) -> primitives.Float3 | None:
        """How much to shift the noise on its axies."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float3) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat3(value=value)
            )

    @property
    def x_noise_offset(self) -> primitives.Float | None:
        """How much to offset the noise on the X axis."""
        member = self.get_member("X_NoiseOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @x_noise_offset.setter
    def x_noise_offset(self, value: primitives.Float) -> None:
        """Set the X_NoiseOffset field value."""
        member = self.get_member("X_NoiseOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "X_NoiseOffset", fields.FieldFloat(value=value)
            )

    @property
    def y_noise_offset(self) -> primitives.Float | None:
        """How much to offset the noise on the Y axis."""
        member = self.get_member("Y_NoiseOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @y_noise_offset.setter
    def y_noise_offset(self, value: primitives.Float) -> None:
        """Set the Y_NoiseOffset field value."""
        member = self.get_member("Y_NoiseOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Y_NoiseOffset", fields.FieldFloat(value=value)
            )

    @property
    def z_noise_offset(self) -> primitives.Float | None:
        """How much to offset the noise on the Z axis."""
        member = self.get_member("Z_NoiseOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @z_noise_offset.setter
    def z_noise_offset(self, value: primitives.Float) -> None:
        """Set the Z_NoiseOffset field value."""
        member = self.get_member("Z_NoiseOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Z_NoiseOffset", fields.FieldFloat(value=value)
            )

