"""Generated component: MoveUpDataFeedCategory."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idata_feed_view import IDataFeedView
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MoveUpDataFeedCategory(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """The MoveUpDataFeedCategory is a component that receives Button Events and goes to the previous parent path in a Data Feed view.

    Category: Radiant UI/Data Feeds/Interactions

    Used to go up one in the category view.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MoveUpDataFeedCategory"

    def __init__(self, view: str | IDataFeedView | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            view: Initial value for View.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if view is not None:
            self.view = view

    @property
    def view(self) -> str | None:
        """The view to go up in category for."""
        member = self.get_member("View")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @view.setter
    def view(self, target: str | IDataFeedView | None) -> None:
        """Set the View reference by target ID or IDataFeedView instance."""
        target_id: str | None = target.id if isinstance(target, IDataFeedView) else target  # type: ignore[assignment]
        member = self.get_member("View")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "View",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IDataFeedView'),
            )

