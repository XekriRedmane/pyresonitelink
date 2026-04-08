"""Generated component: SetType."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync_type import SyncType
from pyresonitelink.generated._types.iundoable import IUndoable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SetType(GeneratedComponent, IUndoable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Undo.SetType.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Undo.SetType"

    def __init__(self, target: str | SyncType | None = None, performed: primitives.Bool | None = None, description: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            performed: Initial value for _performed.
            description: Initial value for _description.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if performed is not None:
            self.performed = performed
        if description is not None:
            self.description = description

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets SyncType)."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | SyncType | None) -> None:
        """Set the Target reference by target ID or SyncType instance."""
        target_id: str | None = target.id if isinstance(target, SyncType) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncType'),
            )

    @property
    def value_before(self) -> members.FieldEnum | None:
        """The ValueBefore member."""
        member = self.get_member("ValueBefore")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @value_before.setter
    def value_before(self, value: members.FieldEnum) -> None:
        """Set the ValueBefore member."""
        self.set_member("ValueBefore", value)

    @property
    def value_after(self) -> members.FieldEnum | None:
        """The ValueAfter member."""
        member = self.get_member("ValueAfter")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @value_after.setter
    def value_after(self, value: members.FieldEnum) -> None:
        """Set the ValueAfter member."""
        self.set_member("ValueAfter", value)

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

