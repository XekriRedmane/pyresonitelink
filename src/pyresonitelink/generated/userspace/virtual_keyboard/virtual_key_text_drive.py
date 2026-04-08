"""Generated component: VirtualKeyTextDrive."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.virtual_key import VirtualKey
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VirtualKeyTextDrive(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VirtualKeyTextDrive.

    Category: Userspace/Virtual Keyboard
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VirtualKeyTextDrive"

    def __init__(self, key: str | VirtualKey | None = None, text: str | IField[str] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            key: Initial value for Key.
            text: Initial value for Text.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if key is not None:
            self.key = key
        if text is not None:
            self.text = text

    @property
    def key(self) -> str | None:
        """Target ID of the Key reference (targets VirtualKey)."""
        member = self.get_member("Key")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @key.setter
    def key(self, target: str | VirtualKey | None) -> None:
        """Set the Key reference by target ID or VirtualKey instance."""
        target_id: str | None = target.id if isinstance(target, VirtualKey) else target  # type: ignore[assignment]
        member = self.get_member("Key")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Key",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.VirtualKey'),
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

