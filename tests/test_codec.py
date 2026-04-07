"""Unit tests for the codec module."""

# pylint: disable=protected-access,missing-function-docstring,missing-class-docstring

from dataclasses import dataclass
from typing import Any

import pytest

from pyresonitelink.data import (
    AddComponent,
    AddSlot,
    Component,
    ComponentData,
    FieldBool,
    FieldFloat3,
    FieldFloatQ,
    FieldString,
    GetComponent,
    GetSlot,
    Reference,
    RemoveComponent,
    RemoveSlot,
    Response,
    Slot,
    SlotData,
    UpdateComponent,
    UpdateSlot,
    decode,
    decode_message,
    decode_response,
    encode,
    Float3,
    FloatQ,
)
from pyresonitelink.data import codec


class TestEncodeMessages:
    """Tests for encoding message types."""

    def test_encode_get_slot(self) -> None:
        msg = GetSlot(slotId="Root", depth=0, includeComponentData=False)
        result = encode(msg)

        assert result["$type"] == "getSlot"
        assert result["slotId"] == "Root"
        assert result["depth"] == 0
        assert result["includeComponentData"] is False

    def test_encode_get_slot_with_message_id(self) -> None:
        msg = GetSlot(messageId="msg_001", slotId="Root", depth=-1)
        result = encode(msg)

        assert result["$type"] == "getSlot"
        assert result["messageId"] == "msg_001"
        assert result["slotId"] == "Root"
        assert result["depth"] == -1

    def test_encode_add_slot(self) -> None:
        msg = AddSlot(
            data=Slot(
                id="MySDK_0",
                parent=Reference(targetId="Root"),
                name=FieldString(value="Hello from MySDK!"),
                position=FieldFloat3(value=Float3(x=0, y=1.5, z=10)),
            )
        )
        result = encode(msg)

        assert result["$type"] == "addSlot"
        assert result["data"]["id"] == "MySDK_0"
        assert result["data"]["parent"]["$type"] == "reference"
        assert result["data"]["parent"]["targetId"] == "Root"
        assert result["data"]["name"]["$type"] == "string"
        assert result["data"]["name"]["value"] == "Hello from MySDK!"
        assert result["data"]["position"]["$type"] == "float3"
        assert result["data"]["position"]["value"]["x"] == 0
        assert result["data"]["position"]["value"]["y"] == 1.5
        assert result["data"]["position"]["value"]["z"] == 10

    def test_encode_update_slot(self) -> None:
        msg = UpdateSlot(
            data=Slot(
                id="MySDK_0",
                scale=FieldFloat3(value=Float3(x=2.5, y=2.5, z=2.5)),
            )
        )
        result = encode(msg)

        assert result["$type"] == "updateSlot"
        assert result["data"]["id"] == "MySDK_0"
        assert result["data"]["scale"]["$type"] == "float3"
        assert result["data"]["scale"]["value"]["x"] == 2.5

    def test_encode_remove_slot(self) -> None:
        msg = RemoveSlot(slotId="MySDK_0")
        result = encode(msg)

        assert result["$type"] == "removeSlot"
        assert result["slotId"] == "MySDK_0"

    def test_encode_get_component(self) -> None:
        msg = GetComponent(componentId="comp_123")
        result = encode(msg)

        assert result["$type"] == "getComponent"
        assert result["componentId"] == "comp_123"

    def test_encode_add_component(self) -> None:
        msg = AddComponent(
            containerSlotId="MySDK_0",
            data=Component(
                id="MySDK_1",
                componentType="[FrooxEngine]FrooxEngine.Grabbable",
                members={"Scalable": FieldBool(value=True)},
            ),
        )
        result = encode(msg)

        assert result["$type"] == "addComponent"
        assert result["containerSlotId"] == "MySDK_0"
        assert result["data"]["id"] == "MySDK_1"
        assert result["data"]["componentType"] == "[FrooxEngine]FrooxEngine.Grabbable"
        assert result["data"]["members"]["Scalable"]["$type"] == "bool"
        assert result["data"]["members"]["Scalable"]["value"] is True

    def test_encode_update_component(self) -> None:
        msg = UpdateComponent(
            data=Component(
                id="MySDK_1",
                members={"Scalable": FieldBool(value=False)},
            )
        )
        result = encode(msg)

        assert result["$type"] == "updateComponent"
        assert result["data"]["id"] == "MySDK_1"
        assert result["data"]["members"]["Scalable"]["$type"] == "bool"
        assert result["data"]["members"]["Scalable"]["value"] is False

    def test_encode_remove_component(self) -> None:
        msg = RemoveComponent(componentId="MySDK_1")
        result = encode(msg)

        assert result["$type"] == "removeComponent"
        assert result["componentId"] == "MySDK_1"


