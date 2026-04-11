"""Generic action node support for Dergflux.

An action node is a ProtoFlux node that is triggered by an impulse,
has value/reference inputs, multiple flow outputs (branches), and
optionally value outputs.  This module provides a declarative way to
define and use them without writing custom Context/Proxy/Builder code
for each node.

Usage::

    # Define the action once
    RaycastOne = ActionDef(
        component_class="pyresonitelink.protoflux.physics.RaycastOne",
        inputs={
            "origin": InputDef("origin", primitives.Float3),
            "direction": InputDef("direction", primitives.Float3),
            "max_distance": InputDef("max_distance", primitives.Float),
        },
        flow_outputs=["on_hit", "on_miss"],
        value_outputs={
            "hit_point": OutputDef("HitPoint", primitives.Float3),
            "hit_distance": OutputDef("HitDistance", primitives.Float),
        },
    )

    # Use it in a graph
    with g.Under(slot):
        with g.Action(RaycastOne, origin=s.pos, direction=s.dir) as r:
            with r.on_hit():
                s.distance = r.hit_distance
            with r.on_miss():
                s.distance = -1
"""

from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Iterator
import uuid

from pyresonitelink.dergflux import _expr
from pyresonitelink.dergflux import _flow

if TYPE_CHECKING:
    from pyresonitelink.dergflux import _graph


@dataclass
class InputDef:
    """Describes an input parameter of an action node.

    Attributes:
        param_name: The Python parameter name on the generated component's
            ``__init__`` (e.g. ``"origin"``, ``"max_distance"``).
        type: The Resonite primitive type, or None if the input is a
            reference type that doesn't need coercion.
        ref_type: For reference inputs, the full Resonite type string
            for the ``RefObjectInput<>`` that bridges a component into
            ProtoFlux.  When the user passes a component instance, the
            builder auto-creates a ``RefObjectInput<ref_type>`` targeting
            the component.  None for value inputs.
        global_type: For ``IGlobalValueProxy`` inputs, the full Resonite
            type string.  When the user passes a component/slot instance,
            the builder auto-creates a ``GlobalReference<global_type>``
            targeting it.  Used for nodes like ``SlotChildrenEvents``
            whose ``Instance`` input requires ``IGlobalValueProxy<Slot>``.
    """

    param_name: str
    type: type | None = None
    ref_type: str | None = None
    global_type: str | None = None


@dataclass
class OutputDef:
    """Describes a value output of an action node.

    Attributes:
        member_name: The Resonite member name (e.g. ``"HitPoint"``).
        type: The Resonite primitive type for the output.
    """

    member_name: str
    type: type


@dataclass
class ActionDef:
    """Declarative definition of a ProtoFlux action node.

    Attributes:
        import_path: Dotted import path relative to ``pyresonitelink``,
            e.g. ``"protoflux.physics"``.
        class_name: The class name to import, e.g. ``"RaycastOne"``.
        inputs: Maps user-facing keyword name to InputDef.
        flow_outputs: List of flow output parameter names on the
            component (e.g. ``["on_hit", "on_miss"]``).  Each becomes
            a context manager on the proxy.
        value_outputs: Maps user-facing property name to OutputDef.
        is_async: If True, the node is async (``IAsyncNodeOperation``)
            and the enclosing flow must use async variants.
        is_event_source: If True, the node fires impulses on its own
            (e.g. ``SlotChildrenEvents`` fires when children change).
            No trigger (Update/DynamicImpulseReceiver) is created.
    """

    import_path: str
    class_name: str
    inputs: dict[str, InputDef] = field(default_factory=dict)
    flow_outputs: list[str] = field(default_factory=list)
    value_outputs: dict[str, OutputDef] = field(default_factory=dict)
    is_async: bool = False
    is_event_source: bool = False


@dataclass
class ActionContext(_flow.FlowContext):
    """Tracks a generic action node during recording.

    Attributes:
        action_def: The action definition.
        input_exprs: Maps input param_name to the coerced ExprProxy.
        component_tag: UUID linking output nodes to this context.
        branch_stmts: Maps flow output name to its recorded writes.
        active_branch: The currently recording branch name.
    """

    action_def: ActionDef = field(default=None)  # type: ignore[assignment]
    input_exprs: dict[str, _expr.ExprProxy] = field(default_factory=dict)
    raw_inputs: dict[str, str] = field(default_factory=dict)
    ref_bridges: dict[str, tuple[Any, str, str]] = field(default_factory=dict)
    component_tag: str = ""
    branch_stmts: dict[str, list[_flow.Statement]] = field(
        default_factory=dict,
    )
    active_branch: str | None = None

    def _require_branch(self) -> str:
        """Return the active branch name, or raise."""
        if self.active_branch is None:
            raise RuntimeError(
                "Writes inside an Action must be inside a flow output "
                "context manager (e.g. r.on_hit())."
            )
        return self.active_branch

    def record_write(self, write: _flow.WriteRecord) -> None:
        """Append a write to the currently active branch."""
        self.branch_stmts[self._require_branch()].append(write)

    def record_nested(self, ctx: _flow.FlowContext) -> None:
        """Append a nested flow to the currently active branch."""
        self.branch_stmts[self._require_branch()].append(ctx)


