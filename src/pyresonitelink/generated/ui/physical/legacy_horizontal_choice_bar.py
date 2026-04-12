"""Generated component: LegacyHorizontalChoiceBar."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.legacy_ui_style import LegacyUIStyle
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyHorizontalChoiceBar(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The LegacyHorizontalChoiceBar component is used in old migrated legacy content. This should not be used in new content, and should be replaced whenever possible. This was primarily used in old Gizmos.

    Category: UI/Physical

    Just dont.

    **SegmentTouchEvent**: SegmentTouchEvent() is a sync delegate that is the type Delegate&lt;LegacyHorizontalChoiceBar sender, Int itemIndex, TouchEventInfo eventInfo&gt; and can be used to handle the press events of a LegacyHorizontalChoiceBar.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyHorizontalChoiceBar"

    def __init__(self, style: str | LegacyUIStyle | None = None, accept_physical_touch: primitives.Bool | None = None, accept_remote_touch: primitives.Bool | None = None, width: primitives.Float | None = None, height: primitives.Float | None = None, thickness: primitives.Float | None = None, spacing: primitives.Float | None = None, slant: primitives.Float | None = None, symmetrical: primitives.Bool | None = None, root: str | Slot | None = None, root_scale: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            style: Initial value for Style.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            width: Initial value for Width.
            height: Initial value for Height.
            thickness: Initial value for Thickness.
            spacing: Initial value for Spacing.
            slant: Initial value for Slant.
            symmetrical: Initial value for Symmetrical.
            root: Initial value for _root.
            root_scale: Initial value for _rootScale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if style is not None:
            self.style = style
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if thickness is not None:
            self.thickness = thickness
        if spacing is not None:
            self.spacing = spacing
        if slant is not None:
            self.slant = slant
        if symmetrical is not None:
            self.symmetrical = symmetrical
        if root is not None:
            self.root = root
        if root_scale is not None:
            self.root_scale = root_scale

    @property
    def style(self) -> str | None:
        """Target ID of the Style reference (targets LegacyUIStyle)."""
        member = self.get_member("Style")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @style.setter
    def style(self, target: str | LegacyUIStyle | None) -> None:
        """Set the Style reference by target ID or LegacyUIStyle instance."""
        target_id: str | None = target.id if isinstance(target, LegacyUIStyle) else target  # type: ignore[assignment]
        member = self.get_member("Style")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Style",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyUIStyle'),
            )

    @property
    def accept_physical_touch(self) -> primitives.Bool | None:
        """The AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_physical_touch.setter
    def accept_physical_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptPhysicalTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_remote_touch(self) -> primitives.Bool | None:
        """The AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_remote_touch.setter
    def accept_remote_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptRemoteTouch", fields.FieldBool(value=value)
            )

    @property
    def items(self) -> members.SyncList | None:
        """A list of items to be able to press."""
        member = self.get_member("_items")
        if isinstance(member, members.SyncList):
            return member
        return None

    @items.setter
    def items(self, value: members.SyncList) -> None:
        """Set _items. A list of items to be able to press."""
        self.set_member("_items", value)

    @property
    def width(self) -> primitives.Float | None:
        """The width of each item."""
        member = self.get_member("Width")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @width.setter
    def width(self, value: primitives.Float) -> None:
        """Set the Width field value."""
        member = self.get_member("Width")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Width", fields.FieldFloat(value=value)
            )

    @property
    def height(self) -> primitives.Float | None:
        """The height of each item."""
        member = self.get_member("Height")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height.setter
    def height(self, value: primitives.Float) -> None:
        """Set the Height field value."""
        member = self.get_member("Height")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Height", fields.FieldFloat(value=value)
            )

    @property
    def thickness(self) -> primitives.Float | None:
        """The thickness of each item."""
        member = self.get_member("Thickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @thickness.setter
    def thickness(self, value: primitives.Float) -> None:
        """Set the Thickness field value."""
        member = self.get_member("Thickness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Thickness", fields.FieldFloat(value=value)
            )

    @property
    def spacing(self) -> primitives.Float | None:
        """How far apart the items should be placed."""
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
    def slant(self) -> primitives.Float | None:
        """The Bevel of the meshes of each item."""
        member = self.get_member("Slant")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @slant.setter
    def slant(self, value: primitives.Float) -> None:
        """Set the Slant field value."""
        member = self.get_member("Slant")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Slant", fields.FieldFloat(value=value)
            )

    @property
    def symmetrical(self) -> primitives.Bool | None:
        """Whether the Horizontal layout should be symmetrical."""
        member = self.get_member("Symmetrical")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @symmetrical.setter
    def symmetrical(self, value: primitives.Bool) -> None:
        """Set the Symmetrical field value."""
        member = self.get_member("Symmetrical")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Symmetrical", fields.FieldBool(value=value)
            )

    @property
    def root(self) -> str | None:
        """the place to parent all the items."""
        member = self.get_member("_root")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root.setter
    def root(self, target: str | Slot | None) -> None:
        """Set the _root reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_root")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_root",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def root_scale(self) -> str | None:
        """The scale field of the slot to place the items."""
        member = self.get_member("_rootScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root_scale.setter
    def root_scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _rootScale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rootScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rootScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

