"""Unit tests for the asset import messages and their payload builders."""

# pylint: disable=protected-access,missing-function-docstring,missing-class-docstring

import numpy as np
import pytest

from pyresonitelink import client
from pyresonitelink.data import codec
from pyresonitelink.data import mesh
from pyresonitelink.data import messages
from pyresonitelink.data import primitives


class TestTexture2D:
    def test_from_pixels_is_row_major(self) -> None:
        # Pixel (x, y) is at index x + y * width, so pixel (2, 1) of a 3x2
        # image is the sixth pixel.
        pixels = np.zeros((2, 3, 4), dtype=np.uint8)
        pixels[1, 2] = (10, 20, 30, 40)
        msg = messages.ImportTexture2DRawData.from_pixels(pixels)
        assert (msg.width, msg.height) == (3, 2)
        assert msg.colorProfile == "sRGB"
        assert msg.payload is not None
        assert len(msg.payload) == msg.expected_payload_size() == 24
        assert bytes(msg.payload[20:24]) == bytes((10, 20, 30, 40))

    def test_hdr_from_pixels(self) -> None:
        pixels = np.full((2, 2, 4), 2.5, dtype=np.float32)
        msg = messages.ImportTexture2DRawDataHDR.from_pixels(pixels)
        assert msg.payload is not None
        assert len(msg.payload) == msg.expected_payload_size() == 64
        assert np.frombuffer(msg.payload, dtype="<f4")[0] == 2.5

    def test_from_pixels_rejects_rgb(self) -> None:
        with pytest.raises(ValueError):
            messages.ImportTexture2DRawData.from_pixels(np.zeros((2, 2, 3)))

    def test_access_raw_data_rejects_wrong_size(self) -> None:
        msg = messages.ImportTexture2DRawData(width=2, height=2, payload=bytearray(15))
        with pytest.raises(ValueError):
            msg.access_raw_data()

    def test_encode_omits_payload(self) -> None:
        msg = messages.ImportTexture2DRawData.from_pixels(np.zeros((1, 1, 4)))
        encoded = codec.encode(msg)
        assert encoded["$type"] == "importTexture2DRawData"
        assert "payload" not in encoded


class TestCubemap:
    def test_mip_count(self) -> None:
        assert messages._cubemap_mip_count(8, False) == 1
        assert messages._cubemap_mip_count(8, True) == 4
        assert messages._cubemap_mip_count(1, True) == 1

    def test_from_levels_without_mips(self) -> None:
        faces = np.zeros((6, 4, 4, 4), dtype=np.uint8)
        # The faces are in the order +X, +Y, +Z, -X, -Y, -Z, so -X is
        # face 3 and starts at 3 * 4 * 4 * 4 bytes.
        faces[3, 0, 0] = (1, 2, 3, 4)
        msg = messages.ImportCubemapRawData.from_levels([faces])
        assert (msg.size, msg.mipMaps) == (4, False)
        assert msg.payload is not None
        assert len(msg.payload) == msg.expected_payload_size() == 6 * 16 * 4
        assert bytes(msg.payload[192:196]) == bytes((1, 2, 3, 4))

    def test_from_levels_with_mips(self) -> None:
        levels = [np.zeros((6, s, s, 4), dtype=np.float32) for s in (4, 2, 1)]
        msg = messages.ImportCubemapRawDataHDR.from_levels(levels)
        assert (msg.size, msg.mipMaps) == (4, True)
        assert msg.payload is not None
        assert len(msg.payload) == msg.expected_payload_size() == 6 * 21 * 16

    def test_from_levels_rejects_partial_mip_chain(self) -> None:
        levels = [np.zeros((6, s, s, 4), dtype=np.uint8) for s in (4, 2)]
        with pytest.raises(ValueError):
            messages.ImportCubemapRawData.from_levels(levels)

    def test_regions_encode_as_rects(self) -> None:
        rect = primitives.Rect(x=0, y=0.5, width=0.25, height=0.5)
        msg = messages.ImportCubemapFileWithRegions(
            filePath="a.png", positiveXregion=rect,
        )
        encoded = codec.encode(msg)
        assert encoded["positiveXregion"] == {
            "position": {"x": 0.0, "y": 0.5},
            "size": {"x": 0.25, "y": 0.5},
        }


