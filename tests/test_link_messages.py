"""Tests against ResoniteLink for session data, reflection, sync methods, batches, and imports.

Run as: pytest --port=<resonite-link-port> tests/test_link_messages.py [-s]

Several of these tests record server bugs in Resonite 2026.9.18.82. Each
says what it expects from that version, so a fix on the server shows up
as a failing test that can then be updated.
"""

# pylint: disable=missing-function-docstring,missing-class-docstring

import os
import uuid

import numpy as np
import pytest

from pyresonitelink import client
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import mesh
from pyresonitelink.data import messages
from pyresonitelink.data import primitives
from pyresonitelink.data import reflection
from pyresonitelink.data import responses
from pyresonitelink.data import workers
from pyresonitelink.generated.rendering import mesh_renderer

_IMAGE = os.path.join(os.path.dirname(__file__), "..", "docs", "tree_example.png")

_IDENTITY = primitives.Float4x4(
    m00=1, m01=0, m02=0, m03=0, m10=0, m11=1, m12=0, m13=0,
    m20=0, m21=0, m22=1, m23=0, m30=0, m31=0, m32=0, m33=1,
)


async def _add(resolink: client.Client, slot_id: str, name: str) -> str:
    """Adds a FrooxEngine component by its short name and returns its ID."""
    resp = await resolink.add_component(
        containerSlotId=slot_id, componentType=f"[FrooxEngine]FrooxEngine.{name}",
    )
    assert resp.success, resp.errorInfo
    assert resp.entityId is not None
    return resp.entityId


class TestSessionAndReflection:

    @pytest.mark.asyncio(loop_scope="session")
    async def test_session_data(self, resolink: client.Client) -> None:
        resp = await resolink.request_session_data()
        assert resp.success
        assert resp.resoniteVersion
        assert resp.resoniteLinkVersion
        assert resp.uniqueSessionId

    @pytest.mark.asyncio(loop_scope="session")
    async def test_type_definition(self, resolink: client.Client) -> None:
        resp = await resolink.get_type_definition("[FrooxEngine]FrooxEngine.IAssetProvider<>")
        assert resp.success
        assert isinstance(resp.definition, reflection.TypeDefinition)
        assert resp.definition.isInterface
        assert resp.definition.genericParameters is not None
        assert resp.definition.genericParameters[0].name == "A"

    @pytest.mark.asyncio(loop_scope="session")
    async def test_generic_type_definition(self, resolink: client.Client) -> None:
        resp = await resolink.get_generic_type_definition(
            "[FrooxEngine]FrooxEngine.ValueField<float>",
        )
        assert resp.success
        assert resp.definition is not None
        assert resp.definition.fullTypeName == "[FrooxEngine]FrooxEngine.ValueField<>"

    @pytest.mark.asyncio(loop_scope="session")
    async def test_enum_definition(self, resolink: client.Client) -> None:
        resp = await resolink.get_enum_definition("[FrooxEngine]FrooxEngine.BlendMode")
        assert resp.success
        assert resp.definition is not None
        assert resp.definition.backingType == "int"
        assert resp.definition.values is not None
        assert resp.definition.values["Opaque"] == 0

    @pytest.mark.asyncio(loop_scope="session")
    async def test_sync_object_definition(self, resolink: client.Client) -> None:
        resp = await resolink.get_sync_object_definition("[FrooxEngine]FrooxEngine.UserRef")
        assert resp.success
        assert resp.definition is not None
        assert resp.definition.members is not None
        assert isinstance(resp.definition.members["User"], reflection.ReferenceDefinition)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_component_definition_members_are_dataclasses(
        self, resolink: client.Client,
    ) -> None:
        resp = await resolink.get_component_definition(
            componentType="[FrooxEngine]FrooxEngine.ValueField<>", flattened=True,
        )
        assert resp.success
        assert resp.definition is not None
        assert resp.definition.members is not None
        assert isinstance(resp.definition.members["Value"], reflection.FieldDefinition)


