"""Generated component: BoxPointGenerator."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ipoint_generator import IPointGenerator
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BoxPointGenerator(GeneratedComponent, IPointGenerator, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BoxPointGenerator.

    Category: Transform/Point Generators
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BoxPointGenerator"

    def __init__(self, size: primitives.Float3 | None = None, shell: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
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
    def size(self) -> primitives.Float3 | None:
        """The Size field value."""
        member = self.get_member("Size")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size.setter
    def size(self, value: primitives.Float3) -> None:
        """Set the Size field value."""
        member = self.get_member("Size")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Size", fields.FieldFloat3(value=value)
            )

    @property
    def shell(self) -> primitives.Bool | None:
        """The Shell field value."""
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

