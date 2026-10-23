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
        # Nodes that take this expression as their only input and have
        # several outputs, by class name, so that the outputs share one
        # node. A vector's .x, .y, and .z share its Unpack node, and a
        # slot's global position and rotation share its GlobalTransform.
        self._shared_calls: dict[str, NodeCall] = {}

    def shared_call(self, module: str, class_name: str, input_name: str) -> NodeCall:
        """Returns the node of a class whose only input is this expression.

        The node is made on the first call and returned again on later
        ones.

        Args:
            module: The module of the node's generated class, relative to
                pyresonitelink.
            class_name: The node's class name, e.g. "Unpack_Float3".
            input_name: The member name of the node's input, e.g. "V".
        """
        call = self._shared_calls.get(class_name)
        if call is None:
            call = NodeCall({input_name: self}, module=module, class_name=class_name)
            self._shared_calls[class_name] = call
        return call


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


class ComponentOutputNode(ExprNode):
    """A value output from a multi-output ProtoFlux node.

    At build time, this references the component that produces the
    output. The ProtoFlux runtime selects the correct output by type.

    Attributes:
        output_name: The output member name (e.g. "HitPoint").
        component_tag: An opaque tag linking this node to its source
            component at build time.
    """

    def __init__(self, output_name: str, component_tag: str, expr_type: type) -> None:
        super().__init__(expr_type)
        self.output_name = output_name
        self.component_tag = component_tag


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


class CastNode(ExprNode):
    """A conversion of an expression to another type.

    At build time, this materializes into a ProtoFlux node such as
    Cast_int_To_float. Implicit conversions only widen, following C#.
    dergflux.math.convert creates the others.

    Attributes:
        expr: The expression node being converted.
    """

    def __init__(self, expr: ExprNode, target_type: type) -> None:
        super().__init__(target_type)
        self.expr = expr


class MemberAccessNode(ExprNode):
    """Accessing a property of a DateTime or TimeSpan expression.

    At build time, this materializes into a ProtoFlux node like
    DateTime_Hour or TimeSpan_TotalSeconds.

    Attributes:
        member_name: The property name (e.g. "hour", "total_seconds").
        expr: The expression node being accessed.
    """

    def __init__(
        self,
        member_name: str,
        expr: ExprNode,
        result_type: type,
    ) -> None:
        super().__init__(result_type)
        self.member_name = member_name
        self.expr = expr


class NodeCall:
    """One ProtoFlux node that computes values from its inputs.

    Several NodeOutputNodes can share one NodeCall, so that a node with
    more than one output, such as GlobalTransform, is added once and each
    output is read from that one node.

    The node is named either by a generated class or by a component type
    string. A type string serves for nodes whose generated class can't be
    parameterized, such as ObjectCast<I, O>.

    Attributes:
        module: The module of the generated class, relative to
            pyresonitelink, e.g. "protoflux.operators.vectors", or None if
            component_type is given.
        class_name: The generated class's name, e.g. "Dot_Float3".
        type_args: The types that a generic class is parameterized with,
            e.g. (primitives.Float,) for ReadDynamicValueVariable[Float].
        component_type: The assembly-qualified component type, used
            instead of module and class_name.
        inputs: The node's inputs, by Resonite member name, e.g. "A". Each
            is the expression node that the input reads.
    """

    def __init__(
        self,
        inputs: dict[str, ExprNode],
        *,
        module: str | None = None,
        class_name: str = "",
        type_args: tuple[type, ...] = (),
        component_type: str | None = None,
    ) -> None:
        self.inputs = inputs
        self.module = module
        self.class_name = class_name
        self.type_args = type_args
        self.component_type = component_type

    def describe(self) -> str:
        """Returns the node's name, for error messages."""
        return self.component_type or self.class_name


class NodeOutputNode(ExprNode):
    """An output of a ProtoFlux node that isn't an operator or a variable.

    Attributes:
        call: The node.
        output_name: The Resonite member name of the output, such as
            "GlobalPosition", or None if the node is its own output, as
            Dot_Float3 is.
    """

    def __init__(
        self, call: NodeCall, output_name: str | None, result_type: type,
    ) -> None:
        super().__init__(result_type)
        self.call = call
        self.output_name = output_name


