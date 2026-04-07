"""Example showing how to create and control an AudioClipPlayer component.

The AudioClipPlayer has a SyncPlayback member with transport controls
(play, loop, position, speed) and a clip reference that points to an
audio asset provider by ID.

Usage:
    python examples/audio_clip_player.py <port>

Requires a running Resonite session with ResoniteLink enabled.
Before running, generate the AudioClipPlayer class:
    python -m pyresonitelink.cli.gencode <port> "[FrooxEngine]FrooxEngine.AudioClipPlayer"
"""

import asyncio
import sys

from pyresonitelink import client
from pyresonitelink.components.audio import AudioClipPlayer


async def main(port: int) -> None:
    """Create an AudioClipPlayer and manipulate its playback state."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    # Create a slot
    slot_resp = await resolink.add_slot_to_root(
        name="AudioClipPlayer Example",
    )
    slot_id = slot_resp.entityId
    assert slot_id is not None
    print(f"Created slot: {slot_id}\n")

    # --- Create an AudioClipPlayer ---
    player = AudioClipPlayer()
    await player.add_to_slot(resolink, slot_id)
    print(f"Component type: {player.COMPONENT_TYPE}")
    print(f"Added component: {player.id}")

    pb = player.playback
    print(f"\nInitial state:")
    print(f"  play:     {pb.play if pb else None}")
    print(f"  loop:     {pb.loop if pb else None}")
    print(f"  position: {pb.position if pb else None}")
    print(f"  speed:    {pb.speed if pb else None}")
    print(f"  clip:     {player.clip}")

    # --- Modify playback: set to looping at 2x speed ---
    if pb is not None:
        pb.loop = True
        pb.speed = 2.0
        pb.play = True

    await player.update(resolink)
    print("\nUpdated: loop=True, speed=2.0, play=True")

    # --- Verify ---
    await player.refresh(resolink)
    pb2 = player.playback
    print(f"\nAfter update:")
    print(f"  play:     {pb2.play if pb2 else None}")
    print(f"  loop:     {pb2.loop if pb2 else None}")
    print(f"  position: {pb2.position if pb2 else None}")
    print(f"  speed:    {pb2.speed if pb2 else None}")

    # --- Demonstrate setting a clip reference by ID ---
    player.clip = "Reso_FAKE_ASSET_ID"
    print(f"\nSet clip to: {player.clip}")

    # --- Clean up ---
    await resolink.remove_slot(slotId=slot_id)
    print("\nCleaned up.")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
