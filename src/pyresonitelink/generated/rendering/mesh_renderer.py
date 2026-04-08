"""Generated component: MeshRenderer."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.mesh import Mesh
from pyresonitelink.generated._types.ibounded import IBounded
from pyresonitelink.generated._types.ihighlightable import IHighlightable
from pyresonitelink.generated._types.irenderable import IRenderable
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MeshRenderer(GeneratedComponent, IBounded, IHighlightable, IRenderable, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.MeshRenderer.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MeshRenderer"

    def __init__(self, mesh: str | IAssetProvider[Mesh] | None = None, sorting_order: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            mesh: Initial value for Mesh.
            sorting_order: Initial value for SortingOrder.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if mesh is not None:
            self.mesh = mesh
        if sorting_order is not None:
            self.sorting_order = sorting_order

    @property
    def mesh(self) -> str | None:
        """Target ID of the Mesh reference (targets IAssetProvider[Mesh])."""
        member = self.get_member("Mesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mesh.setter
    def mesh(self, target: str | IAssetProvider[Mesh] | None) -> None:
        """Set the Mesh reference by target ID or IAssetProvider[Mesh] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Mesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Mesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Mesh>'),
            )

    @property
    def materials(self) -> members.SyncList | None:
        """The Materials member."""
        member = self.get_member("Materials")
        if isinstance(member, members.SyncList):
            return member
        return None

    @materials.setter
    def materials(self, value: members.SyncList) -> None:
        """Set the Materials member."""
        self.set_member("Materials", value)

    @property
    def material_property_blocks(self) -> members.SyncList | None:
        """The MaterialPropertyBlocks member."""
        member = self.get_member("MaterialPropertyBlocks")
        if isinstance(member, members.SyncList):
            return member
        return None

    @material_property_blocks.setter
    def material_property_blocks(self, value: members.SyncList) -> None:
        """Set the MaterialPropertyBlocks member."""
        self.set_member("MaterialPropertyBlocks", value)

    @property
    def shadow_cast_mode(self) -> members.FieldEnum | None:
        """The ShadowCastMode member."""
        member = self.get_member("ShadowCastMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @shadow_cast_mode.setter
    def shadow_cast_mode(self, value: members.FieldEnum) -> None:
        """Set the ShadowCastMode member."""
        self.set_member("ShadowCastMode", value)

    @property
    def motion_vector_mode(self) -> members.FieldEnum | None:
        """The MotionVectorMode member."""
        member = self.get_member("MotionVectorMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @motion_vector_mode.setter
    def motion_vector_mode(self, value: members.FieldEnum) -> None:
        """Set the MotionVectorMode member."""
        self.set_member("MotionVectorMode", value)

    @property
    def sorting_order(self) -> np.int32 | None:
        """The SortingOrder field value."""
        member = self.get_member("SortingOrder")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sorting_order.setter
    def sorting_order(self, value: np.int32) -> None:
        """Set the SortingOrder field value."""
        member = self.get_member("SortingOrder")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SortingOrder", fields.FieldInt(value=value)
            )

    async def split_submeshes(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the SplitSubmeshes sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SplitSubmeshes", {}, debug,
        )

    async def merge_by_material(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the MergeByMaterial sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "MergeByMaterial", {}, debug,
        )

