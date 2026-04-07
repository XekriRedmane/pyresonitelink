"""Example: Calling sync methods on components via CallSyncMethod.

Demonstrates the CallSyncMethod API by calling methods on an
AudioClipPlayer (Play, Stop, Pause) and destroying a slot.

Usage:
    python examples/call_sync_method.py <port>
"""

import asyncio
import sys

from pyresonitelink import client
from pyresonitelink.data import members
from pyresonitelink.data import messages
from pyresonitelink.data import workers
from pyresonitelink.components.audio import AudioClipPlayer


async def call_method(
    resolink: client.Client,
    target_id: str,
    method_name: str,
    arguments: dict[str, object] | None = None,
) -> bool:
    """Call a sync method and print the result.

    Args:
        resolink: Connected client.
        target_id: ID of the target component or worker.
        method_name: Name of the method to call.
        arguments: Named arguments to the method.

    Returns:
        True if the call succeeded.
    """
    resp = await resolink.request_json(
        messages.CallSyncMethod(
            targetID=target_id,
            methodName=method_name,
            arguments=arguments or {},
        )
    )
    success = resp.get("success", False)
    assert isinstance(success, bool)
    if success:
        print(f"  {method_name}(): OK")
    else:
        error = resp.get("errorInfo", "unknown error")
        assert isinstance(error, str)
        print(f"  {method_name}(): FAILED - {error[:60]}")
    return success


async def main(port: int) -> None:
    """Demonstrate calling sync methods on components."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    slot_resp = await resolink.add_slot_to_root(name="CallSyncMethod Example")
    assert slot_resp.entityId is not None
    slot = workers.Slot(id=slot_resp.entityId)
    print(f"Created slot: {slot.id}\n")

    # ===================================================================
    # AudioClipPlayer: Play, Pause, Stop
    # ===================================================================

    player = AudioClipPlayer()
    await player.add_to_slot(resolink, slot)
    assert player.id is not None
    print(f"AudioClipPlayer: {player.id}")

    await call_method(resolink, player.id, "Play")
    await call_method(resolink, player.id, "Pause")
    await call_method(resolink, player.id, "Stop")

    # ===================================================================
    # Slot.Destroy via CallSyncMethod
    # ===================================================================

    child_resp = await resolink.add_slot(
        parent=members.Reference(targetId=slot.id),
        name="to-be-destroyed",
    )
    assert child_resp.entityId is not None
    child = workers.Slot(id=child_resp.entityId)
    assert child.id is not None
    print(f"\nCreated child slot: {child.id}")

    await call_method(resolink, child.id, "Destroy")

    # Verify it's gone
    get_resp = await resolink.get_slot(slot=slot, depth=1)
    assert get_resp.data is not None
    children = get_resp.data.children or []
    remaining = [
        c for c in children
        if c.name and c.name.value == "to-be-destroyed"
    ]
    print(f"  Child still exists: {len(remaining) > 0}")

    # Clean up
    await resolink.remove_slot(slot=slot)
    print("\nCleaned up.")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
