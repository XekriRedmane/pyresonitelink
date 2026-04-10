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

    def test_le_creates_binary_node_with_bool_type(self) -> None:
        a = self._make_proxy(1)
        result = a <= 3
        assert isinstance(result._node, _expr.BinaryOpNode)
        assert result._node.op is _expr.BinOp.LE
        assert result._node._type is primitives.Bool

    def test_ge_creates_binary_node_with_bool_type(self) -> None:
        a = self._make_proxy(1)
        result = a >= 3
        assert isinstance(result._node, _expr.BinaryOpNode)
        assert result._node.op is _expr.BinOp.GE
        assert result._node._type is primitives.Bool

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

    def test_declare_float_var(self) -> None:
        g, s = self._make_graph_and_space()
        s.x = s.FloatVar("x")
        vars_dict = object.__getattribute__(s, "_vars")
        assert "x" in vars_dict
        assert vars_dict["x"].resonite_type is primitives.Float

    def test_declare_int_var(self) -> None:
        g, s = self._make_graph_and_space()
        s.n = s.IntVar("n")
        vars_dict = object.__getattribute__(s, "_vars")
        assert vars_dict["n"].resonite_type is primitives.Int

    def test_declare_bool_var(self) -> None:
        g, s = self._make_graph_and_space()
        s.flag = s.BoolVar("flag")
        vars_dict = object.__getattribute__(s, "_vars")
        assert vars_dict["flag"].resonite_type is primitives.Bool

    def test_declare_string_var(self) -> None:
        g, s = self._make_graph_and_space()
        s.name = s.StringVar("name")
        vars_dict = object.__getattribute__(s, "_vars")
        assert vars_dict["name"].resonite_type is primitives.String

    def test_declare_float3_var(self) -> None:
        g, s = self._make_graph_and_space()
        s.pos = s.Float3Var("pos")
        vars_dict = object.__getattribute__(s, "_vars")
        assert vars_dict["pos"].resonite_type is primitives.Float3

    def test_declare_colorx_var(self) -> None:
        g, s = self._make_graph_and_space()
        s.col = s.ColorXVar("col")
        vars_dict = object.__getattribute__(s, "_vars")
        assert vars_dict["col"].resonite_type is primitives.ColorX

    def test_declare_var_with_explicit_type(self) -> None:
        g, s = self._make_graph_and_space()
        s.x = s.Var("x", primitives.Double)
        vars_dict = object.__getattribute__(s, "_vars")
        assert vars_dict["x"].resonite_type is primitives.Double

    def test_declare_var_with_slot(self) -> None:
        g, s = self._make_graph_and_space()
        child = workers.Slot(id="child-slot")
        s.x = s.FloatVar("x", slot=child)
        vars_dict = object.__getattribute__(s, "_vars")
        assert vars_dict["x"].slot is child

    def test_declare_var_default_no_slot(self) -> None:
        g, s = self._make_graph_and_space()
        s.x = s.FloatVar("x")
        vars_dict = object.__getattribute__(s, "_vars")
        assert vars_dict["x"].slot is None

    def test_read_declared_variable(self) -> None:
        g, s = self._make_graph_and_space()
        s.x = s.FloatVar("x")
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
        s.z = s.FloatVar("z")
        with pytest.raises(RuntimeError, match="outside a flow context"):
            s.z = s.z + 1

    def test_write_inside_if_records(self) -> None:
        g, s = self._make_graph_and_space()
        s.x = s.FloatVar("x")
        s.z = s.FloatVar("z")
        slot = object.__getattribute__(s, "_slot")
        with g.Under(slot):
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

    def test_all_var_types_registered(self) -> None:
        """Verify all _VAR_TYPES produce valid VarDecl objects."""
        g, s = self._make_graph_and_space()
        for method_name, expected_type in _space._VAR_TYPES.items():
            factory = getattr(s, method_name)
            decl = factory("test")
            assert isinstance(decl, _space.VarDecl)
            assert decl.resonite_type is expected_type
            assert decl.path == "test"

    def test_var_type_with_slot_kwarg(self) -> None:
        """Verify that Var factory methods accept a slot keyword argument."""
        g, s = self._make_graph_and_space()
        child = workers.Slot(id="child")
        decl = s.DoubleVar("d", slot=child)
        assert decl.slot is child


# =========================================================================
# Flow control
# =========================================================================


