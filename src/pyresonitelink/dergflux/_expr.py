"""Expression tree nodes and proxy for Dergflux.

ExprNode subclasses form an AST that is materialized into ProtoFlux
components during the build phase.  ExprProxy wraps an ExprNode and
provides Python dunder methods so users can write ``s.x + 3`` to
build expression trees naturally.
"""

from __future__ import annotations

from enum import Enum
from typing import Any


class BinOp(Enum):
    """Binary operation types."""

    # Arithmetic
    ADD = "add"
    SUB = "sub"
    MUL = "mul"
    DIV = "div"
    MOD = "mod"
    POW = "pow"
    # Comparison
    LT = "lt"
    LE = "le"
    GT = "gt"
    GE = "ge"
    EQ = "eq"
    NE = "ne"
    # Bitwise / boolean
    AND = "and"
    OR = "or"
    XOR = "xor"
    LSHIFT = "lshift"
    RSHIFT = "rshift"


class UnOp(Enum):
    """Unary operation types."""

    NEG = "neg"
    NOT = "not"
    ABS = "abs"


# =========================================================================
# AST Nodes
# =========================================================================


class ExprNode:
    """Base class for expression tree nodes."""

    def __init__(self, expr_type: type | None = None) -> None:
        self._type = expr_type


class ConstNode(ExprNode):
    """A literal constant (int, float, bool, str)."""

    def __init__(self, value: Any, expr_type: type | None = None) -> None:
        super().__init__(expr_type)
        self.value = value


class VarReadNode(ExprNode):
    """Reading a declared dynamic variable."""

    def __init__(
        self,
        var_name: str,
        space: Any,  # Space (forward ref to avoid circular import)
        expr_type: type,
    ) -> None:
        super().__init__(expr_type)
        self.var_name = var_name
        self.space = space


class TriggerValueNode(ExprNode):
    """The value received from a DynamicImpulseReceiverWithValue.

    At build time, this references the receiver component's value output.
    """

    def __init__(self, expr_type: type) -> None:
        super().__init__(expr_type)


class LoopIndexNode(ExprNode):
    """The current iteration index of a For loop.

    At build time, this references the For node's Iteration output.
    Always typed as Int.
    """

    def __init__(self) -> None:
        from pyresonitelink.data import primitives
        super().__init__(primitives.Int)


class BinaryOpNode(ExprNode):
    """A binary operation on two expression nodes."""

    def __init__(
        self,
        op: BinOp,
        left: ExprNode,
        right: ExprNode,
        result_type: type | None = None,
    ) -> None:
        super().__init__(result_type)
        self.op = op
        self.left = left
        self.right = right


class UnaryOpNode(ExprNode):
    """A unary operation on one expression node."""

    def __init__(
        self,
        op: UnOp,
        operand: ExprNode,
        result_type: type | None = None,
    ) -> None:
        super().__init__(result_type)
        self.op = op
        self.operand = operand


class MathCallNode(ExprNode):
    """A math function call on one or more expression nodes.

    Used for typed math functions (sin, cos, sqrt, etc.) that don't
    have generic Value* versions and instead use typed variants like
    Sin_Float, Sqrt_Double.

    Attributes:
        func_name: The function name (e.g. "sin", "sqrt", "clamp").
        args: The argument nodes.
    """

    def __init__(
        self,
        func_name: str,
        args: list[ExprNode],
        result_type: type | None = None,
    ) -> None:
        super().__init__(result_type)
        self.func_name = func_name
        self.args = args


# =========================================================================
# Expression Proxy
# =========================================================================

# Comparison ops produce Bool results.
_COMPARISON_OPS = {BinOp.LT, BinOp.LE, BinOp.GT, BinOp.GE, BinOp.EQ, BinOp.NE}

# Bitwise/boolean ops preserve operand type.
_BITWISE_OPS = {BinOp.AND, BinOp.OR, BinOp.XOR, BinOp.LSHIFT, BinOp.RSHIFT}


def _coerce(value: Any) -> ExprProxy:
    """Wrap a Python literal as an ExprProxy if needed."""
    if isinstance(value, ExprProxy):
        return value
    return ExprProxy(ConstNode(value))


def _binop(op: BinOp, left: ExprProxy, right: Any) -> ExprProxy:
    """Create a binary operation proxy."""
    right_proxy = _coerce(right)
    from pyresonitelink.dergflux import _types

    result_type: type | None
    if op in _COMPARISON_OPS:
        from pyresonitelink.data import primitives
        result_type = primitives.Bool
    else:
        result_type = _types.infer_result_type(
            left._node._type, right_proxy._node._type,
        )
    return ExprProxy(
        BinaryOpNode(op, left._node, right_proxy._node, result_type),
    )


