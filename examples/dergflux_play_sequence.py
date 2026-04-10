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
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.components.assets import StaticAudioClip
from pyresonitelink.components.assets.utility import AssetMultiplexer
from pyresonitelink.protoflux.core import RefObjectInput
from pyresonitelink.dergflux import Graph

# Type aliases
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.audio_clip import AudioClip


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

    slot = await resolink.add_slot_to_root(name="Dergflux Play Sequence")
    print(f"Created slot: {slot.id}\n")

    # ===================================================================
    # Import audio files and create StaticAudioClip components
    # ===================================================================

    examples_dir = os.path.dirname(__file__)
    clips: list[StaticAudioClip] = []

    for filename in AUDIO_FILES:
        filepath = os.path.join(examples_dir, filename)
        print(f"Importing {filename}...")
        asset = await resolink.import_audio_clip_file(filePath=filepath)
        clip = StaticAudioClip(url=asset.assetURL)
        await clip.add_to_slot(resolink, slot)
        clips.append(clip)
        print(f"  StaticAudioClip: {clip.id}")

    # ===================================================================
    # Create AssetMultiplexer<AudioClip> with the three clips
    # ===================================================================

    AudioClipMux = AssetMultiplexer[AudioClip]
    mux = AudioClipMux()
    await mux.add_to_slot(resolink, slot)
    print(f"\nAssetMultiplexer: {mux.id}")

    # Populate the Assets SyncList with references to the clips
    assets_list = mux.assets
    if not isinstance(assets_list, members.SyncList):
        assets_list = members.SyncList()
        mux.set_member("Assets", assets_list)
    for clip in clips:
        assets_list.elements.append(
            members.Reference(targetId=clip.id),
        )
    await mux.update(resolink)
    print(f"  Added {len(clips)} clips to multiplexer")

    # Create a RefObjectInput pointing at the multiplexer as clip source
    ClipRef = RefObjectInput[IAssetProvider[AudioClip]]
    clip_ref = ClipRef(target=mux)
    await clip_ref.add_to_slot(resolink, slot)
    print(f"ClipRef -> multiplexer: {clip_ref.id}")

    # ===================================================================
    # Build the Dergflux graph
    # ===================================================================

    g = Graph()

    s = g.Space(slot)
    s.state = s.StringVar("state", value="waiting")

    with g.Under(slot, trigger="play_all"):
        with g.For(len(clips)) as f:
            with f.OnIterate() as i:
                # Bind the loop counter to the multiplexer's Index
                # field. This selects a different clip each iteration.
                g.Bind(i, mux, "Index")

                # Play the current clip and wait for it to finish
                with g.PlayOneShotAndWait(clip=clip_ref, volume=1.0) as r:
                    with r.on_started_playing():
                        s.state = "playing"
                    with r.on_finished_playing():
                        # Won't really be visible, since it will get immediately
                        # overwritten.
                        s.state = "idle"

        # After the loop finishes
        s.state = "waiting"

    print("\nBuilding graph...")
    await g.build(resolink)
    print("Graph built.\n")

    print("\nSetup complete!")
    print("To play all clips in sequence, trigger a dynamic impulse")
    print("with tag 'play_all' on the slot from within Resonite.")
    print("\nSlot left in place for inspection.")

    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
