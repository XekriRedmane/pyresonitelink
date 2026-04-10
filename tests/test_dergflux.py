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


def _stmts(g: _graph.Graph) -> list[_flow.FlowContext]:
    """Get the statements from the first Under record."""
    return g._under_records[0].statements


# =========================================================================
# Type inference
# =========================================================================


class TestTypeInference:
    """Tests for _types module."""

    def test_infer_result_type_prefers_left(self) -> None:
        from pyresonitelink.dergflux import _types
        result = _types.infer_result_type(primitives.Int, primitives.Float)
        assert result is primitives.Int

    def test_infer_result_type_falls_back_to_right(self) -> None:
        from pyresonitelink.dergflux import _types
        result = _types.infer_result_type(None, primitives.Float)
        assert result is primitives.Float

    def test_infer_result_type_both_none(self) -> None:
        from pyresonitelink.dergflux import _types
        result = _types.infer_result_type(None, None)
        assert result is None

    def test_resolve_const_type_uses_context(self) -> None:
        from pyresonitelink.dergflux import _types
        result = _types.resolve_const_type(42, primitives.Float)
        assert result is primitives.Float

    def test_resolve_const_type_maps_int(self) -> None:
        from pyresonitelink.dergflux import _types
        result = _types.resolve_const_type(42, None)
        assert result is primitives.Int

    def test_resolve_const_type_maps_float(self) -> None:
        from pyresonitelink.dergflux import _types
        result = _types.resolve_const_type(3.14, None)
        assert result is primitives.Float

    def test_resolve_const_type_maps_bool(self) -> None:
        from pyresonitelink.dergflux import _types
        result = _types.resolve_const_type(True, None)
        assert result is primitives.Bool

    def test_resolve_const_type_maps_str(self) -> None:
        from pyresonitelink.dergflux import _types
        result = _types.resolve_const_type("hello", None)
        assert result is primitives.String

    def test_resolve_const_type_unknown_defaults_to_float(self) -> None:
        from pyresonitelink.dergflux import _types
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
        assert isinstance(result._node.left, _expr.ConstNode)
        assert result._node.left.value == 2

    def test_mul(self) -> None:
        result = self._make_proxy(1) * 2
        assert result._node.op is _expr.BinOp.MUL

    def test_truediv(self) -> None:
        result = self._make_proxy(1) / 2
        assert result._node.op is _expr.BinOp.DIV

    def test_mod(self) -> None:
        result = self._make_proxy(1) % 2
        assert result._node.op is _expr.BinOp.MOD

    def test_neg(self) -> None:
        result = -self._make_proxy(1)
        assert isinstance(result._node, _expr.UnaryOpNode)
        assert result._node.op is _expr.UnOp.NEG

    def test_lt(self) -> None:
        result = self._make_proxy(1) < 3
        assert result._node.op is _expr.BinOp.LT
        assert result._node._type is primitives.Bool

    def test_le(self) -> None:
        result = self._make_proxy(1) <= 3
        assert result._node.op is _expr.BinOp.LE
        assert result._node._type is primitives.Bool

    def test_gt(self) -> None:
        result = self._make_proxy(1) > 3
        assert result._node.op is _expr.BinOp.GT
        assert result._node._type is primitives.Bool

    def test_ge(self) -> None:
        result = self._make_proxy(1) >= 3
        assert result._node.op is _expr.BinOp.GE
        assert result._node._type is primitives.Bool

    def test_eq(self) -> None:
        result = self._make_proxy(1) == 3
        assert result._node.op is _expr.BinOp.EQ
        assert result._node._type is primitives.Bool

    def test_ne(self) -> None:
        result = self._make_proxy(1) != 3
        assert result._node.op is _expr.BinOp.NE
        assert result._node._type is primitives.Bool

    def test_bool_raises(self) -> None:
        with pytest.raises(TypeError, match="Cannot evaluate"):
            bool(self._make_proxy(1))

    def test_hash_identity(self) -> None:
        a = self._make_proxy(1)
        b = self._make_proxy(1)
        assert hash(a) != hash(b)

    def test_coerce_wraps_literal(self) -> None:
        result = _expr._coerce(42)
        assert isinstance(result._node, _expr.ConstNode)

    def test_coerce_passes_through(self) -> None:
        p = self._make_proxy(1)
        assert _expr._coerce(p) is p

    def test_chained_expression(self) -> None:
        result = (self._make_proxy(1) + 2) * 3
        assert result._node.op is _expr.BinOp.MUL
        assert isinstance(result._node.left, _expr.BinaryOpNode)

    def test_pow(self) -> None:
        result = self._make_proxy(2) ** 3
        assert result._node.op is _expr.BinOp.POW

    def test_rpow(self) -> None:
        result = 3 ** self._make_proxy(2)
        assert result._node.op is _expr.BinOp.POW
        assert isinstance(result._node.left, _expr.ConstNode)

    def test_abs(self) -> None:
        result = abs(self._make_proxy(-5))
        assert isinstance(result._node, _expr.UnaryOpNode)
        assert result._node.op is _expr.UnOp.ABS

    def test_and(self) -> None:
        a = self._make_proxy(True, primitives.Bool)
        result = a & True
        assert result._node.op is _expr.BinOp.AND

    def test_or(self) -> None:
        a = self._make_proxy(True, primitives.Bool)
        result = a | False
        assert result._node.op is _expr.BinOp.OR

    def test_xor(self) -> None:
        a = self._make_proxy(True, primitives.Bool)
        result = a ^ True
        assert result._node.op is _expr.BinOp.XOR

    def test_invert(self) -> None:
        result = ~self._make_proxy(True, primitives.Bool)
        assert result._node.op is _expr.UnOp.NOT

    def test_lshift(self) -> None:
        result = self._make_proxy(1, primitives.Int) << 2
        assert result._node.op is _expr.BinOp.LSHIFT

    def test_rshift(self) -> None:
        result = self._make_proxy(8, primitives.Int) >> 2
        assert result._node.op is _expr.BinOp.RSHIFT

    def test_bitwise_preserves_type(self) -> None:
        result = self._make_proxy(0xFF, primitives.Int) & 0x0F
        assert result._node._type is primitives.Int

    def test_boolean_and_preserves_bool(self) -> None:
        result = self._make_proxy(True, primitives.Bool) & True
        assert result._node._type is primitives.Bool


