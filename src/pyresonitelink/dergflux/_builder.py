"""Builder: materializes a Dergflux Graph as ProtoFlux components.

Walks the recorded spaces, variable declarations, expression trees,
and flow contexts, creating the corresponding ProtoFlux components on
the Resonite server via the ResoniteLink client.
"""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING, Any

from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.dergflux import _expr
from pyresonitelink.dergflux import _flow
from pyresonitelink.dergflux import _space

if TYPE_CHECKING:
    from pyresonitelink.data import protocols
    from pyresonitelink.dergflux import _graph


# =========================================================================
# Generic binary operators (parameterized via [T])
# =========================================================================

# Maps BinOp -> class name in pyresonitelink.protoflux.operators.
_GENERIC_BINOP_NAMES: dict[_expr.BinOp, str] = {
    _expr.BinOp.ADD: "ValueAdd",
    _expr.BinOp.SUB: "ValueSub",
    _expr.BinOp.MUL: "ValueMul",
    _expr.BinOp.DIV: "ValueDiv",
    _expr.BinOp.MOD: "ValueMod",
    _expr.BinOp.LT: "ValueLessThan",
    _expr.BinOp.LE: "ValueLessOrEqual",
    _expr.BinOp.GT: "ValueGreaterThan",
    _expr.BinOp.GE: "ValueGreaterOrEqual",
    _expr.BinOp.EQ: "ValueEquals",
    _expr.BinOp.NE: "ValueNotEquals",
}

# Comparison ops parameterize on the operand type, not Bool result.
_COMPARISON_OPS = {
    _expr.BinOp.LT, _expr.BinOp.LE,
    _expr.BinOp.GT, _expr.BinOp.GE,
    _expr.BinOp.EQ, _expr.BinOp.NE,
}

# Generic unary operators (parameterized via [T]).
# Maps UnOp -> (class_name, param_name) in protoflux.operators.
_GENERIC_UNOP: dict[_expr.UnOp, tuple[str, str]] = {
    _expr.UnOp.NEG: ("ValueNegate", "n"),
}

# Generic math functions using Value* classes.
# Maps func_name -> (module, class_name, param_names).
_GENERIC_MATH: dict[str, tuple[str, str, list[str]]] = {
    "square": ("operators", "ValueSquare", ["n"]),
    "cube": ("operators", "ValueCube", ["n"]),
    "reciprocal": ("operators", "ValueReciprocal", ["n"]),
    "one_minus": ("operators", "ValueOneMinus", ["x"]),
    "min": ("math", "ValueMin", ["a", "b"]),
    "max": ("math", "ValueMax", ["a", "b"]),
    "clamp": ("math", "ValueClamp", ["value", "min", "max"]),
    "abs": ("math", "ValueAbs", ["n"]),
}


# =========================================================================
# Typed operator dispatch (non-generic, type-suffixed classes)
# =========================================================================

# Maps Python primitive type -> PascalCase suffix for typed node names.
_TYPE_SUFFIXES: dict[type, str] = {
    primitives.Bool: "Bool",
    primitives.Byte: "Byte",
    primitives.SByte: "Sbyte",
    primitives.Short: "Short",
    primitives.UShort: "Ushort",
    primitives.Int: "Int",
    primitives.UInt: "Uint",
    primitives.Long: "Long",
    primitives.ULong: "Ulong",
    primitives.Float: "Float",
    primitives.Double: "Double",
    primitives.Float2: "Float2",
    primitives.Float3: "Float3",
    primitives.Float4: "Float4",
    primitives.Double2: "Double2",
    primitives.Double3: "Double3",
    primitives.Double4: "Double4",
    primitives.Int2: "Int2",
    primitives.Int3: "Int3",
    primitives.Int4: "Int4",
    primitives.Long2: "Long2",
    primitives.Long3: "Long3",
    primitives.Long4: "Long4",
    primitives.Color: "Color",
    primitives.ColorX: "ColorX",
    primitives.Bool2: "Bool2",
    primitives.Bool3: "Bool3",
    primitives.Bool4: "Bool4",
}

