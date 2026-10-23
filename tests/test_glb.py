"""Unit tests for the glb module."""

# pylint: disable=missing-function-docstring,missing-class-docstring

import json
import pathlib
import struct
from typing import Any

import numpy as np
import pytest

from pyresonitelink.utils import glb


def _write_glb(path: pathlib.Path, gltf: dict[str, Any], binary: bytes) -> None:
    """Writes a .glb file with a JSON chunk and a BIN chunk.

    Args:
        path (pathlib.Path): The file to write.
        gltf (dict[str, Any]): The glTF JSON. Its single buffer's
            byteLength is set to the length of binary.
        binary (bytes): The binary chunk's data.
    """
    gltf = {**gltf, "buffers": [{"byteLength": len(binary)}]}
    # The JSON chunk is padded with spaces and the BIN chunk with zeros,
    # as the specification requires.
    json_chunk = json.dumps(gltf).encode()
    json_chunk += b" " * (-len(json_chunk) % 4)
    binary += b"\0" * (-len(binary) % 4)
    chunks = (
        struct.pack("<II", len(json_chunk), 0x4E4F534A) + json_chunk
        + struct.pack("<II", len(binary), 0x004E4942) + binary
    )
    path.write_bytes(struct.pack("<III", 0x46546C67, 2, 12 + len(chunks)) + chunks)


# One triangle in the XY plane, wound to face +Z. Its normals tilt toward
# +Y, so they differ from the normals that trimesh would compute from the
# face. The UVs are stored with glTF's top-left origin.
_POSITIONS = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]], dtype=np.float32)
_NORMALS = np.array([[0, 0.6, 0.8]] * 3, dtype=np.float32)
_UVS = np.array([[0, 0], [1, 0], [0, 0.25]], dtype=np.float32)
_INDICES = np.array([0, 1, 2], dtype=np.uint16)
_BINARY = _POSITIONS.tobytes() + _NORMALS.tobytes() + _UVS.tobytes() + _INDICES.tobytes()

# Accessors 0 to 3 are the positions, normals, UVs, and indices.
_ACCESSORS: dict[str, Any] = {
    "bufferViews": [
        {"buffer": 0, "byteLength": 36},
        {"buffer": 0, "byteOffset": 36, "byteLength": 36},
        {"buffer": 0, "byteOffset": 72, "byteLength": 24},
        {"buffer": 0, "byteOffset": 96, "byteLength": 6},
    ],
    "accessors": [
        {"bufferView": 0, "componentType": 5126, "count": 3, "type": "VEC3",
         "min": [0, 0, 0], "max": [1, 1, 0]},
        {"bufferView": 1, "componentType": 5126, "count": 3, "type": "VEC3"},
        {"bufferView": 2, "componentType": 5126, "count": 3, "type": "VEC2"},
        {"bufferView": 3, "componentType": 5123, "count": 3, "type": "SCALAR"},
    ],
}

# Mesh 0 is the triangle with normals, UVs, and material "Paint". Mesh 1
# is the triangle with neither normals nor a material. Mesh 2 draws the
# vertices as points.
_MESHES = [
    {"primitives": [{
        "attributes": {"POSITION": 0, "NORMAL": 1, "TEXCOORD_0": 2},
        "indices": 3,
        "material": 0,
    }]},
    {"primitives": [{"attributes": {"POSITION": 0}, "indices": 3}]},
    {"primitives": [{"attributes": {"POSITION": 0}, "mode": 0}]},
]


def _scene(tmp_path: pathlib.Path, nodes: list[dict[str, Any]]) -> Any:
    """Writes a .glb file with the given nodes and loads it.

    Args:
        tmp_path (pathlib.Path): The directory to write the file in.
        nodes (list[dict[str, Any]]): The nodes. Node 0 is the scene's
            only root.

    Returns:
        The loaded trimesh scene.
    """
    gltf = {
        "asset": {"version": "2.0"},
        "scene": 0,
        "scenes": [{"nodes": [0]}],
        "nodes": nodes,
        "meshes": _MESHES,
        "materials": [{"name": "Paint"}],
        **_ACCESSORS,
    }
    path = tmp_path / "test.glb"
    _write_glb(path, gltf, _BINARY)
    return glb.load(path)


