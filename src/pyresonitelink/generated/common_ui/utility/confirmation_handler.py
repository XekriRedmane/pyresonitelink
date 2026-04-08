"""Generated component: ConfirmationHandler."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ConfirmationHandler(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ConfirmationHandler.

    Category: Common UI/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ConfirmationHandler"

    def __init__(self, label: str | IField[primitives.String] | None = None, color: str | IField[primitives.ColorX] | None = None, original_label: primitives.String | None = None, original_color: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            label: Initial value for Label.
            color: Initial value for Color.
            original_label: Initial value for OriginalLabel.
            original_color: Initial value for OriginalColor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if label is not None:
            self.label = label
        if color is not None:
            self.color = color
        if original_label is not None:
            self.original_label = original_label
        if original_color is not None:
            self.original_color = original_color

    @property
    def label(self) -> str | None:
        """Target ID of the Label reference (targets IField[primitives.String])."""
        member = self.get_member("Label")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @label.setter
    def label(self, target: str | IField[primitives.String] | None) -> None:
        """Set the Label reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Label")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Label",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def color(self) -> str | None:
        """Target ID of the Color reference (targets IField[primitives.ColorX])."""
        member = self.get_member("Color")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color.setter
    def color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the Color reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Color")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Color",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def original_label(self) -> primitives.String | None:
        """The OriginalLabel field value."""
        member = self.get_member("OriginalLabel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @original_label.setter
    def original_label(self, value: primitives.String) -> None:
        """Set the OriginalLabel field value."""
        member = self.get_member("OriginalLabel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OriginalLabel", fields.FieldString(value=value)
            )

    @property
    def original_color(self) -> primitives.ColorX | None:
        """The OriginalColor field value."""
        member = self.get_member("OriginalColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @original_color.setter
    def original_color(self, value: primitives.ColorX) -> None:
        """Set the OriginalColor field value."""
        member = self.get_member("OriginalColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OriginalColor", fields.FieldColorX(value=value)
            )

