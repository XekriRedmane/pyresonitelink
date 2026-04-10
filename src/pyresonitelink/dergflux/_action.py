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
    """

    param_name: str
    type: type | None = None


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
    """

    import_path: str
    class_name: str
    inputs: dict[str, InputDef] = field(default_factory=dict)
    flow_outputs: list[str] = field(default_factory=list)
    value_outputs: dict[str, OutputDef] = field(default_factory=dict)


@dataclass
class ActionContext(_flow.FlowContext):
    """Tracks a generic action node during recording.

    Attributes:
        action_def: The action definition.
        input_exprs: Maps input param_name to the coerced ExprProxy.
        component_tag: UUID linking output nodes to this context.
        branch_writes: Maps flow output name to its recorded writes.
        active_branch: The currently recording branch name.
    """

    action_def: ActionDef = field(default=None)  # type: ignore[assignment]
    input_exprs: dict[str, _expr.ExprProxy] = field(default_factory=dict)
    component_tag: str = ""
    branch_writes: dict[str, list[_flow.WriteRecord]] = field(
        default_factory=dict,
    )
    active_branch: str | None = None

    def record_write(self, write: _flow.WriteRecord) -> None:
        """Append a write to the currently active branch."""
        if self.active_branch is None:
            raise RuntimeError(
                "Writes inside an Action must be inside a flow output "
                "context manager (e.g. r.on_hit())."
            )
        self.branch_writes[self.active_branch].append(write)


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
) -> tuple[ActionContext, ActionProxy]:
    """Create an ActionContext and ActionProxy for an action node.

    Args:
        graph: The owning Graph.
        action_def: The action definition.
        kwargs: User-provided keyword arguments for the inputs.

    Returns:
        Tuple of (context, proxy).
    """
    under = graph._require_under()
    tag = str(uuid.uuid4())

    # Coerce input expressions
    input_exprs: dict[str, _expr.ExprProxy] = {}
    for kwarg_name, value in kwargs.items():
        if kwarg_name not in action_def.inputs:
            raise TypeError(
                f"Unknown input '{kwarg_name}' for {action_def.class_name}. "
                f"Valid inputs: {list(action_def.inputs)}"
            )
        input_exprs[action_def.inputs[kwarg_name].param_name] = (
            _expr._coerce(value)
        )

    # Initialize branch write lists
    branch_writes: dict[str, list[_flow.WriteRecord]] = {
        name: [] for name in action_def.flow_outputs
    }

    ctx = ActionContext(
        slot=under.slot,
        action_def=action_def,
        input_exprs=input_exprs,
        component_tag=tag,
        branch_writes=branch_writes,
    )
    proxy = ActionProxy(graph, ctx, action_def, tag)
    return ctx, proxy
