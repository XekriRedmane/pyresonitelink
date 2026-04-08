"""Generated component: ButtonEditColorX."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.color_dialog_interface import ColorDialogInterface
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonEditColorX(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ButtonEditColorX.

    Category: Common UI/Button Interactions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonEditColorX"

    def __init__(self, target: str | IField[primitives.ColorX] | None = None, color_picker: str | ColorDialogInterface | None = None, continuous: primitives.Bool | None = None, alpha: primitives.Bool | None = None, hdr: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            color_picker: Initial value for _colorPicker.
            continuous: Initial value for Continuous.
            alpha: Initial value for Alpha.
            hdr: Initial value for HDR.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if color_picker is not None:
            self.color_picker = color_picker
        if continuous is not None:
            self.continuous = continuous
        if alpha is not None:
            self.alpha = alpha
        if hdr is not None:
            self.hdr = hdr

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[primitives.ColorX])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def color_picker(self) -> str | None:
        """Target ID of the _colorPicker reference (targets ColorDialogInterface)."""
        member = self.get_member("_colorPicker")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color_picker.setter
    def color_picker(self, target: str | ColorDialogInterface | None) -> None:
        """Set the _colorPicker reference by target ID or ColorDialogInterface instance."""
        target_id: str | None = target.id if isinstance(target, ColorDialogInterface) else target  # type: ignore[assignment]
        member = self.get_member("_colorPicker")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colorPicker",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ColorDialogInterface'),
            )

    @property
    def continuous(self) -> primitives.Bool | None:
        """The Continuous field value."""
        member = self.get_member("Continuous")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @continuous.setter
    def continuous(self, value: primitives.Bool) -> None:
        """Set the Continuous field value."""
        member = self.get_member("Continuous")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Continuous", fields.FieldBool(value=value)
            )

    @property
    def alpha(self) -> primitives.Bool | None:
        """The Alpha field value."""
        member = self.get_member("Alpha")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @alpha.setter
    def alpha(self, value: primitives.Bool) -> None:
        """Set the Alpha field value."""
        member = self.get_member("Alpha")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Alpha", fields.FieldBool(value=value)
            )

    @property
    def hdr(self) -> primitives.Bool | None:
        """The HDR field value."""
        member = self.get_member("HDR")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hdr.setter
    def hdr(self, value: primitives.Bool) -> None:
        """Set the HDR field value."""
        member = self.get_member("HDR")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HDR", fields.FieldBool(value=value)
            )

