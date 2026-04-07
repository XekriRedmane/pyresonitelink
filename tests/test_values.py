"""Tests against ResoniteLink for values.

Run as: pytest --port=<resonite-link-port> tests/test_values.py [-s]

-s: outputs print statements
"""

# pylint: disable=protected-access,missing-function-docstring,missing-class-docstring

import uuid

import numpy as np
import pytest

from pyresonitelink import client
from pyresonitelink import components
from pyresonitelink.data import codec
from pyresonitelink.data import fields
from pyresonitelink.data import messages
from pyresonitelink.data import responses
from pyresonitelink.data import workers


class TestValues:

    async def _add_test_component(
        self,
        resolink: client.Client,
        slot_id: str,
        component_type: str,
        debug: bool = False,
        members: dict[str, fields.Member] | None = None,
    ) -> str:
        component_id = str(uuid.uuid4())
        response = await resolink.add_component(
            messages.AddComponent(
                containerSlotId=slot_id,
                data=workers.Component(
                    id=component_id,
                    componentType=component_type,
                    members=members or {},
                ),
            ),
            debug,
        )
        assert isinstance(response, responses.Response)
        assert response.success is True
        return component_id

    async def _get_component(
        self, resolink: client.Client, component_id: str, debug: bool = False
    ) -> responses.ComponentData:
        response = await resolink.get_component(
            messages.GetComponent(componentId=component_id), debug
        )
        assert response.success is True
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
                    name=workers.FieldString(value="Test Slot"),
                )
            )
        )
        assert (
            json_response["success"] is True
        ), f"Response for adding test slot was failure: {json_response}"
        response = codec.decode_response(json_response)
        assert isinstance(response, responses.Response)
        # From this point on, we can use add_slot.

        response = await resolink.get_slot(
            messages.GetSlot(slotId=slot_id, depth=0, includeComponentData=False)
        )
        assert isinstance(response, responses.SlotData)
        assert response.data is not None
        assert response.data.id == slot_id

        json_response = await resolink.request_json(messages.RemoveSlot(slotId=slot_id))
        assert json_response["success"] is True
        response = codec.decode_response(json_response)
        assert isinstance(response, responses.Response)
        # From this point on, we can use remove_slot.

    @pytest.mark.asyncio(loop_scope="session")
    async def test_add_component(self, resolink: client.Client) -> None:
        slot_id = str(uuid.uuid4())
        response = await resolink.add_slot_to_root(
            id=slot_id,
            name="Test Slot",
        )
        assert isinstance(response, responses.NewEntityId)

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
            messages.GetSlot(slotId=slot_id, depth=0, includeComponentData=True),
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

    @pytest.mark.asyncio(loop_scope="session")
    async def test_update_component(
        self, resolink: client.Client, test_slot_id: str
    ) -> None:
        response: responses.Response  # So mypy doesn't assume a stricter type

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
    @pytest.mark.parametrize("value_type", ["DateTime"])
    async def test_add_valuefield_component(
        self, resolink: client.Client, test_slot_id: str, value_type: str
    ) -> None:
        print(f"Testing ValueField<{value_type}>")
        response: responses.Response  # So mypy doesn't assume a stricter type

        component_type = f"[FrooxEngine]FrooxEngine.ValueField<{value_type}>"
        component_id = await self._add_test_component(
            resolink, test_slot_id, component_type, debug=True,
            members={
                "Value": fields.FieldDateTime(value="1970-01-01T00:00:00W")
            }
        )
        response = await self._get_component(resolink, component_id, True)
        component = components.Component.unmarshal(response)

        assert component is not None
        assert component.id == component_id
        assert isinstance(component, components.NAME_TO_CLASS[component_type])
