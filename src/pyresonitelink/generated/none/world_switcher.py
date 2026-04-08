"""Generated component: WorldSwitcher."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.repulsion_tree_simulator import RepulsionTreeSimulator
from pyresonitelink.generated._types.multi_segment_mesh import MultiSegmentMesh
from pyresonitelink.generated._types.slider import Slider
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldSwitcher(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.WorldSwitcher.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldSwitcher"

    def __init__(self, show: primitives.Bool | None = None, ignore_touches_from: str | Slot | None = None, repulsion_tree: str | RepulsionTreeSimulator | None = None, lines_mesh: str | MultiSegmentMesh | None = None, slider: str | Slider | None = None, center_orb: str | Slot | None = None, visual_root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            show: Initial value for Show.
            ignore_touches_from: Initial value for IgnoreTouchesFrom.
            repulsion_tree: Initial value for _repulsionTree.
            lines_mesh: Initial value for _linesMesh.
            slider: Initial value for _slider.
            center_orb: Initial value for _centerOrb.
            visual_root: Initial value for _visualRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if show is not None:
            self.show = show
        if ignore_touches_from is not None:
            self.ignore_touches_from = ignore_touches_from
        if repulsion_tree is not None:
            self.repulsion_tree = repulsion_tree
        if lines_mesh is not None:
            self.lines_mesh = lines_mesh
        if slider is not None:
            self.slider = slider
        if center_orb is not None:
            self.center_orb = center_orb
        if visual_root is not None:
            self.visual_root = visual_root

    @property
    def show(self) -> primitives.Bool | None:
        """The Show field value."""
        member = self.get_member("Show")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show.setter
    def show(self, value: primitives.Bool) -> None:
        """Set the Show field value."""
        member = self.get_member("Show")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Show", fields.FieldBool(value=value)
            )

    @property
    def ignore_touches_from(self) -> str | None:
        """Target ID of the IgnoreTouchesFrom reference (targets Slot)."""
        member = self.get_member("IgnoreTouchesFrom")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ignore_touches_from.setter
    def ignore_touches_from(self, target: str | Slot | None) -> None:
        """Set the IgnoreTouchesFrom reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("IgnoreTouchesFrom")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IgnoreTouchesFrom",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def repulsion_tree(self) -> str | None:
        """Target ID of the _repulsionTree reference (targets RepulsionTreeSimulator)."""
        member = self.get_member("_repulsionTree")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @repulsion_tree.setter
    def repulsion_tree(self, target: str | RepulsionTreeSimulator | None) -> None:
        """Set the _repulsionTree reference by target ID or RepulsionTreeSimulator instance."""
        target_id: str | None = target.id if isinstance(target, RepulsionTreeSimulator) else target  # type: ignore[assignment]
        member = self.get_member("_repulsionTree")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_repulsionTree",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RepulsionTreeSimulator'),
            )

    @property
    def lines_mesh(self) -> str | None:
        """Target ID of the _linesMesh reference (targets MultiSegmentMesh)."""
        member = self.get_member("_linesMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lines_mesh.setter
    def lines_mesh(self, target: str | MultiSegmentMesh | None) -> None:
        """Set the _linesMesh reference by target ID or MultiSegmentMesh instance."""
        target_id: str | None = target.id if isinstance(target, MultiSegmentMesh) else target  # type: ignore[assignment]
        member = self.get_member("_linesMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_linesMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MultiSegmentMesh'),
            )

    @property
    def slider(self) -> str | None:
        """Target ID of the _slider reference (targets Slider)."""
        member = self.get_member("_slider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @slider.setter
    def slider(self, target: str | Slider | None) -> None:
        """Set the _slider reference by target ID or Slider instance."""
        target_id: str | None = target.id if isinstance(target, Slider) else target  # type: ignore[assignment]
        member = self.get_member("_slider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_slider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slider'),
            )

    @property
    def center_orb(self) -> str | None:
        """Target ID of the _centerOrb reference (targets Slot)."""
        member = self.get_member("_centerOrb")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @center_orb.setter
    def center_orb(self, target: str | Slot | None) -> None:
        """Set the _centerOrb reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_centerOrb")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_centerOrb",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def visual_root(self) -> str | None:
        """Target ID of the _visualRoot reference (targets Slot)."""
        member = self.get_member("_visualRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual_root.setter
    def visual_root(self, target: str | Slot | None) -> None:
        """Set the _visualRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_visualRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visualRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