class TestMeshJSON:
    def test_encode_nested_types(self) -> None:
        msg = messages.ImportMeshJSON(
            vertices=[
                mesh.Vertex(
                    position=primitives.Float3(1, 2, 3),
                    uvs=[mesh.UV2D(uv=primitives.Float2(0.5, 1))],
                    boneWeights=[mesh.BoneWeight(boneIndex=0, weight=1.0)],
                ),
            ],
            submeshes=[
                mesh.TriangleSubmesh(triangles=[mesh.Triangle(0, 0, 0)]),
                mesh.TriangleSubmeshFlat(vertexIndices=[0, 0, 0]),
                mesh.PointSubmesh(vertexIndices=[0]),
            ],
        )
        encoded = codec.encode(msg)
        assert encoded["$type"] == "importMeshJSON"
        vertex = encoded["vertices"][0]
        assert "$type" not in vertex
        assert vertex["position"] == {"x": 1.0, "y": 2.0, "z": 3.0}
        assert vertex["uvs"][0] == {"$type": "2D", "uv": {"x": 0.5, "y": 1.0}}
        assert vertex["boneWeights"][0] == {"boneIndex": 0, "weight": 1.0}
        assert [s["$type"] for s in encoded["submeshes"]] == [
            "triangles", "trianglesFlat", "points",
        ]
        assert encoded["submeshes"][0]["triangles"][0] == {
            "vertex0Index": 0, "vertex1Index": 0, "vertex2Index": 0,
        }

    def test_bone_bind_pose_is_flat(self) -> None:
        identity = primitives.Float4x4(
            m00=1, m01=0, m02=0, m03=0,
            m10=0, m11=1, m12=0, m13=0,
            m20=0, m21=0, m22=1, m23=0,
            m30=0, m31=0, m32=0, m33=1,
        )
        encoded = codec.encode(messages.ImportMeshJSON(
            bones=[mesh.Bone(name="root", bindPose=identity)],
        ))
        assert encoded["bones"][0]["bindPose"]["m00"] == 1.0
        assert encoded["bones"][0]["bindPose"]["m01"] == 0.0


