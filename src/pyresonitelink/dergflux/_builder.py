"""Builder: materializes a Dergflux Graph as ProtoFlux components.

Walks the recorded spaces, variable declarations, expression trees,
and flow contexts, creating the corresponding ProtoFlux components on
the Resonite server via the ResoniteLink client.
"""

from __future__ import annotations

import asyncio
import importlib
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

_BUILD_DELAY = 0.1  # seconds between component creates (temporary)

from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.dergflux import _expr
from pyresonitelink.dergflux import _flow
from pyresonitelink.dergflux import _space

if TYPE_CHECKING:
    from pyresonitelink.data import protocols
    from pyresonitelink.dergflux import _graph


@dataclass
class _Tail:
    """An unwired output on a node, available for continuation wiring.

    Attributes:
        node: The ProtoFlux component.
        output_name: The reference member name to wire (e.g.
            ``"OnSuccess"``, ``"OnFalse"``).
    """

    node: Any
    output_name: str = "OnSuccess"


@dataclass
class FlowResult:
    """Result of building a flow context.

    Attributes:
        head: The first node (entry point for the impulse).
        tails: Unwired outputs available for chaining to the next
            statement.  For an If node with only a true branch,
            this includes the true branch's last OnSuccess AND the
            If node's OnFalse.
    """

    head: Any
    tails: list[_Tail] = field(default_factory=list)


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


async def _create_and_wire(
    resolink: protocols.ResoniteLinkClient,
    slot: workers.Slot,
    component_class: Any,
    references: dict[str, str],
) -> Any:
    """Create a component empty and wire references via update_references.

    This avoids ResoniteLink type compatibility issues that occur when
    reference members are set via constructor data in add_component.
    ProtoFlux nodes often fail constructor-based wiring because the
    server's type check is stricter than ProtoFlux's runtime system.

    Args:
        resolink: Connected client.
        slot: Slot to add the component to.
        component_class: The (possibly parameterized) component class.
        references: Mapping of member name to target component ID.

    Returns:
        The created component instance with server-assigned IDs.
    """
    comp = component_class()
    await comp.add_to_slot(resolink, slot)
    if references:
        resp = await resolink.update_references(
            componentId=comp.id,
            references=references,
        )
        if not resp.success:
            raise RuntimeError(
                f"Failed to wire {type(comp).__name__} "
                f"{comp.id}: {resp.errorInfo}"
            )
    return comp


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
        self.loop_node: Any = None
        self.component_outputs: dict[str, Any] = {}
        self.is_async: bool = False

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
        if isinstance(node, _expr.ComponentOutputNode):
            return self._materialize_component_output(node)
        if isinstance(node, _expr.LoopIndexNode):
            return self._materialize_loop_index(node)
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

    def _materialize_component_output(
        self, node: _expr.ComponentOutputNode,
    ) -> Any:
        """Return the component for a ComponentOutputNode.

        The component is registered in component_outputs by its tag
        before expressions are materialized.
        """
        comp = self.component_outputs.get(node.component_tag)
        if comp is None:
            raise RuntimeError(
                f"ComponentOutputNode '{node.output_name}' references "
                f"tag '{node.component_tag}' but no component was registered. "
                "This is a bug in the Dergflux builder."
            )
        return comp

    def _materialize_loop_index(self, node: _expr.LoopIndexNode) -> Any:
        """Return the For loop node for a LoopIndexNode.

        The For node's Iteration output provides the current index.
        The loop_node is set by ``_build_for_context`` before expressions
        are materialized.
        """
        if self.loop_node is None:
            raise RuntimeError(
                "LoopIndexNode used but no For loop node was created. "
                "This is a bug in the Dergflux builder."
            )
        return self.loop_node

    async def _materialize_const(self, node: _expr.ConstNode) -> Any:
        """Materialize a constant as a ValueInput<T> or ValueObjectInput<T>.

        String types use ValueObjectInput since Resonite treats strings
        as object types in ProtoFlux.
        """
        from pyresonitelink.dergflux import _types
        from pyresonitelink.protoflux.core import ValueInput, ValueObjectInput

        res_type = _types.resolve_const_type(node.value, node._type)
        # Strings are object types in ProtoFlux
        if res_type is str or res_type is primitives.String:
            ConcreteInput = ValueObjectInput[res_type]  # type: ignore[valid-type]
            comp = ConcreteInput(value=node.value)
        else:
            ConcreteInput = ValueInput[res_type]  # type: ignore[valid-type]
            comp = ConcreteInput(value=res_type(node.value))
        await comp.add_to_slot(self.resolink, self.slot)
        return comp

    async def _materialize_var_read(self, node: _expr.VarReadNode) -> Any:
        """Materialize a variable read.

        For model variables (DataModelValueFieldStore), returns the
        DMVFS component directly — it IS INodeValueOutput<T>.

        For dynamic variables (ReadDynamicValueVariable), returns a
        stub whose ``.id`` is the ``Value`` member ID, since other
        nodes must reference the output member, not the component.
        """
        key = (id(node.space), node.var_name)
        if key in self.var_inputs:
            return self.var_inputs[key]

        space: _space.Space = node.space
        vars_dict: dict[str, _space.VarDecl | _space.ModelVarDecl] = (
            object.__getattribute__(space, "_vars")
        )
        decl = vars_dict[node.var_name]

        # Model variables: DMVFS component is directly INodeValueOutput
        if isinstance(decl, _space.ModelVarDecl):
            built_vars: dict[str, Any] = object.__getattribute__(
                space, "_built_vars",
            )
            store = built_vars[node.var_name]
            self.var_inputs[key] = store
            return store

        # Dynamic variables: ReadDVV with member ID wiring
        from pyresonitelink.protoflux.variables.dynamic import (
            ReadDynamicObjectVariable,
            ReadDynamicValueVariable,
        )

        res_type = _resolve_type(node)
        full_path = _full_var_path(space, decl.path)

        slot_ref = await self.ensure_slot_ref()
        path_node = await self.ensure_path_node(full_path)

        if _is_protoflux_object_type(res_type):
            ConcreteRead = ReadDynamicObjectVariable[res_type]  # type: ignore[valid-type]
        else:
            ConcreteRead = ReadDynamicValueVariable[res_type]  # type: ignore[valid-type]

        comp = ConcreteRead()
        await comp.add_to_slot(self.resolink, self.slot)
        await self.resolink.update_references(
            componentId=comp.id,  # type: ignore[arg-type]
            references={
                "Source": slot_ref.id,  # type: ignore[arg-type]
                "Path": path_node.id,  # type: ignore[arg-type]
            },
        )

        value_member = comp.get_member("Value")
        assert value_member is not None, (
            f"ReadDynamicValueVariable {comp.id} has no Value member"
        )
        stub = type("_OutputStub", (), {"id": value_member.id})()
        self.var_inputs[key] = stub
        return stub

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
                refs = {"A": left_comp.id, "Shift": right_comp.id}
            else:
                refs = {"A": left_comp.id, "B": right_comp.id}
            return await _create_and_wire(self.resolink, self.slot, OpClass, refs)

        # Check if this is pow (typed, not generic)
        if node.op is _expr.BinOp.POW:
            subpath, prefix, params = _TYPED_MATH["pow"]
            OpClass = _get_typed_class(subpath, prefix, op_type)
            return await _create_and_wire(
                self.resolink, self.slot, OpClass,
                {"N": left_comp.id, "Power": right_comp.id},
            )

        # Generic binary op
        name = _GENERIC_BINOP_NAMES[node.op]
        from pyresonitelink.protoflux import operators
        OpClass = getattr(operators, name)
        ConcreteOp = OpClass[op_type]
        return await _create_and_wire(
            self.resolink, self.slot, ConcreteOp,
            {"A": left_comp.id, "B": right_comp.id},
        )

    async def _materialize_unop(self, node: _expr.UnaryOpNode) -> Any:
        """Materialize a unary operation."""
        operand_comp = await self.materialize(node.operand)
        res_type = _resolve_type(node)

        # Check if this is a typed unary op (NOT)
        if node.op in _TYPED_UNARY_OPS:
            subpath, prefix = _TYPED_UNARY_OPS[node.op]
            OpClass = _get_typed_class(subpath, prefix, res_type)
            return await _create_and_wire(
                self.resolink, self.slot, OpClass,
                {"A": operand_comp.id},
            )

        # ABS uses generic ValueAbs
        if node.op is _expr.UnOp.ABS:
            from pyresonitelink.protoflux.math import ValueAbs
            ConcreteOp = ValueAbs[res_type]  # type: ignore[valid-type]
            return await _create_and_wire(
                self.resolink, self.slot, ConcreteOp,
                {"N": operand_comp.id},
            )

        # NEG uses generic ValueNegate
        if node.op is _expr.UnOp.NEG:
            from pyresonitelink.protoflux import operators
            ConcreteOp = operators.ValueNegate[res_type]  # type: ignore[valid-type]
            return await _create_and_wire(
                self.resolink, self.slot, ConcreteOp,
                {"N": operand_comp.id},
            )

        raise TypeError(f"Unknown unary op: {node.op}")

    async def _materialize_math_call(self, node: _expr.MathCallNode) -> Any:
        """Materialize a math function call."""
        arg_comps = [await self.materialize(arg) for arg in node.args]
        res_type = _resolve_type(node)

        def _make_refs(
            param_names: list[str],
        ) -> dict[str, str]:
            """Build PascalCase reference dict from param names and arg comps."""
            return {
                # Convert snake_case param to PascalCase member name
                "".join(w.capitalize() for w in p.split("_")): c.id
                for p, c in zip(param_names, arg_comps)
            }

        # Check for generic math functions first
        if node.func_name in _GENERIC_MATH:
            mod_name, class_name, param_names = _GENERIC_MATH[node.func_name]
            module = importlib.import_module(
                f"pyresonitelink.protoflux.{mod_name}",
            )
            GenericClass = getattr(module, class_name)
            ConcreteClass = GenericClass[res_type]  # type: ignore[valid-type]
            return await _create_and_wire(
                self.resolink, self.slot, ConcreteClass,
                _make_refs(param_names),
            )

        # Check for generic math in operators
        if node.func_name in _GENERIC_MATH_OPERATORS:
            class_name, param_names = _GENERIC_MATH_OPERATORS[node.func_name]
            from pyresonitelink.protoflux import operators
            GenericClass = getattr(operators, class_name)
            ConcreteClass = GenericClass[res_type]  # type: ignore[valid-type]
            return await _create_and_wire(
                self.resolink, self.slot, ConcreteClass,
                _make_refs(param_names),
            )

        # Typed math function
        if node.func_name in _TYPED_MATH:
            subpath, prefix, param_names = _TYPED_MATH[node.func_name]
            OpClass = _get_typed_class(subpath, prefix, res_type)
            return await _create_and_wire(
                self.resolink, self.slot, OpClass,
                _make_refs(param_names),
            )

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


