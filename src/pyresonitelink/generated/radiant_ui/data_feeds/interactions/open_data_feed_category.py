"""Generated component: OpenDataFeedCategory."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idata_feed_view import IDataFeedView
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OpenDataFeedCategory(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """The OpenDataFeedCategory component receives Button Events and will open the Category with the path defined by the list ``CategorySubpath``.

    Category: Radiant UI/Data Feeds/Interactions

    Add to a slot with a button and provide a path list for this component
    and it will start working.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.OpenDataFeedCategory"

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
        """The view to change the directory for."""
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

    @property
    def category_subpath(self) -> members.SyncList | None:
        """A list of path directories (Like a folder path split by the slashes) to define the category to go to starting from root for ``View``."""
        member = self.get_member("CategorySubpath")
        if isinstance(member, members.SyncList):
            return member
        return None

    @category_subpath.setter
    def category_subpath(self, value: members.SyncList) -> None:
        """Set CategorySubpath. A list of path directories (Like a folder path split by the slashes) to define the category to go to starting from root for ``View``."""
        self.set_member("CategorySubpath", value)

