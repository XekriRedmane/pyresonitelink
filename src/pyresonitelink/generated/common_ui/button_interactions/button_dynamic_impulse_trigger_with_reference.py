"""Generated component: ButtonDynamicImpulseTriggerWithReference."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.ibutton_hover_receiver import IButtonHoverReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonDynamicImpulseTriggerWithReference(GenericComponent[T], IButtonPressReceiver, IButtonHoverReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ButtonDynamicImpulseTriggerWithReference<>.

    Category: Common UI/Button Interactions

    Parameterize with a value type::

        ButtonDynamicImpulseTriggerWithReference[np.float32]
        ButtonDynamicImpulseTriggerWithReference[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonDynamicImpulseTriggerWithReference<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ButtonDynamicImpulseTriggerWithReference<>"

    def __init__(self, target: str | Slot | None = None, exclude_disabled: bool | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the Target reference (targets Slot)."""
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
    def exclude_disabled(self) -> bool | None:
        """The ExcludeDisabled field value."""
        member = self.get_member("ExcludeDisabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exclude_disabled.setter
    def exclude_disabled(self, value: bool) -> None:
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
        """The PressedData member."""
        member = self.get_member("PressedData")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @pressed_data.setter
    def pressed_data(self, value: members.SyncObject) -> None:
        """Set the PressedData member."""
        self.set_member("PressedData", value)

    @property
    def pressing_data(self) -> members.SyncObject | None:
        """The PressingData member."""
        member = self.get_member("PressingData")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @pressing_data.setter
    def pressing_data(self, value: members.SyncObject) -> None:
        """Set the PressingData member."""
        self.set_member("PressingData", value)

    @property
    def released_data(self) -> members.SyncObject | None:
        """The ReleasedData member."""
        member = self.get_member("ReleasedData")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @released_data.setter
    def released_data(self, value: members.SyncObject) -> None:
        """Set the ReleasedData member."""
        self.set_member("ReleasedData", value)

    @property
    def hover_enter_data(self) -> members.SyncObject | None:
        """The HoverEnterData member."""
        member = self.get_member("HoverEnterData")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @hover_enter_data.setter
    def hover_enter_data(self, value: members.SyncObject) -> None:
        """Set the HoverEnterData member."""
        self.set_member("HoverEnterData", value)

    @property
    def hover_stay_data(self) -> members.SyncObject | None:
        """The HoverStayData member."""
        member = self.get_member("HoverStayData")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @hover_stay_data.setter
    def hover_stay_data(self, value: members.SyncObject) -> None:
        """Set the HoverStayData member."""
        self.set_member("HoverStayData", value)

    @property
    def hover_leave_data(self) -> members.SyncObject | None:
        """The HoverLeaveData member."""
        member = self.get_member("HoverLeaveData")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @hover_leave_data.setter
    def hover_leave_data(self, value: members.SyncObject) -> None:
        """Set the HoverLeaveData member."""
        self.set_member("HoverLeaveData", value)

