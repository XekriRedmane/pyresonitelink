"""Example: PlayOneShotAndWait using the Dergflux DSL.

Imports a WAV file, creates ProtoFlux nodes to play it via
PlayOneShotAndWait, and uses Dergflux flow control to set a flag
when playback starts and finishes.

Usage:
    python examples/dergflux_play_one_shot_and_wait.py <port>

Requires a running Resonite session with ResoniteLink enabled.
"""

import asyncio
import os
import sys
import time

from pyresonitelink import client
from pyresonitelink.data import primitives
from pyresonitelink.components.data.dynamic import DynamicValueVariable
from pyresonitelink.dergflux import Graph


async def main(port: int) -> None:
    """Play an audio clip using Dergflux and track playback state."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    # Delete any leftover slot from a previous run
    old = await resolink.find_slot("Root", name="Dergflux PlayOneShot")
    if old is not None:
        print(f"Deleting old slot {old.id}...")
        await resolink.remove_slot(slot=old)

    slot = await resolink.add_slot_to_root(name="Dergflux PlayOneShot")
    print(f"Created slot: {slot.id}\n")

    # Import audio — idempotent, content-addressed (same file = same URL)
    wav_path = os.path.join(os.path.dirname(__file__), "740423_notification.wav")
    clip = await resolink.create_audio_clip(slot, wav_path)
    print(f"Audio clip: {clip.id}")

    # ===================================================================
    # Build the Dergflux graph
    # ===================================================================

    g = Graph()

    s = g.Space(slot)
    s.state = s.StringVar("state")

    with g.Under(slot, trigger="play_sound"):
        # Set state before playing — this bare write runs first in
        # the async sequence, before PlayOneShotAndWait starts.
        s.state = "triggered"

        # PlayOneShotAndWait has two flow outputs:
        #   on_started_playing — fires when audio begins
        #   on_finished_playing — fires when audio ends
        # Pass the StaticAudioClip directly — the builder auto-creates
        # a RefObjectInput<IAssetProvider<AudioClip>> bridge.
        with g.PlayOneShotAndWait(clip=clip, volume=1.0) as r:
            with r.on_started_playing():
                s.state = "playing"
            with r.on_finished_playing():
                s.state = "finished"

    print("\nBuilding graph...")
    await g.build(resolink)
    print("Graph built.\n")

    # ===================================================================
    # Test: trigger the impulse and watch state changes
    # ===================================================================

    # Find the state variable by scanning components and refreshing
    StringDynVar = DynamicValueVariable[primitives.String]
    slot_data = await resolink.get_slot(slot=slot, depth=0)
    assert slot_data.data is not None

    state_var: DynamicValueVariable[primitives.String] | None = None
    for comp in slot_data.data.components:
        if comp.componentType == StringDynVar.COMPONENT_TYPE:
            dv = StringDynVar(component=comp)
            await dv.refresh(resolink)
            if dv.variable_name == "state":
                state_var = dv

    if state_var is not None:
        print(f"Initial state: {state_var.value}")
    else:
        print("Could not find state variable (string dynvar may not exist).")

    print("\nTo hear the sound, trigger a dynamic impulse with tag")
    print("'play_sound' on the slot from within Resonite.")
    print("\nSlot left in place for inspection.")

    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
