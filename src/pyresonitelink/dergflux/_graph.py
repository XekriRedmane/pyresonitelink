"""Graph: the main Dergflux API object.

A Graph records variable declarations, expression trees, and flow
control structures.  Call ``await g.build(resolink)`` to materialize
everything as ProtoFlux components on the server.
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import TYPE_CHECKING, Iterator

from pyresonitelink.dergflux import _flow
from pyresonitelink.dergflux import _space

if TYPE_CHECKING:
    from pyresonitelink.data import protocols
    from pyresonitelink.data import workers


class Graph:
    """Top-level Dergflux API for building ProtoFlux graphs.

    Usage::

        g = Graph()
        s = g.Space(slot)
        s.x = s.FloatVar("x")
        s.z = s.FloatVar("z")

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

    # --- Space factory ---

    def Space(
        self, slot: workers.Slot, name: str | None = None,
    ) -> _space.Space:
        """Create a Space bound to a slot.

        Args:
            slot: The Resonite slot for the DynamicVariableSpace.
            name: Optional space name. If a DynamicVariableSpace with
                this name already exists on the slot, it is reused.

        Returns:
            A Space proxy for declaring and using variables.
        """
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

        Args:
            condition: An ExprProxy evaluating to bool.

        Yields:
            Nothing.  Writes inside the block are recorded as true-branch.
        """
        from pyresonitelink.dergflux import _expr

        if not isinstance(condition, _expr.ExprProxy):
            raise TypeError(
                f"If() condition must be an ExprProxy, got {type(condition).__name__}."
            )
        ctx = _flow.IfContext(condition=condition)
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
