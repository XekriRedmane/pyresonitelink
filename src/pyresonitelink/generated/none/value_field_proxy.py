"""Generated component: ValueFieldProxy."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ivalue_source import IValueSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueFieldProxy(GenericComponent[T], IValueSource[T], IWorldEventReceiver):
    """The Value Field Proxy component is used to make a field accessible via grabbing when paired with a grabbable. See #Usage for more info.

    Used to make a grabbable object able to put a value into a field. This
    can be done by clicking with or letting go of the object while holding
    it and pointing at a collider that can recieve it. Examples of recievers
    include inspector fields, text fields, and number fields. These objects
    achieve this by using a ValueReceiver.

    Parameterize with a value type::

        ValueFieldProxy[primitives.Float]
        ValueFieldProxy[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueFieldProxy<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ValueFieldProxy<>"

    def __init__(self, source: str | IField[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source

    @property
    def source(self) -> str | None:
        """The field to relay into the grabbable behavior this component has when paired with a grabbable."""
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

