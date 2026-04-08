"""Generated component: ButtonRefRelay."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonRefRelay(GenericComponent[T], IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.ButtonRefRelay<>.

    Category: Common UI/Events

    Parameterize with a value type::

        ButtonRefRelay[primitives.Float]
        ButtonRefRelay[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.ButtonRefRelay<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.UIX.ButtonRefRelay<>"

    def __init__(self, double_press_delay: primitives.Float | None = None, release_press_interval: primitives.Float | None = None, argument: str | T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            double_press_delay: Initial value for DoublePressDelay.
            release_press_interval: Initial value for ReleasePressInterval.
            argument: Initial value for Argument.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if double_press_delay is not None:
            self.double_press_delay = double_press_delay
        if release_press_interval is not None:
            self.release_press_interval = release_press_interval
        if argument is not None:
            self.argument = argument

    @property
    def double_press_delay(self) -> primitives.Float | None:
        """The DoublePressDelay field value."""
        member = self.get_member("DoublePressDelay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @double_press_delay.setter
    def double_press_delay(self, value: primitives.Float) -> None:
        """Set the DoublePressDelay field value."""
        member = self.get_member("DoublePressDelay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DoublePressDelay", fields.FieldFloat(value=value)
            )

    @property
    def release_press_interval(self) -> primitives.Float | None:
        """The ReleasePressInterval field value."""
        member = self.get_member("ReleasePressInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @release_press_interval.setter
    def release_press_interval(self, value: primitives.Float) -> None:
        """Set the ReleasePressInterval field value."""
        member = self.get_member("ReleasePressInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReleasePressInterval", fields.FieldFloat(value=value)
            )

    @property
    def argument(self) -> str | None:
        """Target ID of the Argument reference (targets T)."""
        member = self.get_member("Argument")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @argument.setter
    def argument(self, target: str | T | None) -> None:
        """Set the Argument reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("Argument")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Argument",
                members.Reference(targetId=target_id, targetType='T'),
            )

