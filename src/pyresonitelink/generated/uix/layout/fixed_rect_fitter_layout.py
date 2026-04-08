"""Generated component: FixedRectFitterLayout."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ilayout_element import ILayoutElement
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FixedRectFitterLayout(GeneratedComponent, ILayoutElement, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.FixedRectFitterLayout.

    Category: UIX/Layout
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.FixedRectFitterLayout"

    def __init__(self, allow_shrink: bool | None = None, allow_grow: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            allow_shrink: Initial value for AllowShrink.
            allow_grow: Initial value for AllowGrow.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if allow_shrink is not None:
            self.allow_shrink = allow_shrink
        if allow_grow is not None:
            self.allow_grow = allow_grow

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
    def mode(self) -> members.FieldEnum | None:
        """The Mode member."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @mode.setter
    def mode(self, value: members.FieldEnum) -> None:
        """Set the Mode member."""
        self.set_member("Mode", value)

    @property
    def allow_shrink(self) -> bool | None:
        """The AllowShrink field value."""
        member = self.get_member("AllowShrink")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_shrink.setter
    def allow_shrink(self, value: bool) -> None:
        """Set the AllowShrink field value."""
        member = self.get_member("AllowShrink")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowShrink", fields.FieldBool(value=value)
            )

    @property
    def allow_grow(self) -> bool | None:
        """The AllowGrow field value."""
        member = self.get_member("AllowGrow")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_grow.setter
    def allow_grow(self, value: bool) -> None:
        """Set the AllowGrow field value."""
        member = self.get_member("AllowGrow")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowGrow", fields.FieldBool(value=value)
            )

