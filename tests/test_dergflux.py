"""Tests for the Dergflux DSL layer.

These are offline tests that verify expression tree construction,
space variable declaration/read/write, and flow control recording
without any server interaction.
"""

import pytest

from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.dergflux import _expr
from pyresonitelink.dergflux import _flow
from pyresonitelink.dergflux import _graph
from pyresonitelink.dergflux import _space
from pyresonitelink.dergflux import _types


# =========================================================================
# Type inference
# =========================================================================


class TestTypeInference:
    """Tests for _types module."""

    def test_infer_result_type_prefers_left(self) -> None:
        result = _types.infer_result_type(primitives.Int, primitives.Float)
        assert result is primitives.Int

    def test_infer_result_type_falls_back_to_right(self) -> None:
        result = _types.infer_result_type(None, primitives.Float)
        assert result is primitives.Float

    def test_infer_result_type_both_none(self) -> None:
        result = _types.infer_result_type(None, None)
        assert result is None

    def test_resolve_const_type_uses_context(self) -> None:
        result = _types.resolve_const_type(42, primitives.Float)
        assert result is primitives.Float

    def test_resolve_const_type_maps_int(self) -> None:
        result = _types.resolve_const_type(42, None)
        assert result is primitives.Int

    def test_resolve_const_type_maps_float(self) -> None:
        result = _types.resolve_const_type(3.14, None)
        assert result is primitives.Float

    def test_resolve_const_type_maps_bool(self) -> None:
        result = _types.resolve_const_type(True, None)
        assert result is primitives.Bool

    def test_resolve_const_type_maps_str(self) -> None:
        result = _types.resolve_const_type("hello", None)
        assert result is primitives.String

    def test_resolve_const_type_unknown_defaults_to_float(self) -> None:
        result = _types.resolve_const_type(object(), None)
        assert result is primitives.Float


# =========================================================================
# Expression trees
# =========================================================================


class TestExprProxy:
    """Tests for ExprProxy and AST construction."""

    def _make_proxy(
        self, value: object = 0, expr_type: type = primitives.Float,
    ) -> _expr.ExprProxy:
        """Create an ExprProxy wrapping a ConstNode."""
        return _expr.ExprProxy(_expr.ConstNode(value, expr_type))

    def test_add_creates_binary_node(self) -> None:
        a = self._make_proxy(1)
        result = a + 2
        assert isinstance(result._node, _expr.BinaryOpNode)
        assert result._node.op is _expr.BinOp.ADD

    def test_radd_creates_binary_node(self) -> None:
        a = self._make_proxy(1)
        result = 2 + a
        assert isinstance(result._node, _expr.BinaryOpNode)
        assert result._node.op is _expr.BinOp.ADD

    def test_sub_creates_binary_node(self) -> None:
        a = self._make_proxy(1)
        result = a - 2
        assert isinstance(result._node, _expr.BinaryOpNode)
        assert result._node.op is _expr.BinOp.SUB

    def test_rsub_creates_binary_node(self) -> None:
        a = self._make_proxy(1)
        result = 2 - a
        assert isinstance(result._node, _expr.BinaryOpNode)
        assert result._node.op is _expr.BinOp.SUB
        # In rsub, the literal becomes the left operand
        assert isinstance(result._node.left, _expr.ConstNode)
        assert result._node.left.value == 2

    def test_mul_creates_binary_node(self) -> None:
        a = self._make_proxy(1)
        result = a * 2
        assert isinstance(result._node, _expr.BinaryOpNode)
        assert result._node.op is _expr.BinOp.MUL

    def test_truediv_creates_binary_node(self) -> None:
        a = self._make_proxy(1)
        result = a / 2
        assert isinstance(result._node, _expr.BinaryOpNode)
        assert result._node.op is _expr.BinOp.DIV

    def test_mod_creates_binary_node(self) -> None:
        a = self._make_proxy(1)
        result = a % 2
        assert isinstance(result._node, _expr.BinaryOpNode)
        assert result._node.op is _expr.BinOp.MOD

    def test_neg_creates_unary_node(self) -> None:
        a = self._make_proxy(1)
        result = -a
        assert isinstance(result._node, _expr.UnaryOpNode)
        assert result._node.op is _expr.UnOp.NEG

    def test_lt_creates_binary_node_with_bool_type(self) -> None:
        a = self._make_proxy(1)
        result = a < 3
        assert isinstance(result._node, _expr.BinaryOpNode)
        assert result._node.op is _expr.BinOp.LT
        assert result._node._type is primitives.Bool

    def test_gt_creates_binary_node_with_bool_type(self) -> None:
        a = self._make_proxy(1)
        result = a > 3
        assert isinstance(result._node, _expr.BinaryOpNode)
        assert result._node.op is _expr.BinOp.GT
        assert result._node._type is primitives.Bool

    def test_eq_creates_binary_node_with_bool_type(self) -> None:
        a = self._make_proxy(1)
        result = a == 3
        assert isinstance(result._node, _expr.BinaryOpNode)
        assert result._node.op is _expr.BinOp.EQ
        assert result._node._type is primitives.Bool

    def test_ne_creates_binary_node_with_bool_type(self) -> None:
        a = self._make_proxy(1)
        result = a != 3
        assert isinstance(result._node, _expr.BinaryOpNode)
        assert result._node.op is _expr.BinOp.NE
        assert result._node._type is primitives.Bool

    def test_le_raises_not_implemented(self) -> None:
        a = self._make_proxy(1)
        with pytest.raises(NotImplementedError, match="ValueLessOrEqual"):
            a <= 3

    def test_ge_raises_not_implemented(self) -> None:
        a = self._make_proxy(1)
        with pytest.raises(NotImplementedError, match="ValueGreaterOrEqual"):
            a >= 3

    def test_bool_raises_type_error(self) -> None:
        a = self._make_proxy(1)
        with pytest.raises(TypeError, match="Cannot evaluate"):
            bool(a)

    def test_hash_uses_identity(self) -> None:
        a = self._make_proxy(1)
        b = self._make_proxy(1)
        assert hash(a) != hash(b)
        assert hash(a) == hash(a)

    def test_coerce_wraps_literal(self) -> None:
        result = _expr._coerce(42)
        assert isinstance(result, _expr.ExprProxy)
        assert isinstance(result._node, _expr.ConstNode)
        assert result._node.value == 42

    def test_coerce_passes_through_proxy(self) -> None:
        p = self._make_proxy(1)
        assert _expr._coerce(p) is p

    def test_chained_expression(self) -> None:
        a = self._make_proxy(1, primitives.Float)
        # (a + 2) * 3
        result = (a + 2) * 3
        assert isinstance(result._node, _expr.BinaryOpNode)
        assert result._node.op is _expr.BinOp.MUL
        left = result._node.left
        assert isinstance(left, _expr.BinaryOpNode)
        assert left.op is _expr.BinOp.ADD


