"""Generated component: ControllerHapticPointMapper."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.chirality import Chirality
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ControllerHapticPointMapper(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ControllerHapticPointMapper component allows you to specify a point where you feel your controller haptics, this can be useful in cases where you don't feel touching haptic volumes like objects or other user's avatars line up right.

By default without this component, the haptic point is located on the upper end of your controller, which may not desired if your avatar's hands are far away from the end point of your controller.

This works as part of the game's robust Haptics system.

    Category: Input/Haptics

    **Behavior**: The Haptic Point slot from your Controller slot on your Userroot moves underneath the slot where the ControllerHapticPointMapper component is located, which is how this functionality works.

Placing a slot with ControllerHapticPointMapper underneath a user does this behavior instantly, the user does not need to equip their avatar again or respawn.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ControllerHapticPointMapper"

    def __init__(self, priority: primitives.Int | None = None, show_debug_visuals: primitives.Bool | None = None, side: Chirality | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            priority: Initial value for Priority.
            show_debug_visuals: Initial value for ShowDebugVisuals.
            side: Initial value for Side.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if priority is not None:
            self.priority = priority
        if show_debug_visuals is not None:
            self.show_debug_visuals = show_debug_visuals
        if side is not None:
            self.side = side

    @property
    def priority(self) -> primitives.Int | None:
        """The priority of this over other haptic elements"""
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
        """Enables a sphere visual that lights up when touching haptic zones."""
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
    def side(self) -> Chirality | None:
        """Specifies which controller/hand this component gives haptic data to."""
        member = self.get_member("Side")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Chirality(member.value)
        return None

    @side.setter
    def side(self, value: Chirality | str) -> None:
        """Set Side. Specifies which controller/hand this component gives haptic data to."""
        member = self.get_member("Side")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Side",
                members.FieldEnum(value=str(value)),
            )