# =========================================================================
# Math functions
# =========================================================================


class TestMathFunctions:
    """Tests for _math module function calls."""

    def _make_proxy(
        self, value: object = 0, expr_type: type = primitives.Float,
    ) -> _expr.ExprProxy:
        """Create an ExprProxy wrapping a ConstNode."""
        return _expr.ExprProxy(_expr.ConstNode(value, expr_type))

    def test_sin(self) -> None:
        from pyresonitelink.dergflux import _math
        result = _math.sin(self._make_proxy(1.0))
        assert isinstance(result._node, _expr.MathCallNode)
        assert result._node.func_name == "sin"
        assert len(result._node.args) == 1

    def test_cos(self) -> None:
        from pyresonitelink.dergflux import _math
        assert _math.cos(self._make_proxy(1.0))._node.func_name == "cos"

    def test_sqrt(self) -> None:
        from pyresonitelink.dergflux import _math
        assert _math.sqrt(self._make_proxy(4.0))._node.func_name == "sqrt"

    def test_atan2(self) -> None:
        from pyresonitelink.dergflux import _math
        result = _math.atan2(self._make_proxy(1.0), self._make_proxy(2.0))
        assert result._node.func_name == "atan2"
        assert len(result._node.args) == 2

    def test_min(self) -> None:
        from pyresonitelink.dergflux import _math
        assert _math.min_(self._make_proxy(), self._make_proxy())._node.func_name == "min"

    def test_max(self) -> None:
        from pyresonitelink.dergflux import _math
        assert _math.max_(self._make_proxy(), self._make_proxy())._node.func_name == "max"

    def test_clamp(self) -> None:
        from pyresonitelink.dergflux import _math
        result = _math.clamp(self._make_proxy(), 0, 10)
        assert result._node.func_name == "clamp"
        assert len(result._node.args) == 3

    def test_lerp(self) -> None:
        from pyresonitelink.dergflux import _math
        result = _math.lerp(self._make_proxy(), self._make_proxy(), self._make_proxy())
        assert result._node.func_name == "lerp"

    def test_conditional(self) -> None:
        from pyresonitelink.dergflux import _math
        result = _math.conditional(
            self._make_proxy(True, primitives.Bool),
            self._make_proxy(1.0), self._make_proxy(2.0),
        )
        assert result._node.func_name == "conditional"

    def test_type_inference(self) -> None:
        from pyresonitelink.dergflux import _math
        result = _math.sin(self._make_proxy(1.0, primitives.Double))
        assert result._node._type is primitives.Double

    def test_import_via_module(self) -> None:
        from pyresonitelink.dergflux import math as dm
        result = dm.sin(self._make_proxy(1.0))
        assert result._node.func_name == "sin"


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

    def test_declare_float_var(self) -> None:
        g, s = self._make_graph_and_space()
        s.x = s.FloatVar("x")
        vars_dict = object.__getattribute__(s, "_vars")
        assert "x" in vars_dict
        assert vars_dict["x"].resonite_type is primitives.Float

    def test_declare_with_explicit_type(self) -> None:
        g, s = self._make_graph_and_space()
        s.x = s.Var("x", primitives.Double)
        vars_dict = object.__getattribute__(s, "_vars")
        assert vars_dict["x"].resonite_type is primitives.Double

    def test_declare_with_slot(self) -> None:
        g, s = self._make_graph_and_space()
        child = workers.Slot(id="child-slot")
        s.x = s.FloatVar("x", slot=child)
        vars_dict = object.__getattribute__(s, "_vars")
        assert vars_dict["x"].slot is child

    def test_read_declared_variable(self) -> None:
        g, s = self._make_graph_and_space()
        s.x = s.FloatVar("x")
        proxy = s.x
        assert isinstance(proxy, _expr.ExprProxy)
        assert isinstance(proxy._node, _expr.VarReadNode)
        assert proxy._node._type is primitives.Float

    def test_read_undeclared_raises(self) -> None:
        g, s = self._make_graph_and_space()
        with pytest.raises(AttributeError, match="not declared"):
            _ = s.y

    def test_write_outside_flow_and_under_raises(self) -> None:
        g, s = self._make_graph_and_space()
        s.z = s.FloatVar("z")
        with pytest.raises(RuntimeError, match="Cannot assign"):
            s.z = s.z + 1

    def test_write_inside_if_records(self) -> None:
        g, s = self._make_graph_and_space()
        s.x = s.FloatVar("x")
        s.z = s.FloatVar("z")
        slot = object.__getattribute__(s, "_slot")
        with g.Under(slot):
            with g.If(s.x < 3):
                s.z = s.x + 3
        ctx = _stmts(g)[0]
        assert isinstance(ctx, _flow.IfContext)
        assert len(ctx.true_writes) == 1
        assert ctx.true_writes[0].var_name == "z"

    def test_bare_write_inside_under(self) -> None:
        g, s = self._make_graph_and_space()
        s.z = s.FloatVar("z")
        slot = object.__getattribute__(s, "_slot")
        with g.Under(slot):
            s.z = s.z + 1
        ctx = _stmts(g)[0]
        assert isinstance(ctx, _flow.BareWriteContext)
        assert len(ctx.writes) == 1

    def test_underscore_attrs_bypass_dsl(self) -> None:
        g, s = self._make_graph_and_space()
        s._private = 42
        assert s._private == 42

    def test_all_var_types_registered(self) -> None:
        g, s = self._make_graph_and_space()
        for method_name, expected_type in _space._VAR_TYPES.items():
            factory = getattr(s, method_name)
            decl = factory("test")
            assert isinstance(decl, _space.VarDecl)
            assert decl.resonite_type is expected_type


