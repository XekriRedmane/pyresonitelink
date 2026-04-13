"""Generated component: ContentSizeFitter."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._enums.size_fit import SizeFit
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ilayout_element import ILayoutElement
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ContentSizeFitter(GeneratedComponent, ILayoutElement, IUIComputeComponent, IWorldEventReceiver):
    """The ContentSizeFitter resizes the slots's RectTransform to fit the minimum or preferred size of its other layout components in width or height. In effect, it "shrink-wraps" its contents.

Note that this does not include its children slots, and only works on slots that have a layout component. For working with children, the parent with the ContentSizeFitter needs to also have a HorizontalLayout, VerticalLayout, or GridLayout component. LayoutElement is also a layout component, as is Text and Image.

}}

Fit modes are:
- Disabled: Don't perform any resizing.
- MinSize: Resize to the minimum size of the content.
- PreferredSize: Resize to the preferred size of the content.

    Category: UIX/Layout

    This is used for a polished look of keeping your contents in the bounds
    of a UIX element.

    **Behavior**: The ContentSizeFitter functions as a layout controller that controls the size of its own layout component. The size is determined by the minimum or preferred sizes provided by layout components its own slot. Such layout components can be Image or Text components, VerticalLayout, HorizontalLayout, or a LayoutElement component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.ContentSizeFitter"

    def __init__(self, horizontal_fit: SizeFit | str | None = None, vertical_fit: SizeFit | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            horizontal_fit: Initial value for HorizontalFit.
            vertical_fit: Initial value for VerticalFit.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if horizontal_fit is not None:
            self.horizontal_fit = horizontal_fit
        if vertical_fit is not None:
            self.vertical_fit = vertical_fit

    @property
    def horizontal_fit(self) -> SizeFit | None:
        """The fit mode to use to determine the width."""
        member = self.get_member("HorizontalFit")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SizeFit(member.value)
        return None

    @horizontal_fit.setter
    def horizontal_fit(self, value: SizeFit | str) -> None:
        """Set HorizontalFit. The fit mode to use to determine the width."""
        member = self.get_member("HorizontalFit")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "HorizontalFit",
                members.FieldEnum(value=str(value)),
            )

    @property
    def vertical_fit(self) -> SizeFit | None:
        """The fit mode to use to determine the height."""
        member = self.get_member("VerticalFit")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SizeFit(member.value)
        return None

    @vertical_fit.setter
    def vertical_fit(self, value: SizeFit | str) -> None:
        """Set VerticalFit. The fit mode to use to determine the height."""
        member = self.get_member("VerticalFit")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "VerticalFit",
                members.FieldEnum(value=str(value)),
            )