async def _find_existing_variable_component(
    resolink: protocols.ResoniteLinkClient,
    slot: workers.Slot,
    variable_name: str,
    component_type: str,
) -> Any | None:
    """Find a DynamicValueVariable with the given name on a slot.

    Returns the component instance if found, or None.
    """
    from pyresonitelink.components.data.dynamic import DynamicValueVariable

    slot_data = await resolink.get_slot(slot=slot, depth=0)
    if slot_data.data is None:
        return None
    for comp in slot_data.data.components:
        if comp.componentType != component_type:
            continue
        # Refresh to get full member data
        get_resp = await resolink.get_component(componentId=comp.id)
        if get_resp.data is None:
            continue
        existing = DynamicValueVariable(component=get_resp.data)
        if existing.variable_name == variable_name:
            return existing
    return None


def _full_var_path(space: _space.Space, var_path: str) -> str:
    """Prefix a variable path with the space name if set.

    Resonite dynamic variables require the format ``SpaceName/VarName``
    when the DynamicVariableSpace has a ``SpaceName``.
    """
    space_name: str | None = object.__getattribute__(space, "_space_name")
    if space_name:
        return f"{space_name}/{var_path}"
    return var_path


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

    vars_dict: dict[str, _space.VarDecl | _space.ModelVarDecl] = (
        object.__getattribute__(space, "_vars")
    )
    built_vars: dict[str, Any] = object.__getattribute__(
        space, "_built_vars",
    )
    has_dynvars = any(
        isinstance(d, _space.VarDecl) for d in vars_dict.values()
    )

    # Only create DynamicVariableSpace if there are dynamic variables
    if has_dynvars:
        exists = await _find_existing_space(ctx.resolink, slot, space_name)
        if not exists:
            dyn_space = DynamicVariableSpace(
                space_name=space_name,
                only_direct_binding=bool(space_name),
            )
            await dyn_space.add_to_slot(ctx.resolink, slot)
            await asyncio.sleep(_BUILD_DELAY)

    from pyresonitelink.protoflux.variables import DataModelValueFieldStore

    for attr_name, decl in vars_dict.items():
        if isinstance(decl, _space.ModelVarDecl):
            await _build_model_var(
                ctx, space, slot, attr_name, decl, built_vars,
            )
        else:
            await _build_dynvar(
                ctx, space, slot, attr_name, decl, built_vars,
                DynamicValueVariable,
            )