class TestEncodeSparseValues:
    """Tests for sparse encoding (omitting None and empty values)."""

    def test_omits_none_values(self) -> None:
        msg = GetSlot(slotId="Root")
        result = encode(msg)

        assert "messageId" not in result

    def test_omits_empty_lists(self) -> None:
        slot = Slot(id="test")
        result = encode(slot)

        assert "components" not in result
        assert "children" not in result

    def test_omits_empty_dicts(self) -> None:
        component = Component(id="test", componentType="SomeType")
        result = encode(component)

        assert "members" not in result


class TestEncodePrimitives:
    """Tests for encoding primitive types."""

    def test_encode_Float3(self) -> None:
        field = FieldFloat3(value=Float3(x=1.0, y=2.0, z=3.0))
        result = encode(field)

        assert result["$type"] == "float3"
        assert result["value"]["x"] == 1.0
        assert result["value"]["y"] == 2.0
        assert result["value"]["z"] == 3.0

    def test_encode_floatq(self) -> None:
        field = FieldFloatQ(value=FloatQ(x=0.0, y=0.0, z=0.0, w=1.0))
        result = encode(field)

        assert result["$type"] == "floatQ"
        assert result["value"]["x"] == 0.0
        assert result["value"]["w"] == 1.0


class TestEncodeErrors:
    """Tests for encoding error cases."""

    def test_encode_unknown_dataclass_raises_value_error(self) -> None:
        @dataclass
        class UnknownType:
            value: int = 0

        obj = UnknownType(value=42)

        with pytest.raises(ValueError, match="Cannot encode value of type"):
            codec._encode_value(obj)  # type: ignore[arg-type]

    def test_encode_non_encodable_type_raises_value_error(self) -> None:
        with pytest.raises(ValueError, match="Cannot encode value of type"):
            codec._encode_value(object())  # type: ignore[arg-type]

    def test_encode_set_raises_value_error(self) -> None:
        with pytest.raises(ValueError, match="Cannot encode value of type"):
            codec._encode_value({1, 2, 3})  # type: ignore[arg-type]


class TestDecodeMessages:
    """Tests for decoding message types."""

    def test_decode_get_slot(self) -> None:
        data: dict[str, Any] = {
            "$type": "getSlot",
            "slotId": "Root",
            "depth": 0,
            "includeComponentData": False,
        }
        result = decode(data)

        assert isinstance(result, GetSlot)
        assert result.slotId == "Root"
        assert result.depth == 0
        assert result.includeComponentData is False

    def test_decode_add_slot(self) -> None:
        data: dict[str, Any] = {
            "$type": "addSlot",
            "data": {
                "id": "MySDK_0",
                "parent": {"$type": "reference", "targetId": "Root"},
                "name": {"$type": "string", "value": "Hello from MySDK!"},
                "position": {
                    "$type": "float3",
                    "value": {"x": 0, "y": 1.5, "z": 10},
                },
            },
        }
        result = decode(data)

        assert isinstance(result, AddSlot)
        assert result.data is not None
        assert result.data.id == "MySDK_0"
        assert isinstance(result.data.parent, Reference)
        assert result.data.parent.targetId == "Root"
        assert isinstance(result.data.name, FieldString)
        assert result.data.name.value == "Hello from MySDK!"
        assert isinstance(result.data.position, FieldFloat3)
        assert result.data.position.value is not None
        assert result.data.position.value.x == 0
        assert result.data.position.value.y == 1.5
        assert result.data.position.value.z == 10

    def test_decode_message_helper(self) -> None:
        data: dict[str, Any] = {"$type": "removeSlot", "slotId": "test_slot"}
        result = decode_message(data)

        assert isinstance(result, RemoveSlot)
        assert result.slotId == "test_slot"