class ElementRefNode(ExprNode):
    """A reference to a slot, a component, or another world element.

    At build time, this becomes a RefObjectInput<T> node whose Target is
    the element.

    Attributes:
        target_id: The element's ID.
        type_name: T, the assembly-qualified Resonite type of the
            reference, e.g. "[FrooxEngine]FrooxEngine.Slot".
    """

    def __init__(self, target_id: str, type_name: str, expr_type: type) -> None:
        super().__init__(expr_type)
        self.target_id = target_id
        self.type_name = type_name


class EnumConstNode(ExprNode):
    """A constant of an enum type, such as a keyboard Key.

    At build time, this becomes a ValueInput<E> node whose Value is the
    constant. Dergflux does no arithmetic or comparison on enums, so the
    constant only goes into the inputs of nodes that take one.

    Attributes:
        enum_type: E, the assembly-qualified Resonite name of the enum,
            e.g. "[Renderite.Shared]Renderite.Shared.Key".
        value: The member's name in Resonite, e.g. "Tab".
    """

    def __init__(self, enum_type: str, value: str, expr_type: type) -> None:
        super().__init__(expr_type)
        self.enum_type = enum_type
        self.value = value


def node_output(
    inputs: dict[str, Any],
    result_type: type,
    *,
    module: str | None = None,
    class_name: str = "",
    type_args: tuple[type, ...] = (),
    component_type: str | None = None,
    output_name: str | None = None,
) -> ExprProxy:
    """Returns an expression for the output of a new ProtoFlux node.

    Args:
        inputs: The node's inputs, by Resonite member name. Each is an
            expression or a literal.
        result_type: The output's type.
        module: See NodeCall.
        class_name: See NodeCall.
        type_args: See NodeCall.
        component_type: See NodeCall.
        output_name: The output's member name, or None if the node is its
            own output.

    Returns:
        The output, as an expression.
    """
    call = NodeCall(
        {name: _coerce(value)._node for name, value in inputs.items()},
        module=module, class_name=class_name, type_args=type_args,
        component_type=component_type,
    )
    return ExprProxy(NodeOutputNode(call, output_name, result_type))


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


def _type_literal(const: ConstNode, context_type: type | None) -> None:
    """Gives an untyped literal a type, from the other operand if it fits.

    An int literal next to a float takes the float type, since an int
    widens to a float. A float literal next to an int keeps its own type,
    Float, and the int is widened instead, so ``int_var + 2.5`` is a
    float rather than a truncated int.
    """
    from pyresonitelink.dergflux import _types

    if const._type is not None:
        return
    natural = _types.literal_type(const.value)
    if context_type is not None and (
        natural is None or _types.can_widen(natural, context_type)
    ):
        const._type = context_type
    else:
        const._type = natural


def implicit(value: Any, target_type: type, context: str) -> ExprProxy:
    """Converts a value to a type, widening it if needed.

    Args:
        value: An ExprProxy or a Python literal.
        target_type: The type the value is needed as.
        context: What the value is for, e.g. "assignment to x", for the
            error message.

    Returns:
        The value as an ExprProxy of target_type.

    Raises:
        TypeError: The conversion would narrow, e.g. from a float to an
            int, or there's no conversion between the types.
    """
    from pyresonitelink.dergflux import _types

    proxy = _coerce(value)
    node = proxy._node
    if isinstance(node, ConstNode) and node._type is None:
        _type_literal(node, target_type)
    if node._type is None or node._type == target_type:
        return proxy
    if _types.can_widen(node._type, target_type):
        return ExprProxy(CastNode(node, target_type))
    raise TypeError(
        f"{context}: {_types.type_name(node._type)} doesn't convert to "
        f"{_types.type_name(target_type)} implicitly. Convert it with "
        f"dergflux.math.convert(value, primitives."
        f"{_types.type_name(target_type)})."
    )


def explicit(value: Any, target_type: type) -> ExprProxy:
    """Converts a value to a type, narrowing it if needed.

    Args:
        value: An ExprProxy or a Python literal.
        target_type: The type to convert to.

    Returns:
        The value as an ExprProxy of target_type.
    """
    proxy = _coerce(value)
    node = proxy._node
    if isinstance(node, ConstNode) and node._type is None:
        node._type = target_type
        return proxy
    if node._type == target_type:
        return proxy
    return ExprProxy(CastNode(node, target_type))


