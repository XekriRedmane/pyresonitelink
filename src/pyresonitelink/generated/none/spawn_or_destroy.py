"""Generated component: SpawnOrDestroy."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.worker import Worker
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.saved_reference_table import SavedReferenceTable
from pyresonitelink.generated._types.iundoable import IUndoable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SpawnOrDestroy(GeneratedComponent, IUndoable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Undo.SpawnOrDestroy.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Undo.SpawnOrDestroy"

    def __init__(self, target: str | Worker | None = None, target_parent: str | Slot | None = None, preserve_assets: primitives.Bool | None = None, send_destroying_events: primitives.Bool | None = None, saved_object: str | None = None, is_component: primitives.Bool | None = None, reference_table: str | SavedReferenceTable | None = None, is_saving: primitives.Bool | None = None, description: primitives.String | None = None, performed: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            target_parent: Initial value for TargetParent.
            preserve_assets: Initial value for _preserveAssets.
            send_destroying_events: Initial value for _sendDestroyingEvents.
            saved_object: Initial value for _savedObject.
            is_component: Initial value for _isComponent.
            reference_table: Initial value for _referenceTable.
            is_saving: Initial value for _isSaving.
            description: Initial value for _description.
            performed: Initial value for _performed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if target_parent is not None:
            self.target_parent = target_parent
        if preserve_assets is not None:
            self.preserve_assets = preserve_assets
        if send_destroying_events is not None:
            self.send_destroying_events = send_destroying_events
        if saved_object is not None:
            self.saved_object = saved_object
        if is_component is not None:
            self.is_component = is_component
        if reference_table is not None:
            self.reference_table = reference_table
        if is_saving is not None:
            self.is_saving = is_saving
        if description is not None:
            self.description = description
        if performed is not None:
            self.performed = performed

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets Worker)."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | Worker | None) -> None:
        """Set the Target reference by target ID or Worker instance."""
        target_id: str | None = target.id if isinstance(target, Worker) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Worker'),
            )

    @property
    def target_parent(self) -> str | None:
        """Target ID of the TargetParent reference (targets Slot)."""
        member = self.get_member("TargetParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_parent.setter
    def target_parent(self, target: str | Slot | None) -> None:
        """Set the TargetParent reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("TargetParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def mode(self) -> members.FieldEnum | None:
        """The _mode member."""
        member = self.get_member("_mode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @mode.setter
    def mode(self, value: members.FieldEnum) -> None:
        """Set the _mode member."""
        self.set_member("_mode", value)

    @property
    def preserve_assets(self) -> primitives.Bool | None:
        """The _preserveAssets field value."""
        member = self.get_member("_preserveAssets")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preserve_assets.setter
    def preserve_assets(self, value: primitives.Bool) -> None:
        """Set the _preserveAssets field value."""
        member = self.get_member("_preserveAssets")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_preserveAssets", fields.FieldBool(value=value)
            )

    @property
    def send_destroying_events(self) -> primitives.Bool | None:
        """The _sendDestroyingEvents field value."""
        member = self.get_member("_sendDestroyingEvents")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @send_destroying_events.setter
    def send_destroying_events(self, value: primitives.Bool) -> None:
        """Set the _sendDestroyingEvents field value."""
        member = self.get_member("_sendDestroyingEvents")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_sendDestroyingEvents", fields.FieldBool(value=value)
            )

    @property
    def saved_object(self) -> str | None:
        """The _savedObject field value."""
        member = self.get_member("_savedObject")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @saved_object.setter
    def saved_object(self, value: str) -> None:
        """Set the _savedObject field value."""
        member = self.get_member("_savedObject")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_savedObject", fields.FieldUri(value=value)
            )

    @property
    def is_component(self) -> primitives.Bool | None:
        """The _isComponent field value."""
        member = self.get_member("_isComponent")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_component.setter
    def is_component(self, value: primitives.Bool) -> None:
        """Set the _isComponent field value."""
        member = self.get_member("_isComponent")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_isComponent", fields.FieldBool(value=value)
            )

    @property
    def reference_table(self) -> str | None:
        """Target ID of the _referenceTable reference (targets SavedReferenceTable)."""
        member = self.get_member("_referenceTable")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference_table.setter
    def reference_table(self, target: str | SavedReferenceTable | None) -> None:
        """Set the _referenceTable reference by target ID or SavedReferenceTable instance."""
        target_id: str | None = target.id if isinstance(target, SavedReferenceTable) else target  # type: ignore[assignment]
        member = self.get_member("_referenceTable")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_referenceTable",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SavedReferenceTable'),
            )

    @property
    def is_saving(self) -> primitives.Bool | None:
        """The _isSaving field value."""
        member = self.get_member("_isSaving")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_saving.setter
    def is_saving(self, value: primitives.Bool) -> None:
        """Set the _isSaving field value."""
        member = self.get_member("_isSaving")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_isSaving", fields.FieldBool(value=value)
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

