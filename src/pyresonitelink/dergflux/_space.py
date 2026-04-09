"""Space and variable declaration for Dergflux.

A Space represents a DynamicVariableSpace on a Resonite slot.
Setting attributes declares or writes variables; getting attributes
reads them as expression proxies.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from pyresonitelink.dergflux import _expr

if TYPE_CHECKING:
    from pyresonitelink.data import workers
    from pyresonitelink.dergflux import _graph


@dataclass
class VarDecl:
    """Declaration of a dynamic variable with a name and Resonite type."""

    path: str
    resonite_type: type


class Space:
    """Proxy for a DynamicVariableSpace on a slot.

    Attribute access builds expression trees:
    - ``s.x = g.Float("x")`` declares variable *x* as a float.
    - ``s.x`` reads variable *x*, returning an ExprProxy.
    - ``s.z = s.x + 3`` records a write on the active flow context.

    Attributes starting with ``_`` bypass the DSL and behave normally.

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

    def __setattr__(self, name: str, value: Any) -> None:
        if name.startswith("_"):
            object.__setattr__(self, name, value)
            return

        if isinstance(value, VarDecl):
            # Declaration: s.z = g.Float("z")
            vars_dict: dict[str, VarDecl] = object.__getattribute__(
                self, "_vars",
            )
            vars_dict[name] = value
            return

        # Write: s.z = <expr>
        proxy = _expr._coerce(value)
        graph: _graph.Graph = object.__getattribute__(self, "_graph")
        flow_ctx = graph._active_flow()
        if flow_ctx is None:
            raise RuntimeError(
                f"Cannot assign to '{name}' outside a flow context. "
                "Use inside g.If() or similar."
            )
        from pyresonitelink.dergflux import _flow

        flow_ctx.record_write(_flow.WriteRecord(self, name, proxy))

    def __getattr__(self, name: str) -> _expr.ExprProxy:
        if name.startswith("_"):
            raise AttributeError(name)
        vars_dict: dict[str, VarDecl] = object.__getattribute__(self, "_vars")
        if name not in vars_dict:
            raise AttributeError(
                f"Variable '{name}' not declared on this Space. "
                f"Declare it first with s.{name} = g.Float(\"{name}\")."
            )
        decl = vars_dict[name]
        node = _expr.VarReadNode(decl.path, self, decl.resonite_type)
        return _expr.ExprProxy(node)