async def _build_dynvar(
    ctx: _BuildContext,
    space: _space.Space,
    space_slot: workers.Slot,
    attr_name: str,
    decl: _space.VarDecl,
    built_vars: dict[str, Any],
    DynamicValueVariable: Any,
) -> None:
    """Build a single dynamic variable."""
    var_slot = decl.slot if decl.slot is not None else space_slot

    if decl.slot is not None:
        is_valid = await _is_slot_or_child(
            ctx.resolink, space_slot, decl.slot,
        )
        if not is_valid:
            raise ValueError(
                f"Variable '{decl.path}' slot {decl.slot.id} is not "
                f"equal to or a child of the space's slot "
                f"{space_slot.id}."
            )

    ConcreteVar = DynamicValueVariable[decl.resonite_type]  # type: ignore[name-defined]
    full_path = _full_var_path(space, decl.path)

    existing_comp = await _find_existing_variable_component(
        ctx.resolink, var_slot, full_path, ConcreteVar.COMPONENT_TYPE,
    )
    if existing_comp is not None:
        built_vars[attr_name] = existing_comp
    else:
        var_comp = ConcreteVar(
            variable_name=full_path,
            value=decl.initial_value,
        )
        await var_comp.add_to_slot(ctx.resolink, var_slot)
        await asyncio.sleep(_BUILD_DELAY)
        built_vars[attr_name] = var_comp


async def _build_model_var(
    ctx: _BuildContext,
    space: _space.Space,
    space_slot: workers.Slot,
    attr_name: str,
    decl: _space.ModelVarDecl,
    built_vars: dict[str, Any],
) -> None:
    """Build a model variable (DataModelValueFieldStore on a named slot).

    Creates a child slot named after the variable, adds DMVFS<T>,
    and sets the initial value on the auto-generated +Store companion.
    """
    from pyresonitelink.protoflux.variables import DataModelValueFieldStore
    from pyresonitelink.data import messages

    # Create named child slot
    var_slot = await ctx.resolink.add_slot(
        parent=space_slot, name=decl.path,
    )

    # Create DMVFS
    ConcreteStore = DataModelValueFieldStore[decl.resonite_type]  # type: ignore[name-defined]
    store = ConcreteStore()
    await store.add_to_slot(ctx.resolink, var_slot)

    # Set initial value on the +Store companion if provided
    if decl.initial_value is not None:
        slot_resp: Any = await ctx.resolink.request_json(
            messages.GetSlot(slotId=var_slot.id, depth=0),
        )
        for comp in slot_resp.get("data", {}).get("components", []):
            ct: str = comp.get("componentType", "")
            if "+Store" not in ct:
                continue
            comp_resp: Any = await ctx.resolink.request_json(
                messages.GetComponent(componentId=comp["id"]),
            )
            comp_data: Any = comp_resp.get("data") or {}
            val_info: Any = (comp_data.get("members") or {}).get("Value")
            if val_info is None:
                break
            # Build a minimal update with just the Value field
            from pyresonitelink.generated import _type_map
            type_info = _type_map.from_python_type(decl.resonite_type)
            update_member = type_info.field_class(
                value=decl.initial_value,
            )
            update_member.id = val_info["id"]
            await ctx.resolink.update_component(
                data=workers.Component(
                    id=comp["id"],
                    componentType=ct,
                    members={"Value": update_member},
                ),
            )
            break

    built_vars[attr_name] = store


# =========================================================================
# Flow building
# =========================================================================


async def _build_if_context(
    ctx: _BuildContext,
    if_ctx: _flow.IfContext,
) -> FlowResult:
    """Build a single IfContext into ProtoFlux flow nodes.

    Returns a FlowResult whose tails are the last nodes of each
    branch, so the caller can wire continuations to them.
    """
    from pyresonitelink.protoflux.flow import If

    cond_comp = await ctx.materialize(if_ctx.condition._node)
    true_result = await _build_stmt_chain(ctx, if_ctx.true_stmts)
    false_result = await _build_stmt_chain(ctx, if_ctx.false_stmts)

    if_node = If(
        condition=cond_comp.id,
        on_true=true_result.head.id if true_result else None,
        on_false=false_result.head.id if false_result else None,
    )
    await if_node.add_to_slot(ctx.resolink, ctx.slot)

    # Tails: collect from both branches for continuation wiring
    # Collect tails from both branches for continuation wiring.
    # When a branch is missing, the If node's empty output is a tail
    # so that the continuation gets wired to it.
    tails: list[_Tail] = []
    if true_result:
        tails.extend(true_result.tails)
    else:
        tails.append(_Tail(if_node, "OnTrue"))
    if false_result:
        tails.extend(false_result.tails)
    else:
        tails.append(_Tail(if_node, "OnFalse"))

    return FlowResult(head=if_node, tails=tails)


async def _build_for_context(
    ctx: _BuildContext,
    for_ctx: _flow.ForContext,
) -> Any:
    """Build a ForContext into a ProtoFlux For or AsyncFor node.

    Uses AsyncFor when ctx.is_async is set. The node is created first
    (so LoopIndexNode can reference it), then statement chains are
    built and wired to loop_start/loop_iteration.
    """
    # Materialize count expression
    count_comp = await ctx.materialize(for_ctx.count._node)

    # Materialize reverse if present
    reverse_comp = None
    if for_ctx.reverse is not None:
        reverse_comp = await ctx.materialize(for_ctx.reverse._node)

    # Select sync or async variant
    if ctx.is_async:
        _async_flow = importlib.import_module(
            "pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async",
        )
        ForClass = _async_flow.AsyncFor
    else:
        from pyresonitelink.protoflux.flow import For as ForClass

    for_node = ForClass(
        count=count_comp.id,
        reverse=reverse_comp.id if reverse_comp else None,
    )
    await for_node.add_to_slot(ctx.resolink, ctx.slot)

    # Set loop_node so LoopIndexNode materialization can find it
    ctx.loop_node = for_node

    # Build start writes (loop_start)
    start_result = await _build_stmt_chain(ctx, for_ctx.start_stmts)

    # Build iteration writes (loop_iteration)
    iter_result = await _build_stmt_chain(ctx, for_ctx.iteration_stmts)

    # Wire to the For node
    refs: dict[str, str] = {}
    if start_result is not None:
        refs["LoopStart"] = start_result.head.id
    if iter_result is not None:
        refs["LoopIteration"] = iter_result.head.id
    if refs:
        await ctx.resolink.update_references(
            componentId=for_node.id,
            references=refs,
        )

    return for_node