# =========================================================================
# If / Else
# =========================================================================


class TestFlowControl:
    """Tests for If/Else context managers."""

    def _setup(self) -> tuple[_graph.Graph, _space.Space, workers.Slot]:
        """Create a Graph, Space, and slot for testing."""
        g = _graph.Graph()
        slot = workers.Slot(id="test-slot")
        s = g.Space(slot)
        s.x = s.FloatVar("x")
        s.z = s.FloatVar("z")
        return g, s, slot

    def test_if_records_condition(self) -> None:
        g, s, slot = self._setup()
        cond = s.x < 3
        with g.Under(slot):
            with g.If(cond):
                s.z = s.x + 3
        ctx = _stmts(g)[0]
        assert isinstance(ctx, _flow.IfContext)
        assert ctx.condition is cond

    def test_if_else_records_both_branches(self) -> None:
        g, s, slot = self._setup()
        with g.Under(slot):
            with g.If(s.x < 3):
                s.z = s.x + 3
            with g.Else():
                s.z = s.x - 3
        ctx = _stmts(g)[0]
        assert isinstance(ctx, _flow.IfContext)
        assert len(ctx.true_writes) == 1
        assert len(ctx.false_writes) == 1

    def test_if_without_else(self) -> None:
        g, s, slot = self._setup()
        with g.Under(slot):
            with g.If(s.x < 3):
                s.z = s.x + 3
        ctx = _stmts(g)[0]
        assert isinstance(ctx, _flow.IfContext)
        assert len(ctx.true_writes) == 1
        assert len(ctx.false_writes) == 0

    def test_else_without_if_raises(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="s")
        with pytest.raises(RuntimeError, match="without a preceding If"):
            with g.Under(slot):
                with g.Else():
                    pass

    def test_if_non_proxy_raises(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="s")
        with g.Under(slot):
            with pytest.raises(TypeError, match="must be an ExprProxy"):
                with g.If(True):
                    pass

    def test_if_outside_under_raises(self) -> None:
        g, s, slot = self._setup()
        with pytest.raises(RuntimeError, match="inside g.Under"):
            with g.If(s.x < 3):
                pass

    def test_multiple_ifs_in_sequence(self) -> None:
        g, s, slot = self._setup()
        s.y = s.FloatVar("y")
        with g.Under(slot):
            with g.If(s.x < 3):
                s.z = s.x + 3
            with g.If(s.x > 10):
                s.y = s.x * 2
        stmts = _stmts(g)
        assert len(stmts) == 2
        assert isinstance(stmts[0], _flow.IfContext)
        assert isinstance(stmts[1], _flow.IfContext)

    def test_if_then_bare_write_continuation(self) -> None:
        g, s, slot = self._setup()
        with g.Under(slot):
            with g.If(s.x < 3):
                s.z = s.x + 3
            with g.Else():
                s.z = s.x - 3
            s.z = s.z + 1
        stmts = _stmts(g)
        assert len(stmts) == 2
        assert isinstance(stmts[0], _flow.IfContext)
        assert isinstance(stmts[1], _flow.BareWriteContext)
        assert stmts[1].writes[0].var_name == "z"

    def test_multiple_writes_in_branch(self) -> None:
        g, s, slot = self._setup()
        s.y = s.FloatVar("y")
        with g.Under(slot):
            with g.If(s.x < 3):
                s.z = s.x + 3
                s.y = s.x + 10
        ctx = _stmts(g)[0]
        assert isinstance(ctx, _flow.IfContext)
        assert len(ctx.true_writes) == 2


