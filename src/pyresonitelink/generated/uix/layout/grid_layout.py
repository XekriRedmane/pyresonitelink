"""Generated component: GridLayout."""

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


class GridLayout(GeneratedComponent, ILayoutElement, IUIComputeComponent, IWorldEventReceiver):
    """The GridLayout component aligns the UIX elements from left to right, top to bottom. This component also comes with controllable parameters that a user can use to adjust the way the grid layout is represented on the Canvas or element slot.

}}

    Category: UIX/Layout

    This is used to make a nice grid layout of a user's content. The user
    has a lot of control when it comes to making this kind of layout,
    especially when it comes to the amount of content cells, expanding and
    scaling those cells, and alignments.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.GridLayout"

    def __init__(self, padding_top: primitives.Float | None = None, padding_right: primitives.Float | None = None, padding_bottom: primitives.Float | None = None, padding_left: primitives.Float | None = None, cell_size: primitives.Float2 | None = None, spacing: primitives.Float2 | None = None, horizontal_align: LayoutHorizontalAlignment | str | None = None, vertical_align: LayoutVerticalAlignment | str | None = None, expand_width_to_fit: primitives.Bool | None = None, preserve_aspect_on_expand: primitives.Bool | None = None, align_last_row_individually: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            padding_top: Initial value for PaddingTop.
            padding_right: Initial value for PaddingRight.
            padding_bottom: Initial value for PaddingBottom.
            padding_left: Initial value for PaddingLeft.
            cell_size: Initial value for CellSize.
            spacing: Initial value for Spacing.
            horizontal_align: Initial value for HorizontalAlign.
            vertical_align: Initial value for VerticalAlign.
            expand_width_to_fit: Initial value for ExpandWidthToFit.
            preserve_aspect_on_expand: Initial value for PreserveAspectOnExpand.
            align_last_row_individually: Initial value for AlignLastRowIndividually.
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
        if cell_size is not None:
            self.cell_size = cell_size
        if spacing is not None:
            self.spacing = spacing
        if horizontal_align is not None:
            self.horizontal_align = horizontal_align
        if vertical_align is not None:
            self.vertical_align = vertical_align
        if expand_width_to_fit is not None:
            self.expand_width_to_fit = expand_width_to_fit
        if preserve_aspect_on_expand is not None:
            self.preserve_aspect_on_expand = preserve_aspect_on_expand
        if align_last_row_individually is not None:
            self.align_last_row_individually = align_last_row_individually

    @property
    def padding_top(self) -> primitives.Float | None:
        """Makes padding on the top of this grid, separating it from the top."""
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
        """Makes padding on the right of this grid, separating it from the right."""
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
        """Makes padding on the bottom of this grid, separating it from the bottom."""
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
        """Makes padding on the left of this grid, separating it from the left."""
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
    def cell_size(self) -> primitives.Float2 | None:
        """The size of each content cell."""
        member = self.get_member("CellSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cell_size.setter
    def cell_size(self, value: primitives.Float2) -> None:
        """Set the CellSize field value."""
        member = self.get_member("CellSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CellSize", fields.FieldFloat2(value=value)
            )

    @property
    def spacing(self) -> primitives.Float2 | None:
        """Makes padding between the content cells of this grid, separating it evenly."""
        member = self.get_member("Spacing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spacing.setter
    def spacing(self, value: primitives.Float2) -> None:
        """Set the Spacing field value."""
        member = self.get_member("Spacing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Spacing", fields.FieldFloat2(value=value)
            )

    @property
    def horizontal_align(self) -> LayoutHorizontalAlignment | None:
        """how this grid should be aligned horizontally."""
        member = self.get_member("HorizontalAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return LayoutHorizontalAlignment(member.value)
        return None

    @horizontal_align.setter
    def horizontal_align(self, value: LayoutHorizontalAlignment | str) -> None:
        """Set HorizontalAlign. how this grid should be aligned horizontally."""
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
        """how this grid should be aligned vertically."""
        member = self.get_member("VerticalAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return LayoutVerticalAlignment(member.value)
        return None

    @vertical_align.setter
    def vertical_align(self, value: LayoutVerticalAlignment | str) -> None:
        """Set VerticalAlign. how this grid should be aligned vertically."""
        member = self.get_member("VerticalAlign")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "VerticalAlign",
                members.FieldEnum(value=str(value)),
            )

    @property
    def expand_width_to_fit(self) -> primitives.Bool | None:
        """Extends this grid to fit the entire UIX element that it is on."""
        member = self.get_member("ExpandWidthToFit")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @expand_width_to_fit.setter
    def expand_width_to_fit(self, value: primitives.Bool) -> None:
        """Set the ExpandWidthToFit field value."""
        member = self.get_member("ExpandWidthToFit")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ExpandWidthToFit", fields.FieldBool(value=value)
            )

    @property
    def preserve_aspect_on_expand(self) -> primitives.Bool | None:
        """Preserves the aspect ratio when expanded to fit."""
        member = self.get_member("PreserveAspectOnExpand")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preserve_aspect_on_expand.setter
    def preserve_aspect_on_expand(self, value: primitives.Bool) -> None:
        """Set the PreserveAspectOnExpand field value."""
        member = self.get_member("PreserveAspectOnExpand")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreserveAspectOnExpand", fields.FieldBool(value=value)
            )

    @property
    def align_last_row_individually(self) -> primitives.Bool | None:
        """Alighns the last row for this grid seprately."""
        member = self.get_member("AlignLastRowIndividually")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @align_last_row_individually.setter
    def align_last_row_individually(self, value: primitives.Bool) -> None:
        """Set the AlignLastRowIndividually field value."""
        member = self.get_member("AlignLastRowIndividually")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlignLastRowIndividually", fields.FieldBool(value=value)
            )

