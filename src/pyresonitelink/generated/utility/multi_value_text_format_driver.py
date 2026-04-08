"""Generated component: MultiValueTextFormatDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MultiValueTextFormatDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.MultiValueTextFormatDriver.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MultiValueTextFormatDriver"

    def __init__(self, format_: str | None = None, text: str | IField[str] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            format_: Initial value for Format.
            text: Initial value for Text.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if format_ is not None:
            self.format_ = format_
        if text is not None:
            self.text = text

    @property
    def sources(self) -> members.SyncList | None:
        """The Sources member."""
        member = self.get_member("Sources")
        if isinstance(member, members.SyncList):
            return member
        return None

    @sources.setter
    def sources(self, value: members.SyncList) -> None:
        """Set the Sources member."""
        self.set_member("Sources", value)

    @property
    def format_(self) -> str | None:
        """The Format field value."""
        member = self.get_member("Format")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @format_.setter
    def format_(self, value: str) -> None:
        """Set the Format field value."""
        member = self.get_member("Format")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Format", fields.FieldString(value=value)
            )

    @property
    def text(self) -> str | None:
        """Target ID of the Text reference (targets IField[str])."""
        member = self.get_member("Text")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text.setter
    def text(self, target: str | IField[str] | None) -> None:
        """Set the Text reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Text")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Text",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

