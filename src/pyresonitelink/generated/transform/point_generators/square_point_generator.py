"""Generated component: SquarePointGenerator."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ipoint_generator import IPointGenerator
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SquarePointGenerator(GeneratedComponent, IPointGenerator, IWorldEventReceiver):
    """A generator for points arranged in a rectangle with a given length and width.

    Category: Transform/Point Generators

    Used in a Common Spawn Area to define in what kind of spawn area shape
    users should initially spawn into.

    **Related Components**: * CommonSpawnArea
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SquarePointGenerator"

    def __init__(self, size: primitives.Float2 | None = None, shell: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            size: Initial value for Size.
            shell: Initial value for Shell.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if size is not None:
            self.size = size
        if shell is not None:
            self.shell = shell

    @property
    def size(self) -> primitives.Float2 | None:
        """A flat rectangle size for generating points in"""
        member = self.get_member("Size")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size.setter
    def size(self, value: primitives.Float2) -> None:
        """Set the Size field value."""
        member = self.get_member("Size")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Size", fields.FieldFloat2(value=value)
            )

    @property
    def shell(self) -> primitives.Bool | None:
        """Whether to spawn users on only the perimeter or not."""
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

