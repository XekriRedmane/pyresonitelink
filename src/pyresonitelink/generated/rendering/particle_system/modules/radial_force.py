"""Generated component: RadialForce."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RadialForce(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.RadialForce.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.RadialForce"

    def __init__(self, force: primitives.Float | None = None, min_distance: primitives.Float | None = None, max_distance: primitives.Float | None = None, min_force: primitives.Float | None = None, max_force: primitives.Float | None = None, center: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            force: Initial value for Force.
            min_distance: Initial value for MinDistance.
            max_distance: Initial value for MaxDistance.
            min_force: Initial value for MinForce.
            max_force: Initial value for MaxForce.
            center: Initial value for Center.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if force is not None:
            self.force = force
        if min_distance is not None:
            self.min_distance = min_distance
        if max_distance is not None:
            self.max_distance = max_distance
        if min_force is not None:
            self.min_force = min_force
        if max_force is not None:
            self.max_force = max_force
        if center is not None:
            self.center = center

    @property
    def force(self) -> primitives.Float | None:
        """The Force field value."""
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
    def min_distance(self) -> primitives.Float | None:
        """The MinDistance field value."""
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
        """The MaxDistance field value."""
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
        """The MinForce field value."""
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
        """The MaxForce field value."""
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
        """The OverrideForceSpace member."""
        member = self.get_member("OverrideForceSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @override_force_space.setter
    def override_force_space(self, value: members.SyncObject) -> None:
        """Set the OverrideForceSpace member."""
        self.set_member("OverrideForceSpace", value)

    @property
    def center(self) -> primitives.Float3 | None:
        """The Center field value."""
        member = self.get_member("Center")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @center.setter
    def center(self, value: primitives.Float3) -> None:
        """Set the Center field value."""
        member = self.get_member("Center")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Center", fields.FieldFloat3(value=value)
            )

