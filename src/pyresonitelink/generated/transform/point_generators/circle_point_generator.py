"""Generated component: CirclePointGenerator."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ipoint_generator import IPointGenerator
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CirclePointGenerator(GeneratedComponent, IPointGenerator, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CirclePointGenerator.

    Category: Transform/Point Generators
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CirclePointGenerator"

    def __init__(self, radius: np.float32 | None = None, shell: bool | None = None, *, component: workers.Component | None = None) -> None:
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
    def shell(self) -> bool | None:
        """The Shell field value."""
        member = self.get_member("Shell")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shell.setter
    def shell(self, value: bool) -> None:
        """Set the Shell field value."""
        member = self.get_member("Shell")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Shell", fields.FieldBool(value=value)
            )

