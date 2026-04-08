"""Generated component: ModalOverlayManager."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.modal_overlay import ModalOverlay
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ModalOverlayManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ModalOverlayManager.

    Category: UIX/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ModalOverlayManager"

    def __init__(self, template: str | ModalOverlay | None = None, spawn_root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            template: Initial value for Template.
            spawn_root: Initial value for SpawnRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if template is not None:
            self.template = template
        if spawn_root is not None:
            self.spawn_root = spawn_root

    @property
    def template(self) -> str | None:
        """Target ID of the Template reference (targets ModalOverlay)."""
        member = self.get_member("Template")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @template.setter
    def template(self, target: str | ModalOverlay | None) -> None:
        """Set the Template reference by target ID or ModalOverlay instance."""
        target_id: str | None = target.id if isinstance(target, ModalOverlay) else target  # type: ignore[assignment]
        member = self.get_member("Template")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Template",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.ModalOverlay'),
            )

    @property
    def spawn_root(self) -> str | None:
        """Target ID of the SpawnRoot reference (targets Slot)."""
        member = self.get_member("SpawnRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spawn_root.setter
    def spawn_root(self, target: str | Slot | None) -> None:
        """Set the SpawnRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("SpawnRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpawnRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

