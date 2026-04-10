"""Graph: the main Dergflux API object.

A Graph records variable declarations, expression trees, and flow
control structures.  Call ``await g.build(resolink)`` to materialize
everything as ProtoFlux components on the server.
"""

from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Iterator

from pyresonitelink.dergflux import _expr
from pyresonitelink.dergflux import _flow
from pyresonitelink.dergflux import _space

if TYPE_CHECKING:
    from pyresonitelink.data import protocols
    from pyresonitelink.data import workers


@dataclass
class _UnderContext:
    """Internal state for an active Under() block."""

    slot: workers.Slot
    trigger: _flow.Trigger | None = None
    record: _flow.UnderRecord | None = None


class ForProxy:
    """Proxy returned by ``g.For()`` and ``g.Range()`` for loop sections.

    Use ``f.OnStart()`` and ``f.OnIterate()`` as context managers
    to record statements for loop_start and loop_iteration respectively.
    """

    def __init__(
        self, graph: Graph, ctx: _flow.ForContext | _flow.RangeContext,
    ) -> None:
        self._graph = graph
        self._ctx = ctx

    @contextmanager
    def OnStart(self) -> Iterator[None]:
        """Context manager for loop_start — runs once before the loop.

        Yields:
            Nothing.  Statements go to loop_start.
        """
        self._ctx.phase = "start"
        self._graph._flow_stack.append(self._ctx)
        try:
            yield
        finally:
            self._graph._flow_stack.pop()
            self._ctx.phase = "iteration"

    @contextmanager
    def OnIterate(self) -> Iterator[_expr.ExprProxy]:
        """Context manager for loop_iteration — runs each iteration.

        Yields:
            An ``ExprProxy`` for the iteration index (Int).
        """
        self._ctx.phase = "iteration"
        index_proxy = _expr.ExprProxy(_expr.LoopIndexNode())
        self._graph._flow_stack.append(self._ctx)
        try:
            yield index_proxy
        finally:
            self._graph._flow_stack.pop()