async def _build_range_context(
    ctx: _BuildContext,
    range_ctx: _flow.RangeContext,
) -> Any:
    """Build a RangeContext into a ProtoFlux RangeLoopInt or AsyncRangeLoopInt."""
    start_comp = await ctx.materialize(range_ctx.start._node)
    end_comp = await ctx.materialize(range_ctx.end._node)
    step_comp = None
    if range_ctx.step is not None:
        step_comp = await ctx.materialize(range_ctx.step._node)

    if ctx.is_async:
        _async_flow = importlib.import_module(
            "pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async",
        )
        RangeClass = _async_flow.AsyncRangeLoopInt
    else:
        from pyresonitelink.protoflux.flow import RangeLoopInt as RangeClass

    range_node = RangeClass(
        start=start_comp.id,
        end=end_comp.id,
        step_size=step_comp.id if step_comp else None,
    )
    await range_node.add_to_slot(ctx.resolink, ctx.slot)

    # Set loop_node so LoopIndexNode materialization can find it
    ctx.loop_node = range_node

    start_result = await _build_stmt_chain(ctx, range_ctx.start_stmts)
    iter_result = await _build_stmt_chain(ctx, range_ctx.iteration_stmts)

    refs: dict[str, str] = {}
    if start_result is not None:
        refs["LoopStart"] = start_result.head.id
    if iter_result is not None:
        refs["LoopIteration"] = iter_result.head.id
    if refs:
        await ctx.resolink.update_references(
            componentId=range_node.id,
            references=refs,
        )

    return range_node


async def _build_while_context(
    ctx: _BuildContext,
    while_ctx: _flow.WhileContext,
) -> Any:
    """Build a WhileContext into a ProtoFlux While or AsyncWhile node."""
    # Materialize condition expression
    cond_comp = await ctx.materialize(while_ctx.condition._node)

    # Build the statement chain for the loop body
    body_result = await _build_stmt_chain(ctx, while_ctx.stmts)

    if ctx.is_async:
        _async_flow = importlib.import_module(
            "pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async",
        )
        WhileClass = _async_flow.AsyncWhile
    else:
        from pyresonitelink.protoflux.flow import While as WhileClass

    while_node = WhileClass()
    await while_node.add_to_slot(ctx.resolink, ctx.slot)
    refs: dict[str, str] = {"Condition": cond_comp.id}
    if body_result is not None:
        refs["LoopIteration"] = body_result.head.id
    await ctx.resolink.update_references(
        componentId=while_node.id,
        references=refs,
    )
    return while_node


async def _build_write_node(
    ctx: _BuildContext,
    stmt: _flow.WriteRecord,
) -> tuple[Any, str]:
    """Build a write node for a WriteRecord.

    For model variables: uses ValueWrite<FrooxEngineContext, T>.
    For dynamic variables: uses WriteDynamicValueVariable<T>.

    Returns:
        A tuple of (component, tail_output_name) where the output name
        is ``"OnWritten"`` for model writes or ``"OnSuccess"`` for
        dynamic variable writes.
    """
    expr_comp = await ctx.materialize(stmt.expr._node)
    space: _space.Space = stmt.space
    vars_dict: dict[str, _space.VarDecl | _space.ModelVarDecl] = (
        object.__getattribute__(space, "_vars")
    )
    decl = vars_dict[stmt.var_name]

    if isinstance(decl, _space.ModelVarDecl):
        comp = await _build_model_write_node(
            ctx, space, decl, expr_comp,
        )
        return comp, "OnWritten"
    comp = await _build_dynvar_write_node(
        ctx, space, decl, expr_comp,
    )
    return comp, "OnSuccess"


async def _build_model_write_node(
    ctx: _BuildContext,
    space: _space.Space,
    decl: _space.ModelVarDecl,
    expr_comp: Any,
) -> Any:
    """Build a ValueWrite<FrooxEngineContext, T> for a model variable."""
    from pyresonitelink.generated import _type_map

    built_vars: dict[str, Any] = object.__getattribute__(
        space, "_built_vars",
    )
    # Find the DMVFS component for this variable
    store = None
    for attr_name, d in object.__getattribute__(space, "_vars").items():
        if d is decl:
            store = built_vars[attr_name]
            break
    assert store is not None, f"Model variable '{decl.path}' not built"

    # Construct ValueWrite<FrooxEngineContext, T> component type
    type_info = _type_map.from_python_type(decl.resonite_type)
    wire_type = type_info.resonite_name
    vw_type = (
        "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution"
        ".Nodes.ValueWrite<[FrooxEngine]FrooxEngine.ProtoFlux"
        f".FrooxEngineContext,{wire_type}>"
    )

    resp = await ctx.resolink.add_component(
        containerSlotId=ctx.slot, componentType=vw_type,
    )
    assert resp.entityId is not None, (
        f"Failed to create {vw_type}: {resp.errorInfo}"
    )
    write_id = resp.entityId

    wire_resp = await ctx.resolink.update_references(
        componentId=write_id,
        references={"Variable": store.id, "Value": expr_comp.id},
    )
    if not wire_resp.success:
        raise RuntimeError(
            f"Failed to wire ValueWrite {write_id}: {wire_resp.errorInfo}"
        )

    # Return a stub with the component ID and a compatible interface
    # for OnWritten chaining (the tail output name)
    get_resp = await ctx.resolink.get_component(componentId=write_id)
    assert get_resp.data is not None
    return get_resp.data


