"""Generated component: AvatarRoot."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iavatar_object import IAvatarObject
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarRoot(GeneratedComponent, IAvatarObject, ITouchable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarRoot.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarRoot"

    def __init__(self, scale: primitives.Float3 | None = None, original_parent: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            scale: Initial value for Scale.
            original_parent: Initial value for _originalParent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if scale is not None:
            self.scale = scale
        if original_parent is not None:
            self.original_parent = original_parent

    @property
    def scale(self) -> primitives.Float3 | None:
        """The Scale field value."""
        member = self.get_member("Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale.setter
    def scale(self, value: primitives.Float3) -> None:
        """Set the Scale field value."""
        member = self.get_member("Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Scale", fields.FieldFloat3(value=value)
            )

    @property
    def original_parent(self) -> str | None:
        """Target ID of the _originalParent reference (targets Slot)."""
        member = self.get_member("_originalParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @original_parent.setter
    def original_parent(self, target: str | Slot | None) -> None:
        """Set the _originalParent reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_originalParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_originalParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

