"""Generated component: ValueEqualityDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueEqualityDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """The ValueEqualityDriver component lets you drive a boolean to whether or not one value is equal to another.

    Category: Transform/Drivers

    Use to drive the target boolean with whether the target's value is equal
    to the reference value.

    Parameterize with a value type::

        ValueEqualityDriver[primitives.Float]
        ValueEqualityDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueEqualityDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ValueEqualityDriver<>"

    def __init__(self, target_value: str | IField[T] | None = None, reference: T | None = None, target: str | IField[primitives.Bool] | None = None, invert: primitives.Bool | None = None, use_approximate_comparison: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_value: Initial value for TargetValue.
            reference: Initial value for Reference.
            target: Initial value for Target.
            invert: Initial value for Invert.
            use_approximate_comparison: Initial value for UseApproximateComparison.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_value is not None:
            self.target_value = target_value
        if reference is not None:
            self.reference = reference
        if target is not None:
            self.target = target
        if invert is not None:
            self.invert = invert
        if use_approximate_comparison is not None:
            self.use_approximate_comparison = use_approximate_comparison

    @property
    def target_value(self) -> str | None:
        """The value being compared to ``Reference``."""
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

    @property
    def reference(self) -> T | None:
        """The Reference field value (type depends on type parameter)."""
        member = self.get_member("Reference")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reference.setter
    def reference(self, value: T) -> None:
        """Set the Reference field value."""
        member = self.get_member("Reference")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Reference", self._type_info.field_class(value=value)
            )

    @property
    def target(self) -> str | None:
        """The boolean that is driven to true if ``TargetValue`` is equal to ``Reference`` and false if it isn't."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def invert(self) -> primitives.Bool | None:
        """Whether to invert the result of ``TargetValue``"""
        member = self.get_member("Invert")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @invert.setter
    def invert(self, value: primitives.Bool) -> None:
        """Set the Invert field value."""
        member = self.get_member("Invert")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Invert", fields.FieldBool(value=value)
            )

    @property
    def use_approximate_comparison(self) -> primitives.Bool | None:
        """Whether or not to use approximate comparison for types such as float, where values that seem identical can be very slightly different."""
        member = self.get_member("UseApproximateComparison")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_approximate_comparison.setter
    def use_approximate_comparison(self, value: primitives.Bool) -> None:
        """Set the UseApproximateComparison field value."""
        member = self.get_member("UseApproximateComparison")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseApproximateComparison", fields.FieldBool(value=value)
            )