class TestSyncMethods:

    @pytest.mark.asyncio(loop_scope="session")
    async def test_int_result(self, resolink: client.Client, test_slot_id: str) -> None:
        root_id = await _add(resolink, test_slot_id, "ObjectRoot")
        resp = await resolink.call_sync_method(root_id, "RemoveChildrenObjectRoots")
        assert resp.success, resp.errorInfo
        assert isinstance(resp.result, fields.FieldInt)
        assert resp.result.value == 0

    @pytest.mark.asyncio(loop_scope="session")
    async def test_bool_result_with_null_reference(
        self, resolink: client.Client, test_slot_id: str,
    ) -> None:
        output_id = await _add(resolink, test_slot_id, "AudioOutput")
        resp = await resolink.call_sync_method(
            output_id, "IsUserExluded", {"user": members.DataReference(targetID=None)},
        )
        assert resp.success, resp.errorInfo
        assert isinstance(resp.result, fields.FieldBool)
        assert resp.result.value is False

    @pytest.mark.asyncio(loop_scope="session")
    async def test_missing_method(self, resolink: client.Client, test_slot_id: str) -> None:
        output_id = await _add(resolink, test_slot_id, "AudioOutput")
        resp = await resolink.call_sync_method(output_id, "NoSuchMethod")
        assert not resp.success

    @pytest.mark.asyncio(loop_scope="session")
    async def test_async_method_fails_on_server(
        self, resolink: client.Client, test_slot_id: str,
    ) -> None:
        # Server bug: Task<T> methods fail after they start.
        mesh_id = await _add(resolink, test_slot_id, "StaticMesh")
        resp = await resolink.call_sync_method(mesh_id, "RecalculateNormals")
        assert not resp.success
        assert resp.errorInfo is not None and "Task`1" in resp.errorInfo

    @pytest.mark.asyncio(loop_scope="session")
    async def test_static_method_reaches_method(self, resolink: client.Client) -> None:
        # The null biped makes the method itself throw, which shows that the
        # call was matched and invoked.
        null = members.DataReference(targetID=None)
        arguments: dict[str, object] = {
            name: null for name in (
                "biped", "headReference", "leftHandReference", "rightHandReference",
                "leftFootReference", "rightFootReference", "hipsReference",
            )
        }
        for name in ("setupEyes", "setupProtection", "setupVolumeMeter", "setupFaceTracking"):
            arguments[name] = fields.FieldBool(value=False)
        resp = await resolink.call_static_sync_method(
            "[FrooxEngine]FrooxEngine.AvatarCreator", "CreateBipedAvatar", arguments,
        )
        assert not resp.success
        assert resp.errorInfo is not None
        assert resp.errorInfo.startswith("Method threw an exception")

    @pytest.mark.asyncio(loop_scope="session")
    async def test_static_method_bad_type(self, resolink: client.Client) -> None:
        resp = await resolink.call_static_sync_method("[FrooxEngine]FrooxEngine.NoSuchType", "X")
        assert not resp.success

    @pytest.mark.asyncio(loop_scope="session")
    async def test_static_delegate_method_fails_on_server(
        self, resolink: client.Client, test_slot_id: str,
    ) -> None:
        # Server bug: methods declared with [SyncMethod(typeof(Delegate))].
        collider_id = await _add(resolink, test_slot_id, "BoxCollider")
        with pytest.raises(RuntimeError, match="Type must derive from Delegate"):
            await resolink.call_static_sync_method(
                "[FrooxEngine]FrooxEngine.MeterTool", "FilterUsers",
                {"collider": members.DataReference(targetID=collider_id)},
            )


class TestBatch:

    @pytest.mark.asyncio(loop_scope="session")
    async def test_operations_run_in_order(
        self, resolink: client.Client, test_slot_id: str,
    ) -> None:
        child_id = str(uuid.uuid4())
        resp = await resolink.data_model_operation_batch([
            messages.AddSlot(data=workers.Slot(
                id=child_id,
                parent=members.Reference(targetId=test_slot_id),
                name=fields.FieldString(value="batched"),
            )),
            messages.GetSlot(slotId=test_slot_id, depth=1),
            messages.GetComponent(componentId="no-such-id"),
        ])
        assert resp.success
        assert resp.responses is not None
        added, got, missing = resp.responses
        assert isinstance(added, responses.NewEntityId)
        assert added.entityId == child_id
        # The slot added earlier in the batch is already visible.
        assert isinstance(got, responses.SlotData)
        assert got.data is not None
        assert [c.id for c in got.data.children or []] == [child_id]
        assert isinstance(missing, responses.ComponentData)
        assert not missing.success
        # Each response carries its operation's message ID.
        assert len({r.sourceMessageId for r in resp.responses}) == 3

    @pytest.mark.asyncio(loop_scope="session")
    async def test_rejects_non_batchable(self, resolink: client.Client) -> None:
        with pytest.raises(TypeError):
            await resolink.data_model_operation_batch([messages.RequestSessionData()])


