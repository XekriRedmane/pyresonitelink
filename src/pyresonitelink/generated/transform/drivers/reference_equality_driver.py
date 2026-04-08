"""Generated component: ReferenceEqualityDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceEqualityDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ReferenceEqualityDriver<>.

    Category: Transform/Drivers

    Parameterize with a value type::

        ReferenceEqualityDriver[primitives.Float]
        ReferenceEqualityDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReferenceEqualityDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ReferenceEqualityDriver<>"

    def __init__(self, target_reference: str | SyncRef[T] | None = None, reference: str | T | None = None, target: str | IField[primitives.Bool] | None = None, invert: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_reference: Initial value for TargetReference.
            reference: Initial value for Reference.
            target: Initial value for Target.
            invert: Initial value for Invert.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_reference is not None:
            self.target_reference = target_reference
        if reference is not None:
            self.reference = reference
        if target is not None:
            self.target = target
        if invert is not None:
            self.invert = invert

    @property
    def target_reference(self) -> str | None:
        """Target ID of the TargetReference reference (targets SyncRef[T])."""
        member = self.get_member("TargetReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_reference.setter
    def target_reference(self, target: str | SyncRef[T] | None) -> None:
        """Set the TargetReference reference by target ID or SyncRef[T] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("TargetReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<T>'),
            )

    @property
    def reference(self) -> str | None:
        """Target ID of the Reference reference (targets T)."""
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

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[primitives.Bool])."""
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
        """The Invert field value."""
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

