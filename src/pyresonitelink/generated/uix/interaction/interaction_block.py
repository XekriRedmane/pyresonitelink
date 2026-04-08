"""Generated component: InteractionBlock."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iui_interactable import IUIInteractable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InteractionBlock(GeneratedComponent, IUIInteractable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.InteractionBlock.

    Category: UIX/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.InteractionBlock"

    def __init__(self, touch_exit_lock: bool | None = None, touch_enter_lock: bool | None = None, *, component: workers.Component | None = None) -> None:
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
    def touch_exit_lock(self) -> bool | None:
        """The TouchExitLock field value."""
        member = self.get_member("TouchExitLock")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @touch_exit_lock.setter
    def touch_exit_lock(self, value: bool) -> None:
        """Set the TouchExitLock field value."""
        member = self.get_member("TouchExitLock")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TouchExitLock", fields.FieldBool(value=value)
            )

    @property
    def touch_enter_lock(self) -> bool | None:
        """The TouchEnterLock field value."""
        member = self.get_member("TouchEnterLock")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @touch_enter_lock.setter
    def touch_enter_lock(self, value: bool) -> None:
        """Set the TouchEnterLock field value."""
        member = self.get_member("TouchEnterLock")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TouchEnterLock", fields.FieldBool(value=value)
            )

