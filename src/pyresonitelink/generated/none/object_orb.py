"""Generated component: ObjectOrb."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ObjectOrb(GeneratedComponent, IComponent, IWorldEventReceiver):
    """According to Frooxius this was originally made during the infancy stages of FrooxEngine to serve as an item the user would stick into an "Object Placement Tool" where users could easily place objects into the world in the form of duplicates and make it easier to create worlds. However this never came to fruition and the concept lives on as this remnant in the game code and Component set. (timestamp) https://www.youtube.com/watch?v=OfriYWXMNjk&t=28m59s
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ObjectOrb"

    def __init__(self, preview_root: str | Slot | None = None, template_root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            preview_root: Initial value for PreviewRoot.
            template_root: Initial value for TemplateRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if preview_root is not None:
            self.preview_root = preview_root
        if template_root is not None:
            self.template_root = template_root

    @property
    def preview_root(self) -> str | None:
        """The slot storing the preview visual."""
        member = self.get_member("PreviewRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @preview_root.setter
    def preview_root(self, target: str | Slot | None) -> None:
        """Set the PreviewRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("PreviewRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PreviewRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def template_root(self) -> str | None:
        """The slot to duplicate when placing the object."""
        member = self.get_member("TemplateRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @template_root.setter
    def template_root(self, target: str | Slot | None) -> None:
        """Set the TemplateRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("TemplateRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TemplateRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

