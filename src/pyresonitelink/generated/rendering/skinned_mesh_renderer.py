"""Generated component: SkinnedMeshRenderer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.shadow_cast_mode import ShadowCastMode
from pyresonitelink.generated._enums.motion_vector_mode import MotionVectorMode
from pyresonitelink.generated._enums.skinned_bounds import SkinnedBounds
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.mesh import Mesh
from pyresonitelink.generated._types.skinned_mesh_renderer import SkinnedMeshRenderer
from pyresonitelink.generated._types.icustom_member_name_source import ICustomMemberNameSource
from pyresonitelink.generated._types.ibounded import IBounded
from pyresonitelink.generated._types.ihighlightable import IHighlightable
from pyresonitelink.generated._types.irenderable import IRenderable
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SkinnedMeshRenderer(GeneratedComponent, ICustomMemberNameSource, IBounded, IHighlightable, IRenderable, ICustomInspector, IWorldEventReceiver):
    """The SkinnedMeshRenderer component is used for rendering animated/dynamic 3D meshes in the world, and applying materials to that mesh.

    Category: Rendering

    While it can be used for rendering static meshes, it is not recommended
    as there is a slight performance penalty for using SkinnedMeshRenderer,
    even if the animation features aren't used &mdash; Please try to use
    MeshRenderer where possible.

    **See also**: * MeshRenderer
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SkinnedMeshRenderer"

    def __init__(self, mesh: str | IAssetProvider[Mesh] | None = None, shadow_cast_mode: ShadowCastMode | str | None = None, motion_vector_mode: MotionVectorMode | str | None = None, sorting_order: primitives.Int | None = None, bounds_compute_method: SkinnedBounds | str | None = None, proxy_bounds_source: str | SkinnedMeshRenderer | None = None, explicit_local_bounds: primitives.BoundingBox | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            mesh: Initial value for Mesh.
            shadow_cast_mode: Initial value for ShadowCastMode.
            motion_vector_mode: Initial value for MotionVectorMode.
            sorting_order: Initial value for SortingOrder.
            bounds_compute_method: Initial value for BoundsComputeMethod.
            proxy_bounds_source: Initial value for ProxyBoundsSource.
            explicit_local_bounds: Initial value for ExplicitLocalBounds.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if mesh is not None:
            self.mesh = mesh
        if shadow_cast_mode is not None:
            self.shadow_cast_mode = shadow_cast_mode
        if motion_vector_mode is not None:
            self.motion_vector_mode = motion_vector_mode
        if sorting_order is not None:
            self.sorting_order = sorting_order
        if bounds_compute_method is not None:
            self.bounds_compute_method = bounds_compute_method
        if proxy_bounds_source is not None:
            self.proxy_bounds_source = proxy_bounds_source
        if explicit_local_bounds is not None:
            self.explicit_local_bounds = explicit_local_bounds

    @property
    def mesh(self) -> str | None:
        """The mesh to be rendered. Can be a StaticMesh or a Procedural Mesh"""
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
        """A list of materials to be applied to the mesh"""
        member = self.get_member("Materials")
        if isinstance(member, members.SyncList):
            return member
        return None

    @materials.setter
    def materials(self, value: members.SyncList) -> None:
        """Set Materials. A list of materials to be applied to the mesh"""
        self.set_member("Materials", value)

    @property
    def material_property_blocks(self) -> members.SyncList | None:
        """A list of material property blocks to apply to the materials on this mesh. Usually used for performance reasons where using multiple similar materials would take more resources."""
        member = self.get_member("MaterialPropertyBlocks")
        if isinstance(member, members.SyncList):
            return member
        return None

    @material_property_blocks.setter
    def material_property_blocks(self, value: members.SyncList) -> None:
        """Set MaterialPropertyBlocks. A list of material property blocks to apply to the materials on this mesh. Usually used for performance reasons where using multiple similar materials would take more resources."""
        self.set_member("MaterialPropertyBlocks", value)

    @property
    def shadow_cast_mode(self) -> ShadowCastMode | None:
        """How this object will cast shadows onto the world, or if it only draws a shadow."""
        member = self.get_member("ShadowCastMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ShadowCastMode(member.value)
        return None

    @shadow_cast_mode.setter
    def shadow_cast_mode(self, value: ShadowCastMode | str) -> None:
        """Set ShadowCastMode. How this object will cast shadows onto the world, or if it only draws a shadow."""
        member = self.get_member("ShadowCastMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ShadowCastMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def motion_vector_mode(self) -> MotionVectorMode | None:
        """See Motion vector mode."""
        member = self.get_member("MotionVectorMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return MotionVectorMode(member.value)
        return None

    @motion_vector_mode.setter
    def motion_vector_mode(self, value: MotionVectorMode | str) -> None:
        """Set MotionVectorMode. See Motion vector mode."""
        member = self.get_member("MotionVectorMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "MotionVectorMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def sorting_order(self) -> primitives.Int | None:
        """Whether to render this before or after other renderers with geometry in the same location."""
        member = self.get_member("SortingOrder")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sorting_order.setter
    def sorting_order(self, value: primitives.Int) -> None:
        """Set the SortingOrder field value."""
        member = self.get_member("SortingOrder")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SortingOrder", fields.FieldInt(value=value)
            )

    @property
    def bounds_compute_method(self) -> SkinnedBounds | None:
        """How the bounds of this mesh will be calculated. Should be left as Static if possible, for performance reasons."""
        member = self.get_member("BoundsComputeMethod")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SkinnedBounds(member.value)
        return None

    @bounds_compute_method.setter
    def bounds_compute_method(self, value: SkinnedBounds | str) -> None:
        """Set BoundsComputeMethod. How the bounds of this mesh will be calculated. Should be left as Static if possible, for performance reasons."""
        member = self.get_member("BoundsComputeMethod")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "BoundsComputeMethod",
                members.FieldEnum(value=str(value)),
            )

    @property
    def proxy_bounds_source(self) -> str | None:
        """A SkinnedMeshRenderer to use the ``ExplicitLocalBounds`` of rather than the ``ExplicitLocalBounds`` on this component."""
        member = self.get_member("ProxyBoundsSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @proxy_bounds_source.setter
    def proxy_bounds_source(self, target: str | SkinnedMeshRenderer | None) -> None:
        """Set the ProxyBoundsSource reference by target ID or SkinnedMeshRenderer instance."""
        target_id: str | None = target.id if isinstance(target, SkinnedMeshRenderer) else target  # type: ignore[assignment]
        member = self.get_member("ProxyBoundsSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ProxyBoundsSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SkinnedMeshRenderer'),
            )

    @property
    def explicit_local_bounds(self) -> primitives.BoundingBox | None:
        """A box that within view will render the mesh, and when out of view will cull the mesh and stop rendering it. Is used when ``ProxyBoundsSource`` is null."""
        member = self.get_member("ExplicitLocalBounds")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @explicit_local_bounds.setter
    def explicit_local_bounds(self, value: primitives.BoundingBox) -> None:
        """Set the ExplicitLocalBounds field value."""
        member = self.get_member("ExplicitLocalBounds")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ExplicitLocalBounds", fields.FieldBoundingBox(value=value)
            )

    @property
    def bones(self) -> members.SyncList | None:
        """Automatically Assigned &mdash; List of bones present in this mesh"""
        member = self.get_member("Bones")
        if isinstance(member, members.SyncList):
            return member
        return None

    @bones.setter
    def bones(self, value: members.SyncList) -> None:
        """Set Bones. Automatically Assigned &mdash; List of bones present in this mesh"""
        self.set_member("Bones", value)

    @property
    def blend_shape_weights(self) -> members.SyncList | None:
        """Automatically Assigned &mdash; List of blendshapes present in this mesh, and their respective weights."""
        member = self.get_member("BlendShapeWeights")
        if isinstance(member, members.SyncList):
            return member
        return None

    @blend_shape_weights.setter
    def blend_shape_weights(self, value: members.SyncList) -> None:
        """Set BlendShapeWeights. Automatically Assigned &mdash; List of blendshapes present in this mesh, and their respective weights."""
        self.set_member("BlendShapeWeights", value)

    async def split_blenshape_along_axis(self, resolink: protocols.ResoniteLinkClient, blendshape_index: primitives.Int, axis: str, center_: primitives.Float, transition: primitives.Float, negative_suffix: primitives.String, positive_suffix: primitives.String, debug: bool = False) -> dict:
        """Splits a blendshape along a given axis, and returns a task representing if the operation is done yet.

        Args:
            resolink: Connected ResoniteLink client.
            blendshape_index: The blendshapeIndex parameter.
            axis: The axis parameter.
            center_: The center parameter.
            transition: The transition parameter.
            negative_suffix: The negativeSuffix parameter.
            positive_suffix: The positiveSuffix parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SplitBlenshapeAlongAxis", {"blendshapeIndex": blendshape_index, "axis": axis, "center": center_, "transition": transition, "negativeSuffix": negative_suffix, "positiveSuffix": positive_suffix}, debug,
        )

    async def bake_blendshape(self, resolink: protocols.ResoniteLinkClient, blendshape_index: primitives.Int, debug: bool = False) -> dict:
        """bakes a blendshape to make it part of the mesh rest state, and returns a task representing if the operation is done yet.

        Args:
            resolink: Connected ResoniteLink client.
            blendshape_index: The blendshapeIndex parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeBlendshape", {"blendshapeIndex": blendshape_index}, debug,
        )

    async def remove_blendshape(self, resolink: protocols.ResoniteLinkClient, blendshape_index: primitives.Int, debug: bool = False) -> dict:
        """removes a blendshape from the mesh, and returns a task representing if the operation is done yet.

        Args:
            resolink: Connected ResoniteLink client.
            blendshape_index: The blendshapeIndex parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "RemoveBlendshape", {"blendshapeIndex": blendshape_index}, debug,
        )

    async def split_submeshes(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Will split this mesh into additional submeshes, each having only one material

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SplitSubmeshes", {}, debug,
        )

    async def merge_by_material(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Will merge all submeshes that use the same material

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "MergeByMaterial", {}, debug,
        )

