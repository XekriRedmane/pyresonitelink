"""Generated component: SetType."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.type_ import Type
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync_type import SyncType
from pyresonitelink.generated._types.iundoable import IUndoable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SetType(GeneratedComponent, IUndoable, IWorldEventReceiver):
    """Set type is a component that is part of the undo system. This stores an undo step for setting a type field.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Undo.SetType"

    def __init__(self, target: str | SyncType | None = None, value_before: Type | str | None = None, value_after: Type | str | None = None, performed: primitives.Bool | None = None, description: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            value_before: Initial value for ValueBefore.
            value_after: Initial value for ValueAfter.
            performed: Initial value for _performed.
            description: Initial value for _description.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if value_before is not None:
            self.value_before = value_before
        if value_after is not None:
            self.value_after = value_after
        if performed is not None:
            self.performed = performed
        if description is not None:
            self.description = description

    @property
    def target(self) -> str | None:
        """The value field for a type value that was changed."""
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
    def value_before(self) -> Type | None:
        """The value it was before edit."""
        member = self.get_member("ValueBefore")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Type(member.value)
        return None

    @value_before.setter
    def value_before(self, value: Type | str) -> None:
        """Set ValueBefore. The value it was before edit."""
        member = self.get_member("ValueBefore")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ValueBefore",
                members.FieldEnum(value=str(value)),
            )

    @property
    def value_after(self) -> Type | None:
        """The value it became after edit."""
        member = self.get_member("ValueAfter")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Type(member.value)
        return None

    @value_after.setter
    def value_after(self, value: Type | str) -> None:
        """Set ValueAfter. The value it became after edit."""
        member = self.get_member("ValueAfter")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ValueAfter",
                members.FieldEnum(value=str(value)),
            )

    @property
    def performed(self) -> primitives.Bool | None:
        """Whether this was done (true) or can be redone (false)"""
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
        """The description of this undo step for changing a type field."""
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

