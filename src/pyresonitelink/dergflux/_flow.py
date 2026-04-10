"""Flow control contexts and write records for Dergflux.

FlowContext subclasses track condition/count and writes for each flow
construct (If, For, While, bare writes).  WriteRecord captures a
single variable assignment.  These are pure data structures with no
server interaction.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

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


@dataclass
class FlowContext:
    """Base class for all flow control contexts.

    Attributes:
        slot: The slot where ProtoFlux nodes will be placed.
    """

    slot: workers.Slot


@dataclass
class IfContext(FlowContext):
    """Tracks an if-else construct during recording.

    Attributes:
        condition: The boolean expression proxy for the branch.
        true_writes: Writes recorded inside the ``with g.If(...)`` block.
        false_writes: Writes recorded inside the ``with g.Else()`` block.
        phase: Which branch is currently being recorded.
    """

    condition: _expr.ExprProxy = field(default=None)  # type: ignore[assignment]
    true_writes: list[WriteRecord] = field(default_factory=list)
    false_writes: list[WriteRecord] = field(default_factory=list)
    phase: str = "true"

    def record_write(self, write: WriteRecord) -> None:
        """Append a write to the currently active branch."""
        if self.phase == "true":
            self.true_writes.append(write)
        else:
            self.false_writes.append(write)


@dataclass
class ForContext(FlowContext):
    """Tracks a for-loop construct during recording.

    Attributes:
        count: The iteration count expression.
        reverse: Whether to iterate in reverse.
        start_writes: Writes for loop_start (runs once before loop).
        iteration_writes: Writes for loop_iteration (runs each iteration).
        phase: Which section is currently being recorded.
    """

    count: _expr.ExprProxy = field(default=None)  # type: ignore[assignment]
    reverse: _expr.ExprProxy | None = None
    start_writes: list[WriteRecord] = field(default_factory=list)
    iteration_writes: list[WriteRecord] = field(default_factory=list)
    phase: str = "iteration"

    def record_write(self, write: WriteRecord) -> None:
        """Append a write to the currently active section."""
        if self.phase == "start":
            self.start_writes.append(write)
        else:
            self.iteration_writes.append(write)


@dataclass
class RangeContext(FlowContext):
    """Tracks a range-loop construct during recording.

    Attributes:
        start: The loop start value expression.
        end: The loop end value expression.
        step: The loop step size expression.
        start_writes: Writes for loop_start (runs once before loop).
        iteration_writes: Writes for loop_iteration (runs each iteration).
        phase: Which section is currently being recorded.
    """

    start: _expr.ExprProxy = field(default=None)  # type: ignore[assignment]
    end: _expr.ExprProxy = field(default=None)  # type: ignore[assignment]
    step: _expr.ExprProxy | None = None
    start_writes: list[WriteRecord] = field(default_factory=list)
    iteration_writes: list[WriteRecord] = field(default_factory=list)
    phase: str = "iteration"

    def record_write(self, write: WriteRecord) -> None:
        """Append a write to the currently active section."""
        if self.phase == "start":
            self.start_writes.append(write)
        else:
            self.iteration_writes.append(write)


@dataclass
class WhileContext(FlowContext):
    """Tracks a while-loop construct during recording.

    Attributes:
        condition: The loop condition expression.
        writes: Writes for loop_iteration.
    """

    condition: _expr.ExprProxy = field(default=None)  # type: ignore[assignment]
    writes: list[WriteRecord] = field(default_factory=list)

    def record_write(self, write: WriteRecord) -> None:
        """Append a write to the loop body."""
        self.writes.append(write)


@dataclass
class BareWriteContext(FlowContext):
    """Tracks bare writes inside an Under block (not inside If/For/While).

    These become standalone WriteDynamicValueVariable chains in a
    Sequence.
    """

    writes: list[WriteRecord] = field(default_factory=list)

    def record_write(self, write: WriteRecord) -> None:
        """Append a write."""
        self.writes.append(write)


@dataclass
class UnderRecord:
    """All the flow statements recorded inside a single Under block.

    The builder creates a Sequence node (if >1 statement) and one
    trigger to drive it.

    Attributes:
        slot: The slot for ProtoFlux node placement.
        trigger: How the flow is triggered.
        statements: The flow contexts in order.
    """

    slot: workers.Slot
    trigger: Trigger | None = None
    statements: list[FlowContext] = field(default_factory=list)