class TestReadNode:

    def test_keeps_file_normals(self, tmp_path: pathlib.Path) -> None:
        m = glb.read_node(_scene(tmp_path, [{"name": "a", "mesh": 0}]), "a")
        np.testing.assert_array_equal(m.positions, _POSITIONS)
        np.testing.assert_allclose(m.normals, _NORMALS, atol=1e-6)
        np.testing.assert_array_equal(m.submeshes, [[[0, 1, 2]]])
        assert m.submeshes[0].dtype == np.int32
        assert m.nodes == ["a"]
        assert m.materials[0] is not None and m.materials[0].name == "Paint"

    def test_flips_v(self, tmp_path: pathlib.Path) -> None:
        m = glb.read_node(_scene(tmp_path, [{"name": "a", "mesh": 0}]), "a")
        assert m.uvs is not None
        np.testing.assert_allclose(m.uvs, [[0, 1], [1, 1], [0, 0.75]])

    def test_computes_missing_normals(self, tmp_path: pathlib.Path) -> None:
        m = glb.read_node(_scene(tmp_path, [{"name": "a", "mesh": 1}]), "a")
        np.testing.assert_allclose(m.normals, [[0, 0, 1]] * 3, atol=1e-6)
        assert m.uvs is None
        assert m.materials == [None]

    def test_applies_descendant_transforms(self, tmp_path: pathlib.Path) -> None:
        # Node b has no mesh and moves its child c +10 in X. The root's own
        # translation isn't applied.
        scene = _scene(tmp_path, [
            {"name": "a", "mesh": 0, "children": [1], "translation": [100, 0, 0]},
            {"name": "b", "translation": [10, 0, 0], "children": [2]},
            {"name": "c", "mesh": 1, "scale": [2, 2, 2]},
        ])
        m = glb.read_node(scene, "a")
        assert m.nodes == ["a", "c"]
        np.testing.assert_array_equal(m.positions[:3], _POSITIONS)
        np.testing.assert_array_equal(m.positions[3:], _POSITIONS * 2 + [10, 0, 0])
        np.testing.assert_array_equal(m.submeshes[1], [[3, 4, 5]])
        # The second triangle has no UVs, so it gets zeros.
        assert m.uvs is not None
        np.testing.assert_array_equal(m.uvs[3:], np.zeros((3, 2)))

    def test_reads_from_a_descendant(self, tmp_path: pathlib.Path) -> None:
        scene = _scene(tmp_path, [
            {"name": "a", "mesh": 0, "children": [1]},
            {"name": "b", "mesh": 1, "translation": [0, 0, 5]},
        ])
        m = glb.read_node(scene, "b")
        assert m.nodes == ["b"]
        # b's own translation isn't applied.
        np.testing.assert_array_equal(m.positions, _POSITIONS)

    def test_includes_every_sibling(self, tmp_path: pathlib.Path) -> None:
        # trimesh reverses the order of siblings, so only membership and
        # the pairing of each submesh with its vertices are checked.
        scene = _scene(tmp_path, [
            {"name": "a", "children": [1, 2, 3]},
            {"name": "x", "mesh": 1, "translation": [1, 0, 0]},
            {"name": "y", "mesh": 1, "translation": [2, 0, 0]},
            {"name": "z", "mesh": 1, "translation": [3, 0, 0]},
        ])
        m = glb.read_node(scene, "a")
        assert sorted(m.nodes) == ["x", "y", "z"]
        for node, triangles in zip(m.nodes, m.submeshes):
            first = m.positions[triangles[0, 0]]
            assert first[0] == {"x": 1, "y": 2, "z": 3}[node]

    def test_mirrored_node_keeps_front_faces(self, tmp_path: pathlib.Path) -> None:
        scene = _scene(tmp_path, [
            {"name": "a", "children": [1]},
            {"name": "b", "mesh": 1, "scale": [-1, 1, 1]},
        ])
        m = glb.read_node(scene, "a")
        np.testing.assert_array_equal(m.positions, _POSITIONS * [-1, 1, 1])
        np.testing.assert_array_equal(m.submeshes[0], [[0, 2, 1]])

    def test_skip_leaves_out_subtree(self, tmp_path: pathlib.Path) -> None:
        # b is hidden, so its child c goes too. d isn't hidden.
        scene = _scene(tmp_path, [
            {"name": "a", "mesh": 0, "children": [1, 3]},
            {"name": "b", "mesh": 1, "children": [2], "extras": {"hidden": True}},
            {"name": "c", "mesh": 1},
            {"name": "d", "mesh": 1, "extras": {"hidden": False}},
        ])
        seen: list[str] = []

        def hidden(name: str, extras: dict[str, Any]) -> bool:
            seen.append(name)
            return extras.get("hidden") is True

        m = glb.read_node(scene, "a", skip=hidden)
        assert m.nodes == ["a", "d"]
        # Not called for the node itself, or for anything under b.
        assert sorted(seen) == ["b", "d"]

    def test_node_extras(self, tmp_path: pathlib.Path) -> None:
        scene = _scene(tmp_path, [
            {"name": "a", "children": [1, 2]},
            {"name": "b", "mesh": 1, "extras": {"hidden": True}},
            {"name": "c", "mesh": 1},
        ])
        assert glb.node_extras(scene, "b") == {"hidden": True}
        assert glb.node_extras(scene, "c") == {}
        assert glb.node_extras(scene, "a") == {}

    def test_missing_node(self, tmp_path: pathlib.Path) -> None:
        with pytest.raises(LookupError, match="'q'"):
            glb.read_node(_scene(tmp_path, [{"name": "a", "mesh": 0}]), "q")

    def test_node_without_meshes(self, tmp_path: pathlib.Path) -> None:
        scene = _scene(tmp_path, [{"name": "a", "mesh": 0, "children": [1]}, {"name": "b"}])
        with pytest.raises(ValueError, match="no meshes"):
            glb.read_node(scene, "b")

    def test_rejects_points(self, tmp_path: pathlib.Path) -> None:
        with pytest.raises(ValueError, match="isn't a triangle mesh"):
            glb.read_node(_scene(tmp_path, [{"name": "a", "mesh": 2}]), "a")


