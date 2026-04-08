"""Generated component: FlashHighlightHierarchy."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FlashHighlightHierarchy(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Flash Highlight Hierarchy node takes in the target slot hierarchy, what to exclude, if this flash should track the position, how long the flash should be, and what color it should be. Then this node will make that hierarchy flash, also providing the slot of the flash itself.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Rendering
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Rendering.FlashHighlightHierarchy"

    def __init__(self, next: str | INodeOperation | None = None, hierarchy_root: str | INodeObjectOutput[Slot] | None = None, exclude_colliders: str | INodeValueOutput[primitives.Bool] | None = None, exclude_meshes: str | INodeValueOutput[primitives.Bool] | None = None, exclude_disabled: str | INodeValueOutput[primitives.Bool] | None = None, track_position: str | INodeValueOutput[primitives.Bool] | None = None, duration: str | INodeValueOutput[primitives.Float] | None = None, color: str | INodeValueOutput[primitives.ColorX] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            hierarchy_root: Initial value for HierarchyRoot.
            exclude_colliders: Initial value for ExcludeColliders.
            exclude_meshes: Initial value for ExcludeMeshes.
            exclude_disabled: Initial value for ExcludeDisabled.
            track_position: Initial value for TrackPosition.
            duration: Initial value for Duration.
            color: Initial value for Color.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if hierarchy_root is not None:
            self.hierarchy_root = hierarchy_root
        if exclude_colliders is not None:
            self.exclude_colliders = exclude_colliders
        if exclude_meshes is not None:
            self.exclude_meshes = exclude_meshes
        if exclude_disabled is not None:
            self.exclude_disabled = exclude_disabled
        if track_position is not None:
            self.track_position = track_position
        if duration is not None:
            self.duration = duration
        if color is not None:
            self.color = color

    @property
    def next(self) -> str | None:
        """Target ID of the Next reference (targets INodeOperation)."""
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @next.setter
    def next(self, target: str | INodeOperation | None) -> None:
        """Set the Next reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Next",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def hierarchy_root(self) -> str | None:
        """Target ID of the HierarchyRoot reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("HierarchyRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hierarchy_root.setter
    def hierarchy_root(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the HierarchyRoot reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("HierarchyRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HierarchyRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def exclude_colliders(self) -> str | None:
        """Target ID of the ExcludeColliders reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("ExcludeColliders")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @exclude_colliders.setter
    def exclude_colliders(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the ExcludeColliders reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ExcludeColliders")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ExcludeColliders",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def exclude_meshes(self) -> str | None:
        """Target ID of the ExcludeMeshes reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("ExcludeMeshes")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @exclude_meshes.setter
    def exclude_meshes(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the ExcludeMeshes reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ExcludeMeshes")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ExcludeMeshes",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def exclude_disabled(self) -> str | None:
        """Target ID of the ExcludeDisabled reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("ExcludeDisabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @exclude_disabled.setter
    def exclude_disabled(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the ExcludeDisabled reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ExcludeDisabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ExcludeDisabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def track_position(self) -> str | None:
        """Target ID of the TrackPosition reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("TrackPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @track_position.setter
    def track_position(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the TrackPosition reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("TrackPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TrackPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def duration(self) -> str | None:
        """Target ID of the Duration reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Duration")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @duration.setter
    def duration(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Duration reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Duration")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Duration",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def color(self) -> str | None:
        """Target ID of the Color reference (targets INodeValueOutput[primitives.ColorX])."""
        member = self.get_member("Color")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color.setter
    def color(self, target: str | INodeValueOutput[primitives.ColorX] | None) -> None:
        """Set the Color reference by target ID or INodeValueOutput[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Color")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Color",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<colorX>'),
            )

    @property
    def flash_root(self) -> members.EmptyElement | None:
        """The FlashRoot member."""
        member = self.get_member("FlashRoot")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @flash_root.setter
    def flash_root(self, value: members.EmptyElement) -> None:
        """Set the FlashRoot member."""
        self.set_member("FlashRoot", value)

