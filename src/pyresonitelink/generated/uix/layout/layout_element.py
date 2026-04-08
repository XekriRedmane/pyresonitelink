"""Generated component: LayoutElement."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ilayout_element import ILayoutElement
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LayoutElement(GeneratedComponent, ILayoutElement, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.LayoutElement.

    Category: UIX/Layout
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
        """The MinWidth field value."""
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
        """The PreferredWidth field value."""
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
        """The FlexibleWidth field value."""
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
        """The MinHeight field value."""
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
        """The PreferredHeight field value."""
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
        """The FlexibleHeight field value."""
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
        """The Area field value."""
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
        """The Priority field value."""
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
        """The UseZeroMetrics field value."""
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