_EXAMPLE_CARD = pathlib.Path(__file__).parent.parent / "examples" / "TexturedCard.glb"


class TestExampleCard:

    def test_reads_visible_parts_with_textures(self) -> None:
        scene = glb.load(_EXAMPLE_CARD)
        m = glb.read_node(scene, "TexturedCard", skip=lambda name, extras: extras.get("hidden") is True)
        assert sorted(m.nodes) == ["Card", "Check", "Diagram", "Divider", "Shell", "Target"]
        assert m.uvs is not None
        for node, material in zip(m.nodes, m.materials):
            assert material is not None
            image = getattr(material, "baseColorTexture", None)
            # Only the divider has a plain color. The others have textures,
            # which trimesh decodes because Pillow is installed.
            assert (image is None) == (node == "Divider"), node
            if node not in ("Card", "Divider"):
                assert material.alphaMode == "BLEND", node

    def test_hidden_parts_are_in_the_file(self) -> None:
        m = glb.read_node(glb.load(_EXAMPLE_CARD), "TexturedCard")
        assert {"Guide", "Large Check", "Cross"} <= set(m.nodes)


class TestReadPart:

    def test_centers_on_the_node_with_the_scene_axes(self, tmp_path: pathlib.Path) -> None:
        # b is under a, which moves it +1 in X. b moves itself +2 in Y,
        # turns 90 degrees about +Z, and scales by 2. In glTF, the turn
        # takes +X to +Y and +Y to -X.
        scene = _scene(tmp_path, [
            {"name": "a", "translation": [1, 0, 0], "children": [1]},
            {"name": "b", "mesh": 1, "translation": [0, 2, 0], "scale": [2, 2, 2],
             "rotation": [0, 0, np.sin(np.pi / 4), np.cos(np.pi / 4)]},
        ])
        part, position = glb.read_part(scene, "b")
        in_scene_axes = np.array([[0, 0, 0], [0, 2, 0], [-2, 0, 0]])
        np.testing.assert_allclose(part.positions, in_scene_axes * [-1, 1, 1], atol=1e-6)
        np.testing.assert_allclose(position, [-1, 2, 0])
        # The conversion mirrors X once, so the winding is swapped once.
        np.testing.assert_array_equal(part.submeshes[0], [[0, 2, 1]])

    def test_turn_applies_after_the_conversion(self, tmp_path: pathlib.Path) -> None:
        scene = _scene(tmp_path, [
            {"name": "a", "children": [1]},
            {"name": "b", "mesh": 1, "translation": [1, 2, 3]},
        ])
        half_turn = np.diag([-1.0, 1.0, -1.0])
        part, position = glb.read_part(scene, "b", turn=half_turn)
        np.testing.assert_allclose(part.positions, _POSITIONS * [1, 1, -1], atol=1e-6)
        np.testing.assert_allclose(position, [1, 2, -3])
        # The half turn isn't a mirror, so only the conversion swaps.
        np.testing.assert_array_equal(part.submeshes[0], [[0, 2, 1]])

    def test_skip_is_passed_on(self, tmp_path: pathlib.Path) -> None:
        scene = _scene(tmp_path, [
            {"name": "a", "mesh": 0, "children": [1]},
            {"name": "b", "mesh": 1, "extras": {"hidden": True}},
        ])
        part, _ = glb.read_part(scene, "a", skip=lambda name, extras: extras.get("hidden") is True)
        assert part.nodes == ["a"]


