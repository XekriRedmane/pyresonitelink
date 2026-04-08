"""Generated component: ButtonDelegateRelay."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonDelegateRelay(GenericComponent[T], IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.ButtonDelegateRelay<>.

    Category: Common UI/Events

    Parameterize with a value type::

        ButtonDelegateRelay[np.float32]
        ButtonDelegateRelay[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.ButtonDelegateRelay<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.UIX.ButtonDelegateRelay<>"

    def __init__(self, double_press_delay: np.float32 | None = None, release_press_interval: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            double_press_delay: Initial value for DoublePressDelay.
            release_press_interval: Initial value for ReleasePressInterval.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if double_press_delay is not None:
            self.double_press_delay = double_press_delay
        if release_press_interval is not None:
            self.release_press_interval = release_press_interval

    @property
    def double_press_delay(self) -> np.float32 | None:
        """The DoublePressDelay field value."""
        member = self.get_member("DoublePressDelay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @double_press_delay.setter
    def double_press_delay(self, value: np.float32) -> None:
        """Set the DoublePressDelay field value."""
        member = self.get_member("DoublePressDelay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DoublePressDelay", fields.FieldFloat(value=value)
            )

    @property
    def release_press_interval(self) -> np.float32 | None:
        """The ReleasePressInterval field value."""
        member = self.get_member("ReleasePressInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @release_press_interval.setter
    def release_press_interval(self, value: np.float32) -> None:
        """Set the ReleasePressInterval field value."""
        member = self.get_member("ReleasePressInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReleasePressInterval", fields.FieldFloat(value=value)
            )

