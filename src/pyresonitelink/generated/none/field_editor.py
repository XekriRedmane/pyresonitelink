"""Generated component: FieldEditor."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FieldEditor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """A FieldEditor component takes an IField of any type and deconstructs it's elements into a list of editor components.

    Attach to a slot under a UIX Canvas hiearchy with a RectTransform and
    then insert an IField into ``_targetField`` to be edited for this
    component to generate an editor for the elements of the specified
    ``_targetField``.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FieldEditor"

    def __init__(self, target_field: str | IField | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_field: Initial value for _targetField.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_field is not None:
            self.target_field = target_field

    @property
    def target_field(self) -> str | None:
        """The field to generate an editor list for."""
        member = self.get_member("_targetField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_field.setter
    def target_field(self, target: str | IField | None) -> None:
        """Set the _targetField reference by target ID or IField instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_targetField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField'),
            )

    @property
    def text_editors(self) -> members.SyncList | None:
        """A list of text editors of the specified ``_targetField``'s components."""
        member = self.get_member("_textEditors")
        if isinstance(member, members.SyncList):
            return member
        return None

    @text_editors.setter
    def text_editors(self, value: members.SyncList) -> None:
        """Set _textEditors. A list of text editors of the specified ``_targetField``'s components."""
        self.set_member("_textEditors", value)

    @property
    def text_drives(self) -> members.SyncList | None:
        """A list of text value fields to drive with the contents of the components of the specified ``_targetField``."""
        member = self.get_member("_textDrives")
        if isinstance(member, members.SyncList):
            return member
        return None

    @text_drives.setter
    def text_drives(self, value: members.SyncList) -> None:
        """Set _textDrives. A list of text value fields to drive with the contents of the components of the specified ``_targetField``."""
        self.set_member("_textDrives", value)

