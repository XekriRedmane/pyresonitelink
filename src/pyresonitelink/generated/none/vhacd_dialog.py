"""Generated component: VHACD_Dialog."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.decomposition_mode import DecompositionMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.mesh_collider import MeshCollider
from pyresonitelink.generated._types.checkbox import Checkbox
from pyresonitelink.generated._types.int_text_editor_parser import IntTextEditorParser
from pyresonitelink.generated._types.float_text_editor_parser import FloatTextEditorParser
from pyresonitelink.generated._types.ideveloper_interface import IDeveloperInterface
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VHACD_Dialog(GeneratedComponent, IDeveloperInterface, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VHACD_Dialog.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VHACD_Dialog"

    def __init__(self, target_collider: str | MeshCollider | None = None, merge_doubles: str | Checkbox | None = None, resolution: str | IntTextEditorParser | None = None, depth: str | IntTextEditorParser | None = None, concavity: str | FloatTextEditorParser | None = None, plane_downsampling: str | IntTextEditorParser | None = None, convex_hull_downsampling: str | IntTextEditorParser | None = None, alpha: str | FloatTextEditorParser | None = None, beta: str | FloatTextEditorParser | None = None, gamma: str | FloatTextEditorParser | None = None, delta: str | FloatTextEditorParser | None = None, pca: str | Checkbox | None = None, mode: DecompositionMode | str | None = None, max_vertices_per_hull: str | IntTextEditorParser | None = None, min_volume_per_hull: str | FloatTextEditorParser | None = None, convex_hull_approximation: str | Checkbox | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_collider: Initial value for TargetCollider.
            merge_doubles: Initial value for MergeDoubles.
            resolution: Initial value for Resolution.
            depth: Initial value for Depth.
            concavity: Initial value for Concavity.
            plane_downsampling: Initial value for PlaneDownsampling.
            convex_hull_downsampling: Initial value for ConvexHullDownsampling.
            alpha: Initial value for Alpha.
            beta: Initial value for Beta.
            gamma: Initial value for Gamma.
            delta: Initial value for Delta.
            pca: Initial value for PCA.
            mode: Initial value for Mode.
            max_vertices_per_hull: Initial value for MaxVerticesPerHull.
            min_volume_per_hull: Initial value for MinVolumePerHull.
            convex_hull_approximation: Initial value for ConvexHullApproximation.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_collider is not None:
            self.target_collider = target_collider
        if merge_doubles is not None:
            self.merge_doubles = merge_doubles
        if resolution is not None:
            self.resolution = resolution
        if depth is not None:
            self.depth = depth
        if concavity is not None:
            self.concavity = concavity
        if plane_downsampling is not None:
            self.plane_downsampling = plane_downsampling
        if convex_hull_downsampling is not None:
            self.convex_hull_downsampling = convex_hull_downsampling
        if alpha is not None:
            self.alpha = alpha
        if beta is not None:
            self.beta = beta
        if gamma is not None:
            self.gamma = gamma
        if delta is not None:
            self.delta = delta
        if pca is not None:
            self.pca = pca
        if mode is not None:
            self.mode = mode
        if max_vertices_per_hull is not None:
            self.max_vertices_per_hull = max_vertices_per_hull
        if min_volume_per_hull is not None:
            self.min_volume_per_hull = min_volume_per_hull
        if convex_hull_approximation is not None:
            self.convex_hull_approximation = convex_hull_approximation

    @property
    def target_collider(self) -> str | None:
        """Target ID of the TargetCollider reference (targets MeshCollider)."""
        member = self.get_member("TargetCollider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_collider.setter
    def target_collider(self, target: str | MeshCollider | None) -> None:
        """Set the TargetCollider reference by target ID or MeshCollider instance."""
        target_id: str | None = target.id if isinstance(target, MeshCollider) else target  # type: ignore[assignment]
        member = self.get_member("TargetCollider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetCollider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MeshCollider'),
            )

    @property
    def merge_doubles(self) -> str | None:
        """Target ID of the MergeDoubles reference (targets Checkbox)."""
        member = self.get_member("MergeDoubles")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @merge_doubles.setter
    def merge_doubles(self, target: str | Checkbox | None) -> None:
        """Set the MergeDoubles reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("MergeDoubles")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MergeDoubles",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def resolution(self) -> str | None:
        """Target ID of the Resolution reference (targets IntTextEditorParser)."""
        member = self.get_member("Resolution")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @resolution.setter
    def resolution(self, target: str | IntTextEditorParser | None) -> None:
        """Set the Resolution reference by target ID or IntTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, IntTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("Resolution")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Resolution",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IntTextEditorParser'),
            )

    @property
    def depth(self) -> str | None:
        """Target ID of the Depth reference (targets IntTextEditorParser)."""
        member = self.get_member("Depth")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @depth.setter
    def depth(self, target: str | IntTextEditorParser | None) -> None:
        """Set the Depth reference by target ID or IntTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, IntTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("Depth")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Depth",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IntTextEditorParser'),
            )

    @property
    def concavity(self) -> str | None:
        """Target ID of the Concavity reference (targets FloatTextEditorParser)."""
        member = self.get_member("Concavity")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @concavity.setter
    def concavity(self, target: str | FloatTextEditorParser | None) -> None:
        """Set the Concavity reference by target ID or FloatTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, FloatTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("Concavity")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Concavity",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FloatTextEditorParser'),
            )

    @property
    def plane_downsampling(self) -> str | None:
        """Target ID of the PlaneDownsampling reference (targets IntTextEditorParser)."""
        member = self.get_member("PlaneDownsampling")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @plane_downsampling.setter
    def plane_downsampling(self, target: str | IntTextEditorParser | None) -> None:
        """Set the PlaneDownsampling reference by target ID or IntTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, IntTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("PlaneDownsampling")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PlaneDownsampling",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IntTextEditorParser'),
            )

    @property
    def convex_hull_downsampling(self) -> str | None:
        """Target ID of the ConvexHullDownsampling reference (targets IntTextEditorParser)."""
        member = self.get_member("ConvexHullDownsampling")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @convex_hull_downsampling.setter
    def convex_hull_downsampling(self, target: str | IntTextEditorParser | None) -> None:
        """Set the ConvexHullDownsampling reference by target ID or IntTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, IntTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("ConvexHullDownsampling")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ConvexHullDownsampling",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IntTextEditorParser'),
            )

    @property
    def alpha(self) -> str | None:
        """Target ID of the Alpha reference (targets FloatTextEditorParser)."""
        member = self.get_member("Alpha")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @alpha.setter
    def alpha(self, target: str | FloatTextEditorParser | None) -> None:
        """Set the Alpha reference by target ID or FloatTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, FloatTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("Alpha")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Alpha",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FloatTextEditorParser'),
            )

    @property
    def beta(self) -> str | None:
        """Target ID of the Beta reference (targets FloatTextEditorParser)."""
        member = self.get_member("Beta")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @beta.setter
    def beta(self, target: str | FloatTextEditorParser | None) -> None:
        """Set the Beta reference by target ID or FloatTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, FloatTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("Beta")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Beta",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FloatTextEditorParser'),
            )

    @property
    def gamma(self) -> str | None:
        """Target ID of the Gamma reference (targets FloatTextEditorParser)."""
        member = self.get_member("Gamma")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @gamma.setter
    def gamma(self, target: str | FloatTextEditorParser | None) -> None:
        """Set the Gamma reference by target ID or FloatTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, FloatTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("Gamma")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Gamma",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FloatTextEditorParser'),
            )

    @property
    def delta(self) -> str | None:
        """Target ID of the Delta reference (targets FloatTextEditorParser)."""
        member = self.get_member("Delta")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @delta.setter
    def delta(self, target: str | FloatTextEditorParser | None) -> None:
        """Set the Delta reference by target ID or FloatTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, FloatTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("Delta")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Delta",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FloatTextEditorParser'),
            )

    @property
    def pca(self) -> str | None:
        """Target ID of the PCA reference (targets Checkbox)."""
        member = self.get_member("PCA")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pca.setter
    def pca(self, target: str | Checkbox | None) -> None:
        """Set the PCA reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("PCA")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PCA",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def mode(self) -> DecompositionMode | None:
        """The Mode enum value."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return DecompositionMode(member.value)
        return None

    @mode.setter
    def mode(self, value: DecompositionMode | str) -> None:
        """Set the Mode enum value."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Mode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def max_vertices_per_hull(self) -> str | None:
        """Target ID of the MaxVerticesPerHull reference (targets IntTextEditorParser)."""
        member = self.get_member("MaxVerticesPerHull")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @max_vertices_per_hull.setter
    def max_vertices_per_hull(self, target: str | IntTextEditorParser | None) -> None:
        """Set the MaxVerticesPerHull reference by target ID or IntTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, IntTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("MaxVerticesPerHull")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MaxVerticesPerHull",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IntTextEditorParser'),
            )

    @property
    def min_volume_per_hull(self) -> str | None:
        """Target ID of the MinVolumePerHull reference (targets FloatTextEditorParser)."""
        member = self.get_member("MinVolumePerHull")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @min_volume_per_hull.setter
    def min_volume_per_hull(self, target: str | FloatTextEditorParser | None) -> None:
        """Set the MinVolumePerHull reference by target ID or FloatTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, FloatTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("MinVolumePerHull")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MinVolumePerHull",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FloatTextEditorParser'),
            )

    @property
    def convex_hull_approximation(self) -> str | None:
        """Target ID of the ConvexHullApproximation reference (targets Checkbox)."""
        member = self.get_member("ConvexHullApproximation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @convex_hull_approximation.setter
    def convex_hull_approximation(self, target: str | Checkbox | None) -> None:
        """Set the ConvexHullApproximation reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("ConvexHullApproximation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ConvexHullApproximation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

