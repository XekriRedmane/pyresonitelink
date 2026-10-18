"""Example showing how to call sync methods, with and without arguments.

Imports a WAV file into a StaticAudioClip, then calls the clip's
AdjustVolume(ratio) sync method. AdjustVolume processes the audio and
replaces the clip's URL with that of the processed asset, so the URL read
back afterward differs from the original.

Usage:
    python examples/call_sync_method.py [port]

If the port is omitted, the session is found from its LAN announcement.
Requires a running Resonite session with ResoniteLink enabled.
"""

import asyncio
import os
import sys

from pyresonitelink import client
from pyresonitelink import discovery


async def main(port: int | None) -> None:
    """Calls AdjustVolume on an imported clip."""
    if port is None:
        session = await discovery.find_session()
        print(f"Found {session.name!r} on port {session.port}.")
        port = session.port
    resolink = client.Client()
    await resolink.connect(port)

    slot = await resolink.add_slot(name="Sync Method Example")
    try:
        wav_path = os.path.join(os.path.dirname(__file__), "740423_notification.wav")
        clip = await resolink.create_audio_clip(slot, wav_path)
        print(f"Imported clip: {clip.url}")

        # A primitive argument is passed as a plain value. The generated
        # wrapper tags it with its type, as FieldFloat here, because the
        # server rejects untagged arguments.
        response = await clip.adjust_volume(resolink, ratio=0.5)
        print(f"AdjustVolume succeeded: {response['success']}")

        # The volume is adjusted in the background, and the clip's URL is
        # replaced when the new asset is ready.
        original_url = clip.url
        for _ in range(50):
            await asyncio.sleep(0.2)
            await clip.refresh(resolink)
            if clip.url != original_url:
                break
        print(f"Adjusted clip: {clip.url}")
    finally:
        await resolink.remove_slot(slot)
        await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1]) if len(sys.argv) > 1 else None))
