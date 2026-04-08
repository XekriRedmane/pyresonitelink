"""Generated component: ValueFieldProxySource."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iui_grabbable import IUIGrabbable
from pyresonitelink.generated._types.ivalue_field_proxy_source import IValueFieldProxySource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueFieldProxySource(GenericComponent[T], IUIGrabbable, IValueFieldProxySource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ValueFieldProxySource<>.

    Category: UIX/Interaction

    Parameterize with a value type::

        ValueFieldProxySource[primitives.Float]
        ValueFieldProxySource[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueFieldProxySource<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ValueFieldProxySource<>"

    def __init__(self, field: str | IField[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            field: Initial value for Field.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if field is not None:
            self.field = field

    @property
    def field(self) -> str | None:
        """Target ID of the Field reference (targets IField[T])."""
        member = self.get_member("Field")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @field.setter
    def field(self, target: str | IField[T] | None) -> None:
        """Set the Field reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Field")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Field",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

