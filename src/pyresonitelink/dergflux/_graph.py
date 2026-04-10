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


class Graph:
    """Top-level Dergflux API for building ProtoFlux graphs.

    Use ``g.Under(slot)`` to set the default slot and trigger for
    everything inside the block.

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

        await g.build(resolink)
    """

    def __init__(self) -> None:
        self._spaces: list[_space.Space] = []
        self._flow_stack: list[_flow.IfContext] = []
        self._completed_flows: list[_flow.IfContext] = []
        self._under_stack: list[_UnderContext] = []

    # --- Slot / trigger context ---

    @contextmanager
    def Under(
        self,
        slot: workers.Slot,
        trigger: str | tuple[str, type] | None = None,
    ) -> Iterator[_expr.ExprProxy | None]:
        """Context manager that sets the default slot and trigger.

        Everything inside the block — ``Space()``, ``If()``, variable
        declarations without an explicit slot — will use this slot.
        The trigger controls what drives the impulse flow.

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

        ctx = _UnderContext(slot=slot, trigger=parsed_trigger)
        self._under_stack.append(ctx)
        try:
            yield value_proxy
        finally:
            self._under_stack.pop()

    def _active_under(self) -> _UnderContext | None:
        """Return the current Under context, or None."""
        if self._under_stack:
            return self._under_stack[-1]
        return None

    def _active_slot(self) -> workers.Slot | None:
        """Return the current default slot, or None."""
        ctx = self._active_under()
        return ctx.slot if ctx is not None else None

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

    def _active_flow(self) -> _flow.IfContext | None:
        """Return the currently active flow context, or None."""
        if self._flow_stack:
            return self._flow_stack[-1]
        return None

    @contextmanager
    def If(self, condition: object) -> Iterator[None]:
        """Context manager for an if-branch.

        Must be used inside a ``g.Under(slot)`` context so that the
        generated ProtoFlux nodes have a slot to be placed on.

        Args:
            condition: An ExprProxy evaluating to bool.

        Yields:
            Nothing.  Writes inside the block are recorded as true-branch.

        Raises:
            RuntimeError: If not inside a ``g.Under()`` context.
        """
        if not isinstance(condition, _expr.ExprProxy):
            raise TypeError(
                f"If() condition must be an ExprProxy, got {type(condition).__name__}."
            )
        under = self._active_under()
        if under is None:
            raise RuntimeError(
                "If() must be used inside g.Under(slot)."
            )
        ctx = _flow.IfContext(
            condition=condition,
            slot=under.slot,
            trigger=under.trigger,
        )
        self._flow_stack.append(ctx)
        try:
            yield
        finally:
            self._flow_stack.pop()
            self._completed_flows.append(ctx)

    @contextmanager
    def Else(self) -> Iterator[None]:
        """Context manager for the else-branch of the most recent If.

        Yields:
            Nothing.  Writes inside the block are recorded as false-branch.
        """
        if not self._completed_flows:
            raise RuntimeError("Else() without a preceding If().")
        ctx = self._completed_flows.pop()
        ctx.phase = "false"
        self._flow_stack.append(ctx)
        try:
            yield
        finally:
            self._flow_stack.pop()
            self._completed_flows.append(ctx)

    # --- Build ---

    async def build(self, resolink: protocols.ResoniteLinkClient) -> None:
        """Materialize the recorded graph as ProtoFlux components.

        Args:
            resolink: A connected ResoniteLink client.
        """
        from pyresonitelink.dergflux import _builder

        await _builder.build_graph(self, resolink)
