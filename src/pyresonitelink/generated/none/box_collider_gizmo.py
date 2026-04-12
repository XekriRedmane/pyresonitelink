"""Generated component: BoxColliderGizmo."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.box_collider import BoxCollider
from pyresonitelink.generated._types.box_gizmo import BoxGizmo
from pyresonitelink.generated._types.icomponent_gizmo import IComponentGizmo
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BoxColliderGizmo(GeneratedComponent, IComponentGizmo, IWorldEventReceiver):
    """The BoxColliderGizmo component is used to resize and move BoxColliders in a visual manner using the DevTip.

    Used to adjust the size of a box collider. This can be accessed via the
    gizmo menu using a dev tip in your context menu. The button to activate
    it is the box collider option.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BoxColliderGizmo"

    def __init__(self, target: str | BoxCollider | None = None, cube_gizmo: str | BoxGizmo | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for _target.
            cube_gizmo: Initial value for _cubeGizmo.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if cube_gizmo is not None:
            self.cube_gizmo = cube_gizmo

    @property
    def target(self) -> str | None:
        """The box collider this component is currently editing"""
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | BoxCollider | None) -> None:
        """Set the _target reference by target ID or BoxCollider instance."""
        target_id: str | None = target.id if isinstance(target, BoxCollider) else target  # type: ignore[assignment]
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BoxCollider'),
            )

    @property
    def cube_gizmo(self) -> str | None:
        """The visual for this component which is used to edit ``_target`` in a visual manner."""
        member = self.get_member("_cubeGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cube_gizmo.setter
    def cube_gizmo(self, target: str | BoxGizmo | None) -> None:
        """Set the _cubeGizmo reference by target ID or BoxGizmo instance."""
        target_id: str | None = target.id if isinstance(target, BoxGizmo) else target  # type: ignore[assignment]
        member = self.get_member("_cubeGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cubeGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BoxGizmo'),
            )

