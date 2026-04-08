"""Generated component: ValueRadio."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueRadio(GenericComponent[T], IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.ValueRadio<>.

    Category: UIX/Interaction

    Parameterize with a value type::

        ValueRadio[np.float32]
        ValueRadio[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.ValueRadio<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.UIX.ValueRadio<>"

    def __init__(self, check_visual: str | IField[bool] | None = None, option_value: T | None = None, target_value: str | IField[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            check_visual: Initial value for CheckVisual.
            option_value: Initial value for OptionValue.
            target_value: Initial value for TargetValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if check_visual is not None:
            self.check_visual = check_visual
        if option_value is not None:
            self.option_value = option_value
        if target_value is not None:
            self.target_value = target_value

    @property
    def check_visual(self) -> str | None:
        """Target ID of the CheckVisual reference (targets IField[bool])."""
        member = self.get_member("CheckVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @check_visual.setter
    def check_visual(self, target: str | IField[bool] | None) -> None:
        """Set the CheckVisual reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("CheckVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CheckVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def option_value(self) -> T | None:
        """The OptionValue field value (type depends on type parameter)."""
        member = self.get_member("OptionValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @option_value.setter
    def option_value(self, value: T) -> None:
        """Set the OptionValue field value."""
        member = self.get_member("OptionValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "OptionValue", self._type_info.field_class(value=value)
            )

    @property
    def target_value(self) -> str | None:
        """Target ID of the TargetValue reference (targets IField[T])."""
        member = self.get_member("TargetValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_value.setter
    def target_value(self, target: str | IField[T] | None) -> None:
        """Set the TargetValue reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

