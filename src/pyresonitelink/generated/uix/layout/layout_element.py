"""Generated component: LayoutElement."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ilayout_element import ILayoutElement
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LayoutElement(GeneratedComponent, ILayoutElement, IUIComputeComponent, IWorldEventReceiver):
    """LayoutElement is a component used within UIX, instructing components in slots above it in its hierarchy about how large it would like to be in a variety of dimensions and configurations within the UIX Layout flow. It is often used in combination with various other Layout components such as HorizontalLayout or VerticalLayout. By configuring its various properties, you can achieve a wide variety of effects and layouts.

Many of these values may have unclear meaning, even with the table below. Please see the behavior section for more information.
}}

    Category: UIX/Layout

    LayoutElement is used to inform UIX Layout Components in the layout
    containers and slots above it within the hierarchy about what size it
    should be. This information is then used within the UIX Layout process
    with any other UIX Elements to determine an overall Layout. For Width
    and Height there are 3 Properties which are used as a sort of
    negotiation with the UIX layout to determine the final size of an
    element. Other processes are involved but when it comes to just the
    layout element, the negotiation uses the following method: # Ensure that
    the element is at least MinWidth/MinHeight in terms of units. If a
    layout element does not fit inside a parent container/RectTransform it
    will cause Overflow if these Minimums are too large. # If there's enough
    space, give this element its PreferredWidth/PreferredHeight space in
    units. If there is not enough space for the "Preferred" value it will
    use a number that is between the "Min" value and the "Preferred" value.
    # After both 1 and 2, if there is space available and the "Flexible"
    parameter is set it will give this element a weighted value of space by
    comparing the Flexible values of all other elements in the layout. If a
    parameter should not be used, its value should be set to `-1`. You can
    also manually specify that it should be 0 by checking the
    "UseZeroMetrics" checkbox. The priority parameter determines this
    layout's priority when compared with other elements within the same
    hierarchy. The highest priority wins. You usually do not need to touch
    this.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.LayoutElement"

    def __init__(self, min_width: primitives.Float | None = None, preferred_width: primitives.Float | None = None, flexible_width: primitives.Float | None = None, min_height: primitives.Float | None = None, preferred_height: primitives.Float | None = None, flexible_height: primitives.Float | None = None, area: primitives.Float | None = None, priority: primitives.Int | None = None, use_zero_metrics: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            min_width: Initial value for MinWidth.
            preferred_width: Initial value for PreferredWidth.
            flexible_width: Initial value for FlexibleWidth.
            min_height: Initial value for MinHeight.
            preferred_height: Initial value for PreferredHeight.
            flexible_height: Initial value for FlexibleHeight.
            area: Initial value for Area.
            priority: Initial value for Priority.
            use_zero_metrics: Initial value for UseZeroMetrics.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if min_width is not None:
            self.min_width = min_width
        if preferred_width is not None:
            self.preferred_width = preferred_width
        if flexible_width is not None:
            self.flexible_width = flexible_width
        if min_height is not None:
            self.min_height = min_height
        if preferred_height is not None:
            self.preferred_height = preferred_height
        if flexible_height is not None:
            self.flexible_height = flexible_height
        if area is not None:
            self.area = area
        if priority is not None:
            self.priority = priority
        if use_zero_metrics is not None:
            self.use_zero_metrics = use_zero_metrics

    @property
    def min_width(self) -> primitives.Float | None:
        """The minimum width for this LayoutElement."""
        member = self.get_member("MinWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_width.setter
    def min_width(self, value: primitives.Float) -> None:
        """Set the MinWidth field value."""
        member = self.get_member("MinWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinWidth", fields.FieldFloat(value=value)
            )

    @property
    def preferred_width(self) -> primitives.Float | None:
        """The preferred width for this LayoutElement."""
        member = self.get_member("PreferredWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preferred_width.setter
    def preferred_width(self, value: primitives.Float) -> None:
        """Set the PreferredWidth field value."""
        member = self.get_member("PreferredWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreferredWidth", fields.FieldFloat(value=value)
            )

    @property
    def flexible_width(self) -> primitives.Float | None:
        """If there is any space left over after layouting, the width is used as a weight to decide what width should given to this LayoutElement."""
        member = self.get_member("FlexibleWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flexible_width.setter
    def flexible_width(self, value: primitives.Float) -> None:
        """Set the FlexibleWidth field value."""
        member = self.get_member("FlexibleWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FlexibleWidth", fields.FieldFloat(value=value)
            )

    @property
    def min_height(self) -> primitives.Float | None:
        """The minimum height for this LayoutElement."""
        member = self.get_member("MinHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_height.setter
    def min_height(self, value: primitives.Float) -> None:
        """Set the MinHeight field value."""
        member = self.get_member("MinHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinHeight", fields.FieldFloat(value=value)
            )

    @property
    def preferred_height(self) -> primitives.Float | None:
        """The preferred height for this LayoutElement."""
        member = self.get_member("PreferredHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preferred_height.setter
    def preferred_height(self, value: primitives.Float) -> None:
        """Set the PreferredHeight field value."""
        member = self.get_member("PreferredHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreferredHeight", fields.FieldFloat(value=value)
            )

    @property
    def flexible_height(self) -> primitives.Float | None:
        """If there is any space left over after layouting, the height is used as a weight to decide what height should be given to this LayoutElement."""
        member = self.get_member("FlexibleHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flexible_height.setter
    def flexible_height(self, value: primitives.Float) -> None:
        """Set the FlexibleHeight field value."""
        member = self.get_member("FlexibleHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FlexibleHeight", fields.FieldFloat(value=value)
            )

    @property
    def area(self) -> primitives.Float | None:
        """Currently unused."""
        member = self.get_member("Area")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @area.setter
    def area(self, value: primitives.Float) -> None:
        """Set the Area field value."""
        member = self.get_member("Area")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Area", fields.FieldFloat(value=value)
            )

    @property
    def priority(self) -> primitives.Int | None:
        """The priority for this LayoutElement."""
        member = self.get_member("Priority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @priority.setter
    def priority(self, value: primitives.Int) -> None:
        """Set the Priority field value."""
        member = self.get_member("Priority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Priority", fields.FieldInt(value=value)
            )

    @property
    def use_zero_metrics(self) -> primitives.Bool | None:
        """If checked, it allows "0" to be used in the other properties within this component."""
        member = self.get_member("UseZeroMetrics")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_zero_metrics.setter
    def use_zero_metrics(self, value: primitives.Bool) -> None:
        """Set the UseZeroMetrics field value."""
        member = self.get_member("UseZeroMetrics")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseZeroMetrics", fields.FieldBool(value=value)
            )

