"""Space and variable declaration for Dergflux.

A Space represents a DynamicVariableSpace on a Resonite slot.
Setting attributes declares or writes variables; getting attributes
reads them as expression proxies.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from pyresonitelink.data import primitives
from pyresonitelink.dergflux import _expr

if TYPE_CHECKING:
    from pyresonitelink.data import workers
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


# Maps convenience method names to their Resonite primitive types.
# Used to dynamically generate the Space.*Var() methods.
_VAR_TYPES: dict[str, type] = {
    # Scalars
    "BoolVar": primitives.Bool,
    "ByteVar": primitives.Byte,
    "SByteVar": primitives.SByte,
    "ShortVar": primitives.Short,
    "UShortVar": primitives.UShort,
    "IntVar": primitives.Int,
    "UIntVar": primitives.UInt,
    "LongVar": primitives.Long,
    "ULongVar": primitives.ULong,
    "FloatVar": primitives.Float,
    "DoubleVar": primitives.Double,
    "StringVar": primitives.String,
    "CharVar": primitives.Char,
    # Colors
    "ColorVar": primitives.Color,
    "ColorXVar": primitives.ColorX,
    "Color32Var": primitives.Color32,
    # 2D vectors
    "Float2Var": primitives.Float2,
    "Double2Var": primitives.Double2,
    "Int2Var": primitives.Int2,
    "UInt2Var": primitives.UInt2,
    "Long2Var": primitives.Long2,
    "ULong2Var": primitives.ULong2,
    "Short2Var": primitives.Short2,
    "UShort2Var": primitives.UShort2,
    "Byte2Var": primitives.Byte2,
    "SByte2Var": primitives.SByte2,
    "Bool2Var": primitives.Bool2,
    # 3D vectors
    "Float3Var": primitives.Float3,
    "Double3Var": primitives.Double3,
    "Int3Var": primitives.Int3,
    "UInt3Var": primitives.UInt3,
    "Long3Var": primitives.Long3,
    "ULong3Var": primitives.ULong3,
    "Short3Var": primitives.Short3,
    "UShort3Var": primitives.UShort3,
    "Byte3Var": primitives.Byte3,
    "SByte3Var": primitives.SByte3,
    "Bool3Var": primitives.Bool3,
    # 4D vectors
    "Float4Var": primitives.Float4,
    "Double4Var": primitives.Double4,
    "Int4Var": primitives.Int4,
    "UInt4Var": primitives.UInt4,
    "Long4Var": primitives.Long4,
    "ULong4Var": primitives.ULong4,
    "Short4Var": primitives.Short4,
    "UShort4Var": primitives.UShort4,
    "Byte4Var": primitives.Byte4,
    "SByte4Var": primitives.SByte4,
    "Bool4Var": primitives.Bool4,
    # Quaternions
    "FloatQVar": primitives.FloatQ,
    "DoubleQVar": primitives.DoubleQ,
    # Matrices
    "Float2x2Var": primitives.Float2x2,
    "Double2x2Var": primitives.Double2x2,
    "Float3x3Var": primitives.Float3x3,
    "Double3x3Var": primitives.Double3x3,
    "Float4x4Var": primitives.Float4x4,
    "Double4x4Var": primitives.Double4x4,
    # Geometry
    "RectVar": primitives.Rect,
    "BoundingBoxVar": primitives.BoundingBox,
}


class Space:
    """Proxy for a DynamicVariableSpace on a slot.

    Attribute access builds expression trees:
    - ``s.x = s.FloatVar("x")`` declares variable *x* as a float.
    - ``s.x`` reads variable *x*, returning an ExprProxy.
    - ``s.z = s.x + 3`` records a write on the active flow context.

    Attributes starting with ``_`` bypass the DSL and behave normally.
    Capitalized names (starting with uppercase) are reserved for Var
    factory methods and also bypass the DSL.

    Usage::

        s = g.Space(slot)
        s.x = s.FloatVar("x")                        # on space's slot
        s.z = s.FloatVar("z", slot=child_slot)        # on a child slot
        s.pos = s.Float3Var("pos")                    # 3D vector
        s.col = s.ColorXVar("col")                    # color
        s.custom = s.Var("custom", primitives.Double)  # explicit type

    Every primitive type in ``pyresonitelink.data.primitives`` has a
    corresponding convenience method (e.g. ``IntVar``, ``BoolVar``,
    ``DoubleQVar``, ``Float4x4Var``, ``RectVar``, ``BoundingBoxVar``).

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

        if isinstance(value, VarDecl):
            # Declaration: s.z = s.FloatVar("z")
            vars_dict: dict[str, VarDecl] = object.__getattribute__(
                self, "_vars",
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
        vars_dict: dict[str, VarDecl] = object.__getattribute__(self, "_vars")
        if name not in vars_dict:
            raise AttributeError(
                f"Variable '{name}' not declared on this Space. "
                f"Declare it first with s.{name} = s.FloatVar(\"{name}\")."
            )
        decl = vars_dict[name]
        node = _expr.VarReadNode(decl.path, self, decl.resonite_type)
        return _expr.ExprProxy(node)