# =========================================================================
# Space
# =========================================================================


class TestSpace:
    """Tests for Space variable declaration and access."""

    def _make_graph_and_space(self) -> tuple[_graph.Graph, _space.Space]:
        """Create a Graph and Space for testing."""
        g = _graph.Graph()
        slot = workers.Slot(id="test-slot")
        s = g.Space(slot)
        return g, s

    def test_declare_variable(self) -> None:
        g, s = self._make_graph_and_space()
        s.x = g.Float("x")
        vars_dict = object.__getattribute__(s, "_vars")
        assert "x" in vars_dict
        assert vars_dict["x"].resonite_type is primitives.Float

    def test_read_declared_variable(self) -> None:
        g, s = self._make_graph_and_space()
        s.x = g.Float("x")
        proxy = s.x
        assert isinstance(proxy, _expr.ExprProxy)
        assert isinstance(proxy._node, _expr.VarReadNode)
        assert proxy._node.var_name == "x"
        assert proxy._node._type is primitives.Float

    def test_read_undeclared_variable_raises(self) -> None:
        g, s = self._make_graph_and_space()
        with pytest.raises(AttributeError, match="not declared"):
            _ = s.y

    def test_write_outside_flow_raises(self) -> None:
        g, s = self._make_graph_and_space()
        s.z = g.Float("z")
        with pytest.raises(RuntimeError, match="outside a flow context"):
            s.z = s.z + 1

    def test_write_inside_if_records(self) -> None:
        g, s = self._make_graph_and_space()
        s.x = g.Float("x")
        s.z = g.Float("z")
        with g.If(s.x < 3):
            s.z = s.x + 3
        assert len(g._completed_flows) == 1
        ctx = g._completed_flows[0]
        assert len(ctx.true_writes) == 1
        assert ctx.true_writes[0].var_name == "z"

    def test_underscore_attrs_bypass_dsl(self) -> None:
        g, s = self._make_graph_and_space()
        s._private = 42
        assert s._private == 42


# =========================================================================
# Flow control
# =========================================================================


