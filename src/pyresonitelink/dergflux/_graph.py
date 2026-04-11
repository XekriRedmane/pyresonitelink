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
        self._bindings: list[_flow.DriveRecord] = []

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
        """Add a completed flow statement to the appropriate parent.

        If there's an active flow context (e.g. inside a For loop's
        OnIterate), the statement is nested inside that flow's body.
        Otherwise it's added to the top-level Under record.

        Also detects async actions and marks the UnderRecord as async.
        """
        from pyresonitelink.dergflux import _action

        # Check if this is async and propagate to UnderRecord
        under = self._active_under()
        if under is not None and under.record is not None:
            if isinstance(ctx, _action.ActionContext):
                if ctx.action_def.is_async:
                    under.record.is_async = True
                if ctx.action_def.is_event_source:
                    under.record.is_event_source = True

        # If there's an active flow context, nest inside it
        active = self._active_flow()
        if active is not None:
            active.record_nested(ctx)
            return

        # Otherwise, top-level statement on the UnderRecord
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

    @contextmanager
    def Action(
        self,
        action_def: Any,
        **kwargs: Any,
    ) -> Iterator[Any]:
        """Context manager for a generic action node.

        Action nodes are ProtoFlux nodes with value inputs, multiple
        flow outputs (branches), and optional value outputs.  Define
        them once with ``ActionDef``, then use them with this method.

        Usage::

            with g.Under(slot):
                with g.Action(MyAction, origin=s.pos) as r:
                    with r.on_hit():
                        s.distance = r.hit_distance

        Must be used inside a ``g.Under(slot)`` context.

        Args:
            action_def: An ``ActionDef`` describing the node.
            **kwargs: Input values, matching the keys in
                ``action_def.inputs``.

        Yields:
            An ``ActionProxy`` with flow output context managers and
            value output properties.
        """
        from pyresonitelink.dergflux import _action

        ctx, proxy = _action.create_action_context(self, action_def, kwargs)
        try:
            yield proxy
        finally:
            self._record_statement(ctx)

    # --- Named action shortcuts: event sources ---

    @contextmanager
    def FireOnTrue(self, **kwargs: Any) -> Iterator[Any]:
        """Fire an impulse when condition transitions to true (rising edge).

        Usage::

            with g.Under(slot):
                with g.FireOnTrue(condition=s.flag) as e:
                    with e.on_changed():
                        s.count = s.count + 1
        """
        from pyresonitelink.dergflux import actions
        with self.Action(actions.FireOnTrue, **kwargs) as proxy:
            yield proxy

    @contextmanager
    def FireOnFalse(self, **kwargs: Any) -> Iterator[Any]:
        """Fire an impulse when condition transitions to false (falling edge).

        Usage::

            with g.Under(slot):
                with g.FireOnFalse(condition=s.flag) as e:
                    with e.on_changed():
                        s.count = s.count + 1
        """
        from pyresonitelink.dergflux import actions
        with self.Action(actions.FireOnFalse, **kwargs) as proxy:
            yield proxy

    @contextmanager
    def FireOnLocalTrue(self, **kwargs: Any) -> Iterator[Any]:
        """Fire a local impulse when condition transitions to true.

        Local variant — only fires for the local user.
        """
        from pyresonitelink.dergflux import actions
        with self.Action(actions.FireOnLocalTrue, **kwargs) as proxy:
            yield proxy

    @contextmanager
    def FireOnLocalFalse(self, **kwargs: Any) -> Iterator[Any]:
        """Fire a local impulse when condition transitions to false.

        Local variant — only fires for the local user.
        """
        from pyresonitelink.dergflux import actions
        with self.Action(actions.FireOnLocalFalse, **kwargs) as proxy:
            yield proxy

    @contextmanager
    def FireOnValueChange(self, **kwargs: Any) -> Iterator[Any]:
        """Fire an impulse when a value changes.

        Usage::

            with g.Under(slot):
                with g.FireOnValueChange(value=s.x) as e:
                    with e.on_changed():
                        s.change_count = s.change_count + 1
        """
        from pyresonitelink.dergflux import actions
        with self.Action(actions.FireOnValueChange, **kwargs) as proxy:
            yield proxy

    @contextmanager
    def FireOnLocalValueChange(self, **kwargs: Any) -> Iterator[Any]:
        """Fire a local impulse when a value changes."""
        from pyresonitelink.dergflux import actions
        with self.Action(actions.FireOnLocalValueChange, **kwargs) as proxy:
            yield proxy

    @contextmanager
    def FireOnObjectValueChange(self, **kwargs: Any) -> Iterator[Any]:
        """Fire an impulse when an object value changes."""
        from pyresonitelink.dergflux import actions
        with self.Action(actions.FireOnObjectValueChange, **kwargs) as proxy:
            yield proxy

    @contextmanager
    def FireOnLocalObjectChange(self, **kwargs: Any) -> Iterator[Any]:
        """Fire a local impulse when an object value changes."""
        from pyresonitelink.dergflux import actions
        with self.Action(actions.FireOnLocalObjectChange, **kwargs) as proxy:
            yield proxy

    @contextmanager
    def FireOnRefChange(self, **kwargs: Any) -> Iterator[Any]:
        """Fire an impulse when a reference changes."""
        from pyresonitelink.dergflux import actions
        with self.Action(actions.FireOnRefChange, **kwargs) as proxy:
            yield proxy

    @contextmanager
    def FireOnTypeChange(self, **kwargs: Any) -> Iterator[Any]:
        """Fire an impulse when a Type value changes."""
        from pyresonitelink.dergflux import actions
        with self.Action(actions.FireOnTypeChange, **kwargs) as proxy:
            yield proxy

    @contextmanager
    def FireWhileTrue(self, **kwargs: Any) -> Iterator[Any]:
        """Fire an impulse every frame while condition is true.

        Usage::

            with g.Under(slot):
                with g.FireWhileTrue(condition=s.active) as e:
                    with e.on_update():
                        s.elapsed = s.elapsed + 1
        """
        from pyresonitelink.dergflux import actions
        with self.Action(actions.FireWhileTrue, **kwargs) as proxy:
            yield proxy

    @contextmanager
    def LocalFireWhileTrue(self, **kwargs: Any) -> Iterator[Any]:
        """Fire a local impulse every frame while condition is true.

        Local variant — only fires for the local user.
        """
        from pyresonitelink.dergflux import actions
        with self.Action(actions.LocalFireWhileTrue, **kwargs) as proxy:
            yield proxy

    @contextmanager
    def UpdatesTimer(self, **kwargs: Any) -> Iterator[Any]:
        """Fire an impulse every N engine updates.

        Usage::

            with g.Under(slot):
                with g.UpdatesTimer(interval=60) as e:
                    with e.on_update():
                        s.tick = s.tick + 1
        """
        from pyresonitelink.dergflux import actions
        with self.Action(actions.UpdatesTimer, **kwargs) as proxy:
            yield proxy

    @contextmanager
    def SecondsTimer(self, **kwargs: Any) -> Iterator[Any]:
        """Fire an impulse every N seconds.

        Usage::

            with g.Under(slot):
                with g.SecondsTimer(interval=1.0) as e:
                    with e.on_update():
                        s.seconds = s.seconds + 1
        """
        from pyresonitelink.dergflux import actions
        with self.Action(actions.SecondsTimer, **kwargs) as proxy:
            yield proxy

    @contextmanager
    def DelaySeconds(self, **kwargs: Any) -> Iterator[Any]:
        """Delay for a duration then fire.

        Async — the enclosing flow uses async variants automatically.

        Usage::

            with g.Under(slot):
                with g.DelaySeconds(duration=2.0) as d:
                    with d.on_triggered():
                        s.state = "delayed"

        The ``duration`` type determines the variant:
        Float (default), Double, or Int seconds.

        Also has a ``next`` flow output that fires immediately
        (before the delay).
        """
        from pyresonitelink.dergflux import actions
        with self.Action(actions.DelaySecondsFloat, **kwargs) as proxy:
            yield proxy

    # --- Named action shortcuts: impulse-triggered ---

    @contextmanager
    def RaycastOne(self, **kwargs: Any) -> Iterator[Any]:
        """Context manager for a RaycastOne physics query.

        Casts a ray and branches into hit/miss flows.

        Usage::

            with g.Under(slot):
                with g.RaycastOne(origin=s.pos, direction=s.dir) as r:
                    with r.on_hit():
                        s.hit_pos = r.hit_point
                    with r.on_miss():
                        s.distance = -1

        Args:
            origin: Ray origin (Float3).
            direction: Ray direction (Float3).
            max_distance: Max ray distance (Float).
            hit_triggers: Hit triggers (Bool).
            users_only: Only hit users (Bool).
            debug_duration: Debug visualization duration (Float).
            root: Root slot for coordinate space.

        Yields:
            An ``ActionProxy`` with ``on_hit()``, ``on_miss()``, and
            value outputs: ``hit_point``, ``hit_normal``,
            ``hit_distance``, ``hit_triangle_index``.
        """
        from pyresonitelink.dergflux import actions
        with self.Action(actions.RaycastOne, **kwargs) as proxy:
            yield proxy

    @contextmanager
    def PlayOneShot(self, **kwargs: Any) -> Iterator[Any]:
        """Context manager for playing a one-shot audio clip.

        Usage::

            with g.Under(slot):
                with g.PlayOneShot(clip=clip_ref, volume=1.0) as r:
                    with r.on_started_playing():
                        s.state = "playing"

        Args:
            clip: Audio clip reference.
            volume: Playback volume (Float).
            speed: Playback speed (Float).
            point: Spatial position (Float3).
            root: Root slot.
            local_only: Only play locally (Bool).
            (and other audio parameters)

        Yields:
            An ``ActionProxy`` with ``on_started_playing()``.
        """
        from pyresonitelink.dergflux import actions
        with self.Action(actions.PlayOneShot, **kwargs) as proxy:
            yield proxy

    @contextmanager
    def PlayOneShotAndWait(self, **kwargs: Any) -> Iterator[Any]:
        """Context manager for playing a one-shot audio clip and waiting.

        Usage::

            with g.Under(slot):
                with g.PlayOneShotAndWait(clip=clip_ref, volume=1.0) as r:
                    with r.on_started_playing():
                        s.state = "playing"
                    with r.on_finished_playing():
                        s.state = "finished"

        Args:
            clip: Audio clip reference.
            volume: Playback volume (Float).
            speed: Playback speed (Float).
            point: Spatial position (Float3).
            root: Root slot.
            local_only: Only play locally (Bool).
            (and other audio parameters)

        Yields:
            An ``ActionProxy`` with ``on_started_playing()`` and
            ``on_finished_playing()``.
        """
        from pyresonitelink.dergflux import actions
        with self.Action(actions.PlayOneShotAndWait, **kwargs) as proxy:
            yield proxy

    @contextmanager
    def SlotChildrenEvents(self, **kwargs: Any) -> Iterator[Any]:
        """Context manager for monitoring slot child add/remove events.

        Usage::

            with g.Under(slot):
                with g.SlotChildrenEvents(instance=watched_slot) as e:
                    with e.on_child_added():
                        s.last_child = e.child
                    with e.on_child_removed():
                        s.removed = e.child

        Args:
            instance: The slot to monitor (Slot instance or ID).

        Yields:
            An ``ActionProxy`` with ``on_child_added()``,
            ``on_child_removed()``, and ``child`` (Slot output).
        """
        from pyresonitelink.dergflux import actions
        with self.Action(actions.SlotChildrenEvents, **kwargs) as proxy:
            yield proxy

    # --- Bindings ---

    def Bind(
        self,
        expr: object,
        component: Any,
        member_name: str,
        slot: workers.Slot | None = None,
    ) -> None:
        """Permanently bind a ProtoFlux expression to a component field.

        The binding mechanism depends on the source:

        - **Dynamic variable** (e.g. ``s.x``): Uses
          ``DynamicValueVariableDriver<T>`` for value types or
          ``DynamicReferenceVariableDriver<T>`` for reference types.
          The driver reads the named variable and continuously drives
          the target field.
        - **General expression** (e.g. ``i``, ``s.x + 1``): Uses
          ``ValueFieldDrive<T>`` to drive the target field from the
          ProtoFlux expression.

        This is a permanent, one-time binding — the field always
        reflects the source's current value.  A field can only be
        bound once; attempting to rebind it raises an error.

        Usage::

            # Bind a loop counter to a field
            with g.Under(slot):
                with g.For(3) as f:
                    with f.OnIterate() as i:
                        g.Bind(i, mux, "Index")

            # Bind a dynamic variable to a field
            g.Bind(s.volume, audio_output, "Volume", slot=slot)

        Args:
            expr: The expression to bind from (ExprProxy or literal).
            component: The target component (a GeneratedComponent instance).
            member_name: The Resonite member name to bind to (e.g. ``"Index"``).
            slot: The slot to place the binding node on.  If omitted, uses
                the active ``Under()`` slot.

        Raises:
            RuntimeError: If no slot is available, or if the field is
                already bound.
            ValueError: If the component has no member with the given name.
        """
        expr_proxy = _expr._coerce(expr)
        bind_slot = slot
        if bind_slot is None:
            bind_slot = self._active_slot()
        if bind_slot is None:
            raise RuntimeError(
                "Bind() requires a slot. Either pass one explicitly "
                "or use inside g.Under(slot)."
            )
        member = component.get_member(member_name)
        if member is None:
            raise ValueError(
                f"Component {component!r} has no member '{member_name}'."
            )
        # Check for duplicate binding
        for existing in self._bindings:
            if (existing.component is component
                    and existing.member_name == member_name):
                raise RuntimeError(
                    f"Field '{member_name}' on {component!r} is already "
                    f"bound. A field can only be bound once."
                )
        # Detect if the source is a bare dynamic variable read
        dynvar_name: str | None = None
        dynvar_space: Any = None
        node = expr_proxy._node
        if isinstance(node, _expr.VarReadNode):
            dynvar_name = node.var_name
            dynvar_space = node.space

        self._bindings.append(_flow.BindRecord(
            component=component,
            member_name=member_name,
            expr=expr_proxy,
            slot=bind_slot,
            dynvar_name=dynvar_name,
            dynvar_space=dynvar_space,
        ))

    # --- Build ---

    async def build(self, resolink: protocols.ResoniteLinkClient) -> None:
        """Materialize the recorded graph as ProtoFlux components.

        Args:
            resolink: A connected ResoniteLink client.
        """
        from pyresonitelink.dergflux import _builder

        await _builder.build_graph(self, resolink)
