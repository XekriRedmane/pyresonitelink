"""Generated component: TagHapticPointMapper."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TagHapticPointMapper(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The TagHapticPointMapper allows for defining custom mapping on avatars. 

This works as part of the game's robust Haptics system.

    Category: Input/Haptics

    By frooxius: * Full body avatars are automatically instrumented with
    this component * You can define list of Slots with associated HapticTag
    on this component, which determine where will haptic points be mapped to
    * You can specify that haptic devices (e.g. GigglePuck) can be mapped to
    a specific tag in the settings
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TagHapticPointMapper"

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
        """The priority of this Mapper over other mappers."""
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
        """Whether to show the haptic points for this haptic mapper."""
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
    def haptic_points(self) -> members.SyncList | None:
        """A list of haptic points with tags and where they go."""
        member = self.get_member("HapticPoints")
        if isinstance(member, members.SyncList):
            return member
        return None

    @haptic_points.setter
    def haptic_points(self, value: members.SyncList) -> None:
        """Set HapticPoints. A list of haptic points with tags and where they go."""
        self.set_member("HapticPoints", value)

