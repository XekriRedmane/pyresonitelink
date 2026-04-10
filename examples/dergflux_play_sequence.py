"""Example: Play a sequence of audio clips using Dergflux.

Uses an AssetMultiplexer<AudioClip> to hold three audio clips, then
a Dergflux For loop to iterate through them, playing each one in
sequence with PlayOneShotAndWait.

The For loop index is bound to the multiplexer's Index field via
g.Bind(), so each iteration selects a different clip.

Usage:
    python examples/dergflux_play_sequence.py <port>

Requires a running Resonite session with ResoniteLink enabled.
"""

import asyncio
import os
import sys
import time

from pyresonitelink import client
from pyresonitelink.dergflux import Graph


AUDIO_FILES = [
    "740423_notification.wav",
    "514375_ptink.wav",
    "672766_tikatak.wav",
]


async def main(port: int) -> None:
    """Play three audio clips in sequence using Dergflux."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    # Delete any leftover slot from a previous run
    old = await resolink.find_slot("Root", name="Dergflux Play Sequence")
    if old is not None:
        print(f"Deleting old slot {old.id}...")
        await resolink.remove_slot(slot=old)

    slot = await resolink.add_slot(name="Dergflux Play Sequence")
    print(f"Created slot: {slot.id}\n")

    # ===================================================================
    # Import audio files and create a multiplexer — one call
    # ===================================================================

    examples_dir = os.path.dirname(__file__)
    audio_paths = [
        os.path.join(examples_dir, f) for f in AUDIO_FILES
    ]
    mux = await resolink.create_audio_multiplexer(slot, audio_paths)
    print(f"AssetMultiplexer: {mux.id} ({len(AUDIO_FILES)} clips)")

    # ===================================================================
    # Build the Dergflux graph
    # ===================================================================

    g = Graph()

    s = g.Space(slot)
    s.state = s.StringVar("state", value="waiting")

    with g.Under(slot, trigger="play_all"):
        # g.For(count) yields a ForProxy with OnStart/OnIterate.
        # The For and the following bare write become entries in an
        # AsyncSequence (async because PlayOneShotAndWait is async).
        with g.For(len(AUDIO_FILES)) as f:
            with f.OnIterate() as i:
                # Bind the loop counter to the multiplexer's Index
                # field. This selects a different clip each iteration.
                g.Bind(i, mux, "Index")

                # Play the current clip and wait for it to finish.
                # Pass the multiplexer directly — the builder auto-creates
                # a RefObjectInput<IAssetProvider<AudioClip>> bridge.
                with g.PlayOneShotAndWait(clip=mux, volume=1.0) as r:
                    with r.on_started_playing():
                        s.state = "playing"
                    with r.on_finished_playing():
                        # Won't really be visible, since it will get
                        # immediately overwritten.
                        s.state = "idle"

        # After the loop finishes (via AsyncSequence)
        s.state = "waiting"

    print("\nBuilding graph...")
    await g.build(resolink)
    print("Graph built.\n")

    # After build, access the variable directly from the Space
    state_var = s.state
    await state_var.refresh(resolink)
    print(f"Initial state: {state_var.value}")

    print("\nSetup complete!")
    print("To play all clips in sequence, trigger a dynamic impulse")
    print("with tag 'play_all' on the slot from within Resonite.")
    print("\nSlot left in place for inspection.")

    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
