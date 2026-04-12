"""Generated component: RepulsionTreeSimulator."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.irepulsion_tree_node import IRepulsionTreeNode
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RepulsionTreeSimulator(GeneratedComponent, IRepulsionTreeNode, IWorldEventReceiver):
    """The RepulsionTreeSimulator can be used alongside the RepulsionTreeItem component on it's children slots to create a repulsion tree simulation. A repulsion tree is a simulation that keeps a bunch of RepulsionTreeItems on the outside shell of a sphere. The different slots of the tree will move around as they push or pull each other in real time.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RepulsionTreeSimulator"

    def __init__(self, falloff_power: primitives.Float | None = None, radius: primitives.Float | None = None, force: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
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
    def falloff_power(self) -> primitives.Float | None:
        """how quickly the force power diminishes by distance."""
        member = self.get_member("FalloffPower")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @falloff_power.setter
    def falloff_power(self, value: primitives.Float) -> None:
        """Set the FalloffPower field value."""
        member = self.get_member("FalloffPower")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FalloffPower", fields.FieldFloat(value=value)
            )

    @property
    def radius(self) -> primitives.Float | None:
        """The radius of this repulsion tree's sphere."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: primitives.Float) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    @property
    def force(self) -> primitives.Float | None:
        """how much to multiply the forces of the children objects."""
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