def unify(
    left: ExprNode, right: ExprNode, context: str,
) -> tuple[ExprNode, ExprNode, type | None]:
    """Converts two operands to their common type.

    Args:
        left: The left operand.
        right: The right operand.
        context: What the operands are for, for the error message.

    Returns:
        The operands, each wrapped in a CastNode if it needed widening,
        and their common type.

    Raises:
        TypeError: The operands have no common type, e.g. a bool and an
            int.
    """
    from pyresonitelink.dergflux import _types

    if isinstance(right, ConstNode):
        _type_literal(right, left._type)
    if isinstance(left, ConstNode):
        _type_literal(left, right._type)
    if left._type is None or right._type is None or left._type == right._type:
        return left, right, left._type if left._type is not None else right._type
    common = _types.common_type(left._type, right._type)
    if common is None:
        raise TypeError(
            f"{context}: {_types.type_name(left._type)} and "
            f"{_types.type_name(right._type)} have no common type. Convert "
            f"one of them with dergflux.math.convert."
        )
    if left._type != common:
        left = CastNode(left, common)
    if right._type != common:
        right = CastNode(right, common)
    return left, right, common


def _binop(op: BinOp, left: ExprProxy, right: Any) -> ExprProxy:
    """Create a binary operation proxy.

    Operands of different numeric types are widened to their common type
    first. DateTime and TimeSpan have their own combinations: a DateTime
    plus or minus a TimeSpan is a DateTime, and the difference of two
    DateTimes is a TimeSpan.
    """
    right_proxy = _coerce(right)
    from pyresonitelink.data import primitives

    left_node = left._node
    right_node = right_proxy._node
    if isinstance(right_node, ConstNode):
        _type_literal(right_node, left_node._type)
    if isinstance(left_node, ConstNode):
        _type_literal(left_node, right_node._type)

    types = (left_node._type, right_node._type)
    if op == BinOp.ADD and types == (primitives.TimeSpan, primitives.DateTime):
        # Only DateTime + TimeSpan has a node, and addition commutes.
        left_node, right_node = right_node, left_node
        types = (primitives.DateTime, primitives.TimeSpan)
    if op in (BinOp.ADD, BinOp.SUB) and types == (
        primitives.DateTime, primitives.TimeSpan,
    ):
        return ExprProxy(
            BinaryOpNode(op, left_node, right_node, primitives.DateTime),
        )
    if op == BinOp.SUB and types == (primitives.DateTime, primitives.DateTime):
        return ExprProxy(
            BinaryOpNode(op, left_node, right_node, primitives.TimeSpan),
        )

    # Strings are joined by ConcatenateString. A number isn't converted to
    # a string implicitly, as it isn't in ProtoFlux.
    if op is BinOp.ADD and primitives.String in types:
        if types != (primitives.String, primitives.String):
            from pyresonitelink.dergflux import _types
            raise TypeError(
                f"A string can only be joined to a string, not "
                f"{_types.type_name(types[0] if types[1] is primitives.String else types[1])}. "
                "Convert the value with dergflux.strings.to_string."
            )
        return node_output(
            {"A": ExprProxy(left_node), "B": ExprProxy(right_node)}, primitives.String,
            module="protoflux.strings", class_name="ConcatenateString",
        )

    if op in (BinOp.MUL, BinOp.DIV):
        mixed = _mixed_product(op, left_node, right_node)
        if mixed is not None:
            return mixed

    result_type: type | None
    if op in (BinOp.LSHIFT, BinOp.RSHIFT):
        # The shift count is an int whatever the shifted value's type.
        result_type = left_node._type
    else:
        left_node, right_node, common = unify(
            left_node, right_node, f"The {op.value} operator",
        )
        result_type = primitives.Bool if op in _COMPARISON_OPS else common
    return ExprProxy(
        BinaryOpNode(op, left_node, right_node, result_type),
    )


