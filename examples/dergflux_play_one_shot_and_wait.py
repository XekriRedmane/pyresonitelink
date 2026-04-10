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
from pyresonitelink.data import workers
from pyresonitelink.components.assets import StaticAudioClip
from pyresonitelink.components.data.dynamic import DynamicValueVariable
from pyresonitelink.protoflux.core import RefObjectInput
from pyresonitelink.dergflux import Graph


async def main(port: int) -> None:
    """Play an audio clip using Dergflux and track playback state."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    # Delete any leftover slot from a previous run
    root = await resolink.get_slot(slot="Root", depth=1)
    assert root.data is not None
    for child in root.data.children:
        if child.name and child.name.value == "Dergflux PlayOneShot":
            print(f"Deleting old slot {child.id}...")
            await resolink.remove_slot(slot=child)

    slot_resp = await resolink.add_slot_to_root(name="Dergflux PlayOneShot")
    assert slot_resp.entityId is not None
    slot = workers.Slot(id=slot_resp.entityId)
    print(f"Created slot: {slot.id}\n")

    # ===================================================================
    # Import audio and create the clip asset
    # ===================================================================

    wav_path = os.path.join(os.path.dirname(__file__), "740423_notification.wav")
    print(f"Importing {wav_path}...")
    asset = await resolink.import_audio_clip_file(filePath=wav_path)
    print(f"Asset URL: {asset.assetURL}")

    clip = StaticAudioClip(url=asset.assetURL)
    await clip.add_to_slot(resolink, slot)
    print(f"StaticAudioClip: {clip.id}")

    # Create a RefObjectInput to bridge the clip into ProtoFlux.
    # PlayOneShotAndWait.clip expects INodeObjectOutput<IAssetProvider<AudioClip>>,
    # so we need a ProtoFlux node that outputs a reference to the clip.
    from pyresonitelink.generated._types.iasset_provider import IAssetProvider
    ClipRef = RefObjectInput[IAssetProvider]
    clip_ref = ClipRef(target=clip.id)
    await clip_ref.add_to_slot(resolink, slot)
    print(f"ClipRef: {clip_ref.id}")

    # ===================================================================
    # Build the Dergflux graph
    # ===================================================================

    g = Graph()

    s = g.Space(slot)
    s.state = s.StringVar("state")

    with g.Under(slot, trigger="play_sound"):
        # PlayOneShotAndWait has two flow outputs:
        #   on_started_playing — fires when audio begins
        #   on_finished_playing — fires when audio ends
        #
        # We use these to track playback state in a dynamic variable.

        with g.PlayOneShotAndWait(clip=clip_ref, volume=1.0) as r:
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

    StringDynVar = DynamicValueVariable[primitives.String]

    # Find the state variable
    slot_data = await resolink.get_slot(slot=slot, depth=0)
    assert slot_data.data is not None

    state_var: DynamicValueVariable[primitives.String] | None = None
    for comp in slot_data.data.components:
        if comp.componentType == StringDynVar.COMPONENT_TYPE:
            dv = StringDynVar(component=comp)
            if dv.variable_name == "state":
                state_var = dv

    assert state_var is not None, "Could not find state variable"

    async def read_state() -> object:
        """Read the current state."""
        assert state_var is not None
        await state_var.refresh(resolink)
        return state_var.value

    print(f"Initial state: {await read_state()}")

    # Trigger the dynamic impulse to play the sound.
    # In a real scenario, another ProtoFlux graph or a button would
    # send this impulse. For testing, we'd need a DynamicImpulseTrigger
    # node — which is beyond this example's scope.
    print("\nTo hear the sound, trigger a dynamic impulse with tag")
    print("'play_sound' on the slot from within Resonite.")
    print("\nSlot left in place for inspection.")

    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
