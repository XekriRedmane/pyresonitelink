"""Generated component: ModalOverlay."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.rect_transform import RectTransform
from pyresonitelink.generated._types.iui_interactable import IUIInteractable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ModalOverlay(GeneratedComponent, IUIInteractable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.ModalOverlay.

    Category: UIX/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.ModalOverlay"

    def __init__(self, show_lerp: primitives.Float | None = None, animation_time: primitives.Float | None = None, size_root: str | RectTransform | None = None, content_root: str | RectTransform | None = None, close_on_context_menu_action: primitives.Bool | None = None, close_on_click: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            show_lerp: Initial value for ShowLerp.
            animation_time: Initial value for AnimationTime.
            size_root: Initial value for SizeRoot.
            content_root: Initial value for ContentRoot.
            close_on_context_menu_action: Initial value for CloseOnContextMenuAction.
            close_on_click: Initial value for CloseOnClick.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if show_lerp is not None:
            self.show_lerp = show_lerp
        if animation_time is not None:
            self.animation_time = animation_time
        if size_root is not None:
            self.size_root = size_root
        if content_root is not None:
            self.content_root = content_root
        if close_on_context_menu_action is not None:
            self.close_on_context_menu_action = close_on_context_menu_action
        if close_on_click is not None:
            self.close_on_click = close_on_click

    @property
    def show_lerp(self) -> primitives.Float | None:
        """The ShowLerp field value."""
        member = self.get_member("ShowLerp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_lerp.setter
    def show_lerp(self, value: primitives.Float) -> None:
        """Set the ShowLerp field value."""
        member = self.get_member("ShowLerp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowLerp", fields.FieldFloat(value=value)
            )

    @property
    def animation_time(self) -> primitives.Float | None:
        """The AnimationTime field value."""
        member = self.get_member("AnimationTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @animation_time.setter
    def animation_time(self, value: primitives.Float) -> None:
        """Set the AnimationTime field value."""
        member = self.get_member("AnimationTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnimationTime", fields.FieldFloat(value=value)
            )

    @property
    def size_root(self) -> str | None:
        """Target ID of the SizeRoot reference (targets RectTransform)."""
        member = self.get_member("SizeRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @size_root.setter
    def size_root(self, target: str | RectTransform | None) -> None:
        """Set the SizeRoot reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("SizeRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SizeRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def content_root(self) -> str | None:
        """Target ID of the ContentRoot reference (targets RectTransform)."""
        member = self.get_member("ContentRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @content_root.setter
    def content_root(self, target: str | RectTransform | None) -> None:
        """Set the ContentRoot reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("ContentRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ContentRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def close_on_context_menu_action(self) -> primitives.Bool | None:
        """The CloseOnContextMenuAction field value."""
        member = self.get_member("CloseOnContextMenuAction")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @close_on_context_menu_action.setter
    def close_on_context_menu_action(self, value: primitives.Bool) -> None:
        """Set the CloseOnContextMenuAction field value."""
        member = self.get_member("CloseOnContextMenuAction")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CloseOnContextMenuAction", fields.FieldBool(value=value)
            )

    @property
    def close_on_click(self) -> primitives.Bool | None:
        """The CloseOnClick field value."""
        member = self.get_member("CloseOnClick")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @close_on_click.setter
    def close_on_click(self, value: primitives.Bool) -> None:
        """Set the CloseOnClick field value."""
        member = self.get_member("CloseOnClick")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CloseOnClick", fields.FieldBool(value=value)
            )

