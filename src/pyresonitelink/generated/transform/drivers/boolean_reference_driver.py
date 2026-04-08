"""Generated component: BooleanReferenceDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BooleanReferenceDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BooleanReferenceDriver<>.

    Category: Transform/Drivers

    Parameterize with a value type::

        BooleanReferenceDriver[primitives.Float]
        BooleanReferenceDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BooleanReferenceDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.BooleanReferenceDriver<>"

    def __init__(self, state: primitives.Bool | None = None, target_reference: str | SyncRef[T] | None = None, false_target: str | T | None = None, true_target: str | T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            state: Initial value for State.
            target_reference: Initial value for TargetReference.
            false_target: Initial value for FalseTarget.
            true_target: Initial value for TrueTarget.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if state is not None:
            self.state = state
        if target_reference is not None:
            self.target_reference = target_reference
        if false_target is not None:
            self.false_target = false_target
        if true_target is not None:
            self.true_target = true_target

    @property
    def state(self) -> primitives.Bool | None:
        """The State field value."""
        member = self.get_member("State")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @state.setter
    def state(self, value: primitives.Bool) -> None:
        """Set the State field value."""
        member = self.get_member("State")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "State", fields.FieldBool(value=value)
            )

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
    def false_target(self) -> str | None:
        """Target ID of the FalseTarget reference (targets T)."""
        member = self.get_member("FalseTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @false_target.setter
    def false_target(self, target: str | T | None) -> None:
        """Set the FalseTarget reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("FalseTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FalseTarget",
                members.Reference(targetId=target_id, targetType='T'),
            )

    @property
    def true_target(self) -> str | None:
        """Target ID of the TrueTarget reference (targets T)."""
        member = self.get_member("TrueTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @true_target.setter
    def true_target(self, target: str | T | None) -> None:
        """Set the TrueTarget reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("TrueTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TrueTarget",
                members.Reference(targetId=target_id, targetType='T'),
            )

