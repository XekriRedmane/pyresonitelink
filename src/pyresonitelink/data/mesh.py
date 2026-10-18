"""Mesh data for the ImportMeshJSON and ImportMeshRawData messages.

These mirror ResoniteLink's Assets/Mesh models. The JSON classes describe a
whole mesh in JSON, which is convenient for small meshes. The raw data
classes only describe the structure of a mesh whose vertex data travels in
the binary payload, which messages.ImportMeshRawData.from_arrays builds.

Some of these classes have a "$type" on the wire: the submeshes ("points",
"triangles", "trianglesFlat") and the UV coordinates ("2D", "3D", "4D").
The JSON and raw data submeshes share "points" and "triangles", so the
codec registers them for encoding only.
"""

# pylint: disable=invalid-name

from dataclasses import dataclass

import numpy as np

from .primitives import Color, Float2, Float3, Float4, Float4x4

# =============================================================================
# ImportMeshJSON
# =============================================================================


@dataclass
class BoneWeight:
    """One bone's influence on a vertex.

    Args:
        boneIndex: Index of the bone in the mesh's bones.
        weight: How strongly the bone moves the vertex.
    """

    boneIndex: int = 0
    weight: float = 0.0


@dataclass
class UV2D:
    """A two-component UV coordinate. Its wire $type is "2D"."""

    uv: Float2 | None = None


@dataclass
class UV3D:
    """A three-component UV coordinate. Its wire $type is "3D"."""

    uv: Float3 | None = None


@dataclass
class UV4D:
    """A four-component UV coordinate. Its wire $type is "4D"."""

    uv: Float4 | None = None


@dataclass
class Vertex:
    """One vertex of a JSON mesh.

    Every vertex of a mesh must have the same attributes: if one has a
    normal, all of them must.

    Args:
        position: The vertex position.
        normal: The vertex normal.
        tangent: The vertex tangent. The fourth component is the sign of
            the binormal.
        color: The vertex color.
        uvs: One coordinate per UV channel.
        boneWeights: The bones that move the vertex, for a skinned mesh.
    """

    position: Float3 | None = None
    normal: Float3 | None = None
    tangent: Float4 | None = None
    color: Color | None = None
    uvs: list[UV2D | UV3D | UV4D] | None = None
    boneWeights: list[BoneWeight] | None = None


@dataclass
class Triangle:
    """One triangle, as three indices into the mesh's vertices."""

    vertex0Index: int = 0
    vertex1Index: int = 0
    vertex2Index: int = 0


@dataclass
class PointSubmesh:
    """A submesh of points. Its wire $type is "points".

    Args:
        vertexIndices: One vertex index per point.
    """

    vertexIndices: list[int] | None = None


@dataclass
class TriangleSubmesh:
    """A submesh of triangles. Its wire $type is "triangles".

    Args:
        triangles: The triangles.
    """

    triangles: list[Triangle] | None = None


@dataclass
class TriangleSubmeshFlat:
    """A submesh of triangles as a flat index list. Its wire $type is "trianglesFlat".

    Args:
        vertexIndices: Three vertex indices per triangle.
    """

    vertexIndices: list[int] | None = None


@dataclass
class Bone:
    """A bone of a skinned mesh.

    Used by both ImportMeshJSON and ImportMeshRawData.

    Args:
        name: The bone's name.
        bindPose: The bone's bind pose matrix.
    """

    name: str | None = None
    bindPose: Float4x4 | None = None


@dataclass
class BlendshapeFrame:
    """One frame of a JSON blendshape.

    Args:
        position: Where the frame sits in the blendshape's range, usually
            1.0 for a blendshape with a single frame.
        positionDeltas: One position offset per vertex.
        normalDeltas: One normal offset per vertex, or None.
        tangentDeltas: One tangent offset per vertex, or None. These are
            float3 even though vertex tangents are float4.
    """

    position: float = 1.0
    positionDeltas: list[Float3] | None = None
    normalDeltas: list[Float3] | None = None
    tangentDeltas: list[Float3] | None = None


@dataclass
class BlendShape:
    """A JSON blendshape.

    Args:
        name: The blendshape's name.
        frames: The blendshape's frames.
    """

    name: str | None = None
    frames: list[BlendshapeFrame] | None = None


# =============================================================================
# ImportMeshRawData structure
# =============================================================================


@dataclass
class PointSubmeshRawData:
    """A raw-data submesh of points. Its wire $type is "points".

    Its indices are pointCount int32 values in the payload.
    """

    pointCount: int = 0


@dataclass
class TriangleSubmeshRawData:
    """A raw-data submesh of triangles. Its wire $type is "triangles".

    Its indices are triangleCount * 3 int32 values in the payload.
    """

    triangleCount: int = 0


@dataclass
class BlendShapeFrameRawData:
    """One frame of a raw-data blendshape. Its deltas are in the payload."""

    position: float = 1.0


@dataclass
class BlendShapeRawData:
    """A raw-data blendshape. Its frames' deltas are in the payload.

    Args:
        name: The blendshape's name.
        hasNormalDeltas: Whether each frame has normal deltas.
        hasTangentDeltas: Whether each frame has tangent deltas.
        frames: The blendshape's frames.
    """

    name: str | None = None
    hasNormalDeltas: bool = False
    hasTangentDeltas: bool = False
    frames: list[BlendShapeFrameRawData] | None = None


# =============================================================================
# Inputs for ImportMeshRawData.from_arrays
# =============================================================================


@dataclass
class RawTriangles:
    """A triangle submesh for ImportMeshRawData.from_arrays.

    Args:
        indices: Vertex indices, shaped (triangle count, 3).
    """

    indices: np.ndarray


@dataclass
class RawPoints:
    """A point submesh for ImportMeshRawData.from_arrays.

    Args:
        indices: Vertex indices, one per point.
    """

    indices: np.ndarray


@dataclass
class RawBlendShapeFrame:
    """One blendshape frame for ImportMeshRawData.from_arrays.

    Args:
        position_deltas: One position offset per vertex, shaped (V, 3).
        normal_deltas: One normal offset per vertex, shaped (V, 3), or None.
        tangent_deltas: One tangent offset per vertex, shaped (V, 3), or
            None.
        position: Where the frame sits in the blendshape's range.
    """

    position_deltas: np.ndarray
    normal_deltas: np.ndarray | None = None
    tangent_deltas: np.ndarray | None = None
    position: float = 1.0


@dataclass
class RawBlendShape:
    """A blendshape for ImportMeshRawData.from_arrays.

    Every frame must have normal deltas if any does, and the same for
    tangent deltas.

    Args:
        name: The blendshape's name.
        frames: The blendshape's frames.
    """

    name: str
    frames: list[RawBlendShapeFrame]
