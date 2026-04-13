"""Space and variable declaration for Dergflux.

A Space represents a DynamicVariableSpace on a Resonite slot.
Setting attributes declares or writes variables; getting attributes
reads them as expression proxies.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from pyresonitelink.data import primitives, workers
from pyresonitelink.dergflux import _expr

if TYPE_CHECKING:
    from pyresonitelink.dergflux import _graph


@dataclass
class VarDecl:
    """Declaration of a dynamic variable with a name and Resonite type.

    Attributes:
        path: The variable name/path.
        resonite_type: The Resonite primitive type.
        slot: Optional slot to place the variable on. Must be equal to
            or a recursive child of the space's slot. If None, the
            space's own slot is used.
        initial_value: Optional initial value for the variable.
    """

    path: str
    resonite_type: type
    slot: workers.Slot | None = field(default=None)
    initial_value: Any = field(default=None)


@dataclass
class ModelVarDecl:
    """Declaration of a model variable backed by DataModelValueFieldStore.

    Model variables avoid the dynamic variable binding delay and are
    network-synchronized.  Each variable is placed on its own named
    child slot with a ``DataModelValueFieldStore<T>`` component.

    Attributes:
        path: The variable name (also used as the child slot name).
        resonite_type: The Resonite primitive type.
        initial_value: Optional initial value for the variable.
    """

    path: str
    resonite_type: type
    initial_value: Any = field(default=None)


# Maps convenience method names to their Resonite primitive types.
# Used to dynamically generate the Space.*DynVar() methods.
_VAR_TYPES: dict[str, type] = {
    # Scalars
    "BoolDynVar": primitives.Bool,
    "ByteDynVar": primitives.Byte,
    "SByteDynVar": primitives.SByte,
    "ShortDynVar": primitives.Short,
    "UShortDynVar": primitives.UShort,
    "IntDynVar": primitives.Int,
    "UIntDynVar": primitives.UInt,
    "LongDynVar": primitives.Long,
    "ULongDynVar": primitives.ULong,
    "FloatDynVar": primitives.Float,
    "DoubleDynVar": primitives.Double,
    "StringDynVar": primitives.String,
    "CharDynVar": primitives.Char,
    # Colors
    "ColorDynVar": primitives.Color,
    "ColorXDynVar": primitives.ColorX,
    "Color32DynVar": primitives.Color32,
    # 2D vectors
    "Float2DynVar": primitives.Float2,
    "Double2DynVar": primitives.Double2,
    "Int2DynVar": primitives.Int2,
    "UInt2DynVar": primitives.UInt2,
    "Long2DynVar": primitives.Long2,
    "ULong2DynVar": primitives.ULong2,
    "Short2DynVar": primitives.Short2,
    "UShort2DynVar": primitives.UShort2,
    "Byte2DynVar": primitives.Byte2,
    "SByte2DynVar": primitives.SByte2,
    "Bool2DynVar": primitives.Bool2,
    # 3D vectors
    "Float3DynVar": primitives.Float3,
    "Double3DynVar": primitives.Double3,
    "Int3DynVar": primitives.Int3,
    "UInt3DynVar": primitives.UInt3,
    "Long3DynVar": primitives.Long3,
    "ULong3DynVar": primitives.ULong3,
    "Short3DynVar": primitives.Short3,
    "UShort3DynVar": primitives.UShort3,
    "Byte3DynVar": primitives.Byte3,
    "SByte3DynVar": primitives.SByte3,
    "Bool3DynVar": primitives.Bool3,
    # 4D vectors
    "Float4DynVar": primitives.Float4,
    "Double4DynVar": primitives.Double4,
    "Int4DynVar": primitives.Int4,
    "UInt4DynVar": primitives.UInt4,
    "Long4DynVar": primitives.Long4,
    "ULong4DynVar": primitives.ULong4,
    "Short4DynVar": primitives.Short4,
    "UShort4DynVar": primitives.UShort4,
    "Byte4DynVar": primitives.Byte4,
    "SByte4DynVar": primitives.SByte4,
    "Bool4DynVar": primitives.Bool4,
    # Quaternions
    "FloatQDynVar": primitives.FloatQ,
    "DoubleQDynVar": primitives.DoubleQ,
    # Matrices
    "Float2x2DynVar": primitives.Float2x2,
    "Double2x2DynVar": primitives.Double2x2,
    "Float3x3DynVar": primitives.Float3x3,
    "Double3x3DynVar": primitives.Double3x3,
    "Float4x4DynVar": primitives.Float4x4,
    "Double4x4DynVar": primitives.Double4x4,
    # Geometry
    "RectDynVar": primitives.Rect,
    "BoundingBoxDynVar": primitives.BoundingBox,
    # References and Types
    "RefDynVar": workers.Slot,
    "TypeDynVar": type,
}

# Maps convenience method names to their Resonite primitive types for
# model variables (DataModelValueFieldStore-backed).
_MODEL_VAR_TYPES: dict[str, type] = {
    name.replace("DynVar", "ModelVar"): res_type
    for name, res_type in _VAR_TYPES.items()
}
_MODEL_VAR_TYPES["RefModelVar"] = workers.Slot
_MODEL_VAR_TYPES["TypeModelVar"] = type


class Space:
    """Proxy for a DynamicVariableSpace on a slot.

    Attribute access builds expression trees:
    - ``s.x = s.FloatDynVar("x")`` declares variable *x* as a float.
    - ``s.x`` reads variable *x*, returning an ExprProxy.
    - ``s.z = s.x + 3`` records a write on the active flow context.

    Attributes starting with ``_`` bypass the DSL and behave normally.
    Capitalized names (starting with uppercase) are reserved for Var
    factory methods and also bypass the DSL.

    Usage::

        s = g.Space(slot)
        s.x = s.FloatDynVar("x")                        # on space's slot
        s.z = s.FloatDynVar("z", slot=child_slot)        # on a child slot
        s.pos = s.Float3DynVar("pos")                    # 3D vector
        s.col = s.ColorXDynVar("col")                    # color
        s.custom = s.Var("custom", primitives.Double)  # explicit type

    Every primitive type in ``pyresonitelink.data.primitives`` has a
    corresponding convenience method (e.g. ``IntDynVar``, ``BoolDynVar``,
    ``DoubleQDynVar``, ``Float4x4DynVar``, ``RectDynVar``, ``BoundingBoxDynVar``).

    If a ``slot`` is given, it must be equal to or a recursive child of
    the space's slot (validated at build time). Variables are only
    created if they don't already exist on the target slot.

    Args:
        graph: The owning Graph instance.
        slot: The Resonite slot that will hold the DynamicVariableSpace.
        space_name: Optional name for the DynamicVariableSpace. If a
            space with this name already exists on the slot, it is
            reused instead of creating a new one.
    """

    def __init__(
        self,
        graph: _graph.Graph,
        slot: workers.Slot,
        space_name: str | None = None,
    ) -> None:
        object.__setattr__(self, "_graph", graph)
        object.__setattr__(self, "_slot", slot)
        object.__setattr__(self, "_space_name", space_name)
        object.__setattr__(self, "_vars", {})
        object.__setattr__(self, "_built_vars", {})

    # --- Variable declaration ---

    def Var(
        self,
        name: str,
        resonite_type: type,
        slot: workers.Slot | None = None,
        value: Any = None,
    ) -> VarDecl:
        """Declare a dynamic variable with an explicit type.

        Args:
            name: The variable name/path.
            resonite_type: The Resonite primitive type.
            slot: Optional slot to place the variable on. Must be equal
                to or a recursive child of the space's slot. Validated
                at build time.
            value: Optional initial value for the variable.

        Returns:
            A VarDecl to assign to a Space attribute.
        """
        return VarDecl(name, resonite_type, slot, value)

    def __setattr__(self, name: str, value: Any) -> None:
        if name.startswith("_") or (name[0:1].isupper() if name else False):
            object.__setattr__(self, name, value)
            return

        if isinstance(value, (VarDecl, ModelVarDecl)):
            # Declaration: s.z = s.FloatDynVar("z") or s.z = s.FloatModelVar("z")
            vars_dict: dict[str, VarDecl | ModelVarDecl] = (
                object.__getattribute__(self, "_vars")
            )
            vars_dict[name] = value
            return

        # Write: s.z = <expr>
        proxy = _expr._coerce(value)
        graph: _graph.Graph = object.__getattribute__(self, "_graph")
        from pyresonitelink.dergflux import _flow

        flow_ctx = graph._active_flow()
        if flow_ctx is not None:
            flow_ctx.record_write(_flow.WriteRecord(self, name, proxy))
            return

        # No active flow (If/For/While), but if we're inside Under,
        # this is a bare write that becomes a standalone statement.
        under = graph._active_under()
        if under is None or under.record is None:
            raise RuntimeError(
                f"Cannot assign to '{name}' outside a flow context. "
                "Use inside g.Under() with g.If(), g.For(), etc., "
                "or as a bare write inside g.Under()."
            )

        # Extend the last BareWriteContext, or create a new one
        stmts = under.record.statements
        if stmts and isinstance(stmts[-1], _flow.BareWriteContext):
            stmts[-1].record_write(
                _flow.WriteRecord(self, name, proxy),
            )
        else:
            bare = _flow.BareWriteContext(slot=under.slot)
            bare.record_write(_flow.WriteRecord(self, name, proxy))
            stmts.append(bare)

    def __getattr__(self, name: str) -> Any:
        if name.startswith("_"):
            raise AttributeError(name)
        # Check for dynamically-generated Var methods
        if name in _VAR_TYPES:
            res_type = _VAR_TYPES[name]
            def _var_method(
                var_name: str,
                slot: workers.Slot | None = None,
                value: Any = None,
                _rt: type = res_type,
            ) -> VarDecl:
                return VarDecl(var_name, _rt, slot, value)
            return _var_method
        if name in _MODEL_VAR_TYPES:
            res_type = _MODEL_VAR_TYPES[name]
            def _model_var_method(
                var_name: str,
                value: Any = None,
                _rt: type = res_type,
            ) -> ModelVarDecl:
                return ModelVarDecl(var_name, _rt, value)
            return _model_var_method
        vars_dict: dict[str, VarDecl | ModelVarDecl] = (
            object.__getattribute__(self, "_vars")
        )
        if name not in vars_dict:
            raise AttributeError(
                f"Variable '{name}' not declared on this Space. "
                f"Declare it first with s.{name} = s.FloatDynVar(\"{name}\")."
            )
        # After build, return the built component for direct access
        built: dict[str, Any] = object.__getattribute__(self, "_built_vars")
        if name in built:
            return built[name]
        # During recording, return an ExprProxy for the expression tree
        decl = vars_dict[name]
        node = _expr.VarReadNode(decl.path, self, decl.resonite_type)
        return _expr.ExprProxy(node)
