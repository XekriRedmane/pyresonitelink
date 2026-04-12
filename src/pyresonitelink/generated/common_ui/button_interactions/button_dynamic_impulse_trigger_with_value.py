"""Generated component: ButtonDynamicImpulseTriggerWithValue."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.ibutton_hover_receiver import IButtonHoverReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonDynamicImpulseTriggerWithValue(GenericComponent[T], IButtonPressReceiver, IButtonHoverReceiver, IWorldEventReceiver):
    """The ButtonDynamicImpulseTriggerWithValue component sends Dynamic Impulses to flux node receivers with data. This acts like a combination of Button Events & Dynamic Impulse Trigger With Data ProtoFlux nodes, but as a component instead.

}}

    Category: Common UI/Button Interactions

    Useful for sending dynamic pulses cleanly instead of using flux.

    Parameterize with a value type::

        ButtonDynamicImpulseTriggerWithValue[primitives.Float]
        ButtonDynamicImpulseTriggerWithValue[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonDynamicImpulseTriggerWithValue<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ButtonDynamicImpulseTriggerWithValue<>"

    def __init__(self, target: str | Slot | None = None, exclude_disabled: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            exclude_disabled: Initial value for ExcludeDisabled.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if exclude_disabled is not None:
            self.exclude_disabled = exclude_disabled

    @property
    def target(self) -> str | None:
        """The slot to target with impulses specified by ``PressedData``,``PressingData``,``ReleasedData``,``HoverEnterData``,``HoverStayData``,``HoverLeaveData``."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | Slot | None) -> None:
        """Set the Target reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def exclude_disabled(self) -> primitives.Bool | None:
        """Whether disabled slots and hierarchies should be affected by the dynamic impulses sent."""
        member = self.get_member("ExcludeDisabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exclude_disabled.setter
    def exclude_disabled(self, value: primitives.Bool) -> None:
        """Set the ExcludeDisabled field value."""
        member = self.get_member("ExcludeDisabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ExcludeDisabled", fields.FieldBool(value=value)
            )

    @property
    def pressed_data(self) -> members.SyncObject | None:
        """What value and tag type dynamic impulse to send when an IButton is pressed on the same slot."""
        member = self.get_member("PressedData")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @pressed_data.setter
    def pressed_data(self, value: members.SyncObject) -> None:
        """Set PressedData. What value and tag type dynamic impulse to send when an IButton is pressed on the same slot."""
        self.set_member("PressedData", value)

    @property
    def pressing_data(self) -> members.SyncObject | None:
        """What value and tag type dynamic impulse to send when an IButton is being pressed on the same slot. Fires every update while the button is being pressed."""
        member = self.get_member("PressingData")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @pressing_data.setter
    def pressing_data(self, value: members.SyncObject) -> None:
        """Set PressingData. What value and tag type dynamic impulse to send when an IButton is being pressed on the same slot. Fires every update while the button is being pressed."""
        self.set_member("PressingData", value)

    @property
    def released_data(self) -> members.SyncObject | None:
        """What value and tag type dynamic impulse to send when an IButton stops being pressed on the same slot."""
        member = self.get_member("ReleasedData")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @released_data.setter
    def released_data(self, value: members.SyncObject) -> None:
        """Set ReleasedData. What value and tag type dynamic impulse to send when an IButton stops being pressed on the same slot."""
        self.set_member("ReleasedData", value)

    @property
    def hover_enter_data(self) -> members.SyncObject | None:
        """What value and tag type dynamic impulse to send when an IButton starts being pointed at on the same slot."""
        member = self.get_member("HoverEnterData")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @hover_enter_data.setter
    def hover_enter_data(self, value: members.SyncObject) -> None:
        """Set HoverEnterData. What value and tag type dynamic impulse to send when an IButton starts being pointed at on the same slot."""
        self.set_member("HoverEnterData", value)

    @property
    def hover_stay_data(self) -> members.SyncObject | None:
        """What value and tag type dynamic impulse to send when an IButton is currently pointed at on the same slot. Fires every update while the button is being hovered over."""
        member = self.get_member("HoverStayData")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @hover_stay_data.setter
    def hover_stay_data(self, value: members.SyncObject) -> None:
        """Set HoverStayData. What value and tag type dynamic impulse to send when an IButton is currently pointed at on the same slot. Fires every update while the button is being hovered over."""
        self.set_member("HoverStayData", value)

    @property
    def hover_leave_data(self) -> members.SyncObject | None:
        """What value and tag type dynamic impulse to send when an IButton stops being pointed at on the same slot."""
        member = self.get_member("HoverLeaveData")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @hover_leave_data.setter
    def hover_leave_data(self, value: members.SyncObject) -> None:
        """Set HoverLeaveData. What value and tag type dynamic impulse to send when an IButton stops being pointed at on the same slot."""
        self.set_member("HoverLeaveData", value)

