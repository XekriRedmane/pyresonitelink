"""Generated component: VerticalLayout."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.layout_horizontal_alignment import LayoutHorizontalAlignment
from pyresonitelink.generated._enums.layout_vertical_alignment import LayoutVerticalAlignment
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ilayout_element import ILayoutElement
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VerticalLayout(GeneratedComponent, ILayoutElement, IUIComputeComponent, IWorldEventReceiver):
    """The VerticalLayout component is used to layout child UIX element slots in a column, top to bottom.

The order of the objects depends on each child's OrderOffset property. Normally these are ``0``, but if you change it, the children will be ordered by increasing OrderOffset, with children of equal OrderOffset being ordered by the time they were added to that parent slot.

}}

    Category: UIX/Layout

    The VerticalLayout component places its child layout elements on top of
    each other. Their heights are determined by their respective minimum,
    preferred, and flexible heights according to the following model: # The
    minimum heights of all the child layout elements are added together and
    the spacing between them plus the top and bottom padding is added as
    well. The result is the minimum height of the VerticalLayout. # The
    preferred heights of all the child layout elements are added together
    and the spacing between them plus the top and bottom padding is added as
    well. The result is the preferred height of the VerticalLayout. # If the
    VerticalLayout is at its minimum height or smaller, all the child layout
    elements will also have their minimum height. # The closer the
    VerticalLayout is to its preferred height, the closer each child layout
    element will also get to their preferred height. # If the VerticalLayout
    is taller than its preferred height, it will distribute the extra
    available space proportionally to the child layout elements according to
    their respective flexible heights. For minimum, preferred, and flexible
    heights of child slots, use LayoutElement.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.VerticalLayout"

    def __init__(self, padding_top: primitives.Float | None = None, padding_right: primitives.Float | None = None, padding_bottom: primitives.Float | None = None, padding_left: primitives.Float | None = None, spacing: primitives.Float | None = None, horizontal_align: LayoutHorizontalAlignment | str | None = None, vertical_align: LayoutVerticalAlignment | str | None = None, force_expand_width: primitives.Bool | None = None, force_expand_height: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            padding_top: Initial value for PaddingTop.
            padding_right: Initial value for PaddingRight.
            padding_bottom: Initial value for PaddingBottom.
            padding_left: Initial value for PaddingLeft.
            spacing: Initial value for Spacing.
            horizontal_align: Initial value for HorizontalAlign.
            vertical_align: Initial value for VerticalAlign.
            force_expand_width: Initial value for ForceExpandWidth.
            force_expand_height: Initial value for ForceExpandHeight.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if padding_top is not None:
            self.padding_top = padding_top
        if padding_right is not None:
            self.padding_right = padding_right
        if padding_bottom is not None:
            self.padding_bottom = padding_bottom
        if padding_left is not None:
            self.padding_left = padding_left
        if spacing is not None:
            self.spacing = spacing
        if horizontal_align is not None:
            self.horizontal_align = horizontal_align
        if vertical_align is not None:
            self.vertical_align = vertical_align
        if force_expand_width is not None:
            self.force_expand_width = force_expand_width
        if force_expand_height is not None:
            self.force_expand_height = force_expand_height

    @property
    def padding_top(self) -> primitives.Float | None:
        """The padding to add, in pixels, at the top of the entire layout."""
        member = self.get_member("PaddingTop")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @padding_top.setter
    def padding_top(self, value: primitives.Float) -> None:
        """Set the PaddingTop field value."""
        member = self.get_member("PaddingTop")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PaddingTop", fields.FieldFloat(value=value)
            )

    @property
    def padding_right(self) -> primitives.Float | None:
        """The padding to add, in pixels, at the right of the entire layout."""
        member = self.get_member("PaddingRight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @padding_right.setter
    def padding_right(self, value: primitives.Float) -> None:
        """Set the PaddingRight field value."""
        member = self.get_member("PaddingRight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PaddingRight", fields.FieldFloat(value=value)
            )

    @property
    def padding_bottom(self) -> primitives.Float | None:
        """The padding to add, in pixels, at the bottom of the entire layout."""
        member = self.get_member("PaddingBottom")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @padding_bottom.setter
    def padding_bottom(self, value: primitives.Float) -> None:
        """Set the PaddingBottom field value."""
        member = self.get_member("PaddingBottom")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PaddingBottom", fields.FieldFloat(value=value)
            )

    @property
    def padding_left(self) -> primitives.Float | None:
        """The padding to add, in pixels, at the left of the entire layout."""
        member = self.get_member("PaddingLeft")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @padding_left.setter
    def padding_left(self, value: primitives.Float) -> None:
        """Set the PaddingLeft field value."""
        member = self.get_member("PaddingLeft")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PaddingLeft", fields.FieldFloat(value=value)
            )

    @property
    def spacing(self) -> primitives.Float | None:
        """The padding to add, in pixels, between each object."""
        member = self.get_member("Spacing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spacing.setter
    def spacing(self, value: primitives.Float) -> None:
        """Set the Spacing field value."""
        member = self.get_member("Spacing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Spacing", fields.FieldFloat(value=value)
            )

    @property
    def horizontal_align(self) -> LayoutHorizontalAlignment | None:
        """The horizontal alignment to use for the child objects in the layout."""
        member = self.get_member("HorizontalAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return LayoutHorizontalAlignment(member.value)
        return None

    @horizontal_align.setter
    def horizontal_align(self, value: LayoutHorizontalAlignment | str) -> None:
        """Set HorizontalAlign. The horizontal alignment to use for the child objects in the layout."""
        member = self.get_member("HorizontalAlign")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "HorizontalAlign",
                members.FieldEnum(value=str(value)),
            )

    @property
    def vertical_align(self) -> LayoutVerticalAlignment | None:
        """The vertical alignment to use for the child objects in the layout."""
        member = self.get_member("VerticalAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return LayoutVerticalAlignment(member.value)
        return None

    @vertical_align.setter
    def vertical_align(self, value: LayoutVerticalAlignment | str) -> None:
        """Set VerticalAlign. The vertical alignment to use for the child objects in the layout."""
        member = self.get_member("VerticalAlign")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "VerticalAlign",
                members.FieldEnum(value=str(value)),
            )

    @property
    def force_expand_width(self) -> primitives.Bool | None:
        """Whether to force the children to expand to fill the available horizontal space."""
        member = self.get_member("ForceExpandWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_expand_width.setter
    def force_expand_width(self, value: primitives.Bool) -> None:
        """Set the ForceExpandWidth field value."""
        member = self.get_member("ForceExpandWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceExpandWidth", fields.FieldBool(value=value)
            )

    @property
    def force_expand_height(self) -> primitives.Bool | None:
        """Whether to force the children to expand to fill the available vertical space."""
        member = self.get_member("ForceExpandHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_expand_height.setter
    def force_expand_height(self, value: primitives.Bool) -> None:
        """Set the ForceExpandHeight field value."""
        member = self.get_member("ForceExpandHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceExpandHeight", fields.FieldBool(value=value)
            )