class TestFlowControl:
    """Tests for If/Else context managers."""

    def _make_graph_and_space(self) -> tuple[_graph.Graph, _space.Space, workers.Slot]:
        """Create a Graph, Space, and slot for testing."""
        g = _graph.Graph()
        slot = workers.Slot(id="test-slot")
        s = g.Space(slot)
        s.x = s.FloatVar("x")
        s.z = s.FloatVar("z")
        return g, s, slot

    def test_if_records_condition(self) -> None:
        g, s, slot = self._make_graph_and_space()
        cond = s.x < 3
        with g.Under(slot):
            with g.If(cond):
                s.z = s.x + 3
        assert g._completed_flows[0].condition is cond

    def test_if_records_slot(self) -> None:
        g, s, slot = self._make_graph_and_space()
        with g.Under(slot):
            with g.If(s.x < 3):
                s.z = s.x + 3
        assert g._completed_flows[0].slot is slot

    def test_if_else_records_both_branches(self) -> None:
        g, s, slot = self._make_graph_and_space()
        with g.Under(slot):
            with g.If(s.x < 3):
                s.z = s.x + 3
            with g.Else():
                s.z = s.x - 3
        assert len(g._completed_flows) == 1
        ctx = g._completed_flows[0]
        assert len(ctx.true_writes) == 1
        assert len(ctx.false_writes) == 1

    def test_if_without_else(self) -> None:
        g, s, slot = self._make_graph_and_space()
        with g.Under(slot):
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
        slot = workers.Slot(id="s")
        with g.Under(slot):
            with pytest.raises(TypeError, match="must be an ExprProxy"):
                with g.If(True):
                    pass

    def test_if_outside_under_raises(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="s")
        s = g.Space(slot)
        s.x = s.FloatVar("x")
        with pytest.raises(RuntimeError, match="must be used inside g.Under"):
            with g.If(s.x < 3):
                pass

    def test_multiple_ifs(self) -> None:
        g, s, slot = self._make_graph_and_space()
        s.y = s.FloatVar("y")
        with g.Under(slot):
            with g.If(s.x < 3):
                s.z = s.x + 3
            with g.If(s.x > 10):
                s.y = s.x * 2
        assert len(g._completed_flows) == 2

    def test_nested_flow_stack(self) -> None:
        g, s, slot = self._make_graph_and_space()
        assert g._active_flow() is None
        with g.Under(slot):
            with g.If(s.x < 3):
                assert g._active_flow() is not None
        assert g._active_flow() is None

    def test_multiple_writes_in_branch(self) -> None:
        g, s, slot = self._make_graph_and_space()
        s.y = s.FloatVar("y")
        with g.Under(slot):
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
        slot = workers.Slot(id="s")
        ctx = _flow.IfContext(condition=cond, slot=slot)
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
        slot = workers.Slot(id="s")
        ctx = _flow.IfContext(condition=cond, slot=slot)
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

    def test_space_with_name(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="slot1")
        s = g.Space(slot, name="MySpace")
        space_name = object.__getattribute__(s, "_space_name")
        assert space_name == "MySpace"

    def test_space_without_name(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="slot1")
        s = g.Space(slot)
        space_name = object.__getattribute__(s, "_space_name")
        assert space_name is None

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

    def test_space_explicit_slot_overrides_under(self) -> None:
        g = _graph.Graph()
        under_slot = workers.Slot(id="under")
        explicit_slot = workers.Slot(id="explicit")
        with g.Under(under_slot):
            s = g.Space(explicit_slot)
        space_slot = object.__getattribute__(s, "_slot")
        assert space_slot is explicit_slot

    def test_space_no_slot_no_under_raises(self) -> None:
        g = _graph.Graph()
        with pytest.raises(RuntimeError, match="requires a slot"):
            g.Space()

    def test_full_under_workflow(self) -> None:
        """Verify the full Under workflow from the example."""
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
        assert len(g._completed_flows) == 1
        ctx = g._completed_flows[0]
        assert len(ctx.true_writes) == 1
        assert len(ctx.false_writes) == 1
        assert ctx.trigger is None

    # --- Trigger variants ---

    def test_under_no_trigger_default(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="s")
        s = g.Space(slot)
        s.x = s.FloatVar("x")
        s.z = s.FloatVar("z")
        with g.Under(slot):
            with g.If(s.x < 3):
                s.z = s.x + 3
        assert g._completed_flows[0].trigger is None

    def test_under_string_trigger(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="s")
        s = g.Space(slot)
        s.x = s.FloatVar("x")
        s.z = s.FloatVar("z")
        with g.Under(slot, trigger="MyImpulse"):
            with g.If(s.x < 3):
                s.z = s.x + 3
        trigger = g._completed_flows[0].trigger
        assert trigger is not None
        assert trigger.tag == "MyImpulse"
        assert trigger.value_type is None

    def test_under_typed_trigger_yields_proxy(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="s")
        s = g.Space(slot)
        s.z = s.FloatVar("z")
        with g.Under(slot, trigger=("MyImpulse", primitives.Float)) as value:
            assert isinstance(value, _expr.ExprProxy)
            assert isinstance(value._node, _expr.TriggerValueNode)
            assert value._node._type is primitives.Float

    def test_under_typed_trigger_records_on_if(self) -> None:
        g = _graph.Graph()
        slot = workers.Slot(id="s")
        s = g.Space(slot)
        s.x = s.FloatVar("x")
        s.z = s.FloatVar("z")
        with g.Under(slot, trigger=("MyImpulse", primitives.Float)) as value:
            with g.If(s.x < 3):
                s.z = value + 3
        trigger = g._completed_flows[0].trigger
        assert trigger is not None
        assert trigger.tag == "MyImpulse"
        assert trigger.value_type is primitives.Float

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
