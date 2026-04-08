"""Generated component: SimplexTurbulentForce."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SimplexTurbulentForce(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.SimplexTurbulentForce.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.SimplexTurbulentForce"

    def __init__(self, strength: primitives.Float | None = None, global_noise_offset: primitives.Float | None = None, scale: primitives.Float3 | None = None, offset: primitives.Float3 | None = None, x_noise_offset: primitives.Float | None = None, y_noise_offset: primitives.Float | None = None, z_noise_offset: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
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
    def mode(self) -> members.FieldEnum | None:
        """The Mode member."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @mode.setter
    def mode(self, value: members.FieldEnum) -> None:
        """Set the Mode member."""
        self.set_member("Mode", value)

    @property
    def strength(self) -> primitives.Float | None:
        """The Strength field value."""
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
        """The GlobalNoiseOffset field value."""
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
        """The Scale field value."""
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
        """The Offset field value."""
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
        """The X_NoiseOffset field value."""
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
        """The Y_NoiseOffset field value."""
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
        """The Z_NoiseOffset field value."""
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

