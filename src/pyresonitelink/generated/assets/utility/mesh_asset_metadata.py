"""Generated component: MeshAssetMetadata."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.mesh import Mesh
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MeshAssetMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.MeshAssetMetadata.

    Category: Assets/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MeshAssetMetadata"

    def __init__(self, mesh: str | IAssetProvider[Mesh] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            mesh: Initial value for Mesh.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if mesh is not None:
            self.mesh = mesh

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
    def vertex_count(self) -> members.EmptyElement | None:
        """The VertexCount member."""
        member = self.get_member("VertexCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @vertex_count.setter
    def vertex_count(self, value: members.EmptyElement) -> None:
        """Set the VertexCount member."""
        self.set_member("VertexCount", value)

    @property
    def triangle_count(self) -> members.EmptyElement | None:
        """The TriangleCount member."""
        member = self.get_member("TriangleCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @triangle_count.setter
    def triangle_count(self, value: members.EmptyElement) -> None:
        """Set the TriangleCount member."""
        self.set_member("TriangleCount", value)

    @property
    def point_count(self) -> members.EmptyElement | None:
        """The PointCount member."""
        member = self.get_member("PointCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @point_count.setter
    def point_count(self, value: members.EmptyElement) -> None:
        """Set the PointCount member."""
        self.set_member("PointCount", value)

    @property
    def submesh_count(self) -> members.EmptyElement | None:
        """The SubmeshCount member."""
        member = self.get_member("SubmeshCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @submesh_count.setter
    def submesh_count(self, value: members.EmptyElement) -> None:
        """Set the SubmeshCount member."""
        self.set_member("SubmeshCount", value)

    @property
    def bone_count(self) -> members.EmptyElement | None:
        """The BoneCount member."""
        member = self.get_member("BoneCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bone_count.setter
    def bone_count(self, value: members.EmptyElement) -> None:
        """Set the BoneCount member."""
        self.set_member("BoneCount", value)

    @property
    def blendshape_count(self) -> members.EmptyElement | None:
        """The BlendshapeCount member."""
        member = self.get_member("BlendshapeCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @blendshape_count.setter
    def blendshape_count(self, value: members.EmptyElement) -> None:
        """Set the BlendshapeCount member."""
        self.set_member("BlendshapeCount", value)

    @property
    def has_normals(self) -> members.EmptyElement | None:
        """The HasNormals member."""
        member = self.get_member("HasNormals")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @has_normals.setter
    def has_normals(self, value: members.EmptyElement) -> None:
        """Set the HasNormals member."""
        self.set_member("HasNormals", value)

    @property
    def has_tangents(self) -> members.EmptyElement | None:
        """The HasTangents member."""
        member = self.get_member("HasTangents")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @has_tangents.setter
    def has_tangents(self, value: members.EmptyElement) -> None:
        """Set the HasTangents member."""
        self.set_member("HasTangents", value)

    @property
    def has_vertex_colors(self) -> members.EmptyElement | None:
        """The HasVertexColors member."""
        member = self.get_member("HasVertexColors")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @has_vertex_colors.setter
    def has_vertex_colors(self, value: members.EmptyElement) -> None:
        """Set the HasVertexColors member."""
        self.set_member("HasVertexColors", value)

    @property
    def has_uv0s(self) -> members.EmptyElement | None:
        """The HasUV0s member."""
        member = self.get_member("HasUV0s")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @has_uv0s.setter
    def has_uv0s(self, value: members.EmptyElement) -> None:
        """Set the HasUV0s member."""
        self.set_member("HasUV0s", value)

    @property
    def has_uv1s(self) -> members.EmptyElement | None:
        """The HasUV1s member."""
        member = self.get_member("HasUV1s")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @has_uv1s.setter
    def has_uv1s(self, value: members.EmptyElement) -> None:
        """Set the HasUV1s member."""
        self.set_member("HasUV1s", value)

    @property
    def has_uv2s(self) -> members.EmptyElement | None:
        """The HasUV2s member."""
        member = self.get_member("HasUV2s")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @has_uv2s.setter
    def has_uv2s(self, value: members.EmptyElement) -> None:
        """Set the HasUV2s member."""
        self.set_member("HasUV2s", value)

    @property
    def has_uv3s(self) -> members.EmptyElement | None:
        """The HasUV3s member."""
        member = self.get_member("HasUV3s")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @has_uv3s.setter
    def has_uv3s(self, value: members.EmptyElement) -> None:
        """Set the HasUV3s member."""
        self.set_member("HasUV3s", value)

