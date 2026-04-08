"""Generated component: ValueFieldProxy."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ivalue_source import IValueSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueFieldProxy(GenericComponent[T], IValueSource[T], IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ValueFieldProxy<>.

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
        """Target ID of the Source reference (targets IField[T])."""
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