# Maps (operation_key, import_subpath, class_prefix).
# The class name is "{prefix}_{suffix}" where suffix comes from _TYPE_SUFFIXES.
# For binary ops, params are (a, b). For unary, param is (a,).
_TYPED_BINARY_OPS: dict[_expr.BinOp, tuple[str, str]] = {
    _expr.BinOp.AND: ("operators.boolean", "AND"),
    _expr.BinOp.OR: ("operators.boolean", "OR"),
    _expr.BinOp.XOR: ("operators.boolean", "XOR"),
    _expr.BinOp.LSHIFT: ("operators.boolean", "ShiftLeft"),
    _expr.BinOp.RSHIFT: ("operators.boolean", "ShiftRight"),
}

_TYPED_UNARY_OPS: dict[_expr.UnOp, tuple[str, str]] = {
    _expr.UnOp.NOT: ("operators.boolean", "NOT"),
}

# Typed math functions: func_name -> (import_subpath, class_prefix, param_names).
_TYPED_MATH: dict[str, tuple[str, str, list[str]]] = {
    # Trigonometric
    "sin": ("math.trigonometry", "Sin", ["n"]),
    "cos": ("math.trigonometry", "Cos", ["n"]),
    "tan": ("math.trigonometry", "Tan", ["n"]),
    "asin": ("math.trigonometry", "Asin", ["n"]),
    "acos": ("math.trigonometry", "Acos", ["n"]),
    "atan": ("math.trigonometry", "Atan", ["n"]),
    "atan2": ("math.trigonometry", "Atan2", ["y", "x"]),
    # Exponential / logarithmic
    "exp": ("math", "Exp", ["n"]),
    "log": ("math", "Log", ["n"]),
    "log10": ("math", "Log10", ["n"]),
    "sqrt": ("math", "Sqrt", ["n"]),
    "pow": ("math", "Pow", ["n", "power"]),
    # Rounding
    "ceil": ("math", "Ceil", ["n"]),
    "floor": ("math", "Floor", ["n"]),
    "round": ("math", "Round", ["n"]),
    # Sign / value
    "sign": ("math", "Sign", ["n"]),
    "clamp01": ("math", "Clamp01", ["n"]),
    # Interpolation
    "smoothstep": ("math", "SmoothStep", ["edge0", "edge1", "x"]),
}

# Lerp variants: use generic ValueLerp etc. from protoflux.operators
# Actually these don't exist as generic Value* — check if they're in math
# Let me check... ValueLerp doesn't exist. We need typed Lerp nodes.
# But Lerp_Float etc are in math/interpolation or similar subdirs.
# For now, handle lerp/inverse_lerp as generic math if possible.

# Additional generic math that lives in protoflux.operators (not math):
_GENERIC_MATH_OPERATORS: dict[str, tuple[str, list[str]]] = {
    # ValueConditional is in operators
    "conditional": ("ValueConditional", ["on_true", "on_false", "condition"]),
}


def _get_typed_class(subpath: str, prefix: str, res_type: type) -> Any:
    """Import and return a typed ProtoFlux node class.

    Constructs the class name as ``{prefix}_{suffix}`` and imports from
    ``pyresonitelink.protoflux.{subpath}``.

    Args:
        subpath: The import subpath (e.g. "operators.boolean", "math.trigonometry").
        prefix: The class name prefix (e.g. "AND", "Sin").
        res_type: The Resonite primitive type.

    Returns:
        The class object.

    Raises:
        KeyError: If the type has no known suffix.
        AttributeError: If the class doesn't exist for this type.
    """
    suffix = _TYPE_SUFFIXES[res_type]
    class_name = f"{prefix}_{suffix}"
    module = importlib.import_module(f"pyresonitelink.protoflux.{subpath}")
    return getattr(module, class_name)