def _triangle() -> glb.Mesh:
    """Returns the test triangle as a Mesh, without reading a file."""
    return glb.Mesh(
        positions=_POSITIONS,
        normals=_NORMALS,
        submeshes=[np.array([[0, 1, 2]], dtype=np.int32)],
        materials=[None],
        nodes=["t"],
    )


class TestTransform:

    def test_translates_positions_only(self) -> None:
        matrix = np.identity(4)
        matrix[:3, 3] = [1, 2, 3]
        moved = glb.transform(_triangle(), matrix)
        np.testing.assert_array_equal(moved.positions, _POSITIONS + [1, 2, 3])
        np.testing.assert_allclose(moved.normals, _NORMALS, atol=1e-6)
        np.testing.assert_array_equal(moved.submeshes[0], [[0, 1, 2]])

    def test_to_resonite_mirrors_x(self) -> None:
        m = glb.to_resonite(_triangle())
        np.testing.assert_array_equal(m.positions, _POSITIONS * [-1, 1, 1])
        np.testing.assert_allclose(m.normals, _NORMALS, atol=1e-6)
        np.testing.assert_array_equal(m.submeshes[0], [[0, 2, 1]])

    def test_normals_stay_perpendicular(self) -> None:
        # Stretching X by 2 tilts a 45-degree surface toward the YZ plane,
        # so its normal tilts toward Y.
        m = glb.Mesh(
            positions=np.zeros((1, 3), dtype=np.float32),
            normals=np.array([[1, 1, 0]], dtype=np.float32) / np.float32(np.sqrt(2)),
        )
        stretched = glb.transform(m, np.diag([2.0, 1.0, 1.0]))
        np.testing.assert_allclose(stretched.normals, [[1 / np.sqrt(5), 2 / np.sqrt(5), 0]], rtol=1e-6)


class TestMerge:

    def test_offsets_indices(self) -> None:
        merged = glb.merge([_triangle(), _triangle()])
        assert len(merged.positions) == 6
        np.testing.assert_array_equal(merged.submeshes[0], [[0, 1, 2]])
        np.testing.assert_array_equal(merged.submeshes[1], [[3, 4, 5]])
        assert merged.nodes == ["t", "t"]
        assert merged.uvs is None

    def test_rejects_nothing(self) -> None:
        with pytest.raises(ValueError, match="no meshes"):
            glb.merge([])
