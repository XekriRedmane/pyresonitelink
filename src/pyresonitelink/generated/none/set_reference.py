"""Generated component: SetReference."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.iundoable import IUndoable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SetReference(GenericComponent[T], IUndoable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Undo.SetReference<>.

    Parameterize with a value type::

        SetReference[primitives.Float]
        SetReference[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Undo.SetReference<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.Undo.SetReference<>"

    def __init__(self, target: str | SyncRef[T] | None = None, target_before: str | T | None = None, target_after: str | T | None = None, performed: primitives.Bool | None = None, description: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            target_before: Initial value for TargetBefore.
            target_after: Initial value for TargetAfter.
            performed: Initial value for _performed.
            description: Initial value for _description.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if target_before is not None:
            self.target_before = target_before
        if target_after is not None:
            self.target_after = target_after
        if performed is not None:
            self.performed = performed
        if description is not None:
            self.description = description

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets SyncRef[T])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | SyncRef[T] | None) -> None:
        """Set the Target reference by target ID or SyncRef[T] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<T>'),
            )

    @property
    def target_before(self) -> str | None:
        """Target ID of the TargetBefore reference (targets T)."""
        member = self.get_member("TargetBefore")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_before.setter
    def target_before(self, target: str | T | None) -> None:
        """Set the TargetBefore reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("TargetBefore")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetBefore",
                members.Reference(targetId=target_id, targetType='T'),
            )

    @property
    def target_after(self) -> str | None:
        """Target ID of the TargetAfter reference (targets T)."""
        member = self.get_member("TargetAfter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_after.setter
    def target_after(self, target: str | T | None) -> None:
        """Set the TargetAfter reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("TargetAfter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetAfter",
                members.Reference(targetId=target_id, targetType='T'),
            )

    @property
    def performed(self) -> primitives.Bool | None:
        """The _performed field value."""
        member = self.get_member("_performed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @performed.setter
    def performed(self, value: primitives.Bool) -> None:
        """Set the _performed field value."""
        member = self.get_member("_performed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_performed", fields.FieldBool(value=value)
            )

    @property
    def description(self) -> primitives.String | None:
        """The _description field value."""
        member = self.get_member("_description")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @description.setter
    def description(self, value: primitives.String) -> None:
        """Set the _description field value."""
        member = self.get_member("_description")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_description", fields.FieldString(value=value)
            )

