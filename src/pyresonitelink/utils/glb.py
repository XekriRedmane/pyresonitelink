"""Reads meshes from glTF files for import into Resonite.

trimesh (https://trimesh.org) parses the file, in either the binary (.glb)
or the text (.gltf) form. load returns trimesh's scene, read_node builds a
Mesh from a node and its descendants in that scene, and to_resonite
converts the Mesh from glTF's coordinates to Resonite's.

Converting to Resonite's coordinates
------------------------------------

glTF is right-handed and Resonite is left-handed, and both have +Y up. A
glTF front face is counterclockwise when seen from outside. to_resonite
negates X in the positions and normals, and because the mirror reverses
the winding of every triangle, it swaps two corners of each triangle.
Resonite's own model importer does the same. FrooxEngine's
ModelImporter multiplies every vertex, normal, and tangent by (-1, 1, 1)
and passes PostProcessSteps.FlipWindingOrder to Assimp (decompiled from
build 2026.9.18.82). trimesh doesn't convert handedness at all.

Issues with trimesh
-------------------

These were found with trimesh 5.1.1, by reading its glTF loader
(trimesh/exchange/gltf/__init__.py) and by loading
examples/NumberDrum.glb and small test files. Each one is either worked
around here or stated as a limitation.

- Normals from the file are lost by Trimesh.copy(), Scene.to_geometry(),
  and Scene.dump(concatenate=True), which compute new normals by averaging
  the faces around each vertex. On a model whose sharp-looking edges are
  narrow bevels, such as NumberDrum.glb, that changes the shading, e.g.
  from (0, -1, 0) in the file to (0, -0.886, 0.465). This module reads
  each geometry in place in the loaded scene and never calls those
  methods, and neither should a caller who wants the file's normals.
- Trimesh.apply_transform multiplies normals by the transform itself. Under
  a nonuniform scale, normals have to be multiplied by the inverse
  transpose to stay perpendicular to the surface, so this module applies
  node transforms with its own transform function.
- A primitive without normals gets normals that trimesh computes from its
  faces when vertex_normals is first read. Without scipy installed, trimesh
  logs a warning with a traceback ("unable to use sparse matrix, falling
  back!") and then computes them more slowly. The result is the same.
- The scene graph doesn't keep the order of a node's children. The loader
  walks the node tree with a stack, so siblings come out in reverse order.
  A mesh with several primitives becomes one child frame per primitive,
  named after the node plus a random suffix. Submeshes therefore come in
  trimesh's order, and each one records its frame name and its material so
  that a caller can identify it.
- Frame names are the glTF node names, made unique by trimesh. An unnamed
  node is named after its index in the file.
- A node's extras aren't on its frame. trimesh stores them as the metadata
  of the graph edge from the node's parent, and only when they are a JSON
  object. node_extras reads them from there.
- Normalized integer attributes, as KHR_mesh_quantization allows, are
  returned as stored. A uint8 position of 255 comes back as 255 where it
  should be 1.0, and the scene has no record of the accessor being
  normalized.
- Only the first texture coordinate channel (TEXCOORD_0) is read, and only
  for a primitive that has a material. trimesh flips V on import, to
  1 - v, so the origin is at the bottom left of the texture. Resonite's
  ModelImporter copies Assimp's texture coordinates without flipping them,
  and Assimp's origin is also at the bottom left, so trimesh's texture
  coordinates and Resonite's have the same origin. examples/TexturedCard.glb,
  whose decals are text and asymmetric shapes, showed every one of them the
  right way up and unmirrored in Resonite (21 Oct 2026).
- trimesh decodes a material's images only when Pillow is installed.
  Without it the materials still load, with their names, colors, and alpha
  modes, but baseColorTexture is None and no warning is given. Pillow is a
  dependency of this package for that reason.
- Tangents, vertex colors, skins, and morph targets aren't read here.
"""

import os
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

import numpy as np
import trimesh


