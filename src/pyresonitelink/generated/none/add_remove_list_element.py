"""Generated component: AddRemoveListElement."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.sync_list import SyncList
from pyresonitelink.generated._types.saved_reference_table import SavedReferenceTable
from pyresonitelink.generated._types.iundoable import IUndoable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AddRemoveListElement(GenericComponent[T], IUndoable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Undo.AddRemoveListElement<>.

    Parameterize with a value type::

        AddRemoveListElement[np.float32]
        AddRemoveListElement[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Undo.AddRemoveListElement<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.Undo.AddRemoveListElement<>"

    def __init__(self, target_list: str | SyncList[T] | None = None, target_element: str | T | None = None, description: str | None = None, saved_object: str | None = None, reference_table: str | SavedReferenceTable | None = None, is_saving: bool | None = None, performed: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_list: Initial value for TargetList.
            target_element: Initial value for TargetElement.
            description: Initial value for _description.
            saved_object: Initial value for _savedObject.
            reference_table: Initial value for _referenceTable.
            is_saving: Initial value for _isSaving.
            performed: Initial value for _performed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_list is not None:
            self.target_list = target_list
        if target_element is not None:
            self.target_element = target_element
        if description is not None:
            self.description = description
        if saved_object is not None:
            self.saved_object = saved_object
        if reference_table is not None:
            self.reference_table = reference_table
        if is_saving is not None:
            self.is_saving = is_saving
        if performed is not None:
            self.performed = performed

    @property
    def target_list(self) -> str | None:
        """Target ID of the TargetList reference (targets SyncList[T])."""
        member = self.get_member("TargetList")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_list.setter
    def target_list(self, target: str | SyncList[T] | None) -> None:
        """Set the TargetList reference by target ID or SyncList[T] instance."""
        target_id: str | None = target.id if isinstance(target, SyncList) else target  # type: ignore[assignment]
        member = self.get_member("TargetList")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetList",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncList<T>'),
            )

    @property
    def target_element(self) -> str | None:
        """Target ID of the TargetElement reference (targets T)."""
        member = self.get_member("TargetElement")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_element.setter
    def target_element(self, target: str | T | None) -> None:
        """Set the TargetElement reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("TargetElement")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetElement",
                members.Reference(targetId=target_id, targetType='T'),
            )

    @property
    def description(self) -> str | None:
        """The _description field value."""
        member = self.get_member("_description")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @description.setter
    def description(self, value: str) -> None:
        """Set the _description field value."""
        member = self.get_member("_description")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_description", fields.FieldString(value=value)
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
    def is_saving(self) -> bool | None:
        """The _isSaving field value."""
        member = self.get_member("_isSaving")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_saving.setter
    def is_saving(self, value: bool) -> None:
        """Set the _isSaving field value."""
        member = self.get_member("_isSaving")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_isSaving", fields.FieldBool(value=value)
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
    def performed(self) -> bool | None:
        """The _performed field value."""
        member = self.get_member("_performed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @performed.setter
    def performed(self, value: bool) -> None:
        """Set the _performed field value."""
        member = self.get_member("_performed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_performed", fields.FieldBool(value=value)
            )

