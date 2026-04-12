"""Generated component: ValueRadio."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueRadio(GenericComponent[T], IButtonPressReceiver, IWorldEventReceiver):
    """The ValueRadio component is a listener component that activates or deactivates slots using the ``CheckVisual`` field, based if a ``TargetValue`` matches the ``OptionValue`` field. When a match is found, the ``CheckVisual`` field will be set to true.

    Category: UIX/Interaction

    To function, the component simply needs to be attached to a slot that
    also has a button component attached to it. From then on, pressing that
    button will activate the ValueRadio, making it set its ``TargetValue``
    to its ``OptionValue``, which then also sets its ``CheckVisual`` to
    true. * This is useful for making forms that need one answer from many
    choices, a set of button that should only have one being active, and
    anything that requires only one activation from many things. * the
    ``CheckVisual`` field does not just have to be the active of a slot,
    this can be any IField bool, allowing users to be creative with how they
    want to structure their component's logic.

    Parameterize with a value type::

        ValueRadio[primitives.Float]
        ValueRadio[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.ValueRadio<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.UIX.ValueRadio<>"

    def __init__(self, check_visual: str | IField[primitives.Bool] | None = None, option_value: T | None = None, target_value: str | IField[T] | None = None, *, component: workers.Component | None = None) -> None:
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
        """The boolean that is driven to true whenever the ``TargetValue`` is equal to the ``OptionValue``"""
        member = self.get_member("CheckVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @check_visual.setter
    def check_visual(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the CheckVisual reference by target ID or IField[primitives.Bool] instance."""
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
        """The value to set when the button is pressed."""
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