def _mixed_product(
    op: BinOp, left: ExprNode, right: ExprNode,
) -> ExprProxy | None:
    """Multiplies or divides operands of different shapes.

    A vector times or divided by a number, and a number times or divided
    by a vector, use the typed nodes such as Mul_Float3_Float and
    Div_Float_Float3, which apply the number to each element. A rotation
    times a vector uses Mul_FloatQ_Float3 or Mul_DoubleQ_Double3, which
    rotates the vector. The number is widened to the vector's element
    type, or the vector to a vector of the number's type, as C# would.

    Returns:
        The product or quotient, or None if the operands aren't one of
        these pairs.

    Raises:
        TypeError: The number and the vector's elements have no common
            type.
    """
    from pyresonitelink.data import primitives
    from pyresonitelink.dergflux import _types

    rotations = {
        (primitives.FloatQ, primitives.Float3): primitives.Float3,
        (primitives.DoubleQ, primitives.Double3): primitives.Double3,
    }
    pair = (left._type, right._type)
    if op is BinOp.MUL and pair in rotations:
        return node_output(
            {"A": ExprProxy(left), "B": ExprProxy(right)}, rotations[pair],
            module="protoflux.operators",
            class_name=f"Mul_{_types.type_name(left._type)}_{_types.type_name(right._type)}",
        )

    if left._type in _types._VECTORS and right._type in _types._SCALARS:
        vector, scalar = left, right
    elif right._type in _types._VECTORS and left._type in _types._SCALARS:
        vector, scalar = right, left
    else:
        return None
    assert vector._type is not None and scalar._type is not None
    element, dim = _types._VECTORS[vector._type]
    common = _types.common_type(element, scalar._type)
    if common is None:
        raise TypeError(
            f"The {op.value} operator: {_types.type_name(vector._type)} and "
            f"{_types.type_name(scalar._type)} have no common type."
        )
    vector_type = _types._VECTOR_BY_PARTS[(common, dim)]
    if vector._type != vector_type:
        vector = CastNode(vector, vector_type)
    if scalar._type != common:
        # A literal is given the element type, so no Cast node is added.
        if isinstance(scalar, ConstNode):
            scalar._type = common
        else:
            scalar = CastNode(scalar, common)
    a, b = (vector, scalar) if left._type in _types._VECTORS else (scalar, vector)
    name = "Mul" if op is BinOp.MUL else "Div"
    return node_output(
        {"A": ExprProxy(a), "B": ExprProxy(b)}, vector_type,
        module="protoflux.operators",
        class_name=f"{name}_{_types.type_name(a._type)}_{_types.type_name(b._type)}",
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

    def __getattr__(self, name: str) -> ExprProxy:
        """Access properties for DateTime and TimeSpan expressions."""
        from pyresonitelink.data import primitives

        # Special internal attributes used by builder/serialization
        if name in ("id", "RESONITE_TYPE"):
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

        from pyresonitelink.dergflux import _types

        # A vector's elements come from one Unpack node, such as
        # Unpack_Float3, whose outputs are X, Y, and Z.
        if self._node._type in _types._VECTORS and name in ("x", "y", "z", "w"):
            element, dim = _types._VECTORS[self._node._type]
            if "xyzw".index(name) < dim:
                call = self._node.shared_call(
                    "protoflux.operators.packing",
                    f"Unpack_{_types.type_name(self._node._type)}",
                    "V",
                )
                return ExprProxy(NodeOutputNode(call, name.upper(), element))

        # The types are those of the ProtoFlux nodes, e.g. DateTimeTicks is
        # a DateTimeExtractor<long> and TimeSpanTotalDays a
        # TimeSpanExtractor<double>.
        if self._node._type == primitives.DateTime:
            int_props = {
                "year", "month", "day", "hour", "minute", "second",
                "millisecond", "day_of_year",
            }
            if name in int_props:
                return ExprProxy(MemberAccessNode(name, self._node, primitives.Int))
            if name == "ticks":
                return ExprProxy(MemberAccessNode(name, self._node, primitives.Long))
            if name == "day_of_week":
                raise AttributeError(
                    "day_of_week isn't supported, because the DateTimeDayOfWeek "
                    "node outputs a System.DayOfWeek enum, which Dergflux has "
                    "no type for."
                )

        if self._node._type == primitives.TimeSpan:
            int_props = {"days", "hours", "minutes", "seconds", "milliseconds"}
            float_props = {
                "total_days", "total_hours", "total_minutes",
                "total_seconds", "total_milliseconds",
            }
            if name in int_props:
                return ExprProxy(MemberAccessNode(name, self._node, primitives.Int))
            if name == "ticks":
                return ExprProxy(MemberAccessNode(name, self._node, primitives.Long))
            if name in float_props:
                return ExprProxy(MemberAccessNode(name, self._node, primitives.Double))

        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
