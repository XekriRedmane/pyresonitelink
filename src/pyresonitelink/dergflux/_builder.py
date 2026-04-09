"""Builder: materializes a Dergflux Graph as ProtoFlux components.

Walks the recorded spaces, variable declarations, expression trees,
and flow contexts, creating the corresponding ProtoFlux components on
the Resonite server via the ResoniteLink client.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.dergflux import _expr
from pyresonitelink.dergflux import _flow
from pyresonitelink.dergflux import _space

if TYPE_CHECKING:
    from pyresonitelink.data import protocols
    from pyresonitelink.dergflux import _graph


# Mapping from BinOp to (operator_module_attr, is_comparison).
# The operator classes live in pyresonitelink.protoflux.operators.
_BINOP_CLASS_NAMES: dict[_expr.BinOp, str] = {
    _expr.BinOp.ADD: "ValueAdd",
    _expr.BinOp.SUB: "ValueSub",
    _expr.BinOp.MUL: "ValueMul",
    _expr.BinOp.DIV: "ValueDiv",
    _expr.BinOp.MOD: "ValueMod",
    _expr.BinOp.LT: "ValueLessThan",
    _expr.BinOp.GT: "ValueGreaterThan",
    _expr.BinOp.EQ: "ValueEquals",
    _expr.BinOp.NE: "ValueNotEquals",
}

# BinOps where both operands use the left type (not the result type).
_COMPARISON_OPS = {
    _expr.BinOp.LT, _expr.BinOp.GT, _expr.BinOp.EQ, _expr.BinOp.NE,
}


def _get_operator_class(op: _expr.BinOp) -> Any:
    """Import and return the ProtoFlux operator class for a BinOp."""
    from pyresonitelink.protoflux import operators

    name = _BINOP_CLASS_NAMES[op]
    return getattr(operators, name)


def _resolve_type(node: _expr.ExprNode) -> type:
    """Resolve the Resonite type of an expression node.

    Falls back to primitives.Float if no type is set.
    """
    if node._type is not None:
        return node._type
    return primitives.Float


def _operand_type(node: _expr.BinaryOpNode) -> type:
    """Resolve the operand type for parameterizing a binary operator.

    For comparison ops (LT, GT, EQ, NE), the operator is parameterized
    on the *operand* type, not the result type (which is Bool).
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
        if isinstance(node, _expr.BinaryOpNode):
            return await self._materialize_binop(node)
        if isinstance(node, _expr.UnaryOpNode):
            return await self._materialize_unop(node)
        raise TypeError(f"Unknown node type: {type(node).__name__}")

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
        """Materialize a variable read.

        Creates a ReadDynamicValueVariable or reuses a ValueInput
        placeholder. For v1, we use a ValueInput that the engine
        will not auto-populate — instead, the DynamicValueVariable
        itself is read by the WriteDVV's target/path mechanism.

        Actually, dynamic variable reads in ProtoFlux don't use
        ValueInput at all. The WriteDynamicValueVariable reads and
        writes by path. For pure reads in expressions, we need a
        ReadDynamicValueVariable node.
        """
        key = (id(node.space), node.var_name)
        if key in self.var_inputs:
            return self.var_inputs[key]

        from pyresonitelink.protoflux.variables.dynamic import (
            ReadDynamicValueVariable,
        )

        res_type = _resolve_type(node)
        ConcreteRead = ReadDynamicValueVariable[res_type]  # type: ignore[valid-type]

        slot_ref = await self.ensure_slot_ref()
        # Look up the variable path from the space's declarations
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

        OpClass = _get_operator_class(node.op)
        op_type = _operand_type(node)
        ConcreteOp = OpClass[op_type]

        comp = ConcreteOp(a=left_comp.id, b=right_comp.id)
        await comp.add_to_slot(self.resolink, self.slot)
        return comp

    async def _materialize_unop(self, node: _expr.UnaryOpNode) -> Any:
        """Materialize a unary operation (negation)."""
        operand_comp = await self.materialize(node.operand)

        # Negation: 0 - operand
        from pyresonitelink.protoflux.core import ValueInput
        from pyresonitelink.protoflux import operators

        res_type = _resolve_type(node)
        zero = ValueInput[res_type](value=res_type(0))  # type: ignore[valid-type]
        await zero.add_to_slot(self.resolink, self.slot)

        ConcreteSub = operators.ValueSub[res_type]  # type: ignore[valid-type]
        comp = ConcreteSub(a=zero.id, b=operand_comp.id)
        await comp.add_to_slot(self.resolink, self.slot)
        return comp


