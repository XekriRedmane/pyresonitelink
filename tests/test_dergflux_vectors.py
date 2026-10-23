"""Tests for vector, slot, and transform expressions in Dergflux.

These check the expression trees only. test_dergflux_builder.py builds
them against a mock client.
"""

# pylint: disable=protected-access,missing-function-docstring

import pytest

from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.dergflux import _expr
from pyresonitelink.dergflux import _math as dm
from pyresonitelink.dergflux import slots
from pyresonitelink.dergflux import transform
from pyresonitelink.dergflux import variables
from pyresonitelink.generated._types import icollider
from pyresonitelink.generated._types import icomponent


def _var(expr_type: type) -> _expr.ExprProxy:
    """Returns a proxy for a variable read of the given type."""
    return _expr.ExprProxy(_expr.VarReadNode("v", None, expr_type))


def _node(proxy: _expr.ExprProxy) -> _expr.NodeOutputNode:
    """Returns the node output that a proxy wraps."""
    assert isinstance(proxy._node, _expr.NodeOutputNode)
    return proxy._node


class TestMixedProducts:

    def test_vector_times_float(self) -> None:
        node = _node(_var(primitives.Float3) * _var(primitives.Float))
        assert node.call.class_name == "Mul_Float3_Float"
        assert node._type is primitives.Float3

    def test_float_times_vector_keeps_the_order(self) -> None:
        node = _node(_var(primitives.Float) * _var(primitives.Float3))
        assert node.call.class_name == "Mul_Float_Float3"

    def test_vector_divided_by_float(self) -> None:
        node = _node(_var(primitives.Float3) / _var(primitives.Float))
        assert node.call.class_name == "Div_Float3_Float"

    def test_int_literal_takes_the_element_type_without_a_cast(self) -> None:
        node = _node(_var(primitives.Float3) * 2)
        scalar = node.call.inputs["B"]
        assert isinstance(scalar, _expr.ConstNode)
        assert scalar._type is primitives.Float

    def test_int_vector_widens_to_meet_a_float(self) -> None:
        node = _node(_var(primitives.Int3) * _var(primitives.Float))
        assert node.call.class_name == "Mul_Float3_Float"
        vector = node.call.inputs["A"]
        assert isinstance(vector, _expr.CastNode)
        assert vector._type is primitives.Float3

    def test_double_scalar_widens_the_vector(self) -> None:
        node = _node(_var(primitives.Float3) * _var(primitives.Double))
        assert node.call.class_name == "Mul_Double3_Double"
        assert node._type is primitives.Double3

    def test_rotation_times_vector_rotates_it(self) -> None:
        node = _node(_var(primitives.FloatQ) * _var(primitives.Float3))
        assert node.call.class_name == "Mul_FloatQ_Float3"
        assert node._type is primitives.Float3

    def test_vector_plus_vector_is_still_generic(self) -> None:
        result = _var(primitives.Float3) + _var(primitives.Float3)
        assert isinstance(result._node, _expr.BinaryOpNode)

    def test_bool_times_vector_raises(self) -> None:
        with pytest.raises(TypeError):
            _var(primitives.Float3) * _var(primitives.Bool)


