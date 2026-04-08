"""Generated component: OriginRadialForce."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OriginRadialForce(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.OriginRadialForce.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.OriginRadialForce"

    def __init__(self, force: np.float32 | None = None, min_distance: np.float32 | None = None, max_distance: np.float32 | None = None, min_force: np.float32 | None = None, max_force: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            force: Initial value for Force.
            min_distance: Initial value for MinDistance.
            max_distance: Initial value for MaxDistance.
            min_force: Initial value for MinForce.
            max_force: Initial value for MaxForce.
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

    @property
    def force(self) -> np.float32 | None:
        """The Force field value."""
        member = self.get_member("Force")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force.setter
    def force(self, value: np.float32) -> None:
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
    def min_distance(self) -> np.float32 | None:
        """The MinDistance field value."""
        member = self.get_member("MinDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_distance.setter
    def min_distance(self, value: np.float32) -> None:
        """Set the MinDistance field value."""
        member = self.get_member("MinDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinDistance", fields.FieldFloat(value=value)
            )

    @property
    def max_distance(self) -> np.float32 | None:
        """The MaxDistance field value."""
        member = self.get_member("MaxDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_distance.setter
    def max_distance(self, value: np.float32) -> None:
        """Set the MaxDistance field value."""
        member = self.get_member("MaxDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxDistance", fields.FieldFloat(value=value)
            )

    @property
    def min_force(self) -> np.float32 | None:
        """The MinForce field value."""
        member = self.get_member("MinForce")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_force.setter
    def min_force(self, value: np.float32) -> None:
        """Set the MinForce field value."""
        member = self.get_member("MinForce")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinForce", fields.FieldFloat(value=value)
            )

    @property
    def max_force(self) -> np.float32 | None:
        """The MaxForce field value."""
        member = self.get_member("MaxForce")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_force.setter
    def max_force(self, value: np.float32) -> None:
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