async def _build_dynvar_write_node(
    ctx: _BuildContext,
    space: _space.Space,
    decl: _space.VarDecl,
    expr_comp: Any,
) -> Any:
    """Build a WriteDynamicValueVariable<T> for a dynamic variable."""
    from pyresonitelink.protoflux.variables.dynamic import (
        WriteDynamicObjectVariable,
        WriteDynamicValueVariable,
    )

    slot_ref = await ctx.ensure_slot_ref()
    full_path = _full_var_path(space, decl.path)
    path_node = await ctx.ensure_path_node(full_path)

    if _is_protoflux_object_type(decl.resonite_type):
        ConcreteWrite = WriteDynamicObjectVariable[decl.resonite_type]  # type: ignore[name-defined]
    else:
        ConcreteWrite = WriteDynamicValueVariable[decl.resonite_type]  # type: ignore[name-defined]

    write_comp = ConcreteWrite()
    await write_comp.add_to_slot(ctx.resolink, ctx.slot)
    refs = {
        "Target": slot_ref.id,  # type: ignore[arg-type]
        "Path": path_node.id,  # type: ignore[arg-type]
        "Value": expr_comp.id,
    }
    resp = await ctx.resolink.update_references(
        componentId=write_comp.id,  # type: ignore[arg-type]
        references=refs,
    )
    if not resp.success:
        raise RuntimeError(
            f"Failed to wire WriteDynamicVariable "
            f"{write_comp.id}: {resp.errorInfo}"
        )
    return write_comp


async def _wire_tails_to_head(
    ctx: _BuildContext,
    tails: list[_Tail],
    head: Any,
) -> None:
    """Wire each tail's output to a head node."""
    for tail in tails:
        await ctx.resolink.update_references(
            componentId=tail.node.id,
            references={tail.output_name: head.id},
        )


async def _build_stmt_chain(
    ctx: _BuildContext,
    stmts: list[_flow.Statement],
) -> FlowResult | None:
    """Build a chain of statements (writes and nested flow contexts).

    Each statement becomes a ProtoFlux node.  Multiple statements are
    chained by wiring each result's tails to the next result's head.
    Returns a FlowResult with the first head and the last tails, or
    None if empty.
    """
    if not stmts:
        return None

    results: list[FlowResult] = []

    for stmt in stmts:
        if isinstance(stmt, _flow.WriteRecord):
            write_comp, tail_name = await _build_write_node(ctx, stmt)
            results.append(FlowResult(
                head=write_comp, tails=[_Tail(write_comp, tail_name)],
            ))
        elif isinstance(stmt, _flow.FlowContext):
            result = await _build_flow_context(ctx, stmt)
            if result is not None:
                results.append(result)

    if not results:
        return None

    # Chain: wire each result's tails to the next result's head
    for i in range(len(results) - 1):
        await _wire_tails_to_head(ctx, results[i].tails, results[i + 1].head)

    return FlowResult(head=results[0].head, tails=results[-1].tails)


# =========================================================================
# Trigger building
# =========================================================================


async def _create_start_async_task(
    ctx: _BuildContext,
    async_entry: Any,
) -> Any:
    """Create a StartAsyncTask that bridges sync -> async.

    Returns the StartAsyncTask component (which is ISyncNodeOperation
    and can be wired from sync triggers).
    """
    _async_mod = importlib.import_module(
        "pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async",
    )
    start_async = _async_mod.StartAsyncTask()
    await start_async.add_to_slot(ctx.resolink, ctx.slot)
    await ctx.resolink.update_references(
        componentId=start_async.id,  # type: ignore[arg-type]
        references={"TaskStart": async_entry.id},
    )
    return start_async


async def _build_trigger(
    ctx: _BuildContext,
    entry_node: Any,
    trigger: _flow.Trigger | None,
) -> None:
    """Create the trigger node that drives the impulse flow.

    Always uses sync triggers and receivers. For async flows, a
    StartAsyncTask node bridges from the sync receiver to the async
    entry node. This ensures normal sync DynamicImpulseTrigger nodes
    can fire the flow.
    """
    # If async, insert StartAsyncTask bridge so sync triggers work
    target = entry_node
    if ctx.is_async:
        target = await _create_start_async_task(ctx, entry_node)

    if trigger is None:
        from pyresonitelink.protoflux.flow import Update
        update = Update(on_update=target.id)
        await update.add_to_slot(ctx.resolink, ctx.slot)
        return

    # DynamicImpulseReceiver.Tag expects IGlobalValueProxy<string>,
    # so we use GlobalValue<string>.
    from pyresonitelink.generated.protoflux import global_value
    StringGlobal = global_value.GlobalValue[primitives.String]
    tag_node = StringGlobal()
    await tag_node.add_to_slot(ctx.resolink, ctx.slot)
    tag_node.value = trigger.tag
    await tag_node.update(ctx.resolink)

    if trigger.value_type is None:
        from pyresonitelink.protoflux.flow import DynamicImpulseReceiver
        receiver = DynamicImpulseReceiver()
        await receiver.add_to_slot(ctx.resolink, ctx.slot)
        await ctx.resolink.update_references(
            componentId=receiver.id,  # type: ignore[arg-type]
            references={"Tag": tag_node.id, "OnTriggered": target.id},
        )
    else:
        from pyresonitelink.protoflux.flow import DynamicImpulseReceiverWithValue
        ConcreteReceiver = DynamicImpulseReceiverWithValue[trigger.value_type]  # type: ignore[valid-type]
        receiver = ConcreteReceiver()
        await receiver.add_to_slot(ctx.resolink, ctx.slot)
        await ctx.resolink.update_references(
            componentId=receiver.id,  # type: ignore[arg-type]
            references={"Tag": tag_node.id, "OnTriggered": target.id},
        )
        ctx.trigger_receiver = receiver


# =========================================================================
# Binding building
# =========================================================================


# ProtoFlux object types use ValueObjectInput, WriteDynamicObjectVariable,
# ReadDynamicObjectVariable, etc. instead of the Value* variants.
_PROTOFLUX_OBJECT_TYPES: set[type] = {str, primitives.String}


def _is_protoflux_object_type(res_type: type) -> bool:
    """Check if a type uses ProtoFlux Object variants (not Value variants)."""
    if res_type in _PROTOFLUX_OBJECT_TYPES:
        return True
    return _is_reference_type(res_type)


def _is_reference_type(res_type: type) -> bool:
    """Check if a Resonite type is a reference type (not a value type).

    Reference types (Slot, Component, etc.) have no field_class in the
    type map.  Value types (int, float, Float3, etc.) have one.
    """
    from pyresonitelink.generated import _type_map

    try:
        info = _type_map.from_python_type(res_type)
        return info.field_class is None
    except KeyError:
        # Unknown type — assume reference
        return True