def _resolve_type(node: _expr.ExprNode) -> type:
    """Resolve the Resonite type of an expression node.

    Falls back to primitives.Float if no type is set.
    """
    if node._type is not None:
        return node._type
    return primitives.Float


def _operand_type(node: _expr.BinaryOpNode) -> type:
    """Resolve the operand type for parameterizing a binary operator.

    For comparison ops, the operator is parameterized on the *operand*
    type, not the result type (which is Bool).
    """
    if node.op in _COMPARISON_OPS:
        left_type = node.left._type
        if left_type is not None:
            return left_type
        right_type = node.right._type
        if right_type is not None:
            return right_type
        return primitives.Float
    return _resolve_type(node)


# =========================================================================
# Build context
# =========================================================================


class _BuildContext:
    """Holds state during a single build operation.

    Attributes:
        resolink: The connected client.
        slot: The target slot for all components.
        node_cache: Maps ExprNode id() to the component instance,
            so shared sub-expressions are materialized only once.
        var_inputs: Maps (space_id, var_name) to the ValueInput component
            that reads from that dynamic variable's value.
        slot_ref: The RefObjectInput<Slot> component (shared).
        path_nodes: Maps variable path strings to ValueObjectInput<String>.
        trigger_receiver: The DynamicImpulseReceiverWithValue component,
            if a typed trigger is in use.
    """

    def __init__(
        self,
        resolink: protocols.ResoniteLinkClient,
        slot: workers.Slot,
    ) -> None:
        self.resolink = resolink
        self.slot = slot
        self.node_cache: dict[int, Any] = {}
        self.var_inputs: dict[tuple[int, str], Any] = {}
        self.slot_ref: Any = None
        self.path_nodes: dict[str, Any] = {}
        self.trigger_receiver: Any = None

    async def ensure_slot_ref(self) -> Any:
        """Create the shared RefObjectInput<Slot> if needed."""
        if self.slot_ref is not None:
            return self.slot_ref

        from pyresonitelink.protoflux.core import RefObjectInput

        SlotRef = RefObjectInput[workers.Slot]
        ref = SlotRef(target=self.slot)
        await ref.add_to_slot(self.resolink, self.slot)
        self.slot_ref = ref
        return ref

    async def ensure_path_node(self, path: str) -> Any:
        """Create a ValueObjectInput<String> for a variable path."""
        if path in self.path_nodes:
            return self.path_nodes[path]

        from pyresonitelink.protoflux.core import ValueObjectInput

        StringInput = ValueObjectInput[primitives.String]
        node = StringInput(value=path)
        await node.add_to_slot(self.resolink, self.slot)
        self.path_nodes[path] = node
        return node

    async def materialize(self, node: _expr.ExprNode) -> Any:
        """Recursively materialize an ExprNode into ProtoFlux components.

        Returns the created component instance (which has an .id).
        Uses node_cache to avoid duplicating shared sub-expressions.
        """
        cache_key = id(node)
        if cache_key in self.node_cache:
            return self.node_cache[cache_key]

        result = await self._materialize_uncached(node)
        self.node_cache[cache_key] = result
        return result

    async def _materialize_uncached(self, node: _expr.ExprNode) -> Any:
        """Materialize a single node without caching."""
        if isinstance(node, _expr.ConstNode):
            return await self._materialize_const(node)
        if isinstance(node, _expr.VarReadNode):
            return await self._materialize_var_read(node)
        if isinstance(node, _expr.TriggerValueNode):
            return self._materialize_trigger_value(node)
        if isinstance(node, _expr.BinaryOpNode):
            return await self._materialize_binop(node)
        if isinstance(node, _expr.UnaryOpNode):
            return await self._materialize_unop(node)
        if isinstance(node, _expr.MathCallNode):
            return await self._materialize_math_call(node)
        raise TypeError(f"Unknown node type: {type(node).__name__}")

    def _materialize_trigger_value(self, node: _expr.TriggerValueNode) -> Any:
        """Return the trigger receiver component for a TriggerValueNode."""
        if self.trigger_receiver is None:
            raise RuntimeError(
                "TriggerValueNode used but no trigger receiver was created. "
                "This is a bug in the Dergflux builder."
            )
        return self.trigger_receiver

    async def _materialize_const(self, node: _expr.ConstNode) -> Any:
        """Materialize a constant as a ValueInput<T>."""
        from pyresonitelink.dergflux import _types
        from pyresonitelink.protoflux.core import ValueInput

        res_type = _types.resolve_const_type(node.value, node._type)
        ConcreteInput = ValueInput[res_type]  # type: ignore[valid-type]
        comp = ConcreteInput(value=res_type(node.value))
        await comp.add_to_slot(self.resolink, self.slot)
        return comp

    async def _materialize_var_read(self, node: _expr.VarReadNode) -> Any:
        """Materialize a variable read as ReadDynamicValueVariable."""
        key = (id(node.space), node.var_name)
        if key in self.var_inputs:
            return self.var_inputs[key]

        from pyresonitelink.protoflux.variables.dynamic import (
            ReadDynamicValueVariable,
        )

        res_type = _resolve_type(node)
        ConcreteRead = ReadDynamicValueVariable[res_type]  # type: ignore[valid-type]

        slot_ref = await self.ensure_slot_ref()
        space: _space.Space = node.space
        vars_dict: dict[str, _space.VarDecl] = object.__getattribute__(
            space, "_vars",
        )
        decl = vars_dict[node.var_name]
        path_node = await self.ensure_path_node(decl.path)

        comp = ConcreteRead(source=slot_ref.id, path=path_node.id)
        await comp.add_to_slot(self.resolink, self.slot)
        self.var_inputs[key] = comp
        return comp

    async def _materialize_binop(self, node: _expr.BinaryOpNode) -> Any:
        """Materialize a binary operation."""
        left_comp = await self.materialize(node.left)
        right_comp = await self.materialize(node.right)
        op_type = _operand_type(node)

        # Check if this is a typed binary op (bitwise/boolean/shift)
        if node.op in _TYPED_BINARY_OPS:
            subpath, prefix = _TYPED_BINARY_OPS[node.op]
            OpClass = _get_typed_class(subpath, prefix, op_type)
            if node.op in (_expr.BinOp.LSHIFT, _expr.BinOp.RSHIFT):
                comp = OpClass(a=left_comp.id, shift=right_comp.id)
            else:
                comp = OpClass(a=left_comp.id, b=right_comp.id)
            await comp.add_to_slot(self.resolink, self.slot)
            return comp

        # Check if this is pow (typed, not generic)
        if node.op is _expr.BinOp.POW:
            subpath, prefix, params = _TYPED_MATH["pow"]
            OpClass = _get_typed_class(subpath, prefix, op_type)
            comp = OpClass(n=left_comp.id, power=right_comp.id)
            await comp.add_to_slot(self.resolink, self.slot)
            return comp

        # Generic binary op
        name = _GENERIC_BINOP_NAMES[node.op]
        from pyresonitelink.protoflux import operators
        OpClass = getattr(operators, name)
        ConcreteOp = OpClass[op_type]
        comp = ConcreteOp(a=left_comp.id, b=right_comp.id)
        await comp.add_to_slot(self.resolink, self.slot)
        return comp

    async def _materialize_unop(self, node: _expr.UnaryOpNode) -> Any:
        """Materialize a unary operation."""
        operand_comp = await self.materialize(node.operand)
        res_type = _resolve_type(node)

        # Check if this is a typed unary op (NOT)
        if node.op in _TYPED_UNARY_OPS:
            subpath, prefix = _TYPED_UNARY_OPS[node.op]
            OpClass = _get_typed_class(subpath, prefix, res_type)
            comp = OpClass(a=operand_comp.id)
            await comp.add_to_slot(self.resolink, self.slot)
            return comp

        # ABS uses generic ValueAbs
        if node.op is _expr.UnOp.ABS:
            from pyresonitelink.protoflux.math import ValueAbs
            ConcreteOp = ValueAbs[res_type]  # type: ignore[valid-type]
            comp = ConcreteOp(n=operand_comp.id)
            await comp.add_to_slot(self.resolink, self.slot)
            return comp

        # NEG uses generic ValueNegate
        if node.op is _expr.UnOp.NEG:
            from pyresonitelink.protoflux import operators
            ConcreteOp = operators.ValueNegate[res_type]  # type: ignore[valid-type]
            comp = ConcreteOp(n=operand_comp.id)
            await comp.add_to_slot(self.resolink, self.slot)
            return comp

        raise TypeError(f"Unknown unary op: {node.op}")

    async def _materialize_math_call(self, node: _expr.MathCallNode) -> Any:
        """Materialize a math function call."""
        arg_comps = [await self.materialize(arg) for arg in node.args]
        res_type = _resolve_type(node)

        # Check for generic math functions first
        if node.func_name in _GENERIC_MATH:
            mod_name, class_name, param_names = _GENERIC_MATH[node.func_name]
            module = importlib.import_module(
                f"pyresonitelink.protoflux.{mod_name}",
            )
            GenericClass = getattr(module, class_name)
            ConcreteClass = GenericClass[res_type]  # type: ignore[valid-type]
            kwargs = dict(zip(param_names, [c.id for c in arg_comps]))
            comp = ConcreteClass(**kwargs)
            await comp.add_to_slot(self.resolink, self.slot)
            return comp

        # Check for generic math in operators
        if node.func_name in _GENERIC_MATH_OPERATORS:
            class_name, param_names = _GENERIC_MATH_OPERATORS[node.func_name]
            from pyresonitelink.protoflux import operators
            GenericClass = getattr(operators, class_name)
            ConcreteClass = GenericClass[res_type]  # type: ignore[valid-type]
            kwargs = dict(zip(param_names, [c.id for c in arg_comps]))
            comp = ConcreteClass(**kwargs)
            await comp.add_to_slot(self.resolink, self.slot)
            return comp

        # Typed math function
        if node.func_name in _TYPED_MATH:
            subpath, prefix, param_names = _TYPED_MATH[node.func_name]
            OpClass = _get_typed_class(subpath, prefix, res_type)
            kwargs = dict(zip(param_names, [c.id for c in arg_comps]))
            comp = OpClass(**kwargs)
            await comp.add_to_slot(self.resolink, self.slot)
            return comp

        raise TypeError(
            f"Unknown math function: {node.func_name}"
        )


