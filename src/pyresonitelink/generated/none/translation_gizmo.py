"""Generated component: TranslationGizmo."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.volume_translation_gizmo import VolumeTranslationGizmo
from pyresonitelink.generated._types.plane_translation_gizmo import PlaneTranslationGizmo
from pyresonitelink.generated._types.axis_translation_gizmo import AxisTranslationGizmo
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TranslationGizmo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TranslationGizmo.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TranslationGizmo"

    def __init__(self, xyz_gizmo: str | VolumeTranslationGizmo | None = None, xy_gizmo: str | PlaneTranslationGizmo | None = None, xz_gizmo: str | PlaneTranslationGizmo | None = None, yz_gizmo: str | PlaneTranslationGizmo | None = None, x_gizmo: str | AxisTranslationGizmo | None = None, y_gizmo: str | AxisTranslationGizmo | None = None, z_gizmo: str | AxisTranslationGizmo | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            xyz_gizmo: Initial value for _xyzGizmo.
            xy_gizmo: Initial value for _xyGizmo.
            xz_gizmo: Initial value for _xzGizmo.
            yz_gizmo: Initial value for _yzGizmo.
            x_gizmo: Initial value for _xGizmo.
            y_gizmo: Initial value for _yGizmo.
            z_gizmo: Initial value for _zGizmo.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if xyz_gizmo is not None:
            self.xyz_gizmo = xyz_gizmo
        if xy_gizmo is not None:
            self.xy_gizmo = xy_gizmo
        if xz_gizmo is not None:
            self.xz_gizmo = xz_gizmo
        if yz_gizmo is not None:
            self.yz_gizmo = yz_gizmo
        if x_gizmo is not None:
            self.x_gizmo = x_gizmo
        if y_gizmo is not None:
            self.y_gizmo = y_gizmo
        if z_gizmo is not None:
            self.z_gizmo = z_gizmo

    @property
    def xyz_gizmo(self) -> str | None:
        """Target ID of the _xyzGizmo reference (targets VolumeTranslationGizmo)."""
        member = self.get_member("_xyzGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @xyz_gizmo.setter
    def xyz_gizmo(self, target: str | VolumeTranslationGizmo | None) -> None:
        """Set the _xyzGizmo reference by target ID or VolumeTranslationGizmo instance."""
        target_id: str | None = target.id if isinstance(target, VolumeTranslationGizmo) else target  # type: ignore[assignment]
        member = self.get_member("_xyzGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_xyzGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.VolumeTranslationGizmo'),
            )

    @property
    def xy_gizmo(self) -> str | None:
        """Target ID of the _xyGizmo reference (targets PlaneTranslationGizmo)."""
        member = self.get_member("_xyGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @xy_gizmo.setter
    def xy_gizmo(self, target: str | PlaneTranslationGizmo | None) -> None:
        """Set the _xyGizmo reference by target ID or PlaneTranslationGizmo instance."""
        target_id: str | None = target.id if isinstance(target, PlaneTranslationGizmo) else target  # type: ignore[assignment]
        member = self.get_member("_xyGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_xyGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PlaneTranslationGizmo'),
            )

    @property
    def xz_gizmo(self) -> str | None:
        """Target ID of the _xzGizmo reference (targets PlaneTranslationGizmo)."""
        member = self.get_member("_xzGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @xz_gizmo.setter
    def xz_gizmo(self, target: str | PlaneTranslationGizmo | None) -> None:
        """Set the _xzGizmo reference by target ID or PlaneTranslationGizmo instance."""
        target_id: str | None = target.id if isinstance(target, PlaneTranslationGizmo) else target  # type: ignore[assignment]
        member = self.get_member("_xzGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_xzGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PlaneTranslationGizmo'),
            )

    @property
    def yz_gizmo(self) -> str | None:
        """Target ID of the _yzGizmo reference (targets PlaneTranslationGizmo)."""
        member = self.get_member("_yzGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @yz_gizmo.setter
    def yz_gizmo(self, target: str | PlaneTranslationGizmo | None) -> None:
        """Set the _yzGizmo reference by target ID or PlaneTranslationGizmo instance."""
        target_id: str | None = target.id if isinstance(target, PlaneTranslationGizmo) else target  # type: ignore[assignment]
        member = self.get_member("_yzGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_yzGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PlaneTranslationGizmo'),
            )

    @property
    def x_gizmo(self) -> str | None:
        """Target ID of the _xGizmo reference (targets AxisTranslationGizmo)."""
        member = self.get_member("_xGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @x_gizmo.setter
    def x_gizmo(self, target: str | AxisTranslationGizmo | None) -> None:
        """Set the _xGizmo reference by target ID or AxisTranslationGizmo instance."""
        target_id: str | None = target.id if isinstance(target, AxisTranslationGizmo) else target  # type: ignore[assignment]
        member = self.get_member("_xGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_xGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AxisTranslationGizmo'),
            )

    @property
    def y_gizmo(self) -> str | None:
        """Target ID of the _yGizmo reference (targets AxisTranslationGizmo)."""
        member = self.get_member("_yGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @y_gizmo.setter
    def y_gizmo(self, target: str | AxisTranslationGizmo | None) -> None:
        """Set the _yGizmo reference by target ID or AxisTranslationGizmo instance."""
        target_id: str | None = target.id if isinstance(target, AxisTranslationGizmo) else target  # type: ignore[assignment]
        member = self.get_member("_yGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_yGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AxisTranslationGizmo'),
            )

    @property
    def z_gizmo(self) -> str | None:
        """Target ID of the _zGizmo reference (targets AxisTranslationGizmo)."""
        member = self.get_member("_zGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @z_gizmo.setter
    def z_gizmo(self, target: str | AxisTranslationGizmo | None) -> None:
        """Set the _zGizmo reference by target ID or AxisTranslationGizmo instance."""
        target_id: str | None = target.id if isinstance(target, AxisTranslationGizmo) else target  # type: ignore[assignment]
        member = self.get_member("_zGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_zGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AxisTranslationGizmo'),
            )

