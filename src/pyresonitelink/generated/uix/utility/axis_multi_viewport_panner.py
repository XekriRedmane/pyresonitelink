"""Generated component: AxisMultiViewportPanner."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.align_direction import AlignDirection
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AxisMultiViewportPanner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The AxisMultiViewportPanner component toggles through UIX element's active state, min and max of the RectTransform's anchor. This allows a user to make "pages" in UIX.

}}

    Category: UIX/Utility

    This is useful if you want to make a slideshow, tab pages for UIX, or
    anything that you want to have pan across for multiple pages in your
    design.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.AxisMultiViewportPanner"

    def __init__(self, viewport_index: primitives.Int | None = None, animation_time: primitives.Float | None = None, direction: AlignDirection | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            viewport_index: Initial value for ViewportIndex.
            animation_time: Initial value for AnimationTime.
            direction: Initial value for Direction.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if viewport_index is not None:
            self.viewport_index = viewport_index
        if animation_time is not None:
            self.animation_time = animation_time
        if direction is not None:
            self.direction = direction

    @property
    def viewport_index(self) -> primitives.Int | None:
        """The current focused viewport UIX element."""
        member = self.get_member("ViewportIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @viewport_index.setter
    def viewport_index(self, value: primitives.Int) -> None:
        """Set the ViewportIndex field value."""
        member = self.get_member("ViewportIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ViewportIndex", fields.FieldInt(value=value)
            )

    @property
    def animation_time(self) -> primitives.Float | None:
        """The time it takes to pan across to get to the selected viewport index."""
        member = self.get_member("AnimationTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @animation_time.setter
    def animation_time(self, value: primitives.Float) -> None:
        """Set the AnimationTime field value."""
        member = self.get_member("AnimationTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnimationTime", fields.FieldFloat(value=value)
            )

    @property
    def direction(self) -> AlignDirection | None:
        """The direction this animates to get to the selected viewport index."""
        member = self.get_member("Direction")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return AlignDirection(member.value)
        return None

    @direction.setter
    def direction(self, value: AlignDirection | str) -> None:
        """Set Direction. The direction this animates to get to the selected viewport index."""
        member = self.get_member("Direction")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Direction",
                members.FieldEnum(value=str(value)),
            )

    @property
    def viewports(self) -> members.SyncList | None:
        """The list of UIX element viewports to pan to."""
        member = self.get_member("Viewports")
        if isinstance(member, members.SyncList):
            return member
        return None

    @viewports.setter
    def viewports(self, value: members.SyncList) -> None:
        """Set Viewports. The list of UIX element viewports to pan to."""
        self.set_member("Viewports", value)