# =========================================================================
# For loop
# =========================================================================


class TestForLoop:
    """Tests for g.For() with ForProxy."""

    def _setup(self) -> tuple[_graph.Graph, _space.Space, workers.Slot]:
        """Create a Graph, Space, and slot for testing."""
        g = _graph.Graph()
        slot = workers.Slot(id="test-slot")
        s = g.Space(slot)
        s.total = s.FloatVar("total")
        return g, s, slot

    def test_for_yields_for_proxy(self) -> None:
        g, s, slot = self._setup()
        with g.Under(slot):
            with g.For(10) as f:
                assert isinstance(f, _graph.ForProxy)

    def test_on_iterate_yields_int_proxy(self) -> None:
        g, s, slot = self._setup()
        with g.Under(slot):
            with g.For(10) as f:
                with f.OnIterate() as i:
                    assert isinstance(i, _expr.ExprProxy)
                    assert isinstance(i._node, _expr.LoopIndexNode)
                    assert i._node._type is primitives.Int

    def test_for_records_context(self) -> None:
        g, s, slot = self._setup()
        with g.Under(slot):
            with g.For(10) as f:
                with f.OnIterate() as i:
                    s.total = s.total + i
        ctx = _stmts(g)[0]
        assert isinstance(ctx, _flow.ForContext)

    def test_for_records_count(self) -> None:
        g, s, slot = self._setup()
        with g.Under(slot):
            with g.For(10) as f:
                with f.OnIterate() as i:
                    s.total = s.total + i
        ctx = _stmts(g)[0]
        assert isinstance(ctx, _flow.ForContext)
        assert isinstance(ctx.count._node, _expr.ConstNode)
        assert ctx.count._node.value == 10

    def test_on_start_records_start_writes(self) -> None:
        g, s, slot = self._setup()
        with g.Under(slot):
            with g.For(10) as f:
                with f.OnStart():
                    s.total = 0
                with f.OnIterate() as i:
                    s.total = s.total + i
        ctx = _stmts(g)[0]
        assert isinstance(ctx, _flow.ForContext)
        assert len(ctx.start_writes) == 1
        assert ctx.start_writes[0].var_name == "total"
        assert len(ctx.iteration_writes) == 1

    def test_on_iterate_records_iteration_writes(self) -> None:
        g, s, slot = self._setup()
        with g.Under(slot):
            with g.For(10) as f:
                with f.OnIterate() as i:
                    s.total = s.total + i
        ctx = _stmts(g)[0]
        assert isinstance(ctx, _flow.ForContext)
        assert len(ctx.iteration_writes) == 1
        assert ctx.iteration_writes[0].var_name == "total"

    def test_for_with_reverse(self) -> None:
        g, s, slot = self._setup()
        with g.Under(slot):
            with g.For(10, reverse=True) as f:
                with f.OnIterate() as i:
                    s.total = s.total + i
        ctx = _stmts(g)[0]
        assert isinstance(ctx, _flow.ForContext)
        assert ctx.reverse is not None

    def test_for_outside_under_raises(self) -> None:
        g = _graph.Graph()
        with pytest.raises(RuntimeError, match="inside g.Under"):
            with g.For(10) as f:
                pass

    def test_for_then_if_continuation(self) -> None:
        g, s, slot = self._setup()
        with g.Under(slot):
            with g.For(10) as f:
                with f.OnStart():
                    s.total = 0
                with f.OnIterate() as i:
                    s.total = s.total + i
            with g.If(s.total > 0):
                s.total = s.total * 2
        stmts = _stmts(g)
        assert len(stmts) == 2
        assert isinstance(stmts[0], _flow.ForContext)
        assert isinstance(stmts[1], _flow.IfContext)


