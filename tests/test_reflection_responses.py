"""Unit tests for decoding the session, reflection, method, and batch responses.

The JSON comes from a live server (Resonite 2026.9.18.82, ResoniteLink
0.13.1.0), trimmed to the parts the tests look at.
"""

# pylint: disable=protected-access,missing-function-docstring,missing-class-docstring

from typing import Any

import numpy as np
import pytest

from pyresonitelink.data import codec
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import reflection
from pyresonitelink.data import responses


def _ref(type_name: str, *args: dict[str, Any], generic: bool = False) -> dict[str, Any]:
    """Returns a TypeReference as the server sends it."""
    return {
        "type": type_name,
        "isGenericParameter": generic,
        "genericArguments": list(args) or None,
    }


def _type(name: str, **overrides: Any) -> dict[str, Any]:
    """Returns a TypeDefinition as the server sends it, with defaults."""
    result: dict[str, Any] = {
        "baseType": None, "fullTypeName": f"[FrooxEngine]FrooxEngine.{name}",
        "assemblyName": "FrooxEngine", "namespace": "FrooxEngine", "name": name,
        "isAbstract": False, "isInterface": False, "isGenericType": False,
        "isGenericTypeDefinition": False, "directGenericParameterCount": 0,
        "isEnginePrimitive": False, "isValueType": False, "isEnum": False,
        "isComponent": False, "isSyncObject": False, "isWorldElement": False,
        "isNested": False, "declaringType": None, "genericArguments": None,
        "genericParameters": None, "interfaces": [],
    }
    result.update(overrides)
    return result


def _response(type_name: str, **body: Any) -> dict[str, Any]:
    return {
        "$type": type_name, **body, "sourceMessageId": "m",
        "success": True, "errorInfo": None,
    }


class TestSessionData:
    def test_decode(self) -> None:
        resp = codec.decode_response(_response(
            "sessionData", resoniteVersion="2026.9.18.82",
            resoniteLinkVersion="0.13.1.0", uniqueSessionId="10",
        ))
        assert isinstance(resp, responses.SessionData)
        assert resp.resoniteVersion == "2026.9.18.82"
        assert resp.resoniteLinkVersion == "0.13.1.0"
        assert resp.uniqueSessionId == "10"


class TestTypeDefinitionData:
    def test_generic_parameters_and_class_key(self) -> None:
        parameter = {
            "name": "A", "types": [_ref("[FrooxEngine]FrooxEngine.IAsset")],
            "unmanaged": False, "struct": False, "enum": False, "class": True,
        }
        resp = codec.decode_response(_response(
            "typeDefinitionData",
            definition=_type(
                "IAssetProvider<>", isInterface=True, isGenericType=True,
                genericParameters=[parameter],
                interfaces=[_ref("[FrooxEngine]FrooxEngine.IAssetProvider")],
            ),
        ))
        assert isinstance(resp, responses.TypeDefinitionData)
        definition = resp.definition
        assert isinstance(definition, reflection.TypeDefinition)
        assert definition.isInterface
        assert definition.genericParameters is not None
        param = definition.genericParameters[0]
        assert isinstance(param, reflection.GenericParameter)
        # "class" is a Python keyword, so it's class_ in Python.
        assert param.class_ is True
        assert param.types == [reflection.TypeReference(type="[FrooxEngine]FrooxEngine.IAsset")]
        assert definition.interfaces == [
            reflection.TypeReference(type="[FrooxEngine]FrooxEngine.IAssetProvider"),
        ]

    def test_class_key_encodes_back(self) -> None:
        parameter = reflection.GenericParameter(name="T", class_=True)
        encoded = codec._encode_value(parameter)  # type: ignore[arg-type]
        assert encoded["class"] is True
        assert "class_" not in encoded

    def test_nested_generic_arguments(self) -> None:
        # The forward reference list["TypeReference"] decodes to dataclasses
        # at every level.
        resp = codec.decode_response(_response(
            "typeDefinitionData",
            definition=_type(
                "ValueField<>",
                baseType=_ref("[FrooxEngine]FrooxEngine.Component"),
                interfaces=[_ref(
                    "[FrooxEngine]FrooxEngine.IValueSource<>",
                    _ref("T", generic=True),
                )],
            ),
        ))
        assert isinstance(resp, responses.TypeDefinitionData)
        assert resp.definition is not None
        assert resp.definition.baseType == reflection.TypeReference(
            type="[FrooxEngine]FrooxEngine.Component",
        )
        assert resp.definition.interfaces is not None
        args = resp.definition.interfaces[0].genericArguments
        assert args == [reflection.TypeReference(type="T", isGenericParameter=True)]


class TestEnumDefinitionData:
    def test_decode(self) -> None:
        resp = codec.decode_response(_response(
            "enumDefinitionData",
            definition={
                "type": _type("BlendMode", isEnum=True, isValueType=True),
                "backingType": "int",
                "values": {"Opaque": 0, "Cutout": 1, "Alpha": 2},
                "isFlags": False,
            },
        ))
        assert isinstance(resp, responses.EnumDefinitionData)
        assert isinstance(resp.definition, reflection.EnumDefinition)
        assert resp.definition.backingType == "int"
        assert resp.definition.values == {"Opaque": 0, "Cutout": 1, "Alpha": 2}
        assert isinstance(resp.definition.type, reflection.TypeDefinition)

    def test_failure(self) -> None:
        resp = codec.decode_response({
            "$type": "enumDefinitionData", "definition": None,
            "sourceMessageId": "m", "success": False,
            "errorInfo": "This type is not an enum",
        })
        assert isinstance(resp, responses.EnumDefinitionData)
        assert not resp.success
        assert resp.definition is None


