"""Tests against ResoniteLink for values.

Run as: pytest --port=<resonite-link-port> tests/test_values.py [-s]

-s: outputs print statements
"""

# pylint: disable=protected-access,missing-function-docstring,missing-class-docstring

import asyncio
import datetime
import math
import uuid

import numpy as np
import pytest

from pyresonitelink import client
from pyresonitelink.data import codec
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import messages
from pyresonitelink.data import primitives
from pyresonitelink.data import responses
from pyresonitelink.data import transforms
from pyresonitelink.data import workers
from pyresonitelink.generated.transform.drivers import spinner


class TestValues:

    async def _add_test_component(
        self,
        resolink: client.Client,
        slot_id: str,
        component_type: str,
        debug: bool = False,
        component_members: dict[str, members.Member] | None = None,
    ) -> str:
        component_id = str(uuid.uuid4())
        response = await resolink.add_component(
            slot_id,
            data=workers.Component(
                id=component_id,
                componentType=component_type,
                members=component_members or {},
            ),
            debug=debug,
        )
        assert response.success is True, response.errorInfo
        return component_id

    async def _get_component(
        self, resolink: client.Client, component_id: str, debug: bool = False
    ) -> responses.ComponentData:
        response = await resolink.get_component(component_id, debug=debug)
        assert response.success is True, response.errorInfo
        return response

    @pytest.mark.asyncio(loop_scope="session")
    async def test_get_root_slot(self, resolink: client.Client) -> None:
        json_response = await resolink.request_json(
            messages.GetSlot(slotId="Root", depth=0, includeComponentData=False)
        )
        assert json_response["success"] is True
        response = codec.decode_response(json_response)
        assert isinstance(response, responses.SlotData)
        # From this point on, we can use get_slot.

    @pytest.mark.asyncio(loop_scope="session")
    async def test_add_slot(self, resolink: client.Client) -> None:
        slot_id = str(uuid.uuid4())
        json_response = await resolink.request_json(
            messages.AddSlot(
                data=workers.Slot(
                    id=slot_id,
                    parent=workers.Reference(
                        targetId=workers.Slot.ROOT_SLOT_ID,
                        targetType="FrooxEngine.Slot",
                    ),
                    name=workers.FieldString(value="__test_add_slot__"),
                )
            )
        )
        try:
            assert (
                json_response["success"] is True
            ), f"Response for adding test slot was failure: {json_response}"
            response = codec.decode_response(json_response)
            assert isinstance(response, responses.Response)
            # From this point on, we can use add_slot.

            slot_response = await resolink.get_slot(slot_id)
            assert isinstance(slot_response, responses.SlotData)
            assert slot_response.data is not None
            assert slot_response.data.id == slot_id
        finally:
            json_response = await resolink.request_json(
                messages.RemoveSlot(slotId=slot_id)
            )
        assert json_response["success"] is True
        response = codec.decode_response(json_response)
        assert isinstance(response, responses.Response)
        # From this point on, we can use remove_slot.

    @pytest.mark.asyncio(loop_scope="session")
    async def test_get_global_transform(self, resolink: client.Client) -> None:
        # The parent is turned 90 degrees around +Y, which maps +Z to +X.
        s = math.sqrt(0.5)
        parent = await resolink.add_slot(
            name="__test_get_global_transform__",
            position=(1, 2, 3), rotation=(0, s, 0, s), scale=(2, 2, 2),
        )
        try:
            child = await resolink.add_slot(
                parent=parent, position=(0, 0, 1), rotation=(s, 0, 0, s),
            )
            result = await resolink.get_global_transform(child)
            # Root has the identity transform, so the child's offset of 1
            # along +Z is doubled and turned to +X by the parent alone.
            p, q, k = result.position, result.rotation, result.scale
            np.testing.assert_allclose([p.x, p.y, p.z], [3, 2, 3], atol=1e-5)
            # The rotation is the product (0, s, 0, s) * (s, 0, 0, s). The
            # engine may return its negation, which is the same rotation.
            rotation = np.array([q.x, q.y, q.z, q.w])
            expected = np.array([0.5, 0.5, -0.5, 0.5])
            if np.dot(rotation, expected) < 0:
                rotation = -rotation
            np.testing.assert_allclose(rotation, expected, atol=1e-5)
            np.testing.assert_allclose([k.x, k.y, k.z], [2, 2, 2], atol=1e-5)
        finally:
            await resolink.remove_slot(parent)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_get_global_transform_is_frame_consistent(
        self, resolink: client.Client,
    ) -> None:
        # The parent and child spin at opposite speeds around +Y, so the
        # child's world rotation is the same in every engine update. A
        # result that mixed the two rotations from different updates was
        # off by about 3 degrees at these speeds.
        parent = await resolink.add_slot(
            name="__test_get_global_transform_is_frame_consistent__",
        )
        try:
            child = await resolink.add_slot(parent=parent, position=(1, 0, 0))
            for slot, speed in ((parent, 180), (child, -180)):
                data = (await resolink.get_slot(slot)).data
                assert data is not None and data.rotation is not None
                await spinner.Spinner(
                    target=data.rotation.id,
                    speed=primitives.Float3(0, speed, 0),
                ).add_to_slot(resolink, slot)
            # Each spinner starts turning in the engine update after it's
            # added, and the two may have been added in different updates.
            await asyncio.sleep(0.2)
            first = (await resolink.get_global_transform(child)).rotation
            for _ in range(10):
                q = (await resolink.get_global_transform(child)).rotation
                difference = transforms.multiply(transforms.inverse(first), q)
                angle = math.degrees(2 * math.acos(min(1.0, abs(float(difference.w)))))
                assert angle < 0.1
        finally:
            await resolink.remove_slot(parent)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_update_slot(self, resolink: client.Client) -> None:
        slot = await resolink.add_slot(name="__test_update_slot__")
        try:
            # Each update's fields have fresh member IDs, and the read after
            # each update gives the fields IDs on the server. Sent as they
            # were, the second update's IDs caused an error.
            for x in (1, 2):
                response = await resolink.update_slot(workers.Slot(
                    id=slot.id,
                    position=fields.FieldFloat3(value=primitives.Float3(x, 0, 0)),
                    name=fields.FieldString(value=f"__test_update_slot_{x}__"),
                ))
                assert response.success, response.errorInfo
                data = (await resolink.get_slot(slot)).data
                assert data is not None
                assert data.position is not None and data.name is not None
                assert data.position.value == primitives.Float3(x, 0, 0)
                assert data.name.value == f"__test_update_slot_{x}__"
        finally:
            await resolink.remove_slot(slot)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_add_component(self, resolink: client.Client) -> None:
        slot_id = str(uuid.uuid4())
        slot = await resolink.add_slot(
            id=slot_id,
            name="__test_add_component__",
        )
        assert slot.id == slot_id
        try:
            # Ensure we can add a test component.
            component_id = str(uuid.uuid4())
            json_response = await resolink.request_json(
                messages.AddComponent(
                    containerSlotId=slot_id,
                    data=workers.Component(
                        id=component_id,
                        componentType="[FrooxEngine]FrooxEngine.ValueField<byte>",
                    ),
                ),
            )
            assert (
                json_response["success"] is True
            ), f"Response for adding test component was failure: {json_response}"
            response = codec.decode_response(json_response)
            assert isinstance(response, responses.Response)
            # From this point on, we can use add_component.

            # Ensure the slot contains the new component
            get_slot_response = await resolink.get_slot(
                slot_id, includeComponentData=True,
            )
            assert get_slot_response.data is not None
            assert get_slot_response.data.components is not None
            assert len(get_slot_response.data.components) > 0
            assert get_slot_response.data.components[0].id == component_id
            # This is an inconsistency in component type namings.
            # See https://github.com/Yellow-Dog-Man/ResoniteLink/issues/31
            assert (
                get_slot_response.data.components[0].componentType
                == "[FrooxEngine]FrooxEngine.ValueField<byte>"
            )

            # Ensure the component data has the expected members.
            json_response = await resolink.request_json(
                messages.GetComponent(componentId=component_id)
            )
            assert json_response["success"] is True
            response = codec.decode_response(json_response)
            assert isinstance(response, responses.ComponentData)
            assert response.data is not None
            assert response.data.id == component_id
            assert "persistent" in response.data.members
            assert "UpdateOrder" in response.data.members
            assert "Enabled" in response.data.members
            assert "Value" in response.data.members
            assert isinstance(response.data.members["UpdateOrder"], fields.FieldInt)
            assert isinstance(response.data.members["Enabled"], fields.FieldBool)
            assert isinstance(response.data.members["Value"], fields.FieldByte)
        finally:
            await resolink.remove_slot(slot_id)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_update_component(
        self, resolink: client.Client, test_slot_id: str
    ) -> None:
        response: responses.Response  # So the type checker doesn't assume a stricter type

        component_id = await self._add_test_component(
            resolink, test_slot_id, "[FrooxEngine]FrooxEngine.ValueField<byte>"
        )
        response = await self._get_component(resolink, component_id)
        assert response.data is not None
        assert isinstance(response.data.members["Value"], fields.FieldByte)

        byte_field = response.data.members["Value"]
        byte_field.value = np.uint8(123)

        # Ensure we can update the field value
        json_response = await resolink.request_json(
            messages.UpdateComponent(
                data=workers.Component(
                    id=component_id,
                    members={
                        "Value": byte_field,
                    },
                ),
            ),
        )
        assert json_response["success"] is True
        response = codec.decode_response(json_response)
        assert isinstance(response, responses.Response)
        # From this point on, we can use update_component.

        # Ensure that the update did actually update the value.
        response = await self._get_component(resolink, component_id)
        assert response.data is not None
        assert isinstance(response.data.members["Value"], fields.FieldByte)

        byte_field = response.data.members["Value"]
        assert byte_field.value == np.uint8(123)

    @pytest.mark.asyncio(loop_scope="session")
    @pytest.mark.parametrize(
        "value_type, field_cls, value",
        [
            # Both travel as strings, which the field classes convert:
            # DateTime in ISO 8601, and TimeSpan in .NET's
            # [d.]hh:mm:ss[.fffffff] form.
            (
                "DateTime", fields.FieldDateTime,
                datetime.datetime(
                    2024, 5, 6, 7, 8, 9, 123000, tzinfo=datetime.timezone.utc,
                ),
            ),
            (
                "DateTime", fields.FieldDateTime,
                datetime.datetime(2024, 5, 6, 7, 8, 9),
            ),
            (
                "TimeSpan", fields.FieldTimeSpan,
                datetime.timedelta(days=1, hours=2, minutes=3, seconds=4.5),
            ),
            (
                "TimeSpan", fields.FieldTimeSpan,
                -datetime.timedelta(seconds=1),
            ),
        ],
    )
    async def test_time_value_round_trip(
        self,
        resolink: client.Client,
        test_slot_id: str,
        value_type: str,
        field_cls: type[fields.FieldDateTime] | type[fields.FieldTimeSpan],
        value: datetime.datetime | datetime.timedelta,
    ) -> None:
        component_type = f"[FrooxEngine]FrooxEngine.ValueField<{value_type}>"
        component_id = await self._add_test_component(
            resolink, test_slot_id, component_type,
            component_members={"Value": field_cls(value=value)},  # type: ignore[arg-type]
        )
        response = await self._get_component(resolink, component_id)
        assert response.data is not None
        assert response.data.componentType == component_type
        member = response.data.members["Value"]
        assert isinstance(member, field_cls)
        assert member.value == value