# =========================================================================
# While loop
# =========================================================================


class TestWhileLoop:
    """Tests for g.While() context manager."""

    def _setup(self) -> tuple[_graph.Graph, _space.Space, workers.Slot]:
        """Create a Graph, Space, and slot for testing."""
        g = _graph.Graph()
        slot = workers.Slot(id="test-slot")
        s = g.Space(slot)
        s.x = s.FloatVar("x")
        return g, s, slot

    def test_while_records_context(self) -> None:
        g, s, slot = self._setup()
        with g.Under(slot):
            with g.While(s.x > 0):
                s.x = s.x - 1
        ctx = _stmts(g)[0]
        assert isinstance(ctx, _flow.WhileContext)

    def test_while_records_condition(self) -> None:
        g, s, slot = self._setup()
        cond = s.x > 0
        with g.Under(slot):
            with g.While(cond):
                s.x = s.x - 1
        ctx = _stmts(g)[0]
        assert isinstance(ctx, _flow.WhileContext)
        assert ctx.condition is cond

    def test_while_records_writes(self) -> None:
        g, s, slot = self._setup()
        with g.Under(slot):
            with g.While(s.x > 0):
                s.x = s.x - 1
        ctx = _stmts(g)[0]
        assert isinstance(ctx, _flow.WhileContext)
        assert len(ctx.writes) == 1

    def test_while_outside_under_raises(self) -> None:
        g, s, slot = self._setup()
        with pytest.raises(RuntimeError, match="inside g.Under"):
            with g.While(s.x > 0):
                pass

    def test_while_non_proxy_raises(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="s")
        with g.Under(slot):
            with pytest.raises(TypeError, match="must be an ExprProxy"):
                with g.While(True):
                    pass


# =========================================================================
# IfContext dataclass
# =========================================================================


class TestIfContext:
    """Tests for IfContext data class."""

    def test_record_write_true_phase(self) -> None:
        cond = _expr.ExprProxy(_expr.ConstNode(True, primitives.Bool))
        slot = workers.Slot(id="s")
        ctx = _flow.IfContext(condition=cond, slot=slot)
        space = object.__new__(_space.Space)
        ctx.record_write(_flow.WriteRecord(space, "z", _expr.ExprProxy(_expr.ConstNode(1))))
        assert len(ctx.true_writes) == 1
        assert len(ctx.false_writes) == 0

    def test_record_write_false_phase(self) -> None:
        cond = _expr.ExprProxy(_expr.ConstNode(True, primitives.Bool))
        slot = workers.Slot(id="s")
        ctx = _flow.IfContext(condition=cond, slot=slot)
        ctx.phase = "false"
        space = object.__new__(_space.Space)
        ctx.record_write(_flow.WriteRecord(space, "z", _expr.ExprProxy(_expr.ConstNode(1))))
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
        assert decl.slot is None

    def test_vardecl_with_slot(self) -> None:
        slot = workers.Slot(id="child")
        decl = _space.VarDecl("x", primitives.Float, slot=slot)
        assert decl.slot is slot


