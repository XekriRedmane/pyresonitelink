"""Generated component: RepulsionTreeItem."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.irepulsion_tree_node import IRepulsionTreeNode
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RepulsionTreeItem(GeneratedComponent, IRepulsionTreeNode, IWorldEventReceiver):
    """Repulsion tree item is used along side the Repulsion Tree Simulator Component to make a live repulsion tree simulation. Check the simulator's page for a more detailed explanation.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RepulsionTreeItem"

    def __init__(self, force: primitives.Float | None = None, radius: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            force: Initial value for Force.
            radius: Initial value for Radius.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if force is not None:
            self.force = force
        if radius is not None:
            self.radius = radius

    @property
    def force(self) -> primitives.Float | None:
        """How much force to apply to other RepulsionTreeItems within range."""
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
    def radius(self) -> primitives.Float | None:
        """The radius of influence this item has when interacting with other items."""
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

