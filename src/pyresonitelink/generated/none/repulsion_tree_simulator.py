"""Generated component: RepulsionTreeSimulator."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.irepulsion_tree_node import IRepulsionTreeNode
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RepulsionTreeSimulator(GeneratedComponent, IRepulsionTreeNode, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.RepulsionTreeSimulator.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RepulsionTreeSimulator"

    def __init__(self, falloff_power: np.float32 | None = None, radius: np.float32 | None = None, force: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            falloff_power: Initial value for FalloffPower.
            radius: Initial value for Radius.
            force: Initial value for Force.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if falloff_power is not None:
            self.falloff_power = falloff_power
        if radius is not None:
            self.radius = radius
        if force is not None:
            self.force = force

    @property
    def falloff_power(self) -> np.float32 | None:
        """The FalloffPower field value."""
        member = self.get_member("FalloffPower")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @falloff_power.setter
    def falloff_power(self, value: np.float32) -> None:
        """Set the FalloffPower field value."""
        member = self.get_member("FalloffPower")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FalloffPower", fields.FieldFloat(value=value)
            )

    @property
    def radius(self) -> np.float32 | None:
        """The Radius field value."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: np.float32) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

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