class TestMemberDefinitions:
    def test_sync_object_members(self) -> None:
        resp = codec.decode_response(_response(
            "syncObjectDefinitionData",
            definition={
                "baseTypeIsSyncObject": True,
                "type": _type("UserRef", isSyncObject=True),
                "members": {
                    "User": {
                        "$type": "reference",
                        "targetType": _ref("[FrooxEngine]FrooxEngine.User"),
                        "type": _ref(
                            "[FrooxEngine]FrooxEngine.SyncRef<>",
                            _ref("[FrooxEngine]FrooxEngine.User"),
                        ),
                    },
                    "_userId": {
                        "$type": "field",
                        "valueType": _ref("string"),
                        "type": _ref("[FrooxEngine]FrooxEngine.Sync<>", _ref("string")),
                    },
                },
                "methods": [],
            },
        ))
        assert isinstance(resp, responses.SyncObjectDefinitionData)
        definition = resp.definition
        assert isinstance(definition, reflection.SyncObjectDefinition)
        assert definition.baseTypeIsSyncObject
        assert definition.members is not None
        user = definition.members["User"]
        assert isinstance(user, reflection.ReferenceDefinition)
        assert user.targetType == reflection.TypeReference(type="[FrooxEngine]FrooxEngine.User")
        user_id = definition.members["_userId"]
        assert isinstance(user_id, reflection.FieldDefinition)
        assert user_id.valueType == reflection.TypeReference(type="string")

    def test_component_definition_members(self) -> None:
        resp = codec.decode_response(_response(
            "componentDefinitionData",
            definition={
                "baseTypeIsComponent": True, "categoryPath": "Data",
                "type": _type("ValueField<>", isComponent=True),
                "members": {
                    "Value": {
                        "$type": "field",
                        "valueType": _ref("T", generic=True),
                        "type": _ref("[FrooxEngine]FrooxEngine.Sync<>", _ref("T", generic=True)),
                    },
                },
                "methods": [{
                    "name": "Play", "parameters": {"speed": _ref("float")},
                    "returnType": None, "isStatic": False, "isAsync": False,
                }],
            },
        ))
        assert isinstance(resp, responses.ComponentDefinitionData)
        assert resp.definition is not None
        assert resp.definition.members is not None
        value = resp.definition.members["Value"]
        assert isinstance(value, reflection.FieldDefinition)
        assert value.valueType is not None and value.valueType.isGenericParameter
        assert resp.definition.methods is not None
        method = resp.definition.methods[0]
        assert isinstance(method, reflection.SyncMethodDefinition)
        assert method.parameters == {"speed": reflection.TypeReference(type="float")}


class TestMethodResult:
    def test_value_result(self) -> None:
        resp = codec.decode_response(_response(
            "methodResult", result={"$type": "int", "value": 0},
        ))
        assert isinstance(resp, responses.MethodResult)
        assert isinstance(resp.result, fields.FieldInt)
        assert resp.result.value == 0

    def test_reference_result(self) -> None:
        resp = codec.decode_response(_response(
            "methodResult", result={"$type": "reference", "targetID": "Reso_1"},
        ))
        assert isinstance(resp, responses.MethodResult)
        assert resp.result == members.DataReference(targetID="Reso_1")

    def test_void_result(self) -> None:
        resp = codec.decode_response(_response("methodResult", result=None))
        assert isinstance(resp, responses.MethodResult)
        assert resp.result is None


class TestBatchResponse:
    def test_decode_each_response(self) -> None:
        resp = codec.decode_response(_response("batchResponse", responses=[
            {"$type": "newEntityId", "entityId": "Reso_C7", "sourceMessageId": "a",
             "success": True, "errorInfo": None},
            {"$type": "componentData", "data": None, "sourceMessageId": "b",
             "success": False, "errorInfo": "Component with ID 'x' not found."},
            {"$type": "methodResult", "result": {"$type": "bool", "value": False},
             "sourceMessageId": "c", "success": True, "errorInfo": None},
        ]))
        assert isinstance(resp, responses.BatchResponse)
        assert resp.responses is not None
        first, second, third = resp.responses
        assert isinstance(first, responses.NewEntityId)
        assert first.entityId == "Reso_C7"
        assert isinstance(second, responses.ComponentData)
        assert not second.success
        assert isinstance(third, responses.MethodResult)
        assert isinstance(third.result, fields.FieldBool)


class TestTagMethodArguments:
    def test_members_and_references_pass_through(self) -> None:
        value = fields.FieldFloat(value=np.float32(0.5))
        ref = members.DataReference(targetID="Reso_1")
        assert members.tag_method_arguments({"a": value, "b": ref}) == {"a": value, "b": ref}

    def test_object_with_id_becomes_reference(self) -> None:
        class Thing:
            id = "Reso_2"

        assert members.tag_method_arguments({"t": Thing()}) == {
            "t": members.DataReference(targetID="Reso_2"),
        }

    def test_bare_value_raises(self) -> None:
        with pytest.raises(TypeError):
            members.tag_method_arguments({"x": 2})

    def test_encoded_arguments(self) -> None:
        encoded = codec.encode(members.DataReference(targetID="Reso_1"))
        assert encoded == {"$type": "reference", "targetID": "Reso_1"}