async def _find_existing_space(
    resolink: protocols.ResoniteLinkClient,
    slot: workers.Slot,
    space_name: str | None,
) -> bool:
    """Check if a DynamicVariableSpace with the given name exists on the slot.

    Args:
        resolink: Connected client.
        slot: The slot to search.
        space_name: The space name to look for, or None for unnamed.

    Returns:
        True if a matching DynamicVariableSpace already exists.
    """
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


async def _build_space(
    ctx: _BuildContext,
    space: _space.Space,
) -> None:
    """Create the DynamicVariableSpace and its variables on the server.

    If a DynamicVariableSpace with the same name already exists on the
    slot, it is reused and no new space component is created.
    """
    from pyresonitelink.components.data.dynamic import (
        DynamicValueVariable,
        DynamicVariableSpace,
    )

    slot: workers.Slot = object.__getattribute__(space, "_slot")
    space_name: str | None = object.__getattribute__(space, "_space_name")

    # Only create if one with this name doesn't already exist
    exists = await _find_existing_space(ctx.resolink, slot, space_name)
    if not exists:
        dyn_space = DynamicVariableSpace(space_name=space_name)
        await dyn_space.add_to_slot(ctx.resolink, slot)

    # Create each declared variable
    vars_dict: dict[str, _space.VarDecl] = object.__getattribute__(
        space, "_vars",
    )
    for decl in vars_dict.values():
        ConcreteVar = DynamicValueVariable[decl.resonite_type]  # type: ignore[name-defined]
        var_comp = ConcreteVar(variable_name=decl.path)
        await var_comp.add_to_slot(ctx.resolink, slot)


async def _build_if_context(
    ctx: _BuildContext,
    if_ctx: _flow.IfContext,
) -> Any:
    """Build a single IfContext into ProtoFlux flow nodes.

    Returns the If component so it can be wired to an Update node.
    """
    from pyresonitelink.protoflux.flow import If
    from pyresonitelink.protoflux.variables.dynamic import (
        WriteDynamicValueVariable,
    )

    # Materialize the condition expression
    cond_comp = await ctx.materialize(if_ctx.condition._node)

    # Build true-branch write chain
    true_head = await _build_write_chain(ctx, if_ctx.true_writes)

    # Build false-branch write chain
    false_head = await _build_write_chain(ctx, if_ctx.false_writes)

    # Create the If node
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
    """Build a chain of WriteDynamicValueVariable nodes.

    Multiple writes are chained via on_success references.
    Returns the first write in the chain, or None if empty.
    """
    if not writes:
        return None

    from pyresonitelink.protoflux.variables.dynamic import (
        WriteDynamicValueVariable,
    )

    slot_ref = await ctx.ensure_slot_ref()
    components: list[Any] = []

    for write in writes:
        # Materialize the expression
        expr_comp = await ctx.materialize(write.expr._node)

        # Get variable path
        space: _space.Space = write.space
        vars_dict: dict[str, _space.VarDecl] = object.__getattribute__(
            space, "_vars",
        )
        decl = vars_dict[write.var_name]
        path_node = await ctx.ensure_path_node(decl.path)

        # Create the write node
        ConcreteWrite = WriteDynamicValueVariable[decl.resonite_type]  # type: ignore[name-defined]
        write_comp = ConcreteWrite(
            target=slot_ref.id,
            path=path_node.id,
            value=expr_comp.id,
        )
        await write_comp.add_to_slot(ctx.resolink, ctx.slot)
        components.append(write_comp)

    # Chain via on_success: first -> second -> third -> ...
    for i in range(len(components) - 1):
        components[i].on_success = components[i + 1].id
        await components[i].update(ctx.resolink)

    return components[0]


async def build_graph(
    graph: _graph.Graph,
    resolink: protocols.ResoniteLinkClient,
) -> None:
    """Materialize the entire Graph as ProtoFlux components.

    Args:
        graph: The recorded Dergflux graph.
        resolink: A connected ResoniteLink client.
    """
    from pyresonitelink.protoflux.flow import Update

    if not graph._spaces:
        return

    # Use the first space's slot as the target for ProtoFlux nodes.
    first_space = graph._spaces[0]
    slot: workers.Slot = object.__getattribute__(first_space, "_slot")
    ctx = _BuildContext(resolink, slot)

    # Build spaces and their variables
    for space in graph._spaces:
        await _build_space(ctx, space)

    # Build all completed flow contexts
    if_nodes: list[Any] = []
    for if_ctx in graph._completed_flows:
        if_node = await _build_if_context(ctx, if_ctx)
        if_nodes.append(if_node)

    # Create an Update node to drive the impulse flow.
    # If there are multiple If nodes, chain them: Update -> If1,
    # and we'd need Sequence nodes. For v1, support a single If.
    if if_nodes:
        update = Update(on_update=if_nodes[0].id)
        await update.add_to_slot(ctx.resolink, slot)
