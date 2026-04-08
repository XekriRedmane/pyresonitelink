"""Generated component: ButtonDynamicImpulseTrigger."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.ibutton_hover_receiver import IButtonHoverReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonDynamicImpulseTrigger(GeneratedComponent, IButtonPressReceiver, IButtonHoverReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ButtonDynamicImpulseTrigger.

    Category: Common UI/Button Interactions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonDynamicImpulseTrigger"

    def __init__(self, target: str | Slot | None = None, exclude_disabled: primitives.Bool | None = None, pressed_tag: primitives.String | None = None, pressing_tag: primitives.String | None = None, released_tag: primitives.String | None = None, hover_enter_tag: primitives.String | None = None, hover_stay_tag: primitives.String | None = None, hover_leave_tag: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            exclude_disabled: Initial value for ExcludeDisabled.
            pressed_tag: Initial value for PressedTag.
            pressing_tag: Initial value for PressingTag.
            released_tag: Initial value for ReleasedTag.
            hover_enter_tag: Initial value for HoverEnterTag.
            hover_stay_tag: Initial value for HoverStayTag.
            hover_leave_tag: Initial value for HoverLeaveTag.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if exclude_disabled is not None:
            self.exclude_disabled = exclude_disabled
        if pressed_tag is not None:
            self.pressed_tag = pressed_tag
        if pressing_tag is not None:
            self.pressing_tag = pressing_tag
        if released_tag is not None:
            self.released_tag = released_tag
        if hover_enter_tag is not None:
            self.hover_enter_tag = hover_enter_tag
        if hover_stay_tag is not None:
            self.hover_stay_tag = hover_stay_tag
        if hover_leave_tag is not None:
            self.hover_leave_tag = hover_leave_tag

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
    def exclude_disabled(self) -> primitives.Bool | None:
        """The ExcludeDisabled field value."""
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
    def pressed_tag(self) -> primitives.String | None:
        """The PressedTag field value."""
        member = self.get_member("PressedTag")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pressed_tag.setter
    def pressed_tag(self, value: primitives.String) -> None:
        """Set the PressedTag field value."""
        member = self.get_member("PressedTag")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PressedTag", fields.FieldString(value=value)
            )

    @property
    def pressing_tag(self) -> primitives.String | None:
        """The PressingTag field value."""
        member = self.get_member("PressingTag")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pressing_tag.setter
    def pressing_tag(self, value: primitives.String) -> None:
        """Set the PressingTag field value."""
        member = self.get_member("PressingTag")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PressingTag", fields.FieldString(value=value)
            )

    @property
    def released_tag(self) -> primitives.String | None:
        """The ReleasedTag field value."""
        member = self.get_member("ReleasedTag")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @released_tag.setter
    def released_tag(self, value: primitives.String) -> None:
        """Set the ReleasedTag field value."""
        member = self.get_member("ReleasedTag")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReleasedTag", fields.FieldString(value=value)
            )

    @property
    def hover_enter_tag(self) -> primitives.String | None:
        """The HoverEnterTag field value."""
        member = self.get_member("HoverEnterTag")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hover_enter_tag.setter
    def hover_enter_tag(self, value: primitives.String) -> None:
        """Set the HoverEnterTag field value."""
        member = self.get_member("HoverEnterTag")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HoverEnterTag", fields.FieldString(value=value)
            )

    @property
    def hover_stay_tag(self) -> primitives.String | None:
        """The HoverStayTag field value."""
        member = self.get_member("HoverStayTag")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hover_stay_tag.setter
    def hover_stay_tag(self, value: primitives.String) -> None:
        """Set the HoverStayTag field value."""
        member = self.get_member("HoverStayTag")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HoverStayTag", fields.FieldString(value=value)
            )

    @property
    def hover_leave_tag(self) -> primitives.String | None:
        """The HoverLeaveTag field value."""
        member = self.get_member("HoverLeaveTag")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hover_leave_tag.setter
    def hover_leave_tag(self, value: primitives.String) -> None:
        """Set the HoverLeaveTag field value."""
        member = self.get_member("HoverLeaveTag")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HoverLeaveTag", fields.FieldString(value=value)
            )

