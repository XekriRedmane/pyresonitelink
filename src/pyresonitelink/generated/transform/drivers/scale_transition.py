"""Generated component: ScaleTransition."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.curve_preset import CurvePreset
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ScaleTransition(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ScaleTransition component makes a slot scale from one scale state to another, disabling when fully reaching its disabled scale point. The component's scale transition state is controlled via ``ShowField``.

    Category: Transform/Drivers

    Attach to a slot and provide values to the proper fields. When
    ``ShowField`` is toggled, the scale and enabled fields of the component
    will do a little animation.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ScaleTransition"

    def __init__(self, show_field: primitives.Bool | None = None, transition_time_field: primitives.Float | None = None, show_scale_field: primitives.Float3 | None = None, hidden_scale_field: primitives.Float3 | None = None, curve_field: CurvePreset | str | None = None, scale_drive: str | IField[primitives.Float3] | None = None, enabled_drive: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            show_field: Initial value for ShowField.
            transition_time_field: Initial value for TransitionTimeField.
            show_scale_field: Initial value for ShowScaleField.
            hidden_scale_field: Initial value for HiddenScaleField.
            curve_field: Initial value for CurveField.
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
        if curve_field is not None:
            self.curve_field = curve_field
        if scale_drive is not None:
            self.scale_drive = scale_drive
        if enabled_drive is not None:
            self.enabled_drive = enabled_drive

    @property
    def show_field(self) -> primitives.Bool | None:
        """Whether to be transitioning to hidden (false) or shown (true)"""
        member = self.get_member("ShowField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_field.setter
    def show_field(self, value: primitives.Bool) -> None:
        """Set the ShowField field value."""
        member = self.get_member("ShowField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowField", fields.FieldBool(value=value)
            )

    @property
    def transition_time_field(self) -> primitives.Float | None:
        """How long the transition to shown or hidden should take."""
        member = self.get_member("TransitionTimeField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @transition_time_field.setter
    def transition_time_field(self, value: primitives.Float) -> None:
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
        """What scale the object should transition to from ``HiddenScaleField`` when ``ShowField`` is true."""
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
        """What scale the object should transition to from ``ShowScaleField`` when ``ShowField`` is false."""
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
    def curve_field(self) -> CurvePreset | None:
        """How the object should transition scale over time."""
        member = self.get_member("CurveField")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CurvePreset(member.value)
        return None

    @curve_field.setter
    def curve_field(self, value: CurvePreset | str) -> None:
        """Set CurveField. How the object should transition scale over time."""
        member = self.get_member("CurveField")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "CurveField",
                members.FieldEnum(value=str(value)),
            )

    @property
    def scale_drive(self) -> str | None:
        """The field to drive to make this slot scale up and down. Usually the slot's scale field."""
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
        """The field to drive to false when the object is done scaling to hidden and drive to true when transitioning away from hidden."""
        member = self.get_member("_enabledDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @enabled_drive.setter
    def enabled_drive(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _enabledDrive reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_enabledDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_enabledDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

