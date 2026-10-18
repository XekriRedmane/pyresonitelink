"""Generated component: DynamicBoneSphereColliderGizmo."""

from __future__ import annotations

from typing import TYPE_CHECKING
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent

if TYPE_CHECKING:
    from pyresonitelink.generated.physics.dynamic_bones.dynamic_bone_sphere_collider import DynamicBoneSphereCollider
    from pyresonitelink.generated.hidden.sphere_gizmo import SphereGizmo
from pyresonitelink.generated._types.icomponent_gizmo import IComponentGizmo
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicBoneSphereColliderGizmo(GeneratedComponent, IComponentGizmo, IWorldEventReceiver):
    """The DynamicBoneSphereColliderGizmo allows for interacting with Dynamic Bone Sphere Colliders via a Sphere Gizmo. these are usually created by activating the gizmo option using the context menu while having a slot with a Dynamic Bone Sphere Collider selected.

    Category: Utility/Gizmos
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicBoneSphereColliderGizmo"

    def __init__(self, target: str | DynamicBoneSphereCollider | None = None, sphere_gizmo: str | SphereGizmo | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for _target.
            sphere_gizmo: Initial value for _sphereGizmo.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if sphere_gizmo is not None:
            self.sphere_gizmo = sphere_gizmo

    @property
    def target(self) -> str | None:
        """The collider to make a visual/gizmo for."""
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | DynamicBoneSphereCollider | None) -> None:
        """Set the _target reference by target ID or DynamicBoneSphereCollider instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.DynamicBoneSphereCollider'),
            )

    @property
    def sphere_gizmo(self) -> str | None:
        """The gizmo being used to control ``_target`` through this component."""
        member = self.get_member("_sphereGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sphere_gizmo.setter
    def sphere_gizmo(self, target: str | SphereGizmo | None) -> None:
        """Set the _sphereGizmo reference by target ID or SphereGizmo instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("_sphereGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sphereGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SphereGizmo'),
            )

