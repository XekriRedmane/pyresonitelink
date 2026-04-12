"""Generated component: TextExpandIndicator."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TextExpandIndicator(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The TextExpandIndicator component is used in inspectors to show whether or not a section like slots under another slot is expanded out and/or has any children items.

}}

    This component is combined with the Expander component to show the user
    that the expander has expanded, collapsed, or is empty using symbols.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.TextExpandIndicator"

    def __init__(self, text: str | IField[primitives.String] | None = None, section_root: str | Slot | None = None, children_root: str | Slot | None = None, closed: primitives.String | None = None, opened: primitives.String | None = None, empty: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            text: Initial value for Text.
            section_root: Initial value for SectionRoot.
            children_root: Initial value for ChildrenRoot.
            closed: Initial value for Closed.
            opened: Initial value for Opened.
            empty: Initial value for Empty.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if text is not None:
            self.text = text
        if section_root is not None:
            self.section_root = section_root
        if children_root is not None:
            self.children_root = children_root
        if closed is not None:
            self.closed = closed
        if opened is not None:
            self.opened = opened
        if empty is not None:
            self.empty = empty

    @property
    def text(self) -> str | None:
        """The text to drive with the dropdown indication."""
        member = self.get_member("Text")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text.setter
    def text(self, target: str | IField[primitives.String] | None) -> None:
        """Set the Text reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Text")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Text",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def section_root(self) -> str | None:
        """The slot where children items for a slot is placed for the UI visual."""
        member = self.get_member("SectionRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @section_root.setter
    def section_root(self, target: str | Slot | None) -> None:
        """Set the SectionRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("SectionRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SectionRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def children_root(self) -> str | None:
        """The slot to check for children slots to tell if it has children or not."""
        member = self.get_member("ChildrenRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @children_root.setter
    def children_root(self, target: str | Slot | None) -> None:
        """Set the ChildrenRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ChildrenRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ChildrenRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def closed(self) -> primitives.String | None:
        """The string to display when the section is closed."""
        member = self.get_member("Closed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @closed.setter
    def closed(self, value: primitives.String) -> None:
        """Set the Closed field value."""
        member = self.get_member("Closed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Closed", fields.FieldString(value=value)
            )

    @property
    def opened(self) -> primitives.String | None:
        """The string to display when the section is opened."""
        member = self.get_member("Opened")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @opened.setter
    def opened(self, value: primitives.String) -> None:
        """Set the Opened field value."""
        member = self.get_member("Opened")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Opened", fields.FieldString(value=value)
            )

    @property
    def empty(self) -> primitives.String | None:
        """The string to display when ``ChildrenRoot`` is empty."""
        member = self.get_member("Empty")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @empty.setter
    def empty(self, value: primitives.String) -> None:
        """Set the Empty field value."""
        member = self.get_member("Empty")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Empty", fields.FieldString(value=value)
            )