class TestEnumUpdate:

    @pytest.mark.asyncio(loop_scope="session")
    async def test_generated_enum_round_trip(
        self, resolink: client.Client, test_slot_id: str,
    ) -> None:
        renderer = mesh_renderer.MeshRenderer(shadow_cast_mode="ShadowOnly")
        await renderer.add_to_slot(resolink, test_slot_id)
        assert renderer.shadow_cast_mode == "ShadowOnly"
        renderer.shadow_cast_mode = "Off"
        resp = await renderer.update(resolink)
        assert resp.success, resp.errorInfo
        await renderer.refresh(resolink)
        assert renderer.shadow_cast_mode == "Off"


class TestImports:

    async def _assert_loads(
        self, resolink: client.Client, slot_id: str, url: str | None, provider: str,
    ) -> None:
        """Assigns the URL to a static provider, which fails for a bad URL."""
        assert url is not None and url.startswith("local://")
        provider_id = await _add(resolink, slot_id, provider)
        get = await resolink.get_component(provider_id)
        assert get.data is not None and get.data.members is not None
        url_member = get.data.members["URL"]
        assert isinstance(url_member, fields.FieldUri)
        url_member.value = url
        get.data.members = {"URL": url_member}
        resp = await resolink.update_component(data=get.data)
        assert resp.success, resp.errorInfo

    @pytest.mark.asyncio(loop_scope="session")
    async def test_texture(self, resolink: client.Client, test_slot_id: str) -> None:
        pixels = np.random.default_rng(1).integers(0, 256, (16, 32, 4), dtype=np.uint8)
        resp = await resolink.import_texture_2d_raw_data(pixels)
        assert resp.success, resp.errorInfo
        await self._assert_loads(resolink, test_slot_id, resp.assetURL, "StaticTexture2D")

    @pytest.mark.asyncio(loop_scope="session")
    async def test_texture_hdr(self, resolink: client.Client, test_slot_id: str) -> None:
        pixels = np.full((8, 8, 4), 4.0, dtype=np.float32)
        resp = await resolink.import_texture_2d_raw_data_hdr(pixels)
        assert resp.success, resp.errorInfo
        await self._assert_loads(resolink, test_slot_id, resp.assetURL, "StaticTexture2D")

    @pytest.mark.asyncio(loop_scope="session")
    async def test_cubemap_files(self, resolink: client.Client, test_slot_id: str) -> None:
        image = os.path.abspath(_IMAGE)
        resp = await resolink.import_cubemap_files(image, image, image, image, image, image)
        assert resp.success, resp.errorInfo
        await self._assert_loads(resolink, test_slot_id, resp.assetURL, "StaticCubemap")

    @pytest.mark.asyncio(loop_scope="session")
    async def test_cubemap_regions_fail_on_server(self, resolink: client.Client) -> None:
        # Server bug: region imports always fail the mipmap check.
        rect = primitives.Rect
        resp = await resolink.import_cubemap_file_with_regions(
            os.path.abspath(_IMAGE),
            rect(0, 0, 0.25, 0.5), rect(0.25, 0, 0.25, 0.5), rect(0.5, 0, 0.25, 0.5),
            rect(0, 0.5, 0.25, 0.5), rect(0.25, 0.5, 0.25, 0.5), rect(0.5, 0.5, 0.25, 0.5),
        )
        assert not resp.success
        assert resp.errorInfo is not None and "mipmaps" in resp.errorInfo

    @pytest.mark.asyncio(loop_scope="session")
    async def test_cubemap_raw(self, resolink: client.Client, test_slot_id: str) -> None:
        rng = np.random.default_rng(2)
        levels = [rng.integers(0, 256, (6, s, s, 4), dtype=np.uint8) for s in (8, 4, 2, 1)]
        resp = await resolink.import_cubemap_raw_data(levels)
        assert resp.success, resp.errorInfo
        await self._assert_loads(resolink, test_slot_id, resp.assetURL, "StaticCubemap")
        resp = await resolink.import_cubemap_raw_data([levels[0]])
        assert resp.success, resp.errorInfo

    @pytest.mark.asyncio(loop_scope="session")
    async def test_cubemap_raw_hdr(self, resolink: client.Client, test_slot_id: str) -> None:
        resp = await resolink.import_cubemap_raw_data_hdr([np.ones((6, 4, 4, 4), dtype=np.float32)])
        assert resp.success, resp.errorInfo
        await self._assert_loads(resolink, test_slot_id, resp.assetURL, "StaticCubemap")

    @pytest.mark.asyncio(loop_scope="session")
    async def test_mesh_json(self, resolink: client.Client, test_slot_id: str) -> None:
        f3 = primitives.Float3
        positions = [f3(0, 0, 0), f3(1, 0, 0), f3(0, 1, 0)]
        resp = await resolink.import_mesh_json(
            [
                mesh.Vertex(position=p, normal=f3(0, 0, -1),
                            boneWeights=[mesh.BoneWeight(boneIndex=0, weight=1.0)])
                for p in positions
            ],
            [
                mesh.TriangleSubmesh(triangles=[mesh.Triangle(0, 1, 2)]),
                mesh.TriangleSubmeshFlat(vertexIndices=[0, 2, 1]),
                mesh.PointSubmesh(vertexIndices=[0, 1, 2]),
            ],
            bones=[mesh.Bone(name="root", bindPose=_IDENTITY)],
            blendshapes=[mesh.BlendShape(name="up", frames=[mesh.BlendshapeFrame(
                position=1.0, positionDeltas=[f3(0, 0.1, 0)] * 3,
            )])],
        )
        assert resp.success, resp.errorInfo
        await self._assert_loads(resolink, test_slot_id, resp.assetURL, "StaticMesh")

    @pytest.mark.asyncio(loop_scope="session")
    async def test_mesh_json_uvs_fail_on_server(self, resolink: client.Client) -> None:
        # Server bug: any UV coordinate fails the dimension check.
        f3 = primitives.Float3
        resp = await resolink.import_mesh_json(
            [
                mesh.Vertex(position=p, uvs=[mesh.UV2D(uv=primitives.Float2(0, 0))])
                for p in (f3(0, 0, 0), f3(1, 0, 0), f3(0, 1, 0))
            ],
            [mesh.TriangleSubmesh(triangles=[mesh.Triangle(0, 1, 2)])],
        )
        assert not resp.success
        assert resp.errorInfo is not None and "UV channel 0" in resp.errorInfo

    @pytest.mark.asyncio(loop_scope="session")
    async def test_mesh_raw(self, resolink: client.Client, test_slot_id: str) -> None:
        corners = np.array(
            [[x, y, z] for x in (0, 1) for y in (0, 1) for z in (0, 1)], dtype=np.float32,
        )
        triangles = np.array([
            [0, 1, 3], [0, 3, 2], [4, 6, 7], [4, 7, 5], [0, 4, 5], [0, 5, 1],
            [2, 3, 7], [2, 7, 6], [0, 2, 6], [0, 6, 4], [1, 5, 7], [1, 7, 3],
        ])
        v = len(corners)
        deltas = np.zeros((v, 3))
        resp = await resolink.import_mesh_raw_data(
            corners,
            [mesh.RawTriangles(triangles), mesh.RawPoints(np.arange(v))],
            normals=corners - 0.5,
            tangents=np.tile([1, 0, 0, 1], (v, 1)),
            colors=np.tile([1, 0.5, 0.25, 1], (v, 1)),
            uvs=[corners[:, :2], corners],
            bone_indices=np.zeros((v, 2), dtype=np.int32),
            bone_weights=np.tile([1.0, 0.0], (v, 1)),
            bones=[mesh.Bone(name="root", bindPose=_IDENTITY)],
            blendshapes=[mesh.RawBlendShape("grow", [
                mesh.RawBlendShapeFrame(corners * 0.1, deltas, deltas, position=0.5),
                mesh.RawBlendShapeFrame(corners * 0.2, deltas, deltas, position=1.0),
            ])],
        )
        assert resp.success, resp.errorInfo
        await self._assert_loads(resolink, test_slot_id, resp.assetURL, "StaticMesh")

    @pytest.mark.asyncio(loop_scope="session")
    async def test_audio(self, resolink: client.Client, test_slot_id: str) -> None:
        t = np.arange(4800) / 48000
        tone = 0.2 * np.sin(2 * np.pi * 440 * t)
        resp = await resolink.import_audio_clip_raw_data(tone, 48000)
        assert resp.success, resp.errorInfo
        await self._assert_loads(resolink, test_slot_id, resp.assetURL, "StaticAudioClip")
        resp = await resolink.import_audio_clip_raw_data(np.stack([tone, -tone], axis=1), 48000)
        assert resp.success, resp.errorInfo
