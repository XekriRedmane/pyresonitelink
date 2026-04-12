"""Generated component: VirtualKeyboard."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.itext import IText
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VirtualKeyboard(GeneratedComponent, IItemMetadataSource, IWorldEventReceiver):
    """The Virtual Keyboard is a component that groups many Keys, Modifier Keys, and Multi Keys together.

    Category: Userspace/Virtual Keyboard
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VirtualKeyboard"

    def __init__(self, shift_active: primitives.Bool | None = None, hold_shift: primitives.Bool | None = None, text_preview_active: str | IField[primitives.Bool] | None = None, text_preview: str | IText | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            shift_active: Initial value for ShiftActive.
            hold_shift: Initial value for HoldShift.
            text_preview_active: Initial value for TextPreviewActive.
            text_preview: Initial value for TextPreview.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if shift_active is not None:
            self.shift_active = shift_active
        if hold_shift is not None:
            self.hold_shift = hold_shift
        if text_preview_active is not None:
            self.text_preview_active = text_preview_active
        if text_preview is not None:
            self.text_preview = text_preview

    @property
    def shift_active(self) -> primitives.Bool | None:
        """Whether the Virtual Shift key is toggled to pressed."""
        member = self.get_member("ShiftActive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shift_active.setter
    def shift_active(self, value: primitives.Bool) -> None:
        """Set the ShiftActive field value."""
        member = self.get_member("ShiftActive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShiftActive", fields.FieldBool(value=value)
            )

    @property
    def hold_shift(self) -> primitives.Bool | None:
        """Whether the Virtual Shift key is held."""
        member = self.get_member("HoldShift")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hold_shift.setter
    def hold_shift(self, value: primitives.Bool) -> None:
        """Set the HoldShift field value."""
        member = self.get_member("HoldShift")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HoldShift", fields.FieldBool(value=value)
            )

    @property
    def text_preview_active(self) -> str | None:
        """drives the visibility of the preview text display."""
        member = self.get_member("TextPreviewActive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_preview_active.setter
    def text_preview_active(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the TextPreviewActive reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TextPreviewActive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TextPreviewActive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def text_preview(self) -> str | None:
        """The text preview object that shows what the user is typing."""
        member = self.get_member("TextPreview")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_preview.setter
    def text_preview(self, target: str | IText | None) -> None:
        """Set the TextPreview reference by target ID or IText instance."""
        target_id: str | None = target.id if isinstance(target, IText) else target  # type: ignore[assignment]
        member = self.get_member("TextPreview")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TextPreview",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IText'),
            )