class TestDecodeResponses:
    """Tests for decoding response types."""

    def test_decode_response(self) -> None:
        data: dict[str, Any] = {
            "$type": "response",
            "sourceMessageId": "msg_001",
            "success": True,
        }
        result = decode(data)

        assert isinstance(result, Response)
        assert result.sourceMessageId == "msg_001"
        assert result.success is True

    def test_decode_response_with_error(self) -> None:
        data: dict[str, Any] = {
            "$type": "response",
            "success": False,
            "errorInfo": "Slot not found",
        }
        result = decode(data)

        assert isinstance(result, Response)
        assert result.success is False
        assert result.errorInfo == "Slot not found"

    def test_decode_slot_data(self) -> None:
        data: dict[str, Any] = {
            "$type": "slotData",
            "success": True,
            "depth": 0,
            "data": {
                "id": "Reso_123",
                "name": {"$type": "string", "value": "MySlot"},
            },
        }
        result = decode(data)

        assert isinstance(result, SlotData)
        assert result.success is True
        assert result.depth == 0
        assert result.data is not None
        assert result.data.id == "Reso_123"

    def test_decode_component_data(self) -> None:
        data: dict[str, Any] = {
            "$type": "componentData",
            "success": True,
            "data": {
                "id": "Reso_456",
                "componentType": "[FrooxEngine]FrooxEngine.Grabbable",
                "members": {
                    "Scalable": {"$type": "bool", "value": True},
                },
            },
        }
        result = decode(data)

        assert isinstance(result, ComponentData)
        assert result.success is True
        assert result.data is not None
        assert result.data.id == "Reso_456"
        assert result.data.componentType == "[FrooxEngine]FrooxEngine.Grabbable"
        assert "Scalable" in result.data.members
        assert isinstance(result.data.members["Scalable"], FieldBool)
        assert result.data.members["Scalable"].value is True

    def test_decode_response_helper(self) -> None:
        data: dict[str, Any] = {"$type": "response", "success": True}
        result = decode_response(data)

        assert isinstance(result, Response)
        assert result.success is True


class TestDecodeErrors:
    """Tests for decoding error cases."""

    def test_decode_missing_type_raises_value_error(self) -> None:
        data: dict[str, Any] = {"slotId": "Root"}

        with pytest.raises(ValueError, match="Missing \\$type field"):
            decode(data)

    def test_decode_unknown_type_raises_value_error(self) -> None:
        data: dict[str, Any] = {"$type": "unknownType", "value": 123}

        with pytest.raises(ValueError, match="Unknown type"):
            decode(data)

    def test_decode_response_helper_wrong_type_raises_type_error(self) -> None:
        data: dict[str, Any] = {"$type": "getSlot", "slotId": "Root"}

        with pytest.raises(TypeError, match="Expected Response"):
            decode_response(data)

    def test_decode_message_helper_wrong_type_raises_type_error(self) -> None:
        data: dict[str, Any] = {"$type": "response", "success": True}

        with pytest.raises(TypeError, match="Expected Message"):
            decode_message(data)


class TestRoundTrip:
    """Tests for encode/decode round-trip consistency."""

    def test_roundtrip_get_slot(self) -> None:
        original = GetSlot(messageId="msg_001", slotId="Root", depth=-1)
        encoded = encode(original)
        decoded = decode(encoded)

        assert isinstance(decoded, GetSlot)
        assert decoded.messageId == original.messageId
        assert decoded.slotId == original.slotId
        assert decoded.depth == original.depth

    def test_roundtrip_add_slot(self) -> None:
        original = AddSlot(
            data=Slot(
                id="MySDK_0",
                parent=Reference(targetId="Root"),
                name=FieldString(value="Test Slot"),
                position=FieldFloat3(value=Float3(x=1.0, y=2.0, z=3.0)),
            )
        )
        encoded = encode(original)
        decoded = decode(encoded)

        assert isinstance(decoded, AddSlot)
        assert decoded.data is not None
        assert decoded.data.id == "MySDK_0"
        assert decoded.data.parent is not None
        assert decoded.data.parent.targetId == "Root"
        assert decoded.data.name is not None
        assert decoded.data.name.value == "Test Slot"
        assert decoded.data.position is not None
        assert decoded.data.position.value is not None
        assert decoded.data.position.value.x == 1.0

    def test_roundtrip_add_component(self) -> None:
        original = AddComponent(
            containerSlotId="slot_123",
            data=Component(
                id="comp_456",
                componentType="[FrooxEngine]FrooxEngine.Grabbable",
                members={
                    "Scalable": FieldBool(value=True),
                    "MaxUsers": FieldString(value="5"),
                },
            ),
        )
        encoded = encode(original)
        decoded = decode(encoded)

        assert isinstance(decoded, AddComponent)
        assert decoded.containerSlotId == "slot_123"
        assert decoded.data is not None
        assert decoded.data.id == "comp_456"
        assert decoded.data.componentType == "[FrooxEngine]FrooxEngine.Grabbable"
        assert "Scalable" in decoded.data.members
        assert "MaxUsers" in decoded.data.members

    def test_roundtrip_response(self) -> None:
        original = Response(sourceMessageId="msg_001", success=True, errorInfo=None)
        encoded = encode(original)
        decoded = decode(encoded)

        assert isinstance(decoded, Response)
        assert decoded.sourceMessageId == original.sourceMessageId
        assert decoded.success == original.success
