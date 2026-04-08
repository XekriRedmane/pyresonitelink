"""Generated component: BakeMeshes."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.component_handling import ComponentHandling
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BakeMeshes(GeneratedComponent, IAsyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Bake Meshes is a ProtoFlux node that takes a slot and combines it's meshes and slots into one slot. Allowing for the optimization of content and allowing for packing together objects. For example, many avatar statue makers use this to create statues out of people's avatars with no functionalities. It's a way to make a statue of your favorite contact on your shelf withouut having to have their 10000 ProtoFlux nodes still on it.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Assets
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.BakeMeshes"

    def __init__(self, root: str | INodeObjectOutput[Slot] | None = None, skinned_mesh_mode: str | INodeValueOutput[primitives.Bool] | None = None, include_inactive: str | INodeValueOutput[primitives.Bool] | None = None, destroy_original: str | INodeValueOutput[primitives.Bool] | None = None, assets_slot: str | INodeObjectOutput[Slot] | None = None, grabbable_handling: str | INodeValueOutput[ComponentHandling] | None = None, collider_handling: str | INodeValueOutput[ComponentHandling] | None = None, undoable: str | INodeValueOutput[primitives.Bool] | None = None, on_bake_started: str | INodeOperation | None = None, on_baked: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            root: Initial value for Root.
            skinned_mesh_mode: Initial value for SkinnedMeshMode.
            include_inactive: Initial value for IncludeInactive.
            destroy_original: Initial value for DestroyOriginal.
            assets_slot: Initial value for AssetsSlot.
            grabbable_handling: Initial value for GrabbableHandling.
            collider_handling: Initial value for ColliderHandling.
            undoable: Initial value for Undoable.
            on_bake_started: Initial value for OnBakeStarted.
            on_baked: Initial value for OnBaked.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if root is not None:
            self.root = root
        if skinned_mesh_mode is not None:
            self.skinned_mesh_mode = skinned_mesh_mode
        if include_inactive is not None:
            self.include_inactive = include_inactive
        if destroy_original is not None:
            self.destroy_original = destroy_original
        if assets_slot is not None:
            self.assets_slot = assets_slot
        if grabbable_handling is not None:
            self.grabbable_handling = grabbable_handling
        if collider_handling is not None:
            self.collider_handling = collider_handling
        if undoable is not None:
            self.undoable = undoable
        if on_bake_started is not None:
            self.on_bake_started = on_bake_started
        if on_baked is not None:
            self.on_baked = on_baked

    @property
    def root(self) -> str | None:
        """Target ID of the Root reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root.setter
    def root(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the Root reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Root",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def skinned_mesh_mode(self) -> str | None:
        """Target ID of the SkinnedMeshMode reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("SkinnedMeshMode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @skinned_mesh_mode.setter
    def skinned_mesh_mode(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the SkinnedMeshMode reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SkinnedMeshMode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SkinnedMeshMode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def include_inactive(self) -> str | None:
        """Target ID of the IncludeInactive reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("IncludeInactive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @include_inactive.setter
    def include_inactive(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the IncludeInactive reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("IncludeInactive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IncludeInactive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def destroy_original(self) -> str | None:
        """Target ID of the DestroyOriginal reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("DestroyOriginal")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @destroy_original.setter
    def destroy_original(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the DestroyOriginal reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("DestroyOriginal")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DestroyOriginal",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def assets_slot(self) -> str | None:
        """Target ID of the AssetsSlot reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("AssetsSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @assets_slot.setter
    def assets_slot(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the AssetsSlot reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("AssetsSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AssetsSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def grabbable_handling(self) -> str | None:
        """Target ID of the GrabbableHandling reference (targets INodeValueOutput[ComponentHandling])."""
        member = self.get_member("GrabbableHandling")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grabbable_handling.setter
    def grabbable_handling(self, target: str | INodeValueOutput[ComponentHandling] | None) -> None:
        """Set the GrabbableHandling reference by target ID or INodeValueOutput[ComponentHandling] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("GrabbableHandling")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "GrabbableHandling",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[FrooxEngine]FrooxEngine.ComponentHandling>'),
            )

    @property
    def collider_handling(self) -> str | None:
        """Target ID of the ColliderHandling reference (targets INodeValueOutput[ComponentHandling])."""
        member = self.get_member("ColliderHandling")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider_handling.setter
    def collider_handling(self, target: str | INodeValueOutput[ComponentHandling] | None) -> None:
        """Set the ColliderHandling reference by target ID or INodeValueOutput[ComponentHandling] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ColliderHandling")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ColliderHandling",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[FrooxEngine]FrooxEngine.ComponentHandling>'),
            )

    @property
    def undoable(self) -> str | None:
        """Target ID of the Undoable reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Undoable")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @undoable.setter
    def undoable(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Undoable reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Undoable")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Undoable",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def baked_root(self) -> members.EmptyElement | None:
        """The BakedRoot member."""
        member = self.get_member("BakedRoot")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @baked_root.setter
    def baked_root(self, value: members.EmptyElement) -> None:
        """Set the BakedRoot member."""
        self.set_member("BakedRoot", value)

    @property
    def on_bake_started(self) -> str | None:
        """Target ID of the OnBakeStarted reference (targets INodeOperation)."""
        member = self.get_member("OnBakeStarted")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_bake_started.setter
    def on_bake_started(self, target: str | INodeOperation | None) -> None:
        """Set the OnBakeStarted reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnBakeStarted")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnBakeStarted",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_baked(self) -> str | None:
        """Target ID of the OnBaked reference (targets INodeOperation)."""
        member = self.get_member("OnBaked")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_baked.setter
    def on_baked(self, target: str | INodeOperation | None) -> None:
        """Set the OnBaked reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnBaked")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnBaked",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