# =========================================================================
# Graph
# =========================================================================


class TestGraph:
    """Tests for Graph including Under context manager."""

    def test_space_registers(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="slot1")
        s = g.Space(slot)
        assert s in g._spaces

    def test_space_no_slot_no_under_raises(self) -> None:
        g = _graph.Graph()
        with pytest.raises(RuntimeError, match="requires a slot"):
            g.Space()

    def test_under_sets_active_slot(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="slot1")
        assert g._active_slot() is None
        with g.Under(slot):
            assert g._active_slot() is slot
        assert g._active_slot() is None

    def test_under_nested(self) -> None:
        g = _graph.Graph()
        outer = workers.Slot(id="outer")
        inner = workers.Slot(id="inner")
        with g.Under(outer):
            assert g._active_slot() is outer
            with g.Under(inner):
                assert g._active_slot() is inner
            assert g._active_slot() is outer

    def test_space_inherits_under_slot(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="slot1")
        with g.Under(slot):
            s = g.Space()
        space_slot = object.__getattribute__(s, "_slot")
        assert space_slot is slot

    def test_under_no_trigger_yields_none(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="s")
        with g.Under(slot) as value:
            assert value is None

    def test_under_string_trigger_yields_none(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="s")
        with g.Under(slot, trigger="MyImpulse") as value:
            assert value is None

    def test_under_typed_trigger_yields_proxy(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="s")
        with g.Under(slot, trigger=("MyImpulse", primitives.Float)) as value:
            assert isinstance(value, _expr.ExprProxy)
            assert isinstance(value._node, _expr.TriggerValueNode)

    def test_under_records_trigger(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="s")
        s = g.Space(slot)
        s.x = s.FloatVar("x")
        s.z = s.FloatVar("z")
        with g.Under(slot, trigger="MyImpulse"):
            with g.If(s.x < 3):
                s.z = s.x + 3
        assert g._under_records[0].trigger is not None
        assert g._under_records[0].trigger.tag == "MyImpulse"

    def test_full_under_workflow(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="test-slot")
        with g.Under(slot):
            s = g.Space()
            s.x = s.FloatVar("x")
            s.z = s.FloatVar("z")
            with g.If(s.x < 3):
                s.z = s.x + 3
            with g.Else():
                s.z = s.x - 3
        assert len(g._spaces) == 1
        assert len(g._under_records) == 1
        stmts = _stmts(g)
        assert len(stmts) == 1
        assert isinstance(stmts[0], _flow.IfContext)
        assert len(stmts[0].true_writes) == 1
        assert len(stmts[0].false_writes) == 1

    def test_full_if_continuation_workflow(self) -> None:
        """If/Else followed by a bare write creates two statements."""
        g = _graph.Graph()
        slot = workers.Slot(id="test-slot")
        s = g.Space(slot)
        s.x = s.FloatVar("x")
        s.z = s.FloatVar("z")
        with g.Under(slot):
            with g.If(s.x < 3):
                s.z = s.x + 3
            with g.Else():
                s.z = s.x - 3
            s.z = s.z + 1
        stmts = _stmts(g)
        assert len(stmts) == 2

    def test_full_for_workflow(self) -> None:
        """For with OnStart and OnIterate followed by If."""
        g = _graph.Graph()
        slot = workers.Slot(id="test-slot")
        s = g.Space(slot)
        s.total = s.FloatVar("total")
        with g.Under(slot):
            with g.For(10) as f:
                with f.OnStart():
                    s.total = 0
                with f.OnIterate() as i:
                    s.total = s.total + i
            with g.If(s.total > 0):
                s.total = s.total * 2
        stmts = _stmts(g)
        assert len(stmts) == 2
        assert isinstance(stmts[0], _flow.ForContext)
        assert isinstance(stmts[1], _flow.IfContext)
        assert len(stmts[0].start_writes) == 1
        assert len(stmts[0].iteration_writes) == 1
