"""Generated component: ScrollRect."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.rect_transform import RectTransform
from pyresonitelink.generated._types.iui_interactable import IUIInteractable
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ScrollRect(GeneratedComponent, IUIInteractable, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.ScrollRect.

    Category: UIX/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.ScrollRect"

    def __init__(self, normalized_position: primitives.Float2 | None = None, viewport_override: str | RectTransform | None = None, legacy_content: str | RectTransform | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            normalized_position: Initial value for NormalizedPosition.
            viewport_override: Initial value for ViewportOverride.
            legacy_content: Initial value for __legacyContent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if normalized_position is not None:
            self.normalized_position = normalized_position
        if viewport_override is not None:
            self.viewport_override = viewport_override
        if legacy_content is not None:
            self.legacy_content = legacy_content

    @property
    def normalized_position(self) -> primitives.Float2 | None:
        """The NormalizedPosition field value."""
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
    def viewport_override(self) -> str | None:
        """Target ID of the ViewportOverride reference (targets RectTransform)."""
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
        """Target ID of the __legacyContent reference (targets RectTransform)."""
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
        """Call the MoveToTop sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "MoveToTop", {}, debug,
        )

    async def move_to_bottom(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the MoveToBottom sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "MoveToBottom", {}, debug,
        )

    async def move_to_left(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the MoveToLeft sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "MoveToLeft", {}, debug,
        )

    async def move_to_right(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the MoveToRight sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "MoveToRight", {}, debug,
        )

