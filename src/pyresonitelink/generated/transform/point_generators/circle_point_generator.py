"""Generated component: CirclePointGenerator."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ipoint_generator import IPointGenerator
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CirclePointGenerator(GeneratedComponent, IPointGenerator, IWorldEventReceiver):
    """A generator for points arranged in a circle with a given radius.

    Category: Transform/Point Generators

    Used in a Common Spawn Area to define in what kind of spawn area shape
    users should initially spawn into.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CirclePointGenerator"

    def __init__(self, radius: primitives.Float | None = None, shell: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            radius: Initial value for Radius.
            shell: Initial value for Shell.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if radius is not None:
            self.radius = radius
        if shell is not None:
            self.shell = shell

    @property
    def radius(self) -> primitives.Float | None:
        """The distance from center to outside that this point generator should make points."""
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
    def shell(self) -> primitives.Bool | None:
        """Generate the points for this generator only along the outside edge."""
        member = self.get_member("Shell")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shell.setter
    def shell(self, value: primitives.Bool) -> None:
        """Set the Shell field value."""
        member = self.get_member("Shell")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Shell", fields.FieldBool(value=value)
            )

