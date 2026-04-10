# Sync vs Async Flow in ProtoFlux

ProtoFlux has two kinds of impulse flow: **sync** and **async**. This
distinction affects which flow nodes you use and how they wire together.
Dergflux handles this automatically, but understanding the model is
important.

## The Two Impulse Types

### Sync impulses (`ISyncNodeOperation`)

Sync impulses execute within a single engine update. The entire chain
from trigger to final node runs in one frame. If a sync chain takes
too long, it blocks the engine.

Examples of sync nodes:
- `WriteDynamicValueVariable<T>` / `WriteDynamicObjectVariable<T>`
- `If`, `For`, `While`, `Sequence`
- `DynamicImpulseReceiver`, `DynamicImpulseTrigger`
- `Update`, `FireOnTrue`

### Async impulses (`INodeOperation`)

Async impulses can suspend and resume across frames. They're used for
operations that take time — playing audio, waiting for delays, making
network requests.

Examples of async nodes:
- `PlayOneShotAndWait` (waits for audio to finish)
- `Delay` (waits for a duration)
- `AsyncFor`, `AsyncWhile`, `AsyncSequence`
- `AsyncDynamicImpulseReceiver`

## The Key Insight: Async Accepts Sync

`ISyncNodeOperation` **extends** `INodeOperation`. This means:

- **Async flow outputs accept both sync and async targets.** An
  `AsyncFor.LoopIteration` (targeting `INodeOperation`) can wire to
  a `WriteDynamicValueVariable` (which is `ISyncNodeOperation`) OR
  to a `PlayOneShotAndWait` (which is async).

- **Sync flow outputs only accept sync targets.** A sync `For.LoopIteration`
  (targeting `ISyncNodeOperation`) CANNOT wire to `PlayOneShotAndWait`.

This means you can freely mix sync operations (variable writes, if/else)
inside an async flow. The sync nodes simply execute as part of the async
task.

## When to Use Async

If ANY operation in a flow chain is async, all enclosing flow nodes
must use their async variants:

| Sync variant | Async variant |
|---|---|
| `For` | `AsyncFor` |
| `While` | `AsyncWhile` |
| `Sequence` | `AsyncSequence` |
| `DynamicImpulseReceiver` | `AsyncDynamicImpulseReceiver` |
| `DynamicImpulseReceiverWithValue` | `AsyncDynamicImpulseReceiverWithValue` |

Nodes that are always sync and work in both contexts:
- `WriteDynamicValueVariable<T>` / `WriteDynamicObjectVariable<T>`
- `If` (no async variant exists — it's always sync, but works inside async flows)
- `ValueFieldDrive<T>` (not impulse-driven, always active)

## Node Interface Summary

| Node | Implements | Outputs target |
|---|---|---|
| `For` | `ISyncNodeOperation` | `ISyncNodeOperation` (start/iteration), `INodeOperation` (end) |
| `AsyncFor` | `IAsyncNodeOperation` | `INodeOperation` (start/iteration/end) |
| `While` | `ISyncNodeOperation` | `ISyncNodeOperation` (start/iteration), `INodeOperation` (end) |
| `AsyncWhile` | `IAsyncNodeOperation` | `INodeOperation` (start/iteration/end) |
| `Sequence` | `ISyncNodeOperation` | SyncList of `ISyncNodeOperation` |
| `AsyncSequence` | `IAsyncNodeOperation` | SyncList of `INodeOperation` |
| `If` | `ISyncNodeOperation` | `INodeOperation` (on_true/on_false) |
| `WriteDVV<T>` | `ISyncNodeOperation` | `INodeOperation` (on_success/on_failed) |
| `DynamicImpulseReceiver` | — | `ISyncNodeOperation` (on_triggered) |
| `AsyncDynamicImpulseReceiver` | — | `INodeOperation` (on_triggered) |
| `PlayOneShotAndWait` | `IAsyncNodeOperation` | `INodeOperation` (on_started/on_finished) |
| `StartAsyncTask` | `ISyncNodeOperation` | `INodeOperation` (task_start) |
| `Update` | — | `ISyncNodeOperation` (on_update) |

### Notable details

- **`For.LoopEnd` targets `INodeOperation`**, not `ISyncNodeOperation`.
  This is because after a sync loop finishes, the continuation might be
  async. Same for `While.LoopEnd`.

- **`If.OnTrue` and `If.OnFalse` target `INodeOperation`**, so If
  branches can contain async nodes. But `If` itself is `ISyncNodeOperation`,
  so it can only be triggered by sync or async-compatible triggers.

- **`WriteDVV.OnSuccess` targets `INodeOperation`**, so writes can chain
  into async operations.

## `StartAsyncTask`

`StartAsyncTask` bridges from sync to async:
- It implements `ISyncNodeOperation` (can be triggered by sync impulses)
- Its `TaskStart` output targets `INodeOperation` (can start async tasks)
- Has `OnStarted` and `OnFailed` continuations

Use this when you need to kick off an async operation from a sync trigger
like `Update`. In Dergflux, this bridging is handled automatically when
the builder detects async actions in a flow.

## How Dergflux Handles This

Dergflux automatically detects whether a flow is sync or async:

1. If any action in an `Under` block is marked async (e.g.
   `PlayOneShotAndWait`), the builder uses async variants for all
   flow nodes: `AsyncFor`, `AsyncWhile`, `AsyncSequence`.

2. Sync operations (`WriteDynamicValueVariable`, `If`) work in both
   contexts — they implement `ISyncNodeOperation` which is accepted
   by async flow outputs.

3. **Triggers and receivers are always sync.** A `StartAsyncTask` node
   bridges from the sync trigger/receiver to the async flow entry.
   This is critical — see below.

The user doesn't need to think about sync vs async — Dergflux figures
it out from the actions used.

## Why Triggers Are Always Sync

A sync `DynamicImpulseTrigger` can only trigger sync receivers
(`DynamicImpulseReceiver`), not async ones
(`AsyncDynamicImpulseReceiver`). Since most triggers in Resonite are
sync (buttons, ProtoFlux Tool interactions, other graphs), Dergflux
always creates **sync** receivers and uses `StartAsyncTask` to bridge
into async flows.

The chain for an async flow with a named trigger:

```
DynamicImpulseReceiver (sync)
  → StartAsyncTask (sync, bridges to async)
    → AsyncSequence / AsyncFor / etc. (async)
      → PlayOneShotAndWait / other async actions
```

For an async flow with `Update` (every frame):

```
Update (sync)
  → StartAsyncTask (sync, bridges to async)
    → AsyncSequence / AsyncFor / etc. (async)
```

For a sync flow (no async actions), no bridge is needed:

```
DynamicImpulseReceiver (sync)
  → Sequence / For / If / etc. (sync)
```

This design means any existing sync trigger (buttons, other graphs,
manual `DynamicImpulseTrigger` nodes) can fire Dergflux flows
regardless of whether they contain async actions.
