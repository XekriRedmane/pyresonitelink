"""Generated component: InteractionBlock."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iui_interactable import IUIInteractable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InteractionBlock(GeneratedComponent, IUIInteractable, IWorldEventReceiver):
    """The InteractionBlock component is used to block UIX interaction events from the user. It requires an Image on the same Slot this component is on for this to work.

}}

    Category: UIX/Interaction

    Any time you want to stop any UIX element from interacting (like having
    a popup menu to be on top of your main UIX), you can use this component
    to make the main UIX elements not respond to the user, making them focus
    on the newly spawned UIX.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.InteractionBlock"

    def __init__(self, touch_exit_lock: primitives.Bool | None = None, touch_enter_lock: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            touch_exit_lock: Initial value for TouchExitLock.
            touch_enter_lock: Initial value for TouchEnterLock.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if touch_exit_lock is not None:
            self.touch_exit_lock = touch_exit_lock
        if touch_enter_lock is not None:
            self.touch_enter_lock = touch_enter_lock

    @property
    def touch_exit_lock(self) -> primitives.Bool | None:
        """Blocks interactions when an interaction ends."""
        member = self.get_member("TouchExitLock")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @touch_exit_lock.setter
    def touch_exit_lock(self, value: primitives.Bool) -> None:
        """Set the TouchExitLock field value."""
        member = self.get_member("TouchExitLock")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TouchExitLock", fields.FieldBool(value=value)
            )

    @property
    def touch_enter_lock(self) -> primitives.Bool | None:
        """Blocks interactions when an interaction starts."""
        member = self.get_member("TouchEnterLock")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @touch_enter_lock.setter
    def touch_enter_lock(self, value: primitives.Bool) -> None:
        """Set the TouchEnterLock field value."""
        member = self.get_member("TouchEnterLock")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TouchEnterLock", fields.FieldBool(value=value)
            )

