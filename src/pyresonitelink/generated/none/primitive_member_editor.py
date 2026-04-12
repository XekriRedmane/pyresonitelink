"""Generated component: PrimitiveMemberEditor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.text_editor import TextEditor
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PrimitiveMemberEditor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The PrimitiveMemberEditor component is a lower-level component for accessing and editing the members of a particular primitive element. Its intention is for use in Scene Inspectors, since they use a text field to drive member properties, but it can be more generally used on player-made objects as well. It is also, as indicated by a big warning on it, commonly used for Ref Hacking due to being able to read and write the ``id`` field of a RefID.

    This component needs, at minimum, ``_target`` to point to an element
    with fields, a ``_textDrive`` that points to the ``Content`` field of a
    component implementing IText, and a ``_textEditor`` that points to a
    TextEditor with its ``Text`` field pointing to the to the aforementioned
    IText component. The ``_textDrive`` field acts as a drive with write
    back, allowing one to interface with the field it points to, by way of a
    Write node or the ``_textEditor``, to change the ``_target`` via the
    text field. Additionally, there exists three Sync Delegates one may
    apply to the ``_textEditor``. These sync delegates are not strictly
    required for functionality of the component, but they do make the
    editing experience nicer if one hooks some editable field up to the
    TextEditor. ``EditingStarted`` breaks the ``_textDrive`` drive when
    called, allowing for more flexible editing by not requiring the text
    always be a parsable number. ``EditingChanged`` is only functional when
    ``Continuous`` is used, and it writes the current text to the
    ``_target`` every time the text is changed, hence being continuous.
    ``EditingFinished`` restores the ``_textDrive`` to before and writes the
    text value into ``_target``, and is required for proper functionality of
    this component if ``EditingStarted`` is also used. The final sync
    delegate of the component, ``OnReset``, is not needed unless one wishes
    to add a reset button. When it is called, it will simply reset the
    ``_target`` value to the type's default value. One may fill in the
    ``_button`` and ``_resetButton`` fields. These fields are not too
    terribly useful, as they don't provide much functionality themselves
    (rather the Sync Delegates do), but they are used when internally
    building the Inspector UI and when any part of the component is changed.
    When any part of the component changes, including when the field it is
    pointing to is edited, if ``_button`` is filled, all colors in the
    ``ColorDrivers`` list will be set to the first color drive. If
    ``_resetButton`` is filled, its slot will disable if the field that the
    component is editing is not a string, which can be worked around by
    driving the ``Enabled`` state of the slot to ``true``.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PrimitiveMemberEditor"

    def __init__(self, continuous: primitives.Bool | None = None, path: primitives.String | None = None, target: str | IField | None = None, format_: primitives.String | None = None, text_editor: str | TextEditor | None = None, text_drive: str | IField[primitives.String] | None = None, button: str | Button | None = None, reset_button: str | Button | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            continuous: Initial value for Continuous.
            path: Initial value for _path.
            target: Initial value for _target.
            format_: Initial value for Format.
            text_editor: Initial value for _textEditor.
            text_drive: Initial value for _textDrive.
            button: Initial value for _button.
            reset_button: Initial value for _resetButton.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if continuous is not None:
            self.continuous = continuous
        if path is not None:
            self.path = path
        if target is not None:
            self.target = target
        if format_ is not None:
            self.format_ = format_
        if text_editor is not None:
            self.text_editor = text_editor
        if text_drive is not None:
            self.text_drive = text_drive
        if button is not None:
            self.button = button
        if reset_button is not None:
            self.reset_button = reset_button

    @property
    def continuous(self) -> primitives.Bool | None:
        """Whether to update the target field while editing the text field. If disabled, it will only update at the end of editing."""
        member = self.get_member("Continuous")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @continuous.setter
    def continuous(self, value: primitives.Bool) -> None:
        """Set the Continuous field value."""
        member = self.get_member("Continuous")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Continuous", fields.FieldBool(value=value)
            )

    @property
    def path(self) -> primitives.String | None:
        """Member path of target element field to access/edit."""
        member = self.get_member("_path")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @path.setter
    def path(self, value: primitives.String) -> None:
        """Set the _path field value."""
        member = self.get_member("_path")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_path", fields.FieldString(value=value)
            )

    @property
    def target(self) -> str | None:
        """The primitive element to access/edit."""
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField | None) -> None:
        """Set the _target reference by target ID or IField instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField'),
            )

    @property
    def format_(self) -> primitives.String | None:
        """The format for representing the target primitive. About the same as the Format field for the To String node, but only works on a limited set of primitives."""
        member = self.get_member("Format")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @format_.setter
    def format_(self, value: primitives.String) -> None:
        """Set the Format field value."""
        member = self.get_member("Format")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Format", fields.FieldString(value=value)
            )

    @property
    def text_editor(self) -> str | None:
        """The TextEditor that points to any component that implements the IText type used for ``_textDrive``."""
        member = self.get_member("_textEditor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_editor.setter
    def text_editor(self, target: str | TextEditor | None) -> None:
        """Set the _textEditor reference by target ID or TextEditor instance."""
        target_id: str | None = target.id if isinstance(target, TextEditor) else target  # type: ignore[assignment]
        member = self.get_member("_textEditor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textEditor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextEditor'),
            )

    @property
    def text_drive(self) -> str | None:
        """Text field used as an interface to the member. Should be the ``Content`` field of a component implementing IText."""
        member = self.get_member("_textDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_drive.setter
    def text_drive(self, target: str | IField[primitives.String] | None) -> None:
        """Set the _textDrive reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_textDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def button(self) -> str | None:
        """Button used for editing, like on a TextField."""
        member = self.get_member("_button")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @button.setter
    def button(self, target: str | Button | None) -> None:
        """Set the _button reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_button")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_button",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def reset_button(self) -> str | None:
        """Button used to reset the value. Intended to only be used for strings."""
        member = self.get_member("_resetButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reset_button.setter
    def reset_button(self, target: str | Button | None) -> None:
        """Set the _resetButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_resetButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_resetButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

