"""Finds ResoniteLink sessions by listening for their LAN announcements.

Every world running ResoniteLink broadcasts a small JSON datagram on UDP port
12512 every 10 seconds, such as::

    {"sessionName": "My World", "sessionID": "S-01a1...", "linkPort": 49152}

A ``linkPort`` below zero announces that the session has closed. The
mechanism is described by ``LinkSessionListener`` in the ResoniteLink
repository, https://github.com/Yellow-Dog-Man/ResoniteLink, and this module
follows it.

Example::

    sessions = await discovery.discover_sessions()
    resolink = client.Client()
    await resolink.connect(sessions[0].port, sessions[0].host)
"""

from __future__ import annotations

import asyncio
import json
import socket
from dataclasses import dataclass

ANNOUNCE_PORT = 12512
# Seconds between announcements of one session.
ANNOUNCE_INTERVAL = 10.0


@dataclass(frozen=True)
class LinkSession:
    """Represents a world that announced a running ResoniteLink."""

    # The world name. It can change during the session.
    name: str
    # The session ID, which never changes during the session.
    session_id: str
    # The address the announcement came from. ResoniteLink listens on all
    # interfaces, so this works as the host to connect to.
    host: str
    # The port ResoniteLink listens on.
    port: int


class _AnnouncementProtocol(asyncio.DatagramProtocol):
    """Collects session announcements, keyed by session ID."""

    def __init__(self) -> None:
        self.sessions: dict[str, LinkSession] = {}
        self.first_seen = asyncio.Event()

    def datagram_received(self, data: bytes, addr: tuple[str | int, int]) -> None:
        """Records or removes the session in one announcement.

        A datagram that isn't a valid announcement is ignored, the same way
        the upstream listener ignores it.
        """
        try:
            announcement = json.loads(data)
            session_id = announcement["sessionID"]
            port = int(announcement["linkPort"])
        except (ValueError, KeyError, TypeError):
            return
        if not session_id:
            return
        if port < 0:
            self.sessions.pop(session_id, None)
            return
        self.sessions[session_id] = LinkSession(
            name=str(announcement.get("sessionName") or ""),
            session_id=session_id,
            host=str(addr[0]),
            port=port,
        )
        self.first_seen.set()


async def discover_sessions(
    timeout: float = ANNOUNCE_INTERVAL + 1.0,
    stop_at_first: bool = False,
) -> list[LinkSession]:
    """Returns the ResoniteLink sessions announced on the LAN.

    Each session announces itself once every 10 seconds, so the default
    timeout hears every running session at least once. A shorter timeout
    can miss sessions.

    The socket is bound with SO_REUSEADDR, as the upstream listener does,
    so that more than one program can listen at the same time.

    Args:
        timeout (float): How long to listen, in seconds.
        stop_at_first (bool): Return as soon as one session is heard
            instead of listening for the whole timeout.

    Returns:
        The sessions heard, sorted by name and then by port. The list is
        empty if no session was heard.

    Raises:
        OSError: The announcement port couldn't be bound.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("0.0.0.0", ANNOUNCE_PORT))
    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        _AnnouncementProtocol, sock=sock,
    )
    try:
        if stop_at_first:
            try:
                await asyncio.wait_for(protocol.first_seen.wait(), timeout)
            except TimeoutError:
                pass
        else:
            await asyncio.sleep(timeout)
    finally:
        transport.close()
    return sorted(protocol.sessions.values(), key=lambda s: (s.name, s.port))


async def find_session(
    name: str | None = None,
    timeout: float = ANNOUNCE_INTERVAL + 1.0,
) -> LinkSession:
    """Returns the one announced session with the given world name.

    Args:
        name (str | None): The world name to match exactly, or None to
            accept any session.
        timeout (float): How long to listen, in seconds.

    Returns:
        The matching session.

    Raises:
        LookupError: No session matched, or more than one did. The message
            lists the sessions that were heard.
    """
    sessions = await discover_sessions(timeout)
    matches = [s for s in sessions if name is None or s.name == name]
    if len(matches) == 1:
        return matches[0]
    heard = ", ".join(f"{s.name!r} on port {s.port}" for s in sessions) or "none"
    which = "any session" if name is None else f"a session named {name!r}"
    if not matches:
        raise LookupError(f"No ResoniteLink announcement for {which}. Heard: {heard}")
    raise LookupError(
        f"More than one ResoniteLink announcement for {which}. Heard: {heard}"
    )
