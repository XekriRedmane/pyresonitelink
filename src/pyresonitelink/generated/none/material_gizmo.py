"""Generated component: MaterialGizmo."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.material_provider import MaterialProvider
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent_gizmo import IComponentGizmo
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MaterialGizmo(GeneratedComponent, IComponentGizmo, IWorldEventReceiver):
    """The MaterialGizmo component is used to set up and manage Material orbs and their behavior for snapping to snapper components.

    Used with the Material Tool and Scene Inspector to manage references to
    materials as an item that can be held and looked at.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MaterialGizmo"

    def __init__(self, target: str | MaterialProvider | None = None, inspector_root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for _target.
            inspector_root: Initial value for _inspectorRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if inspector_root is not None:
            self.inspector_root = inspector_root

    @property
    def target(self) -> str | None:
        """The material this Gizmo was made for."""
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | MaterialProvider | None) -> None:
        """Set the _target reference by target ID or MaterialProvider instance."""
        target_id: str | None = target.id if isinstance(target, MaterialProvider) else target  # type: ignore[assignment]
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MaterialProvider'),
            )

    @property
    def inspector_root(self) -> str | None:
        """The inspector made in order to view ``_target``"""
        member = self.get_member("_inspectorRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @inspector_root.setter
    def inspector_root(self, target: str | Slot | None) -> None:
        """Set the _inspectorRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_inspectorRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_inspectorRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