# =========================================================================
# Space / variable building
# =========================================================================


async def _find_existing_space(
    resolink: protocols.ResoniteLinkClient,
    slot: workers.Slot,
    space_name: str | None,
) -> bool:
    """Check if a DynamicVariableSpace with the given name exists on the slot."""
    from pyresonitelink.components.data.dynamic import DynamicVariableSpace

    slot_data = await resolink.get_slot(slot=slot, depth=0)
    if slot_data.data is None:
        return False
    for comp in slot_data.data.components:
        if comp.componentType != DynamicVariableSpace.COMPONENT_TYPE:
            continue
        existing = DynamicVariableSpace(component=comp)
        existing_name = existing.space_name
        if space_name is None and not existing_name:
            return True
        if existing_name == space_name:
            return True
    return False


async def _is_slot_or_child(
    resolink: protocols.ResoniteLinkClient,
    parent: workers.Slot,
    candidate: workers.Slot,
) -> bool:
    """Check if candidate is equal to or a recursive child of parent."""
    if parent.id == candidate.id:
        return True
    current = candidate
    while True:
        slot_data = await resolink.get_slot(slot=current, depth=0)
        if slot_data.data is None or slot_data.data.parent is None:
            return False
        parent_id = slot_data.data.parent.target
        if parent_id is None:
            return False
        if parent_id == parent.id:
            return True
        current = workers.Slot(id=parent_id)