async def _build_bindings(
    graph: _graph.Graph,
    resolink: protocols.ResoniteLinkClient,
) -> None:
    """Build all recorded bindings.

    Dispatches between three driver types:
    - DynamicValueVariableDriver<T> for dynvar -> value field
    - DynamicReferenceVariableDriver<T> for dynvar -> reference field
    - ValueFieldDrive<T> for general expression -> field
    """
    for bind_rec in graph._bindings:
        member = bind_rec.component.get_member(bind_rec.member_name)
        assert member is not None
        res_type = _resolve_type(bind_rec.expr._node)

        if bind_rec.dynvar_name is not None:
            # Source is a dynamic variable — use a driver component
            await _build_dynvar_binding(
                resolink, bind_rec, member, res_type,
            )
        else:
            # Source is a general expression — use ValueFieldDrive
            await _build_expr_binding(
                resolink, bind_rec, member, res_type,
            )


async def _build_dynvar_binding(
    resolink: protocols.ResoniteLinkClient,
    bind_rec: _flow.BindRecord,
    member: Any,
    res_type: type,
) -> None:
    """Build a binding from a dynamic variable to a component field.

    Uses DynamicValueVariableDriver<T> for value types or
    DynamicReferenceVariableDriver<T> for reference types.
    """
    # Look up the variable path from the space's declarations
    space = bind_rec.dynvar_space
    vars_dict: dict[str, _space.VarDecl] = object.__getattribute__(
        space, "_vars",
    )
    decl = vars_dict[bind_rec.dynvar_name]  # type: ignore[index]
    full_path = _full_var_path(space, decl.path)

    if _is_reference_type(res_type):
        from pyresonitelink.components.data.dynamic import (
            DynamicReferenceVariableDriver,
        )
        ConcreteDriver = DynamicReferenceVariableDriver[res_type]  # type: ignore[valid-type]
        driver = ConcreteDriver(
            variable_name=full_path,
            target=member.id,
        )
    else:
        from pyresonitelink.components.data.dynamic import (
            DynamicValueVariableDriver,
        )
        ConcreteDriver = DynamicValueVariableDriver[res_type]  # type: ignore[valid-type]
        driver = ConcreteDriver(
            variable_name=full_path,
            target=member.id,
        )

    await driver.add_to_slot(resolink, bind_rec.slot)


async def _build_expr_binding(
    resolink: protocols.ResoniteLinkClient,
    bind_rec: _flow.BindRecord,
    member: Any,
    res_type: type,
) -> None:
    """Build a binding from a ProtoFlux expression to a component field."""
    ctx = _BuildContext(resolink, bind_rec.slot)
    await _build_expr_binding_with_ctx(ctx, bind_rec, member, res_type)


async def _build_expr_binding_with_ctx(
    ctx: _BuildContext,
    bind_rec: _flow.BindRecord,
    member: Any,
    res_type: type,
) -> None:
    """Build a binding using a specific build context.

    Uses ValueFieldDrive<T>.  The ctx may carry loop_node and other
    state from flow building, allowing bindings to reference loop
    indices and other flow-scoped values.

    Creates the drive without references in the constructor, then
    wires Value and _value via update_references to avoid ResoniteLink
    type compatibility issues with ProtoFlux node outputs.
    """
    from pyresonitelink.protoflux.core import ValueFieldDrive

    expr_comp = await ctx.materialize(bind_rec.expr._node)

    ConcreteDrive = ValueFieldDrive[res_type]  # type: ignore[valid-type]
    bind_node = ConcreteDrive()
    await bind_node.add_to_slot(ctx.resolink, bind_rec.slot)

    await ctx.resolink.update_references(
        componentId=bind_node.id,  # type: ignore[arg-type]
        references={
            "Value": expr_comp.id,
            "_value": member.id,
        },
    )


# =========================================================================
# Top-level build
# =========================================================================


async def _setup_typed_trigger(
    ctx: _BuildContext,
    trigger: _flow.Trigger,
) -> Any:
    """Pre-create a typed trigger receiver so TriggerValueNode works.

    Returns the receiver component. The caller must wire on_triggered
    after building the flow node.
    """
    from pyresonitelink.generated.protoflux import global_value

    StringGlobal = global_value.GlobalValue[primitives.String]
    tag_node = StringGlobal()
    await tag_node.add_to_slot(ctx.resolink, ctx.slot)
    tag_node.value = trigger.tag
    await tag_node.update(ctx.resolink)

    assert trigger.value_type is not None
    from pyresonitelink.protoflux.flow import DynamicImpulseReceiverWithValue
    ConcreteReceiver = DynamicImpulseReceiverWithValue[trigger.value_type]  # type: ignore[valid-type]
    receiver = ConcreteReceiver()
    await receiver.add_to_slot(ctx.resolink, ctx.slot)
    await ctx.resolink.update_references(
        componentId=receiver.id,  # type: ignore[arg-type]
        references={"Tag": tag_node.id},
    )
    ctx.trigger_receiver = receiver
    return receiver


async def _build_raycast_one_context(
    ctx: _BuildContext,
    rc_ctx: _flow.RaycastOneContext,
) -> Any:
    """Build a RaycastOneContext into a ProtoFlux RaycastOne node."""
    from pyresonitelink.protoflux.physics import RaycastOne

    # Materialize input expressions
    origin_comp = await ctx.materialize(rc_ctx.origin._node)
    dir_comp = await ctx.materialize(rc_ctx.direction._node)
    max_dist_comp = None
    if rc_ctx.max_distance is not None:
        max_dist_comp = await ctx.materialize(rc_ctx.max_distance._node)
    hit_trig_comp = None
    if rc_ctx.hit_triggers is not None:
        hit_trig_comp = await ctx.materialize(rc_ctx.hit_triggers._node)
    users_comp = None
    if rc_ctx.users_only is not None:
        users_comp = await ctx.materialize(rc_ctx.users_only._node)
    root_comp = None
    if rc_ctx.root is not None:
        root_comp = await ctx.materialize(rc_ctx.root._node)

    # Create the RaycastOne node
    rc_node = RaycastOne(
        origin=origin_comp.id,
        direction=dir_comp.id,
        max_distance=max_dist_comp.id if max_dist_comp else None,
        hit_triggers=hit_trig_comp.id if hit_trig_comp else None,
        users_only=users_comp.id if users_comp else None,
        root=root_comp.id if root_comp else None,
    )
    await rc_node.add_to_slot(ctx.resolink, ctx.slot)

    # Register so ComponentOutputNode can reference it
    ctx.component_outputs[rc_ctx.component_tag] = rc_node

    # Build hit and miss write chains
    hit_result = await _build_stmt_chain(ctx, rc_ctx.hit_stmts)
    miss_result = await _build_stmt_chain(ctx, rc_ctx.miss_stmts)

    refs: dict[str, str] = {}
    if hit_result is not None:
        refs["OnHit"] = hit_result.head.id
    if miss_result is not None:
        refs["OnMiss"] = miss_result.head.id
    if refs:
        await ctx.resolink.update_references(
            componentId=rc_node.id,
            references=refs,
        )

    return rc_node


