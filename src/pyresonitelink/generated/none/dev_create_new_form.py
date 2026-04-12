"""Generated component: DevCreateNewForm."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ideveloper_interface import IDeveloperInterface
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DevCreateNewForm(GeneratedComponent, IDeveloperInterface, IWorldEventReceiver):
    """See Create New Wizard.

    See Create New Wizard.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DevCreateNewForm"

    def __init__(self, category_root: primitives.String | None = None, content_root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            category_root: Initial value for CategoryRoot.
            content_root: Initial value for _contentRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if category_root is not None:
            self.category_root = category_root
        if content_root is not None:
            self.content_root = content_root

    @property
    def category_root(self) -> primitives.String | None:
        """The current location in the create menu we are at."""
        member = self.get_member("CategoryRoot")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @category_root.setter
    def category_root(self, value: primitives.String) -> None:
        """Set the CategoryRoot field value."""
        member = self.get_member("CategoryRoot")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CategoryRoot", fields.FieldString(value=value)
            )

    @property
    def content_root(self) -> str | None:
        """Where to list content like buttons and such."""
        member = self.get_member("_contentRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @content_root.setter
    def content_root(self, target: str | Slot | None) -> None:
        """Set the _contentRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_contentRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_contentRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

