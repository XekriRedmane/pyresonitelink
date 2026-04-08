"""Generated component: UserDistanceValueDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserDistanceValueDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UserDistanceValueDriver<>.

    Category: Transform/Drivers

    Parameterize with a value type::

        UserDistanceValueDriver[primitives.Float]
        UserDistanceValueDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserDistanceValueDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.UserDistanceValueDriver<>"

    def __init__(self, distance: primitives.Float | None = None, target_field: str | IField[T] | None = None, near_value: T | None = None, far_value: T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            distance: Initial value for Distance.
            target_field: Initial value for TargetField.
            near_value: Initial value for NearValue.
            far_value: Initial value for FarValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if distance is not None:
            self.distance = distance
        if target_field is not None:
            self.target_field = target_field
        if near_value is not None:
            self.near_value = near_value
        if far_value is not None:
            self.far_value = far_value

    @property
    def node(self) -> members.FieldEnum | None:
        """The Node member."""
        member = self.get_member("Node")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @node.setter
    def node(self, value: members.FieldEnum) -> None:
        """Set the Node member."""
        self.set_member("Node", value)

    @property
    def distance(self) -> primitives.Float | None:
        """The Distance field value."""
        member = self.get_member("Distance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distance.setter
    def distance(self, value: primitives.Float) -> None:
        """Set the Distance field value."""
        member = self.get_member("Distance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Distance", fields.FieldFloat(value=value)
            )

    @property
    def target_field(self) -> str | None:
        """Target ID of the TargetField reference (targets IField[T])."""
        member = self.get_member("TargetField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_field.setter
    def target_field(self, target: str | IField[T] | None) -> None:
        """Set the TargetField reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def near_value(self) -> T | None:
        """The NearValue field value (type depends on type parameter)."""
        member = self.get_member("NearValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_value.setter
    def near_value(self, value: T) -> None:
        """Set the NearValue field value."""
        member = self.get_member("NearValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "NearValue", self._type_info.field_class(value=value)
            )

    @property
    def far_value(self) -> T | None:
        """The FarValue field value (type depends on type parameter)."""
        member = self.get_member("FarValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_value.setter
    def far_value(self, value: T) -> None:
        """Set the FarValue field value."""
        member = self.get_member("FarValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "FarValue", self._type_info.field_class(value=value)
            )

