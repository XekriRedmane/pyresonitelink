"""Generated component: ScaleTransition."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ScaleTransition(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ScaleTransition.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ScaleTransition"

    def __init__(self, show_field: bool | None = None, transition_time_field: np.float32 | None = None, show_scale_field: primitives.Float3 | None = None, hidden_scale_field: primitives.Float3 | None = None, scale_drive: str | IField[primitives.Float3] | None = None, enabled_drive: str | IField[bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            show_field: Initial value for ShowField.
            transition_time_field: Initial value for TransitionTimeField.
            show_scale_field: Initial value for ShowScaleField.
            hidden_scale_field: Initial value for HiddenScaleField.
            scale_drive: Initial value for _scaleDrive.
            enabled_drive: Initial value for _enabledDrive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if show_field is not None:
            self.show_field = show_field
        if transition_time_field is not None:
            self.transition_time_field = transition_time_field
        if show_scale_field is not None:
            self.show_scale_field = show_scale_field
        if hidden_scale_field is not None:
            self.hidden_scale_field = hidden_scale_field
        if scale_drive is not None:
            self.scale_drive = scale_drive
        if enabled_drive is not None:
            self.enabled_drive = enabled_drive

    @property
    def show_field(self) -> bool | None:
        """The ShowField field value."""
        member = self.get_member("ShowField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_field.setter
    def show_field(self, value: bool) -> None:
        """Set the ShowField field value."""
        member = self.get_member("ShowField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowField", fields.FieldBool(value=value)
            )

    @property
    def transition_time_field(self) -> np.float32 | None:
        """The TransitionTimeField field value."""
        member = self.get_member("TransitionTimeField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @transition_time_field.setter
    def transition_time_field(self, value: np.float32) -> None:
        """Set the TransitionTimeField field value."""
        member = self.get_member("TransitionTimeField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TransitionTimeField", fields.FieldFloat(value=value)
            )

    @property
    def show_scale_field(self) -> primitives.Float3 | None:
        """The ShowScaleField field value."""
        member = self.get_member("ShowScaleField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_scale_field.setter
    def show_scale_field(self, value: primitives.Float3) -> None:
        """Set the ShowScaleField field value."""
        member = self.get_member("ShowScaleField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowScaleField", fields.FieldFloat3(value=value)
            )

    @property
    def hidden_scale_field(self) -> primitives.Float3 | None:
        """The HiddenScaleField field value."""
        member = self.get_member("HiddenScaleField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hidden_scale_field.setter
    def hidden_scale_field(self, value: primitives.Float3) -> None:
        """Set the HiddenScaleField field value."""
        member = self.get_member("HiddenScaleField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HiddenScaleField", fields.FieldFloat3(value=value)
            )

    @property
    def curve_field(self) -> members.FieldEnum | None:
        """The CurveField member."""
        member = self.get_member("CurveField")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @curve_field.setter
    def curve_field(self, value: members.FieldEnum) -> None:
        """Set the CurveField member."""
        self.set_member("CurveField", value)

    @property
    def scale_drive(self) -> str | None:
        """Target ID of the _scaleDrive reference (targets IField[primitives.Float3])."""
        member = self.get_member("_scaleDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale_drive.setter
    def scale_drive(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _scaleDrive reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_scaleDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_scaleDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def enabled_drive(self) -> str | None:
        """Target ID of the _enabledDrive reference (targets IField[bool])."""
        member = self.get_member("_enabledDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @enabled_drive.setter
    def enabled_drive(self, target: str | IField[bool] | None) -> None:
        """Set the _enabledDrive reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_enabledDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_enabledDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