async def _find_existing_variable(
    resolink: protocols.ResoniteLinkClient,
    slot: workers.Slot,
    variable_name: str,
    component_type: str,
) -> bool:
    """Check if a DynamicValueVariable with the given name exists on a slot."""
    from pyresonitelink.components.data.dynamic import DynamicValueVariable

    slot_data = await resolink.get_slot(slot=slot, depth=0)
    if slot_data.data is None:
        return False
    for comp in slot_data.data.components:
        if comp.componentType != component_type:
            continue
        existing = DynamicValueVariable(component=comp)
        if existing.variable_name == variable_name:
            return True
    return False


async def _build_space(
    ctx: _BuildContext,
    space: _space.Space,
) -> None:
    """Create the DynamicVariableSpace and its variables on the server."""
    from pyresonitelink.components.data.dynamic import (
        DynamicValueVariable,
        DynamicVariableSpace,
    )

    slot: workers.Slot = object.__getattribute__(space, "_slot")
    space_name: str | None = object.__getattribute__(space, "_space_name")

    exists = await _find_existing_space(ctx.resolink, slot, space_name)
    if not exists:
        dyn_space = DynamicVariableSpace(space_name=space_name)
        await dyn_space.add_to_slot(ctx.resolink, slot)

    vars_dict: dict[str, _space.VarDecl] = object.__getattribute__(
        space, "_vars",
    )
    for decl in vars_dict.values():
        var_slot = decl.slot if decl.slot is not None else slot

        if decl.slot is not None:
            is_valid = await _is_slot_or_child(
                ctx.resolink, slot, decl.slot,
            )
            if not is_valid:
                raise ValueError(
                    f"Variable '{decl.path}' slot {decl.slot.id} is not "
                    f"equal to or a child of the space's slot {slot.id}."
                )

        ConcreteVar = DynamicValueVariable[decl.resonite_type]  # type: ignore[name-defined]

        var_exists = await _find_existing_variable(
            ctx.resolink, var_slot, decl.path, ConcreteVar.COMPONENT_TYPE,
        )
        if not var_exists:
            var_comp = ConcreteVar(variable_name=decl.path)
            await var_comp.add_to_slot(ctx.resolink, var_slot)


