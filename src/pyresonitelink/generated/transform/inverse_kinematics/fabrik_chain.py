"""Generated component: FABRIK_Chain."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FABRIK_Chain(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FABRIK_Chain.

    Category: Transform/Inverse Kinematics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FABRIK_Chain"

    def __init__(self, max_iterations: primitives.Int | None = None, show_debug_visuals: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            max_iterations: Initial value for MaxIterations.
            show_debug_visuals: Initial value for ShowDebugVisuals.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if max_iterations is not None:
            self.max_iterations = max_iterations
        if show_debug_visuals is not None:
            self.show_debug_visuals = show_debug_visuals

    @property
    def max_iterations(self) -> primitives.Int | None:
        """The MaxIterations field value."""
        member = self.get_member("MaxIterations")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_iterations.setter
    def max_iterations(self, value: primitives.Int) -> None:
        """Set the MaxIterations field value."""
        member = self.get_member("MaxIterations")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxIterations", fields.FieldInt(value=value)
            )

    @property
    def bones(self) -> members.SyncList | None:
        """The Bones member."""
        member = self.get_member("Bones")
        if isinstance(member, members.SyncList):
            return member
        return None

    @bones.setter
    def bones(self, value: members.SyncList) -> None:
        """Set the Bones member."""
        self.set_member("Bones", value)

    @property
    def show_debug_visuals(self) -> primitives.Bool | None:
        """The ShowDebugVisuals field value."""
        member = self.get_member("ShowDebugVisuals")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_debug_visuals.setter
    def show_debug_visuals(self, value: primitives.Bool) -> None:
        """Set the ShowDebugVisuals field value."""
        member = self.get_member("ShowDebugVisuals")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowDebugVisuals", fields.FieldBool(value=value)
            )

