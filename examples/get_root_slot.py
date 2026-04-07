"""Example showing connecting and getting root slot data."""

import asyncio
import sys

from pyresonitelink import client


async def main(port: int) -> None:
    """Connect and fetch the root slot."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected, getting root slot...")
    slot = await resolink.get_slot(slotId="Root")
    print(slot)
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
