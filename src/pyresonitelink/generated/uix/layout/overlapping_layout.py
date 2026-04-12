"""Generated component: OverlappingLayout."""

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


class OverlappingLayout(GeneratedComponent, ILayoutElement, IUIComputeComponent, IWorldEventReceiver):
    """The OverlappingLayout is best explained on the UIX page. The description for such is as follows:

A [Overlapping layout] layout overlaps or places on top of another layout in the same space.

    Category: UIX/Layout

    See UIX.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.OverlappingLayout"

    def __init__(self, padding_top: primitives.Float | None = None, padding_right: primitives.Float | None = None, padding_bottom: primitives.Float | None = None, padding_left: primitives.Float | None = None, horizontal_align: LayoutHorizontalAlignment | str | None = None, vertical_align: LayoutVerticalAlignment | str | None = None, force_expand_width: primitives.Bool | None = None, force_expand_height: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            padding_top: Initial value for PaddingTop.
            padding_right: Initial value for PaddingRight.
            padding_bottom: Initial value for PaddingBottom.
            padding_left: Initial value for PaddingLeft.
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
        """The padding from the center content to the top side."""
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
        """The padding from the center content to the right side."""
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
        """The padding from the center content to the bottom side."""
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
        """The padding from the center content to the left side."""
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
    def horizontal_align(self) -> LayoutHorizontalAlignment | None:
        """The alignment of the content horizontally."""
        member = self.get_member("HorizontalAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return LayoutHorizontalAlignment(member.value)
        return None

    @horizontal_align.setter
    def horizontal_align(self, value: LayoutHorizontalAlignment | str) -> None:
        """Set HorizontalAlign. The alignment of the content horizontally."""
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
        """The alignment of the content vertically."""
        member = self.get_member("VerticalAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return LayoutVerticalAlignment(member.value)
        return None

    @vertical_align.setter
    def vertical_align(self, value: LayoutVerticalAlignment | str) -> None:
        """Set VerticalAlign. The alignment of the content vertically."""
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
        """Whether content inside this layout going beyond the normal container size of this layout should be forced to go beyond the container so it fits width wise."""
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
        """Whether content inside this layout going beyond the normal container size of this layout should be forced to go beyond the container so it fits height wise."""
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

