"""Generated component: BreadcrumbInterface."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BreadcrumbInterface(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The BreadcrumbInterface component is used by data feeds to get the translated name of one directory in a list of directories that makes a path. This is most commonly used in the Settings at the top to show a user where in the settings they are.

    Category: Radiant UI/Navigation

    Used with a BreadcrumbManager to generate a list of path elements to
    show to the user in their language.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BreadcrumbInterface"

    def __init__(self, item_name: str | IField[primitives.String] | None = None, path_segment: primitives.String | None = None, item_depth: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            item_name: Initial value for ItemName.
            path_segment: Initial value for PathSegment.
            item_depth: Initial value for ItemDepth.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if item_name is not None:
            self.item_name = item_name
        if path_segment is not None:
            self.path_segment = path_segment
        if item_depth is not None:
            self.item_depth = item_depth

    @property
    def item_name(self) -> str | None:
        """The field to drive with the localized string of the path segment (on an OS, this would be like the programmer name of a folder translated to your language)"""
        member = self.get_member("ItemName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_name.setter
    def item_name(self, target: str | IField[primitives.String] | None) -> None:
        """Set the ItemName reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ItemName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ItemName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def path_segment(self) -> primitives.String | None:
        """The path segment programmer name to convert to your language."""
        member = self.get_member("PathSegment")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @path_segment.setter
    def path_segment(self, value: primitives.String) -> None:
        """Set the PathSegment field value."""
        member = self.get_member("PathSegment")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PathSegment", fields.FieldString(value=value)
            )

    @property
    def item_depth(self) -> primitives.Int | None:
        """How many levels down in the path this string element would be."""
        member = self.get_member("ItemDepth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @item_depth.setter
    def item_depth(self, value: primitives.Int) -> None:
        """Set the ItemDepth field value."""
        member = self.get_member("ItemDepth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ItemDepth", fields.FieldInt(value=value)
            )

