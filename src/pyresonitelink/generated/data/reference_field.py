"""Generated component: ReferenceField."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ireference_source import IReferenceSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceField(GenericComponent[T], IReferenceSource[T], IWorldEventReceiver):
    """Reference Field is a component that is able to store a reference for later use, as long as the reference still exists by then.

    Category: Data

    This can be used in tandem with a Reference Grab Receiver Component as a
    place to store the value received by said component. This component's
    ``Reference`` field can be accessed with ProtoFlux. Using this as a Data
    Model Store is considered bad practice due to it making your code harder
    to read, use, and transfer.

    Parameterize with a value type::

        ReferenceField[primitives.Float]
        ReferenceField[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReferenceField<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ReferenceField<>"

    def __init__(self, reference: str | T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            reference: Initial value for Reference.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if reference is not None:
            self.reference = reference

    @property
    def reference(self) -> str | None:
        """A field that can be used to store any reference type."""
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference.setter
    def reference(self, target: str | T | None) -> None:
        """Set the Reference reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Reference",
                members.Reference(targetId=target_id, targetType='T'),
            )