@dataclass
class Mesh:
    """Represents a triangle mesh with one set of vertices and any number of submeshes.

    The arrays have the shapes and types that Client.import_mesh_raw_data
    takes, so a mesh m is imported with the following call, where mesh is
    pyresonitelink.data.mesh.

        await resolink.import_mesh_raw_data(
            m.positions,
            [mesh.RawTriangles(t) for t in m.submeshes],
            normals=m.normals,
            uvs=[] if m.uvs is None else [m.uvs],
        )

    Attributes:
        positions (np.ndarray): The vertex positions, shaped (V, 3), as
            float32.
        normals (np.ndarray): The vertex normals, shaped (V, 3), as
            float32. They are the file's normals where it has them, and
            normals that trimesh computed from the faces elsewhere.
        uvs (np.ndarray | None): The texture coordinates, shaped (V, 2),
            as float32, with the origin at the bottom left, or None if no
            submesh has any. A submesh without texture coordinates gets
            zeros when it is merged with one that has them.
        submeshes (list[np.ndarray]): The triangles of each submesh, each
            shaped (N, 3), as int32 indices into positions.
        materials (list[trimesh.visual.material.Material | None]): The
            material of each submesh, as trimesh parsed it from the file,
            or None for a submesh with no material. A material's name is
            the glTF material's name.
        nodes (list[str]): The name of the scene graph frame that each
            submesh came from.
    """

    positions: np.ndarray
    normals: np.ndarray
    uvs: np.ndarray | None = None
    submeshes: list[np.ndarray] = field(default_factory=list)
    materials: list[trimesh.visual.material.Material | None] = field(default_factory=list)
    nodes: list[str] = field(default_factory=list)


def load(path: str | os.PathLike[str]) -> trimesh.Scene:
    """Loads a glTF file as a trimesh scene.

    Args:
        path (str | os.PathLike[str]): The .glb or .gltf file. A .gltf
            file's external buffers are read from paths relative to it.

    Returns:
        The scene. Its geometry is in glTF's coordinates.
    """
    return trimesh.load_scene(os.fspath(path))


def _read_geometry(geometry: trimesh.Trimesh, frame: str) -> Mesh:
    """Reads one of a scene's geometries as a Mesh with one submesh.

    The geometry must be the one in the scene, not a copy, because a copy
    loses the normals read from the file.

    Args:
        geometry (trimesh.Trimesh): The geometry, from scene.geometry.
        frame (str): The name of the scene graph frame that shows it.

    Returns:
        The geometry's vertices and triangles, in its own coordinates.
    """
    uv = getattr(geometry.visual, "uv", None)
    return Mesh(
        positions=np.asarray(geometry.vertices, dtype=np.float32),
        normals=np.asarray(geometry.vertex_normals, dtype=np.float32),
        uvs=None if uv is None else np.asarray(uv, dtype=np.float32),
        submeshes=[np.asarray(geometry.faces, dtype=np.int32)],
        materials=[getattr(geometry.visual, "material", None)],
        nodes=[frame],
    )


def merge(meshes: list[Mesh]) -> Mesh:
    """Combines meshes into one set of vertices, keeping each submesh.

    Args:
        meshes (list[Mesh]): The meshes.

    Returns:
        A mesh whose submeshes are those of the meshes, in order, with
        their indices offset into the combined vertices. If any mesh has
        texture coordinates, the vertices of the others get (0, 0).

    Raises:
        ValueError: There are no meshes.
    """
    if not meshes:
        raise ValueError("There are no meshes to merge.")
    uvs = None
    if any(m.uvs is not None for m in meshes):
        uvs = np.concatenate([
            np.zeros((len(m.positions), 2), dtype=np.float32) if m.uvs is None else m.uvs
            for m in meshes
        ])
    submeshes: list[np.ndarray] = []
    offset = 0
    for m in meshes:
        submeshes.extend(t + offset for t in m.submeshes)
        offset += len(m.positions)
    return Mesh(
        positions=np.concatenate([m.positions for m in meshes]),
        normals=np.concatenate([m.normals for m in meshes]),
        uvs=uvs,
        submeshes=submeshes,
        materials=[material for m in meshes for material in m.materials],
        nodes=[node for m in meshes for node in m.nodes],
    )


def transform(m: Mesh, matrix: np.ndarray) -> Mesh:
    """Applies a linear or affine transform to a mesh.

    Normals are transformed by the inverse transpose of the matrix's linear
    part and renormalized, so that they stay perpendicular to the surface
    under a nonuniform scale. A transform with a negative determinant is a
    mirror, which reverses the winding of every triangle, so two corners of
    each triangle are swapped to keep the front faces in front. Texture
    coordinates are unchanged.

    Args:
        m (Mesh): The mesh.
        matrix (np.ndarray): A 3x3 linear transform, or a 4x4 affine
            transform whose last row is (0, 0, 0, 1). Either one maps
            column vectors.

    Returns:
        The transformed mesh. The original mesh is unchanged.
    """
    matrix = np.asarray(matrix, dtype=np.float64)
    linear = matrix[:3, :3]
    translation = matrix[:3, 3] if matrix.shape == (4, 4) else np.zeros(3)
    positions = m.positions.astype(np.float64) @ linear.T + translation
    # n' = inverse(linear).T @ n, written for row vectors.
    normals = m.normals.astype(np.float64) @ np.linalg.inv(linear)
    lengths = np.linalg.norm(normals, axis=1, keepdims=True)
    normals /= np.where(lengths == 0, 1, lengths)
    submeshes = list(m.submeshes)
    if np.linalg.det(linear) < 0:
        submeshes = [t[:, [0, 2, 1]] for t in submeshes]
    return Mesh(
        positions=positions.astype(np.float32),
        normals=normals.astype(np.float32),
        uvs=m.uvs,
        submeshes=submeshes,
        materials=list(m.materials),
        nodes=list(m.nodes),
    )


