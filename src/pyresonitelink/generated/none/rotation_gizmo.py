"""Generated component: RotationGizmo."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.axis_rotation_gizmo import AxisRotationGizmo
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RotationGizmo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The RotationGizmo component is used by dev tools to allow rotation of slots.

See Dev tool.

    See Dev tool.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RotationGizmo"

    def __init__(self, x_gizmo: str | AxisRotationGizmo | None = None, y_gizmo: str | AxisRotationGizmo | None = None, z_gizmo: str | AxisRotationGizmo | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            x_gizmo: Initial value for _xGizmo.
            y_gizmo: Initial value for _yGizmo.
            z_gizmo: Initial value for _zGizmo.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if x_gizmo is not None:
            self.x_gizmo = x_gizmo
        if y_gizmo is not None:
            self.y_gizmo = y_gizmo
        if z_gizmo is not None:
            self.z_gizmo = z_gizmo

    @property
    def x_gizmo(self) -> str | None:
        """The rotation gizmo for the x axis."""
        member = self.get_member("_xGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @x_gizmo.setter
    def x_gizmo(self, target: str | AxisRotationGizmo | None) -> None:
        """Set the _xGizmo reference by target ID or AxisRotationGizmo instance."""
        target_id: str | None = target.id if isinstance(target, AxisRotationGizmo) else target  # type: ignore[assignment]
        member = self.get_member("_xGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_xGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AxisRotationGizmo'),
            )

    @property
    def y_gizmo(self) -> str | None:
        """The rotation gizmo for the y axis."""
        member = self.get_member("_yGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @y_gizmo.setter
    def y_gizmo(self, target: str | AxisRotationGizmo | None) -> None:
        """Set the _yGizmo reference by target ID or AxisRotationGizmo instance."""
        target_id: str | None = target.id if isinstance(target, AxisRotationGizmo) else target  # type: ignore[assignment]
        member = self.get_member("_yGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_yGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AxisRotationGizmo'),
            )

    @property
    def z_gizmo(self) -> str | None:
        """The rotation gizmo for the z axis."""
        member = self.get_member("_zGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @z_gizmo.setter
    def z_gizmo(self, target: str | AxisRotationGizmo | None) -> None:
        """Set the _zGizmo reference by target ID or AxisRotationGizmo instance."""
        target_id: str | None = target.id if isinstance(target, AxisRotationGizmo) else target  # type: ignore[assignment]
        member = self.get_member("_zGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_zGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AxisRotationGizmo'),
            )