async def _build_action_context(
    ctx: _BuildContext,
    action_ctx: Any,
) -> Any:
    """Build a generic ActionContext into its ProtoFlux node.

    Dynamically imports the component class, materializes inputs,
    creates the node, registers outputs, and wires flow branches.
    """
    from pyresonitelink.dergflux import _action

    action_def: _action.ActionDef = action_ctx.action_def

    # Import the component class
    module = importlib.import_module(
        f"pyresonitelink.{action_def.import_path}",
    )
    ComponentClass = getattr(module, action_def.class_name)

    # Materialize input expressions and collect raw reference IDs.
    # Convert snake_case param names to PascalCase member names for
    # update_references (Resonite members are PascalCase).
    def _to_pascal(name: str) -> str:
        return "".join(part.capitalize() for part in name.split("_"))

    init_kwargs: dict[str, str] = {}
    for param_name, expr_proxy in action_ctx.input_exprs.items():
        comp = await ctx.materialize(expr_proxy._node)
        init_kwargs[_to_pascal(param_name)] = comp.id
    for param_name, raw_id in action_ctx.raw_inputs.items():
        init_kwargs[_to_pascal(param_name)] = raw_id

    # Auto-create bridge components for reference inputs
    REF_INPUT_TEMPLATE = (
        "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution"
        ".Nodes.RefObjectInput<{type_str}>"
    )
    GLOBAL_REF_TEMPLATE = (
        "[FrooxEngine]FrooxEngine.ProtoFlux.GlobalReference<{type_str}>"
    )
    for param_name, (component, type_str, bridge_kind) in action_ctx.ref_bridges.items():
        if bridge_kind == "global_ref":
            comp_type = GLOBAL_REF_TEMPLATE.format(type_str=type_str)
            target_member = "Reference"
        else:
            comp_type = REF_INPUT_TEMPLATE.format(type_str=type_str)
            target_member = "Target"
        bridge_resp = await ctx.resolink.add_component(
            containerSlotId=ctx.slot,
            componentType=comp_type,
        )
        assert bridge_resp.entityId is not None, (
            f"Failed to create bridge {comp_type}"
        )
        await ctx.resolink.update_references(
            componentId=bridge_resp.entityId,
            references={target_member: component.id},
        )
        init_kwargs[_to_pascal(param_name)] = bridge_resp.entityId

    # If the component is generic, parameterize it from the first
    # expression input's type (e.g. FireOnValueChange[Float]).
    if hasattr(ComponentClass, "_GENERIC_TYPE_TEMPLATE") and ComponentClass._GENERIC_TYPE_TEMPLATE:
        # Find the type from the first expression input
        for expr_proxy in action_ctx.input_exprs.values():
            res_type = _resolve_type(expr_proxy._node)
            ComponentClass = ComponentClass[res_type]  # type: ignore[index]
            break

    # Create the component empty, then wire inputs via update_references
    # to avoid ResoniteLink type compatibility issues.
    node = ComponentClass()
    await node.add_to_slot(ctx.resolink, ctx.slot)
    if init_kwargs:
        await ctx.resolink.update_references(
            componentId=node.id,  # type: ignore[arg-type]
            references=init_kwargs,
        )

    # Register so ComponentOutputNode can reference it
    ctx.component_outputs[action_ctx.component_tag] = node

    # Build and wire each flow output branch
    branch_refs: dict[str, str] = {}
    for branch_name in action_def.flow_outputs:
        writes = action_ctx.branch_stmts.get(branch_name, [])
        result = await _build_stmt_chain(ctx, writes)
        if result is not None:
            # Convert snake_case branch name to PascalCase member name
            member_name = "".join(
                part.capitalize() for part in branch_name.split("_")
            )
            branch_refs[member_name] = result.head.id
    if branch_refs:
        await ctx.resolink.update_references(
            componentId=node.id,
            references=branch_refs,
        )

    return node


async def _build_indexed_branch_context(
    ctx: _BuildContext,
    ib_ctx: _flow.IndexedBranchContext,
) -> Any:
    """Build a node with indexed flow outputs (SyncList-based).

    Creates the component, builds statement chains for each indexed
    branch, populates the SyncList, and wires named flow outputs.
    """
    from pyresonitelink.data import members as mem

    # Materialize input expressions
    refs: dict[str, str] = {}
    for param_name, expr_proxy in ib_ctx.input_exprs.items():
        comp = await ctx.materialize(expr_proxy._node)
        # Convert snake_case param to PascalCase member name
        member_name = "".join(w.capitalize() for w in param_name.split("_"))
        refs[member_name] = comp.id
    for param_name, raw_id in ib_ctx.raw_inputs.items():
        member_name = "".join(w.capitalize() for w in param_name.split("_"))
        refs[member_name] = raw_id

    # Create the component
    node_resp = await ctx.resolink.add_component(
        containerSlotId=ctx.slot,
        componentType=ib_ctx.node_type,
    )
    if node_resp.entityId is None:
        raise RuntimeError(
            f"Failed to create {ib_ctx.node_type}: {node_resp.errorInfo}"
        )
    node_id = node_resp.entityId

    # Register for ComponentOutputNode references
    ctx.component_outputs[ib_ctx.component_tag] = type(
        "_NodeStub", (), {"id": node_id},
    )()

    # Wire inputs
    if refs:
        await ctx.resolink.update_references(
            componentId=node_id, references=refs,
        )

    # Build each indexed branch and collect head node IDs
    branch_heads: list[str | None] = []
    for i in range(ib_ctx.num_branches):
        stmts = ib_ctx.branch_stmts.get(i, [])
        result = await _build_stmt_chain(ctx, stmts)
        branch_heads.append(result.head.id if result else None)

    # Determine the SyncList member name.
    # PulseRandom and ImpulseMultiplexer use "Impulses".
    # ImpulseDemultiplexer uses "Operations".
    get_resp = await ctx.resolink.get_component(componentId=node_id)
    assert get_resp.data is not None
    list_member_name = None
    list_member_id = None
    for mname, mdata in get_resp.data.members.items():
        if isinstance(mdata, mem.SyncList) or (
            isinstance(mdata, dict) and mdata.get("$type") == "list"
        ):
            list_member_name = mname
            list_member_id = (
                mdata.id if isinstance(mdata, mem.SyncList)
                else mdata.get("id")
            )
            break

    if list_member_name is not None:
        # Populate the SyncList with references to branch heads
        new_list = mem.SyncList(
            elements=[
                mem.Reference(targetId=hid) if hid else mem.Reference()
                for hid in branch_heads
            ],
        )
        if list_member_id is not None:
            new_list.id = list_member_id
        update_comp = workers.Component(
            id=node_id,
            componentType=ib_ctx.node_type,
            members={list_member_name: new_list},
        )
        await ctx.resolink.update_component(data=update_comp)

    # Wire named flow outputs (e.g. ImpulseDemultiplexer.OnTriggered)
    named_refs: dict[str, str] = {}
    for name, stmts in ib_ctx.named_stmts.items():
        result = await _build_stmt_chain(ctx, stmts)
        if result is not None:
            member_name = "".join(w.capitalize() for w in name.split("_"))
            named_refs[member_name] = result.head.id
    if named_refs:
        await ctx.resolink.update_references(
            componentId=node_id, references=named_refs,
        )

    # Return a stub with .id for sequence wiring
    return type("_NodeStub", (), {"id": node_id})()


