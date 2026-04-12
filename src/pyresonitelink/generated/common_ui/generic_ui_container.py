"""Generated component: GenericUIContainer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GenericUIContainer(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Generic UI Container is a component that is seen on UIX panels and canvases. It does two primary things, match the title for the panel of a provided text, and flag when it closes and then destroys the provided hierarchy root slot.

    Category: Common UI

    There is no known usage for this component to be used in projects, but
    only seen on certain panels and canvases.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GenericUIContainer"

    def __init__(self, title: str | IField[primitives.String] | None = None, close_request: primitives.Bool | None = None, close_destroy_root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            title: Initial value for Title.
            close_request: Initial value for CloseRequest.
            close_destroy_root: Initial value for CloseDestroyRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if title is not None:
            self.title = title
        if close_request is not None:
            self.close_request = close_request
        if close_destroy_root is not None:
            self.close_destroy_root = close_destroy_root

    @property
    def title(self) -> str | None:
        """Changes the title for this panel."""
        member = self.get_member("Title")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @title.setter
    def title(self, target: str | IField[primitives.String] | None) -> None:
        """Set the Title reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Title")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Title",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def close_request(self) -> primitives.Bool | None:
        """Becomes true when this container (UIX panel/canvas) is closing."""
        member = self.get_member("CloseRequest")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @close_request.setter
    def close_request(self, value: primitives.Bool) -> None:
        """Set the CloseRequest field value."""
        member = self.get_member("CloseRequest")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CloseRequest", fields.FieldBool(value=value)
            )

    @property
    def close_destroy_root(self) -> str | None:
        """The target slot to destroy."""
        member = self.get_member("CloseDestroyRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @close_destroy_root.setter
    def close_destroy_root(self, target: str | Slot | None) -> None:
        """Set the CloseDestroyRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("CloseDestroyRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CloseDestroyRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