class TestVectorFunctions:

    def test_dot_is_a_number(self) -> None:
        node = _node(dm.dot(_var(primitives.Float3), _var(primitives.Float3)))
        assert node.call.class_name == "Dot_Float3"
        assert node._type is primitives.Float
        assert set(node.call.inputs) == {"A", "B"}

    def test_dot_widens_to_the_common_type(self) -> None:
        node = _node(dm.dot(_var(primitives.Float3), _var(primitives.Double3)))
        assert node.call.class_name == "Dot_Double3"
        assert isinstance(node.call.inputs["A"], _expr.CastNode)

    def test_cross_magnitude_normalized_distance(self) -> None:
        v = _var(primitives.Float3)
        assert _node(dm.cross(v, v)).call.class_name == "Cross_Float3"
        assert _node(dm.magnitude(v))._type is primitives.Float
        assert _node(dm.normalized(v))._type is primitives.Float3
        assert _node(dm.distance(v, v)).call.class_name == "Distance_Float3"

    def test_int_vectors_raise(self) -> None:
        with pytest.raises(TypeError):
            dm.magnitude(_var(primitives.Int3))

    def test_pack_from_numbers_and_literals(self) -> None:
        node = _node(dm.pack(_var(primitives.Float), 0, 1.5))
        assert node.call.class_name == "Pack_Float3"
        assert set(node.call.inputs) == {"X", "Y", "Z"}

    def test_pack_of_doubles(self) -> None:
        node = _node(dm.pack(_var(primitives.Double), _var(primitives.Float)))
        assert node.call.class_name == "Pack_Double2"

    def test_elements_share_one_unpack_node(self) -> None:
        v = _var(primitives.Float3)
        x, z = _node(v.x), _node(v.z)
        assert x.call is z.call
        assert x.call.class_name == "Unpack_Float3"
        assert (x.output_name, z.output_name) == ("X", "Z")
        assert x._type is primitives.Float

    def test_float3_has_no_w(self) -> None:
        with pytest.raises(AttributeError):
            _ = _var(primitives.Float3).w


class TestSlotsAndTransforms:

    def test_slot_reference(self) -> None:
        node = slots.ref(workers.Slot(id="ball"))._node
        assert isinstance(node, _expr.ElementRefNode)
        assert node.target_id == "ball"
        assert node._type is workers.Slot

    def test_one_global_transform_per_reference(self) -> None:
        ball = slots.ref("ball")
        position = _node(transform.global_position(ball))
        rotation = _node(transform.global_rotation(ball))
        assert position.call is rotation.call
        assert position.output_name == "GlobalPosition"
        assert rotation._type is primitives.FloatQ

    def test_conversion_takes_a_float3(self) -> None:
        node = _node(transform.global_point_to_local("head", (0, 0, 1)))
        assert node.call.class_name == "GlobalPointToLocal"
        assert set(node.call.inputs) == {"Instance", "GlobalPoint"}

    def test_slot_of_a_collider_is_cast_to_icomponent(self) -> None:
        collider = _expr.ExprProxy(_expr.ComponentOutputNode("HitCollider", "tag", icollider.ICollider))
        node = _node(slots.of_component(collider))
        assert node.call.class_name == "GetSlot"
        cast = node.call.inputs["Component"]
        assert isinstance(cast, _expr.NodeOutputNode)
        assert cast.call.component_type is not None
        assert cast.call.component_type.endswith(
            "ObjectCast<[FrooxEngine]FrooxEngine.ICollider,[FrooxEngine]FrooxEngine.IComponent>"
        )
        assert cast._type is icomponent.IComponent

    def test_dynamic_read_outputs_share_a_node(self) -> None:
        r = variables.read(slots.ref("floor"), "Physics/Friction", primitives.Float)
        value, found = _node(r.value), _node(r.found)
        assert value.call is found.call
        assert value.call.type_args == (primitives.Float,)
        assert (value.output_name, found.output_name) == ("Value", "FoundValue")
        assert found._type is primitives.Bool


class TestStrings:

    def test_strings_join_with_concatenate_string(self) -> None:
        from pyresonitelink.dergflux import strings
        node = _node("y=" + strings.to_string(_var(primitives.Float)))
        assert node.call.class_name == "ConcatenateString"
        assert node._type is primitives.String
        assert isinstance(node.call.inputs["A"], _expr.ConstNode)

    def test_to_string_is_typed_by_the_value(self) -> None:
        from pyresonitelink.dergflux import strings
        assert _node(strings.to_string(_var(primitives.Double))).call.class_name == "ToString_Double"
        assert _node(strings.to_string(_var(primitives.Float3))).call.class_name == "ToString_Float3"

    def test_a_number_is_not_joined_to_a_string_implicitly(self) -> None:
        with pytest.raises(TypeError, match="to_string"):
            "y=" + _var(primitives.Float)
