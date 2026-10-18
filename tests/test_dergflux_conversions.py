"""Tests for implicit widening and explicit conversion in Dergflux expressions."""

# pylint: disable=protected-access,missing-function-docstring

import pytest

from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.dergflux import _expr
from pyresonitelink.dergflux import _graph
from pyresonitelink.dergflux import _math as dm


def _var(expr_type: type) -> _expr.ExprProxy:
    """Returns a proxy for a variable read of the given type."""
    return _expr.ExprProxy(_expr.VarReadNode("v", None, expr_type))


def _cast_to(node: _expr.ExprNode, target: type) -> bool:
    """Returns True if node is a conversion to target."""
    return isinstance(node, _expr.CastNode) and node._type is target


class TestBinaryWidening:

    def test_int_plus_float_widens_the_int(self) -> None:
        result = _var(primitives.Int) + _var(primitives.Float)
        assert result._node._type is primitives.Float
        assert _cast_to(result._node.left, primitives.Float)
        assert isinstance(result._node.right, _expr.VarReadNode)

    def test_float_plus_int_widens_the_int(self) -> None:
        # The result no longer depends on which operand comes first.
        result = _var(primitives.Float) + _var(primitives.Int)
        assert result._node._type is primitives.Float
        assert _cast_to(result._node.right, primitives.Float)

    def test_int_and_uint_meet_at_long(self) -> None:
        result = _var(primitives.Int) + _var(primitives.UInt)
        assert result._node._type is primitives.Long
        assert _cast_to(result._node.left, primitives.Long)
        assert _cast_to(result._node.right, primitives.Long)

    def test_float_and_double_meet_at_double(self) -> None:
        result = _var(primitives.Double) * _var(primitives.Float)
        assert result._node._type is primitives.Double
        assert _cast_to(result._node.right, primitives.Double)

    def test_int_vector_widens_to_float_vector(self) -> None:
        result = _var(primitives.Int3) + _var(primitives.Float3)
        assert result._node._type is primitives.Float3
        assert _cast_to(result._node.left, primitives.Float3)

    def test_comparison_widens_operands_and_returns_bool(self) -> None:
        result = _var(primitives.Int) < _var(primitives.Double)
        assert result._node._type is primitives.Bool
        assert _cast_to(result._node.left, primitives.Double)

    def test_same_types_need_no_cast(self) -> None:
        result = _var(primitives.Int) + _var(primitives.Int)
        assert isinstance(result._node.left, _expr.VarReadNode)
        assert isinstance(result._node.right, _expr.VarReadNode)

    def test_shift_count_stays_int(self) -> None:
        result = _var(primitives.Long) << _var(primitives.Int)
        assert result._node._type is primitives.Long
        assert isinstance(result._node.right, _expr.VarReadNode)

    def test_bool_and_int_have_no_common_type(self) -> None:
        with pytest.raises(TypeError, match="no common type"):
            _var(primitives.Bool) + _var(primitives.Int)  # pylint: disable=expression-not-assigned


class TestLiterals:

    def test_int_literal_takes_float_type(self) -> None:
        result = _var(primitives.Float) + 2
        assert result._node._type is primitives.Float
        assert result._node.right._type is primitives.Float

    def test_float_literal_widens_int_operand(self) -> None:
        # Before, the 2.5 was typed Int and silently truncated.
        result = _var(primitives.Int) + 2.5
        assert result._node._type is primitives.Float
        assert result._node.right._type is primitives.Float
        assert _cast_to(result._node.left, primitives.Float)

    def test_bool_literal_takes_bool_type(self) -> None:
        result = _var(primitives.Bool) == False  # noqa: E712
        assert result._node.right._type is primitives.Bool


class TestMathFunctions:

    def test_min_widens_its_arguments(self) -> None:
        result = dm.min_(_var(primitives.Int), _var(primitives.Float))
        assert result._node._type is primitives.Float
        assert _cast_to(result._node.args[0], primitives.Float)

    def test_convert_narrows(self) -> None:
        result = dm.to_int(_var(primitives.Float))
        assert _cast_to(result._node, primitives.Int)

    def test_convert_of_same_type_is_unchanged(self) -> None:
        var = _var(primitives.Int)
        assert dm.convert(var, primitives.Int)._node is var._node

    def test_convert_of_literal_types_it(self) -> None:
        result = dm.to_double(3)
        assert isinstance(result._node, _expr.ConstNode)
        assert result._node._type is primitives.Double


class TestAssignment:

    def _space(self) -> tuple[_graph.Graph, object, workers.Slot]:
        g = _graph.Graph()
        slot = workers.Slot(id="s")
        s = g.Space(slot)
        s.f = s.FloatDynVar("f")
        s.i = s.IntDynVar("i")
        return g, s, slot

    def _written(self, g: _graph.Graph) -> _expr.ExprNode:
        stmt = g._under_records[0].statements[-1]
        return stmt.stmts[-1].expr._node  # type: ignore[attr-defined]

    def test_int_written_to_float_variable_widens(self) -> None:
        g, s, slot = self._space()
        with g.Under(slot):
            s.f = s.i + 1  # type: ignore[attr-defined]
        assert _cast_to(self._written(g), primitives.Float)

    def test_float_written_to_int_variable_needs_convert(self) -> None:
        g, s, slot = self._space()
        with g.Under(slot):
            with pytest.raises(TypeError, match="Assignment to i"):
                s.i = s.f * 2  # type: ignore[attr-defined]

    def test_float_literal_written_to_int_variable_needs_convert(self) -> None:
        g, s, slot = self._space()
        with g.Under(slot):
            with pytest.raises(TypeError, match="Assignment to i"):
                s.i = 2.5  # type: ignore[attr-defined]

    def test_explicit_convert_allows_narrowing(self) -> None:
        g, s, slot = self._space()
        with g.Under(slot):
            s.i = dm.to_int(s.f)  # type: ignore[attr-defined]
        assert _cast_to(self._written(g), primitives.Int)


class TestConditional:

    def test_result_type_comes_from_the_values(self) -> None:
        # It used to take the condition's type, building ValueConditional<bool>.
        result = dm.conditional(
            _var(primitives.Bool), _var(primitives.Int), _var(primitives.Float),
        )
        assert result._node._type is primitives.Float
        assert _cast_to(result._node.args[1], primitives.Float)
