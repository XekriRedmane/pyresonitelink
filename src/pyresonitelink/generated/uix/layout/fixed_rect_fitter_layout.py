"""Generated component: FixedRectFitterLayout."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.layout_horizontal_alignment import LayoutHorizontalAlignment
from pyresonitelink.generated._enums.layout_vertical_alignment import LayoutVerticalAlignment
from pyresonitelink.generated._enums.fit_mode import FitMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ilayout_element import ILayoutElement
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FixedRectFitterLayout(GeneratedComponent, ILayoutElement, IUIComputeComponent, IWorldEventReceiver):
    """The FixedRectFitterLayout component attempts to fit child elements into the RectTransform of the FixedRectFitterLayout slot.

To use a FixedRectFitterLayout at least one child element will need an ``OffsetMax`` value that is not ``[0.0; 0.0]``.

|AllowShrink|Bool|Should the child elements shrink to fit the space if needed.|AllowGrow|Bool|Should the child elements grow to fill the space if needed.}}

    Category: UIX/Layout

    The FixedRectFitterLayout component computes the bounds of child
    elements using their computed ``OffsetMax`` values and attempts to to
    fit the child elements into the FixedRectFitterLayout's RectTransform
    according to the mode.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.FixedRectFitterLayout"

    def __init__(self, horizontal_align: LayoutHorizontalAlignment | str | None = None, vertical_align: LayoutVerticalAlignment | str | None = None, mode: FitMode | str | None = None, allow_shrink: primitives.Bool | None = None, allow_grow: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            horizontal_align: Initial value for HorizontalAlign.
            vertical_align: Initial value for VerticalAlign.
            mode: Initial value for Mode.
            allow_shrink: Initial value for AllowShrink.
            allow_grow: Initial value for AllowGrow.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if horizontal_align is not None:
            self.horizontal_align = horizontal_align
        if vertical_align is not None:
            self.vertical_align = vertical_align
        if mode is not None:
            self.mode = mode
        if allow_shrink is not None:
            self.allow_shrink = allow_shrink
        if allow_grow is not None:
            self.allow_grow = allow_grow

    @property
    def horizontal_align(self) -> LayoutHorizontalAlignment | None:
        """The HorizontalAlign enum value."""
        member = self.get_member("HorizontalAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return LayoutHorizontalAlignment(member.value)
        return None

    @horizontal_align.setter
    def horizontal_align(self, value: LayoutHorizontalAlignment | str) -> None:
        """Set the HorizontalAlign enum value."""
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
    def mode(self) -> FitMode | None:
        """How the child elements should attempt to fit into this RectTransform"""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return FitMode(member.value)
        return None

    @mode.setter
    def mode(self, value: FitMode | str) -> None:
        """Set Mode. How the child elements should attempt to fit into this RectTransform"""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Mode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def allow_shrink(self) -> primitives.Bool | None:
        """Should the child elements shrink to fit the space if needed. AllowGrow Bool Should the child elements grow to fill the space if needed."""
        member = self.get_member("AllowShrink")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_shrink.setter
    def allow_shrink(self, value: primitives.Bool) -> None:
        """Set the AllowShrink field value."""
        member = self.get_member("AllowShrink")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowShrink", fields.FieldBool(value=value)
            )

    @property
    def allow_grow(self) -> primitives.Bool | None:
        """The AllowGrow field value."""
        member = self.get_member("AllowGrow")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_grow.setter
    def allow_grow(self, value: primitives.Bool) -> None:
        """Set the AllowGrow field value."""
        member = self.get_member("AllowGrow")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowGrow", fields.FieldBool(value=value)
            )