class TestMeshRawData:
    def test_positions_and_triangles(self) -> None:
        positions = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
        msg = messages.ImportMeshRawData.from_arrays(
            positions, [mesh.RawTriangles(np.array([[0, 1, 2]]))],
        )
        assert msg.vertexCount == 3
        assert msg.submeshes == [mesh.TriangleSubmeshRawData(triangleCount=1)]
        assert msg.payload is not None
        assert len(msg.payload) == msg.expected_payload_size() == 36 + 12
        assert list(np.frombuffer(msg.payload[36:], dtype="<i4")) == [0, 1, 2]

    def test_segment_order(self) -> None:
        # Each segment gets a distinct fill value so that its position in
        # the payload can be found.
        v = 2
        msg = messages.ImportMeshRawData.from_arrays(
            np.full((v, 3), 1.0),
            [mesh.RawPoints(np.array([0, 1]))],
            normals=np.full((v, 3), 2.0),
            tangents=np.full((v, 4), 3.0),
            colors=np.full((v, 4), 4.0),
            uvs=[np.full((v, 2), 5.0), np.full((v, 3), 6.0)],
            bone_indices=np.array([[7, 8], [7, 8]]),
            bone_weights=np.full((v, 2), 9.0),
            blendshapes=[mesh.RawBlendShape("smile", [
                mesh.RawBlendShapeFrame(
                    np.full((v, 3), 10.0), normal_deltas=np.full((v, 3), 11.0),
                ),
            ])],
        )
        assert msg.payload is not None
        assert len(msg.payload) == msg.expected_payload_size()
        assert msg.uvChannelDimensions == [2, 3]
        assert msg.boneWeightCount == 2
        assert msg.blendshapes == [mesh.BlendShapeRawData(
            name="smile", hasNormalDeltas=True, hasTangentDeltas=False,
            frames=[mesh.BlendShapeFrameRawData(position=1.0)],
        )]

        data = bytes(msg.payload)
        offset = 0

        def take(count: int, dtype: str) -> np.ndarray:
            nonlocal offset
            size = count * np.dtype(dtype).itemsize
            result = np.frombuffer(data[offset:offset + size], dtype=dtype)
            offset += size
            return result

        assert set(take(v * 3, "<f4")) == {1.0}
        assert set(take(v * 3, "<f4")) == {2.0}
        assert set(take(v * 4, "<f4")) == {3.0}
        assert set(take(v * 4, "<f4")) == {4.0}
        assert set(take(v * 2, "<f4")) == {5.0}
        assert set(take(v * 3, "<f4")) == {6.0}
        # Each bone weight is an int32 index followed by a float32 weight.
        weights = take(v * 2, "<i4,<f4")
        assert [int(w[0]) for w in weights] == [7, 8, 7, 8]
        assert {float(w[1]) for w in weights} == {9.0}
        assert list(take(2, "<i4")) == [0, 1]
        assert set(take(v * 3, "<f4")) == {10.0}
        assert set(take(v * 3, "<f4")) == {11.0}
        assert offset == len(data)

    def test_encode_structure(self) -> None:
        msg = messages.ImportMeshRawData.from_arrays(
            np.zeros((3, 3)),
            [mesh.RawTriangles(np.array([[0, 1, 2]])), mesh.RawPoints(np.array([0]))],
        )
        encoded = codec.encode(msg)
        assert encoded["submeshes"] == [
            {"$type": "triangles", "triangleCount": 1},
            {"$type": "points", "pointCount": 1},
        ]
        assert "payload" not in encoded

    def test_rejects_mismatched_vertex_count(self) -> None:
        with pytest.raises(ValueError):
            messages.ImportMeshRawData.from_arrays(
                np.zeros((3, 3)), [], normals=np.zeros((2, 3)),
            )

    def test_rejects_frame_missing_normals(self) -> None:
        with pytest.raises(ValueError):
            messages.ImportMeshRawData.from_arrays(
                np.zeros((1, 3)), [],
                blendshapes=[mesh.RawBlendShape("b", [
                    mesh.RawBlendShapeFrame(np.zeros((1, 3)), normal_deltas=np.zeros((1, 3))),
                    mesh.RawBlendShapeFrame(np.zeros((1, 3))),
                ])],
            )


class TestAudio:
    def test_mono(self) -> None:
        msg = messages.ImportAudioClipRawData.from_samples(np.zeros(100), 48000)
        assert (msg.sampleCount, msg.channelCount, msg.sampleRate) == (100, 1, 48000)
        assert msg.payload is not None
        assert len(msg.payload) == msg.expected_payload_size() == 400

    def test_stereo_is_interleaved(self) -> None:
        samples = np.array([[0.1, -0.1], [0.2, -0.2]])
        msg = messages.ImportAudioClipRawData.from_samples(samples, 44100)
        assert (msg.sampleCount, msg.channelCount) == (2, 2)
        assert msg.payload is not None
        np.testing.assert_allclose(
            np.frombuffer(msg.payload, dtype="<f4"), [0.1, -0.1, 0.2, -0.2],
            rtol=1e-6,
        )


class _FakeWebSocket:
    """Records what is sent. Receiving is never reached in these tests."""

    def __init__(self) -> None:
        self.sent: list[object] = []

    async def send(self, data: object, text: bool) -> None:
        del text
        self.sent.append(data)

    async def recv(self) -> str:
        raise AssertionError("nothing should be received")


class TestClientPayloadCheck:
    async def test_wrong_payload_size_raises_before_sending(self) -> None:
        resolink = client.Client()
        websocket = _FakeWebSocket()
        resolink._websocket = websocket  # type: ignore[assignment]
        msg = messages.ImportAudioClipRawData(
            sampleCount=10, sampleRate=48000, channelCount=1, payload=bytearray(39),
        )
        with pytest.raises(ValueError, match="40-byte payload"):
            await resolink.request(msg)
        assert not websocket.sent