# =========================================================================
# Flow building
# =========================================================================


async def _build_if_context(
    ctx: _BuildContext,
    if_ctx: _flow.IfContext,
) -> Any:
    """Build a single IfContext into ProtoFlux flow nodes."""
    from pyresonitelink.protoflux.flow import If

    cond_comp = await ctx.materialize(if_ctx.condition._node)
    true_head = await _build_write_chain(ctx, if_ctx.true_writes)
    false_head = await _build_write_chain(ctx, if_ctx.false_writes)

    if_node = If(
        condition=cond_comp.id,
        on_true=true_head.id if true_head else None,
        on_false=false_head.id if false_head else None,
    )
    await if_node.add_to_slot(ctx.resolink, ctx.slot)
    return if_node


async def _build_write_chain(
    ctx: _BuildContext,
    writes: list[_flow.WriteRecord],
) -> Any | None:
    """Build a chain of WriteDynamicValueVariable nodes."""
    if not writes:
        return None

    from pyresonitelink.protoflux.variables.dynamic import (
        WriteDynamicValueVariable,
    )

    slot_ref = await ctx.ensure_slot_ref()
    components: list[Any] = []

    for write in writes:
        expr_comp = await ctx.materialize(write.expr._node)
        space: _space.Space = write.space
        vars_dict: dict[str, _space.VarDecl] = object.__getattribute__(
            space, "_vars",
        )
        decl = vars_dict[write.var_name]
        path_node = await ctx.ensure_path_node(decl.path)

        ConcreteWrite = WriteDynamicValueVariable[decl.resonite_type]  # type: ignore[name-defined]
        write_comp = ConcreteWrite(
            target=slot_ref.id,
            path=path_node.id,
            value=expr_comp.id,
        )
        await write_comp.add_to_slot(ctx.resolink, ctx.slot)
        components.append(write_comp)

    for i in range(len(components) - 1):
        components[i].on_success = components[i + 1].id
        await components[i].update(ctx.resolink)

    return components[0]


