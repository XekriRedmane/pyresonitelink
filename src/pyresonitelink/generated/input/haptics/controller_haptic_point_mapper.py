"""Generated component: ControllerHapticPointMapper."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ControllerHapticPointMapper(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ControllerHapticPointMapper.

    Category: Input/Haptics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ControllerHapticPointMapper"

    def __init__(self, priority: primitives.Int | None = None, show_debug_visuals: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            priority: Initial value for Priority.
            show_debug_visuals: Initial value for ShowDebugVisuals.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if priority is not None:
            self.priority = priority
        if show_debug_visuals is not None:
            self.show_debug_visuals = show_debug_visuals

    @property
    def priority(self) -> primitives.Int | None:
        """The Priority field value."""
        member = self.get_member("Priority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @priority.setter
    def priority(self, value: primitives.Int) -> None:
        """Set the Priority field value."""
        member = self.get_member("Priority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Priority", fields.FieldInt(value=value)
            )

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

    @property
    def side(self) -> members.FieldEnum | None:
        """The Side member."""
        member = self.get_member("Side")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @side.setter
    def side(self, value: members.FieldEnum) -> None:
        """Set the Side member."""
        self.set_member("Side", value)

