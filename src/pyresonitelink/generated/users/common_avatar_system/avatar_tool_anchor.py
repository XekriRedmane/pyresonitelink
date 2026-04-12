"""Generated component: AvatarToolAnchor."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.point import Point
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarToolAnchor(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Avatar Tool anchor is a component that defines where to place either the tool, toolshelf, or grab area anchors when the avatar is equipped. Or where to position the context menu when it is opened.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarToolAnchor"

    def __init__(self, anchor_point: Point | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            anchor_point: Initial value for AnchorPoint.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if anchor_point is not None:
            self.anchor_point = anchor_point

    @property
    def anchor_point(self) -> Point | None:
        """The type of tool anchor to place under the slot this component is on for this hand."""
        member = self.get_member("AnchorPoint")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Point(member.value)
        return None

    @anchor_point.setter
    def anchor_point(self, value: Point | str) -> None:
        """Set AnchorPoint. The type of tool anchor to place under the slot this component is on for this hand."""
        member = self.get_member("AnchorPoint")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "AnchorPoint",
                members.FieldEnum(value=str(value)),
            )