# =========================================================================
# Trigger building
# =========================================================================


async def _build_trigger(
    ctx: _BuildContext,
    if_node: Any,
    trigger: _flow.Trigger | None,
) -> None:
    """Create the trigger node that drives the impulse flow."""
    if trigger is None:
        from pyresonitelink.protoflux.flow import Update
        update = Update(on_update=if_node.id)
        await update.add_to_slot(ctx.resolink, ctx.slot)
        return

    from pyresonitelink.protoflux.core import ValueObjectInput
    StringInput = ValueObjectInput[primitives.String]
    tag_node = StringInput(value=trigger.tag)
    await tag_node.add_to_slot(ctx.resolink, ctx.slot)

    if trigger.value_type is None:
        from pyresonitelink.protoflux.flow import DynamicImpulseReceiver
        receiver = DynamicImpulseReceiver(
            tag=tag_node.id, on_triggered=if_node.id,
        )
        await receiver.add_to_slot(ctx.resolink, ctx.slot)
    else:
        from pyresonitelink.protoflux.flow import (
            DynamicImpulseReceiverWithValue,
        )
        ConcreteReceiver = DynamicImpulseReceiverWithValue[trigger.value_type]  # type: ignore[valid-type]
        receiver = ConcreteReceiver(
            tag=tag_node.id, on_triggered=if_node.id,
        )
        await receiver.add_to_slot(ctx.resolink, ctx.slot)
        ctx.trigger_receiver = receiver


# =========================================================================
# Top-level build
# =========================================================================


async def build_graph(
    graph: _graph.Graph,
    resolink: protocols.ResoniteLinkClient,
) -> None:
    """Materialize the entire Graph as ProtoFlux components."""
    # Build spaces and their variables
    for space in graph._spaces:
        space_slot: workers.Slot = object.__getattribute__(space, "_slot")
        ctx = _BuildContext(resolink, space_slot)
        await _build_space(ctx, space)

    # Build all completed flow contexts
    for if_ctx in graph._completed_flows:
        ctx = _BuildContext(resolink, if_ctx.slot)

        # For typed triggers, create receiver first so TriggerValueNode
        # can reference it during expression materialization.
        if if_ctx.trigger is not None and if_ctx.trigger.value_type is not None:
            from pyresonitelink.protoflux.core import ValueObjectInput
            from pyresonitelink.protoflux.flow import (
                DynamicImpulseReceiverWithValue,
            )

            StringInput = ValueObjectInput[primitives.String]
            tag_node = StringInput(value=if_ctx.trigger.tag)
            await tag_node.add_to_slot(ctx.resolink, ctx.slot)

            ConcreteReceiver = DynamicImpulseReceiverWithValue[if_ctx.trigger.value_type]  # type: ignore[valid-type]
            receiver = ConcreteReceiver(tag=tag_node.id)
            await receiver.add_to_slot(ctx.resolink, ctx.slot)
            ctx.trigger_receiver = receiver

            if_node = await _build_if_context(ctx, if_ctx)

            receiver.on_triggered = if_node.id
            await receiver.update(ctx.resolink)
        else:
            if_node = await _build_if_context(ctx, if_ctx)
            await _build_trigger(ctx, if_node, if_ctx.trigger)
