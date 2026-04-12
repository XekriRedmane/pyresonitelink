"""Generated component: OriginRadialForce."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.radial_force_mode import RadialForceMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OriginRadialForce(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The Origin Radial Force component is used with Photon Dust to make particles have force applied on them to make them return to their original starting point over time. This was a personal addition by Frooxius.

    Category: Rendering/Particle System/Modules

    Used in Photon Dust systems.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.OriginRadialForce"

    def __init__(self, force: primitives.Float | None = None, mode: RadialForceMode | str | None = None, min_distance: primitives.Float | None = None, max_distance: primitives.Float | None = None, min_force: primitives.Float | None = None, max_force: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            force: Initial value for Force.
            mode: Initial value for Mode.
            min_distance: Initial value for MinDistance.
            max_distance: Initial value for MaxDistance.
            min_force: Initial value for MinForce.
            max_force: Initial value for MaxForce.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if force is not None:
            self.force = force
        if mode is not None:
            self.mode = mode
        if min_distance is not None:
            self.min_distance = min_distance
        if max_distance is not None:
            self.max_distance = max_distance
        if min_force is not None:
            self.min_force = min_force
        if max_force is not None:
            self.max_force = max_force

    @property
    def force(self) -> primitives.Float | None:
        """The constant force applied to particles to make them return to where they started."""
        member = self.get_member("Force")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force.setter
    def force(self, value: primitives.Float) -> None:
        """Set the Force field value."""
        member = self.get_member("Force")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Force", fields.FieldFloat(value=value)
            )

    @property
    def mode(self) -> RadialForceMode | None:
        """how the Radial area and effect for this component is defined."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return RadialForceMode(member.value)
        return None

    @mode.setter
    def mode(self, value: RadialForceMode | str) -> None:
        """Set Mode. how the Radial area and effect for this component is defined."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Mode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def min_distance(self) -> primitives.Float | None:
        """The distance from 0 where the minimum force is defined in the force gradient."""
        member = self.get_member("MinDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_distance.setter
    def min_distance(self, value: primitives.Float) -> None:
        """Set the MinDistance field value."""
        member = self.get_member("MinDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinDistance", fields.FieldFloat(value=value)
            )

    @property
    def max_distance(self) -> primitives.Float | None:
        """The distance from 0 where the maximum force is defined in the force gradient."""
        member = self.get_member("MaxDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_distance.setter
    def max_distance(self, value: primitives.Float) -> None:
        """Set the MaxDistance field value."""
        member = self.get_member("MaxDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxDistance", fields.FieldFloat(value=value)
            )

    @property
    def min_force(self) -> primitives.Float | None:
        """The minimum force value for the gradient."""
        member = self.get_member("MinForce")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_force.setter
    def min_force(self, value: primitives.Float) -> None:
        """Set the MinForce field value."""
        member = self.get_member("MinForce")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinForce", fields.FieldFloat(value=value)
            )

    @property
    def max_force(self) -> primitives.Float | None:
        """The maximum force value for the gradient."""
        member = self.get_member("MaxForce")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_force.setter
    def max_force(self, value: primitives.Float) -> None:
        """Set the MaxForce field value."""
        member = self.get_member("MaxForce")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxForce", fields.FieldFloat(value=value)
            )

    @property
    def override_force_space(self) -> members.SyncObject | None:
        """The space to apply forces for this component in."""
        member = self.get_member("OverrideForceSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @override_force_space.setter
    def override_force_space(self, value: members.SyncObject) -> None:
        """Set OverrideForceSpace. The space to apply forces for this component in."""
        self.set_member("OverrideForceSpace", value)

