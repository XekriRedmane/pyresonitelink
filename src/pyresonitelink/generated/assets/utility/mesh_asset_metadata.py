"""Generated component: MeshAssetMetadata."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
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

    def __init__(self, mesh: str | IAssetProvider[Mesh] | None = None, vertex_count: primitives.Int | None = None, triangle_count: primitives.Int | None = None, point_count: primitives.Int | None = None, submesh_count: primitives.Int | None = None, bone_count: primitives.Int | None = None, blendshape_count: primitives.Int | None = None, has_normals: primitives.Bool | None = None, has_tangents: primitives.Bool | None = None, has_vertex_colors: primitives.Bool | None = None, has_uv0s: primitives.Bool | None = None, has_uv1s: primitives.Bool | None = None, has_uv2s: primitives.Bool | None = None, has_uv3s: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            mesh: Initial value for Mesh.
            vertex_count: Initial value for VertexCount.
            triangle_count: Initial value for TriangleCount.
            point_count: Initial value for PointCount.
            submesh_count: Initial value for SubmeshCount.
            bone_count: Initial value for BoneCount.
            blendshape_count: Initial value for BlendshapeCount.
            has_normals: Initial value for HasNormals.
            has_tangents: Initial value for HasTangents.
            has_vertex_colors: Initial value for HasVertexColors.
            has_uv0s: Initial value for HasUV0s.
            has_uv1s: Initial value for HasUV1s.
            has_uv2s: Initial value for HasUV2s.
            has_uv3s: Initial value for HasUV3s.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if mesh is not None:
            self.mesh = mesh
        if vertex_count is not None:
            self.vertex_count = vertex_count
        if triangle_count is not None:
            self.triangle_count = triangle_count
        if point_count is not None:
            self.point_count = point_count
        if submesh_count is not None:
            self.submesh_count = submesh_count
        if bone_count is not None:
            self.bone_count = bone_count
        if blendshape_count is not None:
            self.blendshape_count = blendshape_count
        if has_normals is not None:
            self.has_normals = has_normals
        if has_tangents is not None:
            self.has_tangents = has_tangents
        if has_vertex_colors is not None:
            self.has_vertex_colors = has_vertex_colors
        if has_uv0s is not None:
            self.has_uv0s = has_uv0s
        if has_uv1s is not None:
            self.has_uv1s = has_uv1s
        if has_uv2s is not None:
            self.has_uv2s = has_uv2s
        if has_uv3s is not None:
            self.has_uv3s = has_uv3s

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
    def vertex_count(self) -> primitives.Int | None:
        """The VertexCount field value."""
        member = self.get_member("VertexCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertex_count.setter
    def vertex_count(self, value: primitives.Int) -> None:
        """Set the VertexCount field value."""
        member = self.get_member("VertexCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VertexCount", fields.FieldInt(value=value)
            )

    @property
    def triangle_count(self) -> primitives.Int | None:
        """The TriangleCount field value."""
        member = self.get_member("TriangleCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @triangle_count.setter
    def triangle_count(self, value: primitives.Int) -> None:
        """Set the TriangleCount field value."""
        member = self.get_member("TriangleCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TriangleCount", fields.FieldInt(value=value)
            )

    @property
    def point_count(self) -> primitives.Int | None:
        """The PointCount field value."""
        member = self.get_member("PointCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @point_count.setter
    def point_count(self, value: primitives.Int) -> None:
        """Set the PointCount field value."""
        member = self.get_member("PointCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PointCount", fields.FieldInt(value=value)
            )

    @property
    def submesh_count(self) -> primitives.Int | None:
        """The SubmeshCount field value."""
        member = self.get_member("SubmeshCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @submesh_count.setter
    def submesh_count(self, value: primitives.Int) -> None:
        """Set the SubmeshCount field value."""
        member = self.get_member("SubmeshCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SubmeshCount", fields.FieldInt(value=value)
            )

    @property
    def bone_count(self) -> primitives.Int | None:
        """The BoneCount field value."""
        member = self.get_member("BoneCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bone_count.setter
    def bone_count(self, value: primitives.Int) -> None:
        """Set the BoneCount field value."""
        member = self.get_member("BoneCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BoneCount", fields.FieldInt(value=value)
            )

    @property
    def blendshape_count(self) -> primitives.Int | None:
        """The BlendshapeCount field value."""
        member = self.get_member("BlendshapeCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @blendshape_count.setter
    def blendshape_count(self, value: primitives.Int) -> None:
        """Set the BlendshapeCount field value."""
        member = self.get_member("BlendshapeCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlendshapeCount", fields.FieldInt(value=value)
            )

    @property
    def has_normals(self) -> primitives.Bool | None:
        """The HasNormals field value."""
        member = self.get_member("HasNormals")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @has_normals.setter
    def has_normals(self, value: primitives.Bool) -> None:
        """Set the HasNormals field value."""
        member = self.get_member("HasNormals")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HasNormals", fields.FieldBool(value=value)
            )

    @property
    def has_tangents(self) -> primitives.Bool | None:
        """The HasTangents field value."""
        member = self.get_member("HasTangents")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @has_tangents.setter
    def has_tangents(self, value: primitives.Bool) -> None:
        """Set the HasTangents field value."""
        member = self.get_member("HasTangents")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HasTangents", fields.FieldBool(value=value)
            )

    @property
    def has_vertex_colors(self) -> primitives.Bool | None:
        """The HasVertexColors field value."""
        member = self.get_member("HasVertexColors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @has_vertex_colors.setter
    def has_vertex_colors(self, value: primitives.Bool) -> None:
        """Set the HasVertexColors field value."""
        member = self.get_member("HasVertexColors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HasVertexColors", fields.FieldBool(value=value)
            )

    @property
    def has_uv0s(self) -> primitives.Bool | None:
        """The HasUV0s field value."""
        member = self.get_member("HasUV0s")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @has_uv0s.setter
    def has_uv0s(self, value: primitives.Bool) -> None:
        """Set the HasUV0s field value."""
        member = self.get_member("HasUV0s")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HasUV0s", fields.FieldBool(value=value)
            )

    @property
    def has_uv1s(self) -> primitives.Bool | None:
        """The HasUV1s field value."""
        member = self.get_member("HasUV1s")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @has_uv1s.setter
    def has_uv1s(self, value: primitives.Bool) -> None:
        """Set the HasUV1s field value."""
        member = self.get_member("HasUV1s")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HasUV1s", fields.FieldBool(value=value)
            )

    @property
    def has_uv2s(self) -> primitives.Bool | None:
        """The HasUV2s field value."""
        member = self.get_member("HasUV2s")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @has_uv2s.setter
    def has_uv2s(self, value: primitives.Bool) -> None:
        """Set the HasUV2s field value."""
        member = self.get_member("HasUV2s")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HasUV2s", fields.FieldBool(value=value)
            )

    @property
    def has_uv3s(self) -> primitives.Bool | None:
        """The HasUV3s field value."""
        member = self.get_member("HasUV3s")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @has_uv3s.setter
    def has_uv3s(self, value: primitives.Bool) -> None:
        """Set the HasUV3s field value."""
        member = self.get_member("HasUV3s")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HasUV3s", fields.FieldBool(value=value)
            )