class Graph:
    """Top-level Dergflux API for building ProtoFlux graphs.

    Use ``g.Under(slot)`` to set the default slot and trigger for
    everything inside the block.  Flow statements inside ``Under``
    are chained via a Sequence node when there are multiple.

    Usage::

        g = Graph()

        s = g.Space(slot)
        s.x = s.FloatVar("x")
        s.z = s.FloatVar("z")

        with g.Under(slot):
            with g.If(s.x < 3):
                s.z = s.x + 3
            with g.Else():
                s.z = s.x - 3

            # Continuation: runs after the If/Else completes
            s.z = s.z + 1

        await g.build(resolink)
    """

    def __init__(self) -> None:
        self._spaces: list[_space.Space] = []
        self._flow_stack: list[_flow.FlowContext] = []
        self._under_records: list[_flow.UnderRecord] = []
        self._under_stack: list[_UnderContext] = []

    # --- Slot / trigger context ---

    @contextmanager
    def Under(
        self,
        slot: workers.Slot,
        trigger: str | tuple[str, type] | None = None,
    ) -> Iterator[_expr.ExprProxy | None]:
        """Context manager that sets the default slot and trigger.

        Everything inside the block — ``Space()``, ``If()``, ``For()``,
        ``While()``, and bare writes — will use this slot.  The trigger
        controls what drives the impulse flow.

        Multiple flow statements inside a single ``Under`` block are
        chained via a Sequence node — each runs to completion before
        the next starts.

        **No trigger (default) — fires every frame**::

            with g.Under(slot):
                with g.If(s.x < 3):
                    s.z = s.x + 3

        This creates an ``Update`` node that fires the flow every frame.

        **Named dynamic impulse — no argument**::

            with g.Under(slot, trigger="MyImpulse"):
                with g.If(s.x < 3):
                    s.z = s.x + 3

        This creates a ``DynamicImpulseReceiver`` that fires when a
        ``DynamicImpulseTrigger`` sends an impulse with the tag
        ``"MyImpulse"``.

        **Named dynamic impulse — with typed value**::

            with g.Under(slot, trigger=("MyImpulse", primitives.Float)) as value:
                s.z = value + 3

        This creates a ``DynamicImpulseReceiverWithValue<Float>`` that
        fires when triggered and provides the received value as an
        ``ExprProxy``.  Use the ``as`` clause to capture it.

        Args:
            slot: The slot to place ProtoFlux nodes on.
            trigger: How the flow is triggered:

                - ``None`` (default): ``Update`` node, fires every frame.
                - ``"tag"``: ``DynamicImpulseReceiver`` with the given tag.
                - ``("tag", type)``: ``DynamicImpulseReceiverWithValue<type>``
                  with the given tag.  The context manager yields an
                  ``ExprProxy`` for the received value.

        Yields:
            An ``ExprProxy`` for the received value when ``trigger`` is a
            ``(tag, type)`` tuple, otherwise ``None``.
        """
        parsed_trigger: _flow.Trigger | None = None
        value_proxy: _expr.ExprProxy | None = None

        if isinstance(trigger, str):
            parsed_trigger = _flow.Trigger(tag=trigger)
        elif isinstance(trigger, tuple):
            tag, value_type = trigger
            parsed_trigger = _flow.Trigger(tag=tag, value_type=value_type)
            value_proxy = _expr.ExprProxy(
                _expr.TriggerValueNode(value_type),
            )

        record = _flow.UnderRecord(
            slot=slot, trigger=parsed_trigger,
        )
        ctx = _UnderContext(
            slot=slot, trigger=parsed_trigger, record=record,
        )
        self._under_stack.append(ctx)
        try:
            yield value_proxy
        finally:
            self._under_stack.pop()
            if record.statements:
                self._under_records.append(record)

    def _active_under(self) -> _UnderContext | None:
        """Return the current Under context, or None."""
        if self._under_stack:
            return self._under_stack[-1]
        return None

    def _active_slot(self) -> workers.Slot | None:
        """Return the current default slot, or None."""
        ctx = self._active_under()
        return ctx.slot if ctx is not None else None

    def _active_flow(self) -> _flow.FlowContext | None:
        """Return the currently active flow context, or None."""
        if self._flow_stack:
            return self._flow_stack[-1]
        return None

    def _require_under(self) -> _UnderContext:
        """Return the active Under context, or raise."""
        under = self._active_under()
        if under is None:
            raise RuntimeError(
                "Flow control must be used inside g.Under(slot)."
            )
        return under

    def _record_statement(self, ctx: _flow.FlowContext) -> None:
        """Add a completed flow statement to the active Under record."""
        under = self._active_under()
        if under is not None and under.record is not None:
            under.record.statements.append(ctx)

    # --- Space factory ---

    def Space(
        self,
        slot: workers.Slot | None = None,
        name: str | None = None,
    ) -> _space.Space:
        """Create a Space bound to a slot.

        Args:
            slot: The Resonite slot for the DynamicVariableSpace. If
                omitted, uses the slot from the enclosing ``Under()``
                context.
            name: Optional space name. If a DynamicVariableSpace with
                this name already exists on the slot, it is reused.

        Returns:
            A Space proxy for declaring and using variables.

        Raises:
            RuntimeError: If no slot is provided and there is no active
                ``Under()`` context.
        """
        if slot is None:
            slot = self._active_slot()
        if slot is None:
            raise RuntimeError(
                "Space() requires a slot. Either pass one explicitly "
                "or use inside g.Under(slot)."
            )
        space = _space.Space(self, slot, space_name=name)
        self._spaces.append(space)
        return space

    # --- Flow control ---

    @contextmanager
    def If(self, condition: object) -> Iterator[None]:
        """Context manager for an if-branch.

        Must be used inside a ``g.Under(slot)`` context.

        Args:
            condition: An ExprProxy evaluating to bool.

        Yields:
            Nothing.  Writes inside the block are recorded as true-branch.
        """
        if not isinstance(condition, _expr.ExprProxy):
            raise TypeError(
                f"If() condition must be an ExprProxy, got {type(condition).__name__}."
            )
        under = self._require_under()
        ctx = _flow.IfContext(
            condition=condition,
            slot=under.slot,
        )
        self._flow_stack.append(ctx)
        try:
            yield
        finally:
            self._flow_stack.pop()
            self._record_statement(ctx)

    @contextmanager
    def Else(self) -> Iterator[None]:
        """Context manager for the else-branch of the most recent If.

        Yields:
            Nothing.  Writes inside the block are recorded as false-branch.
        """
        under = self._active_under()
        if under is None or under.record is None or not under.record.statements:
            raise RuntimeError("Else() without a preceding If().")
        last = under.record.statements[-1]
        if not isinstance(last, _flow.IfContext):
            raise RuntimeError("Else() without a preceding If().")
        # Remove from statements, switch to false phase, re-record when done
        under.record.statements.pop()
        last.phase = "false"
        self._flow_stack.append(last)
        try:
            yield
        finally:
            self._flow_stack.pop()
            self._record_statement(last)

    @contextmanager
    def For(
        self,
        count: object,
        reverse: object | None = None,
    ) -> Iterator[ForProxy]:
        """Context manager for a for-loop.

        Yields a ``ForProxy`` with ``OnStart()`` and ``OnIterate()``
        context managers for the loop sections.

        Usage::

            with g.Under(slot):
                with g.For(10) as f:
                    with f.OnStart():
                        s.total = 0
                    with f.OnIterate() as i:
                        s.total = s.total + i

        Must be used inside a ``g.Under(slot)`` context.

        Args:
            count: An ExprProxy or literal for the iteration count.
            reverse: Optional ExprProxy or bool to iterate in reverse.

        Yields:
            A ``ForProxy`` for accessing loop sections.
        """
        count_proxy = _expr._coerce(count)
        reverse_proxy: _expr.ExprProxy | None = None
        if reverse is not None:
            reverse_proxy = _expr._coerce(reverse)

        under = self._require_under()
        ctx = _flow.ForContext(
            count=count_proxy,
            reverse=reverse_proxy,
            slot=under.slot,
        )
        proxy = ForProxy(self, ctx)
        try:
            yield proxy
        finally:
            self._record_statement(ctx)

    @contextmanager
    def Range(
        self,
        start: object,
        end: object,
        step: object | None = None,
    ) -> Iterator[ForProxy]:
        """Context manager for a range loop.

        Iterates from ``start`` to ``end`` with ``step`` increments,
        like Python's ``range()``.  Yields a ``ForProxy`` with
        ``OnStart()`` and ``OnIterate()`` context managers.

        Usage::

            with g.Under(slot):
                with g.Range(0, 10, 2) as f:
                    with f.OnIterate() as i:
                        s.total = s.total + i

        Must be used inside a ``g.Under(slot)`` context.

        Args:
            start: Loop start value (Int expression or literal).
            end: Loop end value (Int expression or literal).
            step: Loop step size (Int expression or literal).
                Defaults to 1 if omitted.

        Yields:
            A ``ForProxy`` for accessing loop sections.
        """
        start_proxy = _expr._coerce(start)
        end_proxy = _expr._coerce(end)
        step_proxy: _expr.ExprProxy | None = None
        if step is not None:
            step_proxy = _expr._coerce(step)

        under = self._require_under()
        ctx = _flow.RangeContext(
            start=start_proxy,
            end=end_proxy,
            step=step_proxy,
            slot=under.slot,
        )
        proxy = ForProxy(self, ctx)
        try:
            yield proxy
        finally:
            self._record_statement(ctx)

    @contextmanager
    def While(self, condition: object) -> Iterator[None]:
        """Context manager for a while-loop.

        Usage::

            with g.Under(slot):
                with g.While(s.x > 0):
                    s.x = s.x - 1

        Must be used inside a ``g.Under(slot)`` context.

        Args:
            condition: An ExprProxy evaluating to bool.

        Yields:
            Nothing.
        """
        if not isinstance(condition, _expr.ExprProxy):
            raise TypeError(
                f"While() condition must be an ExprProxy, "
                f"got {type(condition).__name__}."
            )
        under = self._require_under()
        ctx = _flow.WhileContext(
            condition=condition,
            slot=under.slot,
        )
        self._flow_stack.append(ctx)
        try:
            yield
        finally:
            self._flow_stack.pop()
            self._record_statement(ctx)

    # --- Build ---

    async def build(self, resolink: protocols.ResoniteLinkClient) -> None:
        """Materialize the recorded graph as ProtoFlux components.

        Args:
            resolink: A connected ResoniteLink client.
        """
        from pyresonitelink.dergflux import _builder

        await _builder.build_graph(self, resolink)
