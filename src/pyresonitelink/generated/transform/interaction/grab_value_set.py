"""Generated component: GrabValueSet."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.igrab_event_receiver import IGrabEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabValueSet(GenericComponent[T], IGrabEventReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GrabValueSet<>.

    Category: Transform/Interaction

    Parameterize with a value type::

        GrabValueSet[np.float32]
        GrabValueSet[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabValueSet<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.GrabValueSet<>"

    def __init__(self, target: str | IField[T] | None = None, grabbed_value: T | None = None, released_value: T | None = None, set_on_grabbed: bool | None = None, set_on_released: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            grabbed_value: Initial value for GrabbedValue.
            released_value: Initial value for ReleasedValue.
            set_on_grabbed: Initial value for SetOnGrabbed.
            set_on_released: Initial value for SetOnReleased.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if grabbed_value is not None:
            self.grabbed_value = grabbed_value
        if released_value is not None:
            self.released_value = released_value
        if set_on_grabbed is not None:
            self.set_on_grabbed = set_on_grabbed
        if set_on_released is not None:
            self.set_on_released = set_on_released

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[T])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[T] | None) -> None:
        """Set the Target reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def grabbed_value(self) -> T | None:
        """The GrabbedValue field value (type depends on type parameter)."""
        member = self.get_member("GrabbedValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grabbed_value.setter
    def grabbed_value(self, value: T) -> None:
        """Set the GrabbedValue field value."""
        member = self.get_member("GrabbedValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "GrabbedValue", self._type_info.field_class(value=value)
            )

    @property
    def released_value(self) -> T | None:
        """The ReleasedValue field value (type depends on type parameter)."""
        member = self.get_member("ReleasedValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @released_value.setter
    def released_value(self, value: T) -> None:
        """Set the ReleasedValue field value."""
        member = self.get_member("ReleasedValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "ReleasedValue", self._type_info.field_class(value=value)
            )

    @property
    def set_on_grabbed(self) -> bool | None:
        """The SetOnGrabbed field value."""
        member = self.get_member("SetOnGrabbed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @set_on_grabbed.setter
    def set_on_grabbed(self, value: bool) -> None:
        """Set the SetOnGrabbed field value."""
        member = self.get_member("SetOnGrabbed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetOnGrabbed", fields.FieldBool(value=value)
            )

    @property
    def set_on_released(self) -> bool | None:
        """The SetOnReleased field value."""
        member = self.get_member("SetOnReleased")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @set_on_released.setter
    def set_on_released(self, value: bool) -> None:
        """Set the SetOnReleased field value."""
        member = self.get_member("SetOnReleased")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetOnReleased", fields.FieldBool(value=value)
            )

