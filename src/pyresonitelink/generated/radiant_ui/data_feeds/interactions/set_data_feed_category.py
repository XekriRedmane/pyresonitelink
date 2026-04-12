"""Generated component: SetDataFeedCategory."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idata_feed_view import IDataFeedView
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SetDataFeedCategory(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """The SetDataFeedCategory sets the Path field for ``View`` when it receives a button event from a button on the same slot or somewhere else.

    Category: Radiant UI/Data Feeds/Interactions

    Attach to the same slot as an IButton and provide settings for this
    component in order for it to start working.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SetDataFeedCategory"

    def __init__(self, view: str | IDataFeedView | None = None, is_inside_category_path: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            view: Initial value for View.
            is_inside_category_path: Initial value for IsInsideCategoryPath.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if view is not None:
            self.view = view
        if is_inside_category_path is not None:
            self.is_inside_category_path = is_inside_category_path

    @property
    def view(self) -> str | None:
        """The view to change the Path for."""
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
    def category_path(self) -> members.SyncList | None:
        """What to set the path to for ``View``"""
        member = self.get_member("CategoryPath")
        if isinstance(member, members.SyncList):
            return member
        return None

    @category_path.setter
    def category_path(self, value: members.SyncList) -> None:
        """Set CategoryPath. What to set the path to for ``View``"""
        self.set_member("CategoryPath", value)

    @property
    def is_inside_category_path(self) -> primitives.Bool | None:
        """Whether the View is already under ``CategoryPath``."""
        member = self.get_member("IsInsideCategoryPath")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_inside_category_path.setter
    def is_inside_category_path(self, value: primitives.Bool) -> None:
        """Set the IsInsideCategoryPath field value."""
        member = self.get_member("IsInsideCategoryPath")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsInsideCategoryPath", fields.FieldBool(value=value)
            )