class ActionProxy:
    """Proxy returned by ``g.Action()`` for accessing branches and outputs.

    Flow outputs become context manager methods (e.g. ``r.on_hit()``).
    Value outputs become properties returning ``ExprProxy`` objects
    (e.g. ``r.hit_distance``).
    """

    def __init__(
        self,
        graph: _graph.Graph,
        ctx: ActionContext,
        action_def: ActionDef,
        tag: str,
    ) -> None:
        self._graph = graph
        self._ctx = ctx
        self._action_def = action_def
        self._tag = tag

    def __getattr__(self, name: str) -> Any:
        # Check for flow outputs — return a context manager factory
        if name in self._action_def.flow_outputs:
            return self._make_branch_cm(name)

        # Check for value outputs — return an ExprProxy
        if name in self._action_def.value_outputs:
            output_def = self._action_def.value_outputs[name]
            return _expr.ExprProxy(
                _expr.ComponentOutputNode(
                    output_def.member_name, self._tag, output_def.type,
                ),
            )

        raise AttributeError(
            f"ActionProxy has no attribute '{name}'. "
            f"Flow outputs: {self._action_def.flow_outputs}, "
            f"Value outputs: {list(self._action_def.value_outputs)}"
        )

    def _make_branch_cm(self, branch_name: str) -> Any:
        """Create a context manager for a flow output branch."""
        @contextmanager
        def _branch_cm() -> Iterator[None]:
            self._ctx.active_branch = branch_name
            self._graph._flow_stack.append(self._ctx)
            try:
                yield
            finally:
                self._graph._flow_stack.pop()
                self._ctx.active_branch = None
        return _branch_cm


def create_action_context(
    graph: _graph.Graph,
    action_def: ActionDef,
    kwargs: dict[str, Any],
    override_slot: Any = None,
) -> tuple[ActionContext, ActionProxy]:
    """Create an ActionContext and ActionProxy for an action node.

    Args:
        graph: The owning Graph.
        action_def: The action definition.
        kwargs: User-provided keyword arguments for the inputs.
        override_slot: If set, use this slot instead of the Under slot.

    Returns:
        Tuple of (context, proxy).
    """
    if override_slot is not None:
        from pyresonitelink.data import workers
        slot = override_slot if isinstance(override_slot, workers.Slot) else workers.Slot(id=override_slot)
    else:
        under = graph._require_under()
        slot = under.slot
    tag = str(uuid.uuid4())

    # Coerce input expressions.  Reference-type inputs (InputDef.type is
    # None) accept raw string IDs or component instances and are passed
    # directly to the component constructor without materialization.
    input_exprs: dict[str, _expr.ExprProxy] = {}
    raw_inputs: dict[str, str] = {}
    ref_bridges: dict[str, tuple[Any, str]] = {}
    for kwarg_name, value in kwargs.items():
        if kwarg_name not in action_def.inputs:
            raise TypeError(
                f"Unknown input '{kwarg_name}' for {action_def.class_name}. "
                f"Valid inputs: {list(action_def.inputs)}"
            )
        input_def = action_def.inputs[kwarg_name]
        param_name = input_def.param_name
        if input_def.type is None:
            # Reference input
            has_id = hasattr(value, "id") and not isinstance(value, str)
            if input_def.ref_type is not None and has_id:
                ref_bridges[param_name] = (value, input_def.ref_type, "ref")
            elif input_def.global_type is not None and has_id:
                ref_bridges[param_name] = (value, input_def.global_type, "global_ref")
            elif isinstance(value, str):
                raw_inputs[param_name] = value
            elif hasattr(value, "id"):
                raw_inputs[param_name] = value.id
            else:
                raise TypeError(
                    f"Reference input '{kwarg_name}' expects a string ID "
                    f"or component instance, got {type(value).__name__}."
                )
        elif isinstance(value, _expr.ExprProxy):
            input_exprs[param_name] = value
        else:
            input_exprs[param_name] = _expr._coerce(value)

    # Initialize branch write lists
    branch_stmts: dict[str, list[_flow.WriteRecord]] = {
        name: [] for name in action_def.flow_outputs
    }

    ctx = ActionContext(
        slot=slot,
        action_def=action_def,
        input_exprs=input_exprs,
        raw_inputs=raw_inputs,
        ref_bridges=ref_bridges,
        component_tag=tag,
        branch_stmts=branch_stmts,
    )
    proxy = ActionProxy(graph, ctx, action_def, tag)
    return ctx, proxy