def to_resonite(m: Mesh) -> Mesh:
    """Converts a mesh from glTF's coordinates to Resonite's.

    The conversion negates X and restores the winding, as described in the
    module docstring.

    Args:
        m (Mesh): The mesh, in glTF's coordinates.

    Returns:
        The mesh in Resonite's coordinates.
    """
    return transform(m, np.diag([-1.0, 1.0, 1.0]))


def node_extras(scene: trimesh.Scene, node: str) -> dict[str, Any]:
    """Gets a node's glTF extras from a trimesh scene.

    trimesh keeps a node's extras, when they are a JSON object, as the
    metadata of the scene graph edge from the node's parent. It adds the
    node's glTF extensions to the same dictionary under "gltf_extensions".

    Args:
        scene (trimesh.Scene): The scene, as returned by load.
        node (str): The name of the node's frame in scene.graph.

    Returns:
        The extras, or an empty dictionary if the node has none. The
        dictionary belongs to the scene, so the caller doesn't change it.
    """
    parent = scene.graph.transforms.parents.get(node)
    if parent is None:
        return {}
    edge = scene.graph.transforms.edge_data.get((parent, node), {})
    return edge.get("metadata") or {}


def read_node(
    scene: trimesh.Scene,
    node: str,
    *,
    skip: Callable[[str, dict[str, Any]], bool] | None = None,
) -> Mesh:
    """Reads the meshes of a node and its descendants as one Mesh.

    Each glTF primitive becomes a submesh, in trimesh's order, which is
    depth first from the node but not the order of the file (see the module
    docstring). The result is in the node's own coordinates, so each
    descendant's transform relative to the node is applied, and the node's
    transform relative to its parent isn't. A node without a mesh
    contributes only its transform.

    glTF has no flag for a hidden node, so exporters record one in a node's
    extras in their own way. skip lets the caller leave such nodes out.
    examples/TexturedCard.glb marks hidden nodes with {"hidden": true}, and
    the following call leaves out each such node and everything under it,
    as an engine hides the children of a hidden object.

        glb.read_node(scene, "TexturedCard", skip=lambda name, extras:
                      extras.get("hidden") is True)

    Args:
        scene (trimesh.Scene): The scene, as returned by load.
        node (str): The name of the node's frame in scene.graph, which is
            the glTF node's name if that is unique in the file.
        skip (Callable[[str, dict[str, Any]], bool] | None): Called with the
            name and the extras (see node_extras) of each descendant of
            node. A descendant for which it returns True is left out, along
            with its own descendants. It isn't called for node itself.

    Returns:
        The mesh, in glTF's coordinates.

    Raises:
        LookupError: The scene has no frame with the name.
        ValueError: There are no meshes in the node or its descendants, or
            one of them is points or lines.
    """
    graph = scene.graph
    if node not in graph.nodes:
        raise LookupError(f"The scene has no node named {node!r}.")
    children = graph.transforms.children
    with_geometry = set(graph.nodes_geometry)
    parts: list[Mesh] = []
    stack = [node]
    while stack:
        frame = stack.pop()
        if frame != node and skip is not None and skip(frame, node_extras(scene, frame)):
            continue
        if frame in with_geometry:
            matrix, geometry_name = graph.get(frame_to=frame, frame_from=node)
            geometry = scene.geometry[geometry_name]
            # glTF points and lines load as other trimesh geometry types.
            if not isinstance(geometry, trimesh.Trimesh):
                raise ValueError(
                    f"Node {frame!r} has a {type(geometry).__name__}, which"
                    " isn't a triangle mesh."
                )
            parts.append(transform(_read_geometry(geometry, frame), matrix))
        # Reversed so that the first child in trimesh's list is visited first.
        stack.extend(reversed(children.get(frame, [])))
    if not parts:
        raise ValueError(f"Node {node!r} and its descendants have no meshes.")
    return merge(parts)