class TestFlowControl:
    """Tests for If/Else context managers."""

    def _make_graph_and_space(self) -> tuple[_graph.Graph, _space.Space]:
        """Create a Graph and Space for testing."""
        g = _graph.Graph()
        slot = workers.Slot(id="test-slot")
        s = g.Space(slot)
        s.x = g.Float("x")
        s.z = g.Float("z")
        return g, s

    def test_if_records_condition(self) -> None:
        g, s = self._make_graph_and_space()
        cond = s.x < 3
        with g.If(cond):
            s.z = s.x + 3
        assert g._completed_flows[0].condition is cond

    def test_if_else_records_both_branches(self) -> None:
        g, s = self._make_graph_and_space()
        with g.If(s.x < 3):
            s.z = s.x + 3
        with g.Else():
            s.z = s.x - 3
        assert len(g._completed_flows) == 1
        ctx = g._completed_flows[0]
        assert len(ctx.true_writes) == 1
        assert len(ctx.false_writes) == 1

    def test_if_without_else(self) -> None:
        g, s = self._make_graph_and_space()
        with g.If(s.x < 3):
            s.z = s.x + 3
        ctx = g._completed_flows[0]
        assert len(ctx.true_writes) == 1
        assert len(ctx.false_writes) == 0

    def test_else_without_if_raises(self) -> None:
        g = _graph.Graph()
        with pytest.raises(RuntimeError, match="without a preceding If"):
            with g.Else():
                pass

    def test_if_non_proxy_condition_raises(self) -> None:
        g = _graph.Graph()
        with pytest.raises(TypeError, match="must be an ExprProxy"):
            with g.If(True):
                pass

    def test_multiple_ifs(self) -> None:
        g, s = self._make_graph_and_space()
        s.y = g.Float("y")
        with g.If(s.x < 3):
            s.z = s.x + 3
        with g.If(s.x > 10):
            s.y = s.x * 2
        assert len(g._completed_flows) == 2

    def test_nested_flow_stack(self) -> None:
        g, s = self._make_graph_and_space()
        assert g._active_flow() is None
        with g.If(s.x < 3):
            assert g._active_flow() is not None
        assert g._active_flow() is None

    def test_multiple_writes_in_branch(self) -> None:
        g, s = self._make_graph_and_space()
        s.y = g.Float("y")
        with g.If(s.x < 3):
            s.z = s.x + 3
            s.y = s.x + 10
        ctx = g._completed_flows[0]
        assert len(ctx.true_writes) == 2
        assert ctx.true_writes[0].var_name == "z"
        assert ctx.true_writes[1].var_name == "y"


# =========================================================================
# WriteRecord and IfContext
# =========================================================================


class TestIfContext:
    """Tests for IfContext data class."""

    def test_record_write_true_phase(self) -> None:
        cond = _expr.ExprProxy(_expr.ConstNode(True, primitives.Bool))
        ctx = _flow.IfContext(condition=cond)
        space = object.__new__(_space.Space)
        write = _flow.WriteRecord(
            space=space,
            var_name="z",
            expr=_expr.ExprProxy(_expr.ConstNode(1)),
        )
        ctx.record_write(write)
        assert len(ctx.true_writes) == 1
        assert len(ctx.false_writes) == 0

    def test_record_write_false_phase(self) -> None:
        cond = _expr.ExprProxy(_expr.ConstNode(True, primitives.Bool))
        ctx = _flow.IfContext(condition=cond)
        ctx.phase = "false"
        space = object.__new__(_space.Space)
        write = _flow.WriteRecord(
            space=space,
            var_name="z",
            expr=_expr.ExprProxy(_expr.ConstNode(1)),
        )
        ctx.record_write(write)
        assert len(ctx.true_writes) == 0
        assert len(ctx.false_writes) == 1


# =========================================================================
# VarDecl
# =========================================================================


class TestVarDecl:
    """Tests for VarDecl."""

    def test_vardecl_creation(self) -> None:
        decl = _space.VarDecl("x", primitives.Float)
        assert decl.path == "x"
        assert decl.resonite_type is primitives.Float


# =========================================================================
# Graph
# =========================================================================


class TestGraph:
    """Tests for Graph factory methods."""

    def test_float_returns_vardecl(self) -> None:
        g = _graph.Graph()
        decl = g.Float("x")
        assert isinstance(decl, _space.VarDecl)
        assert decl.resonite_type is primitives.Float

    def test_int_returns_vardecl(self) -> None:
        g = _graph.Graph()
        decl = g.Int("n")
        assert isinstance(decl, _space.VarDecl)
        assert decl.resonite_type is primitives.Int

    def test_bool_returns_vardecl(self) -> None:
        g = _graph.Graph()
        decl = g.Bool("flag")
        assert isinstance(decl, _space.VarDecl)
        assert decl.resonite_type is primitives.Bool

    def test_string_returns_vardecl(self) -> None:
        g = _graph.Graph()
        decl = g.String("name")
        assert isinstance(decl, _space.VarDecl)
        assert decl.resonite_type is primitives.String

    def test_space_registers(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="slot1")
        s = g.Space(slot)
        assert s in g._spaces
