"""Generated component: ValueCopy."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueCopy(GenericComponent[T], IComponent, IWorldEventReceiver):
    """The ValueCopy component is used to ensure that a value from one field is the same as another field via a one-way relation or a two-way relation with writeback. The source and target types must be value types.

    Category: Transform/Drivers

    thumb|You can create a ValueCopy component quickly by dragging one
    drivable field to another using your laser. This context menu will let
    you choose what type of ValueCopy to create. This component ensures that
    the value in the ``Target`` field is equal to the value in the
    ``Source`` field. To do this, it drives the ``Target`` field to give it
    exclusive access to the value, then whenever the value in the ``Source``
    field updates, it will write the new value to the ``Target`` field. When
    ``WriteBack`` is enabled, the target field will have the ability to be
    changed. Changes made to the target field will then be written back to
    the source field. Using a ValueCopy from a field to itself will
    essentially make the field read-only. If WriteBack is enabled, it
    presents an interesting combination of the locality of drives and
    writing of values: It will make the value of the field local to each
    individual user. This may be used as a version of ValueUserOverride that
    doesn't do any kind of network writes, but it should be noted that users
    joining the session will first receive the value from the host user
    before it gets changed. As such, it should only be used when the value
    doesn't quite matter specifically or gets updated frequently.

    **See also**: * ReferenceCopy for the same behavior but with reference types.
* ValueMultiDriver for forming this relation to multiple target fields.
* ValueDriver for continuously updating a field from an IValue source rather than a field.

    Parameterize with a value type::

        ValueCopy[primitives.Float]
        ValueCopy[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueCopy<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ValueCopy<>"

    def __init__(self, source: str | IField[T] | None = None, target: str | IField[T] | None = None, write_back: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            target: Initial value for Target.
            write_back: Initial value for WriteBack.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if target is not None:
            self.target = target
        if write_back is not None:
            self.write_back = write_back

    @property
    def source(self) -> str | None:
        """The source to copy the value from."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IField[T] | None) -> None:
        """Set the Source reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def target(self) -> str | None:
        """The target to copy the value to."""
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
    def write_back(self) -> primitives.Bool | None:
        """Allow Target to write back to Source. See write backs."""
        member = self.get_member("WriteBack")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @write_back.setter
    def write_back(self, value: primitives.Bool) -> None:
        """Set the WriteBack field value."""
        member = self.get_member("WriteBack")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WriteBack", fields.FieldBool(value=value)
            )

