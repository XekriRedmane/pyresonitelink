"""Generated component: BagEditorItem."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_element import IWorldElement
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BagEditorItem(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The BagEditorItem component is used in conjunction with a BagEditor. This is a reference to an item in the bag. For more information, please see the page on BagEditor.

    See BagEditor.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BagEditorItem"

    def __init__(self, item: str | IWorldElement | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            item: Initial value for Item.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if item is not None:
            self.item = item

    @property
    def item(self) -> str | None:
        """The bag item this is referencing."""
        member = self.get_member("Item")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item.setter
    def item(self, target: str | IWorldElement | None) -> None:
        """Set the Item reference by target ID or IWorldElement instance."""
        target_id: str | None = target.id if isinstance(target, IWorldElement) else target  # type: ignore[assignment]
        member = self.get_member("Item")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Item",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IWorldElement'),
            )