def _rbinop(op: BinOp, right: ExprProxy, left: Any) -> ExprProxy:
    """Create a binary operation proxy for reflected operations."""
    left_proxy = _coerce(left)
    return _binop(op, left_proxy, right)


def _unop(op: UnOp, operand: ExprProxy) -> ExprProxy:
    """Create a unary operation proxy."""
    from pyresonitelink.dergflux import _types
    result_type = _types.infer_result_type(operand._node._type)
    return ExprProxy(UnaryOpNode(op, operand._node, result_type))


class ExprProxy:
    """User-facing proxy that builds expression trees via dunder methods.

    Users interact with ExprProxy objects returned from Space attribute
    access and dunder operations.  Each operation returns a new
    ExprProxy wrapping a new AST node.
    """

    def __init__(self, node: ExprNode) -> None:
        self._node = node

    # --- Arithmetic ---

    def __add__(self, other: Any) -> ExprProxy:
        return _binop(BinOp.ADD, self, other)

    def __radd__(self, other: Any) -> ExprProxy:
        return _rbinop(BinOp.ADD, self, other)

    def __sub__(self, other: Any) -> ExprProxy:
        return _binop(BinOp.SUB, self, other)

    def __rsub__(self, other: Any) -> ExprProxy:
        return _rbinop(BinOp.SUB, self, other)

    def __mul__(self, other: Any) -> ExprProxy:
        return _binop(BinOp.MUL, self, other)

    def __rmul__(self, other: Any) -> ExprProxy:
        return _rbinop(BinOp.MUL, self, other)

    def __truediv__(self, other: Any) -> ExprProxy:
        return _binop(BinOp.DIV, self, other)

    def __rtruediv__(self, other: Any) -> ExprProxy:
        return _rbinop(BinOp.DIV, self, other)

    def __mod__(self, other: Any) -> ExprProxy:
        return _binop(BinOp.MOD, self, other)

    def __rmod__(self, other: Any) -> ExprProxy:
        return _rbinop(BinOp.MOD, self, other)

    def __pow__(self, other: Any) -> ExprProxy:
        return _binop(BinOp.POW, self, other)

    def __rpow__(self, other: Any) -> ExprProxy:
        return _rbinop(BinOp.POW, self, other)

    def __neg__(self) -> ExprProxy:
        return _unop(UnOp.NEG, self)

    def __abs__(self) -> ExprProxy:
        return _unop(UnOp.ABS, self)

    # --- Comparison ---

    def __lt__(self, other: Any) -> ExprProxy:
        return _binop(BinOp.LT, self, other)

    def __gt__(self, other: Any) -> ExprProxy:
        return _binop(BinOp.GT, self, other)

    def __eq__(self, other: Any) -> ExprProxy:  # type: ignore[override]
        return _binop(BinOp.EQ, self, other)

    def __ne__(self, other: Any) -> ExprProxy:  # type: ignore[override]
        return _binop(BinOp.NE, self, other)

    def __le__(self, other: Any) -> ExprProxy:
        return _binop(BinOp.LE, self, other)

    def __ge__(self, other: Any) -> ExprProxy:
        return _binop(BinOp.GE, self, other)

    # --- Bitwise / Boolean ---

    def __and__(self, other: Any) -> ExprProxy:
        return _binop(BinOp.AND, self, other)

    def __rand__(self, other: Any) -> ExprProxy:
        return _rbinop(BinOp.AND, self, other)

    def __or__(self, other: Any) -> ExprProxy:
        return _binop(BinOp.OR, self, other)

    def __ror__(self, other: Any) -> ExprProxy:
        return _rbinop(BinOp.OR, self, other)

    def __xor__(self, other: Any) -> ExprProxy:
        return _binop(BinOp.XOR, self, other)

    def __rxor__(self, other: Any) -> ExprProxy:
        return _rbinop(BinOp.XOR, self, other)

    def __invert__(self) -> ExprProxy:
        return _unop(UnOp.NOT, self)

    def __lshift__(self, other: Any) -> ExprProxy:
        return _binop(BinOp.LSHIFT, self, other)

    def __rlshift__(self, other: Any) -> ExprProxy:
        return _rbinop(BinOp.LSHIFT, self, other)

    def __rshift__(self, other: Any) -> ExprProxy:
        return _binop(BinOp.RSHIFT, self, other)

    def __rrshift__(self, other: Any) -> ExprProxy:
        return _rbinop(BinOp.RSHIFT, self, other)

    # --- Safety ---

    def __bool__(self) -> bool:
        raise TypeError(
            "Cannot evaluate ExprProxy as bool. "
            "Use inside g.If() instead of Python if."
        )

    def __hash__(self) -> int:
        return id(self)

    def __repr__(self) -> str:
        return f"ExprProxy({self._node!r})"
