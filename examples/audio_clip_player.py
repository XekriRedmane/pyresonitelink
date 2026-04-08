"""Example showing how to import and play an audio clip.

Imports a WAV file as an asset, creates a StaticAudioClip to hold it,
creates an AudioClipPlayer pointing at the clip, and plays it.

Usage:
    python examples/audio_clip_player.py <port>

Requires a running Resonite session with ResoniteLink enabled.
"""

import asyncio
import os
import sys
import time

from pyresonitelink import client
from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.components.audio import AudioClipPlayer


async def main(port: int) -> None:
    """Import an audio clip and play it."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    # Create a slot
    slot_resp = await resolink.add_slot_to_root(
        name="AudioClipPlayer Example",
    )
    assert slot_resp.entityId is not None
    slot = workers.Slot(id=slot_resp.entityId)
    print(f"Created slot: {slot.id}\n")

    # --- Import the audio file ---
    wav_path = os.path.join(os.path.dirname(__file__), "740423_notification.wav")
    print(f"Importing {wav_path}...")
    asset = await resolink.import_audio_clip_file(filePath=wav_path)
    print(f"Asset URL: {asset.assetURL}")

    # --- Create a StaticAudioClip and set its URL to the imported asset ---
    sac_resp = await resolink.add_component(
        containerSlotId=slot,
        componentType="[FrooxEngine]FrooxEngine.StaticAudioClip",
    )
    sac_id = sac_resp.entityId
    assert sac_id is not None

    # Set the URL member to the imported asset URL
    sac_get = await resolink.get_component(componentId=sac_id)
    assert sac_get.data is not None
    url_member = sac_get.data.members["URL"]
    sac_get.data.members["URL"] = fields.FieldUri(
        id=url_member.id, value=asset.assetURL,
    )
    await resolink.update_component(data=sac_get.data)
    print(f"StaticAudioClip: {sac_id}")

    # --- Create an AudioClipPlayer and point it at the clip ---
    player = AudioClipPlayer(clip=sac_id)
    await player.add_to_slot(resolink, slot)
    assert player.id is not None
    print(f"AudioClipPlayer: {player.id}")
    print(f"  clip -> {player.clip}")

    # --- Play it ---
    print("\nPlaying...")
    await player.play(resolink)

    # Wait for the clip to play
    time.sleep(3)

    # --- Check playback state ---
    await player.refresh(resolink)
    pb = player.playback
    print(f"\nPlayback state:")
    print(f"  play:     {pb.play if pb else None}")
    print(f"  loop:     {pb.loop if pb else None}")
    print(f"  position: {pb.position if pb else None}")
    print(f"  speed:    {pb.speed if pb else None}")

    # --- Stop ---
    await player.stop(resolink)
    print("\nStopped.")

    # --- Clean up ---
    await resolink.remove_slot(slot=slot)
    print("Cleaned up.")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
