"""Flow control contexts and write records for Dergflux.

FlowContext subclasses track condition/count and statements for each
flow construct (If, For, While, bare writes).  WriteRecord captures a
single variable assignment.  These are pure data structures with no
server interaction.

A "statement" is either a WriteRecord (variable write) or a nested
FlowContext (e.g. an ActionContext inside a For loop).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from pyresonitelink.data import workers
    from pyresonitelink.dergflux import _expr
    from pyresonitelink.dergflux import _space


@dataclass
class Trigger:
    """Describes how a flow is triggered.

    Attributes:
        tag: The dynamic impulse tag name.
        value_type: If set, uses DynamicImpulseReceiverWithValue<T>
            and the received value is available as an ExprProxy.
            If None, uses DynamicImpulseReceiver (no value).
    """

    tag: str
    value_type: type | None = None


@dataclass
class WriteRecord:
    """A single variable write: space.var = expr."""

    space: _space.Space
    var_name: str
    expr: _expr.ExprProxy


# A statement is either a write or a nested flow context.
Statement = Union[WriteRecord, "FlowContext"]


@dataclass
class FlowContext:
    """Base class for all flow control contexts.

    Attributes:
        slot: The slot where ProtoFlux nodes will be placed.
    """

    slot: workers.Slot

    def record_write(self, write: WriteRecord) -> None:
        """Record a write in the current phase. Override in subclasses."""
        raise NotImplementedError

    def record_nested(self, ctx: FlowContext) -> None:
        """Record a nested flow context. Override in subclasses."""
        raise NotImplementedError


@dataclass
class IfContext(FlowContext):
    """Tracks an if-else construct during recording.

    Attributes:
        condition: The boolean expression proxy for the branch.
        true_stmts: Statements recorded inside the ``with g.If(...)`` block.
        false_stmts: Statements recorded inside the ``with g.Else()`` block.
        phase: Which branch is currently being recorded.
    """

    condition: _expr.ExprProxy = field(default=None)  # type: ignore[assignment]
    true_stmts: list[Statement] = field(default_factory=list)
    false_stmts: list[Statement] = field(default_factory=list)
    phase: str = "true"

    def record_write(self, write: WriteRecord) -> None:
        """Append a write to the currently active branch."""
        if self.phase == "true":
            self.true_stmts.append(write)
        else:
            self.false_stmts.append(write)

    def record_nested(self, ctx: FlowContext) -> None:
        """Append a nested flow to the currently active branch."""
        if self.phase == "true":
            self.true_stmts.append(ctx)
        else:
            self.false_stmts.append(ctx)


@dataclass
class ForContext(FlowContext):
    """Tracks a for-loop construct during recording.

    Attributes:
        count: The iteration count expression.
        reverse: Whether to iterate in reverse.
        start_stmts: Statements for loop_start (runs once before loop).
        iteration_stmts: Statements for loop_iteration (runs each iteration).
        phase: Which section is currently being recorded.
    """

    count: _expr.ExprProxy = field(default=None)  # type: ignore[assignment]
    reverse: _expr.ExprProxy | None = None
    start_stmts: list[Statement] = field(default_factory=list)
    iteration_stmts: list[Statement] = field(default_factory=list)
    phase: str = "iteration"

    def record_write(self, write: WriteRecord) -> None:
        """Append a write to the currently active section."""
        if self.phase == "start":
            self.start_stmts.append(write)
        else:
            self.iteration_stmts.append(write)

    def record_nested(self, ctx: FlowContext) -> None:
        """Append a nested flow to the currently active section."""
        if self.phase == "start":
            self.start_stmts.append(ctx)
        else:
            self.iteration_stmts.append(ctx)


@dataclass
class RangeContext(FlowContext):
    """Tracks a range-loop construct during recording.

    Attributes:
        start: The loop start value expression.
        end: The loop end value expression.
        step: The loop step size expression.
        start_stmts: Statements for loop_start (runs once before loop).
        iteration_stmts: Statements for loop_iteration (runs each iteration).
        phase: Which section is currently being recorded.
    """

    start: _expr.ExprProxy = field(default=None)  # type: ignore[assignment]
    end: _expr.ExprProxy = field(default=None)  # type: ignore[assignment]
    step: _expr.ExprProxy | None = None
    start_stmts: list[Statement] = field(default_factory=list)
    iteration_stmts: list[Statement] = field(default_factory=list)
    phase: str = "iteration"

    def record_write(self, write: WriteRecord) -> None:
        """Append a write to the currently active section."""
        if self.phase == "start":
            self.start_stmts.append(write)
        else:
            self.iteration_stmts.append(write)

    def record_nested(self, ctx: FlowContext) -> None:
        """Append a nested flow to the currently active section."""
        if self.phase == "start":
            self.start_stmts.append(ctx)
        else:
            self.iteration_stmts.append(ctx)


@dataclass
class WhileContext(FlowContext):
    """Tracks a while-loop construct during recording.

    Attributes:
        condition: The loop condition expression.
        stmts: Statements for loop_iteration.
    """

    condition: _expr.ExprProxy = field(default=None)  # type: ignore[assignment]
    stmts: list[Statement] = field(default_factory=list)

    def record_write(self, write: WriteRecord) -> None:
        """Append a write to the loop body."""
        self.stmts.append(write)

    def record_nested(self, ctx: FlowContext) -> None:
        """Append a nested flow to the loop body."""
        self.stmts.append(ctx)


@dataclass
class RaycastOneContext(FlowContext):
    """Tracks a RaycastOne node during recording."""

    origin: _expr.ExprProxy = field(default=None)  # type: ignore[assignment]
    direction: _expr.ExprProxy = field(default=None)  # type: ignore[assignment]
    max_distance: _expr.ExprProxy | None = None
    hit_triggers: _expr.ExprProxy | None = None
    users_only: _expr.ExprProxy | None = None
    root: _expr.ExprProxy | None = None
    component_tag: str = ""
    hit_stmts: list[Statement] = field(default_factory=list)
    miss_stmts: list[Statement] = field(default_factory=list)
    phase: str = "hit"

    def record_write(self, write: WriteRecord) -> None:
        """Append a write to the currently active section."""
        if self.phase == "hit":
            self.hit_stmts.append(write)
        else:
            self.miss_stmts.append(write)

    def record_nested(self, ctx: FlowContext) -> None:
        """Append a nested flow to the currently active section."""
        if self.phase == "hit":
            self.hit_stmts.append(ctx)
        else:
            self.miss_stmts.append(ctx)


@dataclass
class IndexedBranchContext(FlowContext):
    """Tracks a node with indexed flow outputs (SyncList-based).

    Used by PulseRandom, ImpulseMultiplexer, and similar nodes
    that route impulses to one of N indexed outputs.

    Attributes:
        node_type: The Resonite component type string.
        num_branches: The number of indexed branches.
        input_exprs: Maps input param_name to ExprProxy.
        raw_inputs: Maps input param_name to raw string ID.
        branch_stmts: Maps branch index to statement list.
        active_branch: The currently recording branch index.
        component_tag: UUID for output node references.
        value_output_name: If set, the name of a value output member.
        value_output_type: The type of the value output.
    """

    node_type: str = ""
    num_branches: int = 0
    input_exprs: dict[str, _expr.ExprProxy] = field(default_factory=dict)
    raw_inputs: dict[str, str] = field(default_factory=dict)
    branch_stmts: dict[int, list[Statement]] = field(default_factory=dict)
    active_branch: int | None = None
    component_tag: str = ""
    value_output_name: str | None = None
    value_output_type: type | None = None
    named_flow_outputs: list[str] = field(default_factory=list)
    named_stmts: dict[str, list[Statement]] = field(default_factory=dict)
    is_event_source: bool = False

    def record_write(self, write: WriteRecord) -> None:
        """Append a write to the currently active branch or named output."""
        named = getattr(self, "_active_named", None)
        if named is not None:
            self.named_stmts.setdefault(named, []).append(write)
        elif self.active_branch is not None:
            self.branch_stmts[self.active_branch].append(write)
        else:
            raise RuntimeError(
                "Writes must be inside an indexed branch (pr[0]) "
                "or named output (demux.on_triggered()) context manager."
            )

    def record_nested(self, ctx: FlowContext) -> None:
        """Append a nested flow to the currently active branch or named output."""
        named = getattr(self, "_active_named", None)
        if named is not None:
            self.named_stmts.setdefault(named, []).append(ctx)
        elif self.active_branch is not None:
            self.branch_stmts[self.active_branch].append(ctx)
        else:
            raise RuntimeError(
                "Nested flows must be inside an indexed branch or "
                "named output context manager."
            )


@dataclass
class BareWriteContext(FlowContext):
    """Tracks bare writes inside an Under block."""

    stmts: list[Statement] = field(default_factory=list)

    def record_write(self, write: WriteRecord) -> None:
        """Append a write."""
        self.stmts.append(write)

    def record_nested(self, ctx: FlowContext) -> None:
        """Append a nested flow."""
        self.stmts.append(ctx)


@dataclass
class BindRecord:
    """A permanent binding from a value source to a component field."""

    component: Any
    member_name: str
    expr: _expr.ExprProxy
    slot: workers.Slot
    dynvar_name: str | None = None
    dynvar_space: Any = None


@dataclass
class UnderRecord:
    """All the flow statements recorded inside a single Under block.

    The builder creates a Sequence node (if >1 statement) and one
    trigger to drive it.  If ``is_async`` is True, async variants
    are used for all flow nodes.

    Attributes:
        slot: The slot for ProtoFlux node placement.
        trigger: How the flow is triggered.
        statements: The flow contexts in order.
        is_async: True if any statement contains an async action.
    """

    slot: workers.Slot
    trigger: Trigger | None = None
    statements: list[FlowContext] = field(default_factory=list)
    is_async: bool = False
    is_event_source: bool = False
