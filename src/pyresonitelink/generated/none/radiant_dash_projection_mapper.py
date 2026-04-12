"""Generated component: RadiantDashProjectionMapper."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.radiant_dash import RadiantDash
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.curved_plane_mesh import CurvedPlaneMesh
from pyresonitelink.generated._types.camera import Camera
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icanvas_point_projector import ICanvasPointProjector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RadiantDashProjectionMapper(GeneratedComponent, ICanvasPointProjector, IWorldEventReceiver):
    """See Dash menu.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RadiantDashProjectionMapper"

    def __init__(self, dash: str | RadiantDash | None = None, root: str | Slot | None = None, mesh: str | CurvedPlaneMesh | None = None, camera: str | Camera | None = None, uv_scale: str | IField[primitives.Float2] | None = None, uv_offset: str | IField[primitives.Float2] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            dash: Initial value for Dash.
            root: Initial value for Root.
            mesh: Initial value for Mesh.
            camera: Initial value for Camera.
            uv_scale: Initial value for UVScale.
            uv_offset: Initial value for UVOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if dash is not None:
            self.dash = dash
        if root is not None:
            self.root = root
        if mesh is not None:
            self.mesh = mesh
        if camera is not None:
            self.camera = camera
        if uv_scale is not None:
            self.uv_scale = uv_scale
        if uv_offset is not None:
            self.uv_offset = uv_offset

    @property
    def dash(self) -> str | None:
        """The Dash this is pointing to."""
        member = self.get_member("Dash")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @dash.setter
    def dash(self, target: str | RadiantDash | None) -> None:
        """Set the Dash reference by target ID or RadiantDash instance."""
        target_id: str | None = target.id if isinstance(target, RadiantDash) else target  # type: ignore[assignment]
        member = self.get_member("Dash")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Dash",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RadiantDash'),
            )

    @property
    def root(self) -> str | None:
        """The root of the thing this is trying to project from."""
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root.setter
    def root(self, target: str | Slot | None) -> None:
        """Set the Root reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Root",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def mesh(self) -> str | None:
        """The mesh this is trying to project to."""
        member = self.get_member("Mesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mesh.setter
    def mesh(self, target: str | CurvedPlaneMesh | None) -> None:
        """Set the Mesh reference by target ID or CurvedPlaneMesh instance."""
        target_id: str | None = target.id if isinstance(target, CurvedPlaneMesh) else target  # type: ignore[assignment]
        member = self.get_member("Mesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Mesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CurvedPlaneMesh'),
            )

    @property
    def camera(self) -> str | None:
        """The camera that is rendering ``Root``."""
        member = self.get_member("Camera")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @camera.setter
    def camera(self, target: str | Camera | None) -> None:
        """Set the Camera reference by target ID or Camera instance."""
        target_id: str | None = target.id if isinstance(target, Camera) else target  # type: ignore[assignment]
        member = self.get_member("Camera")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Camera",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Camera'),
            )

    @property
    def uv_scale(self) -> str | None:
        """The scale field to drive in order to do the remapping."""
        member = self.get_member("UVScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @uv_scale.setter
    def uv_scale(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the UVScale reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("UVScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UVScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def uv_offset(self) -> str | None:
        """The offset field to drive in order to do the remapping."""
        member = self.get_member("UVOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @uv_offset.setter
    def uv_offset(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the UVOffset reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("UVOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UVOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

