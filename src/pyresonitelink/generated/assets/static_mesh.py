"""Generated component: StaticMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.istatic_asset_provider import IStaticAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StaticMesh(GeneratedComponent, IStaticAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The StaticMesh component is used to load a static mesh asset from the Uri specified in `URL`

Generally, you will not need to use this component directly, as it is created automatically when importing a new mesh, or when baking a Procedural Mesh using the Sync Method ``BakeMesh()``

    Category: Assets

    Attach to a slot, provide a ``URL`` and insert into a
    SkinnedMeshRenderer or MeshRenderer. Don't forget the Material(s).
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.StaticMesh"

    def __init__(self, url: str | None = None, readable: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            readable: Initial value for Readable.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if url is not None:
            self.url = url
        if readable is not None:
            self.readable = readable

    @property
    def url(self) -> str | None:
        """The Uri pointing to the .meshx asset to be loaded"""
        member = self.get_member("URL")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @url.setter
    def url(self, value: str) -> None:
        """Set the URL field value."""
        member = self.get_member("URL")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "URL", fields.FieldUri(value=value)
            )

    @property
    def readable(self) -> primitives.Bool | None:
        """Whether this component's data can be read via protoflux."""
        member = self.get_member("Readable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @readable.setter
    def readable(self, value: primitives.Bool) -> None:
        """Set the Readable field value."""
        member = self.get_member("Readable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Readable", fields.FieldBool(value=value)
            )

    async def recalculate_normals(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Use above function instead.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "RecalculateNormals", {}, debug,
        )

    async def recalculate_normals_merged(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Use above function instead.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "RecalculateNormalsMerged", {}, debug,
        )

    async def recalculate_tangents_simple(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Use above function instead.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "RecalculateTangentsSimple", {}, debug,
        )

    async def recalculate_tangents_mikktspace(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Recalcates mesh tangents which affect shading. This is Mikkspace which is defined by UnityEngine's definition.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "RecalculateTangentsMikktspace", {}, debug,
        )

    async def recalculate_blendshape_normals(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Use above function instead.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "RecalculateBlendshapeNormals", {}, debug,
        )

    async def recalculate_blendshape_normals_merged(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Use above function instead.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "RecalculateBlendshapeNormalsMerged", {}, debug,
        )

    async def recalculate_blendshape_tangents_mikktspace(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Recalculate the normals of blendshape data in Mikktspace.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "RecalculateBlendshapeTangentsMikktspace", {}, debug,
        )

    async def flip_normals(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Use above function instead.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "FlipNormals", {}, debug,
        )

    async def reverse_winding(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Use above function instead.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ReverseWinding", {}, debug,
        )

    async def make_dual_sided(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Use above function instead.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "MakeDualSided", {}, debug,
        )

    async def convert_to_flat_shading(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Use above function instead.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ConvertToFlatShading", {}, debug,
        )

    async def merge_doubles(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Use above function instead.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "MergeDoubles", {}, debug,
        )

    async def strip_empty_blendshapes(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Use above function instead.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "StripEmptyBlendshapes", {}, debug,
        )

    async def merge_blendshapes(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Use above function instead.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "MergeBlendshapes", {}, debug,
        )

    async def strip_blendshape_normals(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Use above function instead.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "StripBlendshapeNormals", {}, debug,
        )

    async def strip_blendshape_tangents(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Use above function instead.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "StripBlendshapeTangents", {}, debug,
        )

    async def trim_bone_weight_count(self, resolink: protocols.ResoniteLinkClient, max_bone_count: primitives.Int, debug: bool = False) -> dict:
        """Use above function instead.

        Args:
            resolink: Connected ResoniteLink client.
            max_bone_count: The maxBoneCount parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "TrimBoneWeightCount", {"maxBoneCount": max_bone_count}, debug,
        )

    async def convert_to_convex_hull(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Converts the mesh to a convex hull.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ConvertToConvexHull", {}, debug,
        )

    async def convert_to_point_cloud(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Converts the mesh to a point cloud.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ConvertToPointCloud", {}, debug,
        )

    async def translate_uvs(self, resolink: protocols.ResoniteLinkClient, offset: primitives.Float4, scale: primitives.Float4, debug: bool = False) -> dict:
        """Transforms the mesh UVs around.

        Args:
            resolink: Connected ResoniteLink client.
            offset: The offset parameter.
            scale: The scale parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "TranslateUVs", {"offset": offset, "scale": scale}, debug,
        )

