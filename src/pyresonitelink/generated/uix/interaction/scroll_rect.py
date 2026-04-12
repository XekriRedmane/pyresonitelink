"""Generated component: ScrollRect."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.layout_horizontal_alignment import LayoutHorizontalAlignment
from pyresonitelink.generated._enums.layout_vertical_alignment import LayoutVerticalAlignment
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.rect_transform import RectTransform
from pyresonitelink.generated._types.iui_interactable import IUIInteractable
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ScrollRect(GeneratedComponent, IUIInteractable, IUIComputeComponent, IWorldEventReceiver):
    """The ScrollRect component is for making the contents of this Slot (such as child objects with RectTransforms) scrollable.

The scrollRect will not do any clipping on its own. If it is a child of an object with a Mask component, it effectively becomes a window into the scrolled content.

}}

    Category: UIX/Interaction

    This is useful when you have a lot of text or other UIX elements that
    you want to be scrollable, much like how a webpage has a lot of content
    that can't fit in just one screen.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.ScrollRect"

    def __init__(self, normalized_position: primitives.Float2 | None = None, horizontal_align: LayoutHorizontalAlignment | str | None = None, vertical_align: LayoutVerticalAlignment | str | None = None, viewport_override: str | RectTransform | None = None, legacy_content: str | RectTransform | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            normalized_position: Initial value for NormalizedPosition.
            horizontal_align: Initial value for HorizontalAlign.
            vertical_align: Initial value for VerticalAlign.
            viewport_override: Initial value for ViewportOverride.
            legacy_content: Initial value for __legacyContent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if normalized_position is not None:
            self.normalized_position = normalized_position
        if horizontal_align is not None:
            self.horizontal_align = horizontal_align
        if vertical_align is not None:
            self.vertical_align = vertical_align
        if viewport_override is not None:
            self.viewport_override = viewport_override
        if legacy_content is not None:
            self.legacy_content = legacy_content

    @property
    def normalized_position(self) -> primitives.Float2 | None:
        """The scroll position between (0,0) and (1,1) with (0,0) being the lower left corner."""
        member = self.get_member("NormalizedPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normalized_position.setter
    def normalized_position(self, value: primitives.Float2) -> None:
        """Set the NormalizedPosition field value."""
        member = self.get_member("NormalizedPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalizedPosition", fields.FieldFloat2(value=value)
            )

    @property
    def horizontal_align(self) -> LayoutHorizontalAlignment | None:
        """Aligns the scrollrect's contents horizontal."""
        member = self.get_member("HorizontalAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return LayoutHorizontalAlignment(member.value)
        return None

    @horizontal_align.setter
    def horizontal_align(self, value: LayoutHorizontalAlignment | str) -> None:
        """Set HorizontalAlign. Aligns the scrollrect's contents horizontal."""
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
        """Aligns the scrollrect's contents vertically."""
        member = self.get_member("VerticalAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return LayoutVerticalAlignment(member.value)
        return None

    @vertical_align.setter
    def vertical_align(self, value: LayoutVerticalAlignment | str) -> None:
        """Set VerticalAlign. Aligns the scrollrect's contents vertically."""
        member = self.get_member("VerticalAlign")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "VerticalAlign",
                members.FieldEnum(value=str(value)),
            )

    @property
    def viewport_override(self) -> str | None:
        """Overrides the viewport of this scrollrect."""
        member = self.get_member("ViewportOverride")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @viewport_override.setter
    def viewport_override(self, target: str | RectTransform | None) -> None:
        """Set the ViewportOverride reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("ViewportOverride")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ViewportOverride",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def legacy_content(self) -> str | None:
        """Internal - Used for the content of the scrollrect."""
        member = self.get_member("__legacyContent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @legacy_content.setter
    def legacy_content(self, target: str | RectTransform | None) -> None:
        """Set the __legacyContent reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("__legacyContent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "__legacyContent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    async def move_to_top(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Moves the scroll view to the top.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "MoveToTop", {}, debug,
        )

    async def move_to_bottom(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Mobes the scroll view to the bottom.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "MoveToBottom", {}, debug,
        )

    async def move_to_left(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Moves the scroll view to the left.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "MoveToLeft", {}, debug,
        )

    async def move_to_right(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Moves the scroll view to the right.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "MoveToRight", {}, debug,
        )

