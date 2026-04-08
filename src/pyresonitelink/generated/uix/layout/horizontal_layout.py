"""Generated component: HorizontalLayout."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ilayout_element import ILayoutElement
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HorizontalLayout(GeneratedComponent, ILayoutElement, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.HorizontalLayout.

    Category: UIX/Layout
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.HorizontalLayout"

    def __init__(self, padding_top: primitives.Float | None = None, padding_right: primitives.Float | None = None, padding_bottom: primitives.Float | None = None, padding_left: primitives.Float | None = None, spacing: primitives.Float | None = None, force_expand_width: primitives.Bool | None = None, force_expand_height: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            padding_top: Initial value for PaddingTop.
            padding_right: Initial value for PaddingRight.
            padding_bottom: Initial value for PaddingBottom.
            padding_left: Initial value for PaddingLeft.
            spacing: Initial value for Spacing.
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
        if force_expand_width is not None:
            self.force_expand_width = force_expand_width
        if force_expand_height is not None:
            self.force_expand_height = force_expand_height

    @property
    def padding_top(self) -> primitives.Float | None:
        """The PaddingTop field value."""
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
        """The PaddingRight field value."""
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
        """The PaddingBottom field value."""
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
        """The PaddingLeft field value."""
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
        """The Spacing field value."""
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
    def horizontal_align(self) -> members.FieldEnum | None:
        """The HorizontalAlign member."""
        member = self.get_member("HorizontalAlign")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @horizontal_align.setter
    def horizontal_align(self, value: members.FieldEnum) -> None:
        """Set the HorizontalAlign member."""
        self.set_member("HorizontalAlign", value)

    @property
    def vertical_align(self) -> members.FieldEnum | None:
        """The VerticalAlign member."""
        member = self.get_member("VerticalAlign")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @vertical_align.setter
    def vertical_align(self, value: members.FieldEnum) -> None:
        """Set the VerticalAlign member."""
        self.set_member("VerticalAlign", value)

    @property
    def force_expand_width(self) -> primitives.Bool | None:
        """The ForceExpandWidth field value."""
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
        """The ForceExpandHeight field value."""
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

