"""Generated component: EyeRotationDriverGizmo."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.eye_rotation_driver import EyeRotationDriver
from pyresonitelink.generated._types.icomponent_gizmo import IComponentGizmo
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class EyeRotationDriverGizmo(GeneratedComponent, IComponentGizmo, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.EyeRotationDriverGizmo.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.EyeRotationDriverGizmo"

    def __init__(self, target: str | EyeRotationDriver | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for _target.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target

    @property
    def target(self) -> str | None:
        """Target ID of the _target reference (targets EyeRotationDriver)."""
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | EyeRotationDriver | None) -> None:
        """Set the _target reference by target ID or EyeRotationDriver instance."""
        target_id: str | None = target.id if isinstance(target, EyeRotationDriver) else target  # type: ignore[assignment]
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.EyeRotationDriver'),
            )

    @property
    def vector_gizmos(self) -> members.SyncList | None:
        """The _vectorGizmos member."""
        member = self.get_member("_vectorGizmos")
        if isinstance(member, members.SyncList):
            return member
        return None

    @vector_gizmos.setter
    def vector_gizmos(self, value: members.SyncList) -> None:
        """Set the _vectorGizmos member."""
        self.set_member("_vectorGizmos", value)

    @property
    def cone_gizmos(self) -> members.SyncList | None:
        """The _coneGizmos member."""
        member = self.get_member("_coneGizmos")
        if isinstance(member, members.SyncList):
            return member
        return None

    @cone_gizmos.setter
    def cone_gizmos(self, value: members.SyncList) -> None:
        """Set the _coneGizmos member."""
        self.set_member("_coneGizmos", value)