async def _build_bare_write_context(
    ctx: _BuildContext,
    bare_ctx: _flow.BareWriteContext,
) -> FlowResult | None:
    """Build bare writes as a statement chain.

    Returns a FlowResult for chaining with other statements.
    """
    return await _build_stmt_chain(ctx, bare_ctx.stmts)


async def _build_flow_context(
    ctx: _BuildContext,
    flow_ctx: _flow.FlowContext,
) -> FlowResult | None:
    """Build a single flow context into ProtoFlux nodes.

    Returns a FlowResult with head and tail nodes for chaining.
    """
    if isinstance(flow_ctx, _flow.IfContext):
        return await _build_if_context(ctx, flow_ctx)
    if isinstance(flow_ctx, _flow.BareWriteContext):
        return await _build_bare_write_context(ctx, flow_ctx)

    # For context types that return a single node, wrap in FlowResult.
    # These nodes handle their own internal flow (loops, actions) and
    # the node itself is both the entry and the tail.
    node: Any | None = None
    if isinstance(flow_ctx, _flow.ForContext):
        node = await _build_for_context(ctx, flow_ctx)
    elif isinstance(flow_ctx, _flow.RangeContext):
        node = await _build_range_context(ctx, flow_ctx)
    elif isinstance(flow_ctx, _flow.WhileContext):
        node = await _build_while_context(ctx, flow_ctx)
    elif isinstance(flow_ctx, _flow.RaycastOneContext):
        node = await _build_raycast_one_context(ctx, flow_ctx)
    else:
        from pyresonitelink.dergflux import _action
        if isinstance(flow_ctx, _action.ActionContext):
            node = await _build_action_context(ctx, flow_ctx)
        elif isinstance(flow_ctx, _flow.IndexedBranchContext):
            node = await _build_indexed_branch_context(ctx, flow_ctx)
        else:
            raise TypeError(
                f"Unknown flow context: {type(flow_ctx).__name__}"
            )
    if node is None:
        return None
    return FlowResult(head=node, tails=[_Tail(node)])


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

    # Build each Under record.
    # Each record contains a sequence of flow statements sharing one
    # trigger. If there's only one statement, wire the trigger directly.
    # If there are multiple, wrap in a Sequence node.
    # Save contexts keyed by slot ID so bindings can reuse them.
    under_contexts: dict[str, _BuildContext] = {}
    for under_rec in graph._under_records:
        ctx = _BuildContext(resolink, under_rec.slot)
        ctx.is_async = under_rec.is_async
        trigger = under_rec.trigger
        under_contexts[under_rec.slot.id] = ctx

        # For typed triggers, create receiver first so TriggerValueNode
        # can reference it during expression materialization.
        receiver = None
        if trigger is not None and trigger.value_type is not None:
            receiver = await _setup_typed_trigger(ctx, trigger)

        # Separate event-source statements from triggered statements.
        # Event sources (FireOnValueChange, SlotChildrenEvents, etc.)
        # fire on their own — they don't need a trigger node.
        # Everything else shares the Under block's trigger.
        from pyresonitelink.dergflux import _action
        triggered_stmts: list[_flow.FlowContext] = []
        event_source_stmts: list[_flow.FlowContext] = []
        for stmt in under_rec.statements:
            is_evt = False
            if isinstance(stmt, _action.ActionContext):
                is_evt = stmt.action_def.is_event_source
            elif isinstance(stmt, _flow.IndexedBranchContext):
                is_evt = stmt.is_event_source
            if is_evt:
                event_source_stmts.append(stmt)
            else:
                triggered_stmts.append(stmt)

        # Build event-source statements (self-triggering, no Sequence)
        for stmt in event_source_stmts:
            await _build_flow_context(ctx, stmt)

        # Build triggered statements and chain them via FlowResult
        results: list[FlowResult] = []
        for stmt in triggered_stmts:
            result = await _build_flow_context(ctx, stmt)
            if result is not None:
                results.append(result)

        if not results:
            continue

        # Chain results: wire each result's tails to the next's head
        for i in range(len(results) - 1):
            await _wire_tails_to_head(
                ctx, results[i].tails, results[i + 1].head,
            )

        entry = results[0].head

        # Wire the trigger to the entry point.
        if receiver is not None:
            target = entry
            if ctx.is_async:
                target = await _create_start_async_task(ctx, entry)
            await ctx.resolink.update_references(
                componentId=receiver.id,  # type: ignore[arg-type]
                references={"OnTriggered": target.id},
            )
        else:
            await _build_trigger(ctx, entry, trigger)

    # Build bindings (ValueFieldDrive<T>, DynamicValueVariableDriver, etc.)
    # Bindings are built using the ctx from the last Under block that
    # matches their slot, so they have access to loop_node and other
    # flow state (e.g. for g.Bind(i, mux, "Index") inside a For loop).
    for bind_rec in graph._bindings:
        bind_ctx = under_contexts.get(bind_rec.slot.id)
        if bind_ctx is None:
            bind_ctx = _BuildContext(resolink, bind_rec.slot)
        member = bind_rec.component.get_member(bind_rec.member_name)
        assert member is not None
        res_type = _resolve_type(bind_rec.expr._node)

        if bind_rec.dynvar_name is not None:
            await _build_dynvar_binding(
                resolink, bind_rec, member, res_type,
            )
        else:
            await _build_expr_binding_with_ctx(
                bind_ctx, bind_rec, member, res_type,
            )
