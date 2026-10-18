"""Unit tests for parsing ResoniteLink session announcements."""

# pylint: disable=protected-access,missing-function-docstring

import json

import pytest

from pyresonitelink import discovery

_ADDR = ("192.168.0.5", 51897)


def _announce(protocol: discovery._AnnouncementProtocol, **fields: object) -> None:
    protocol.datagram_received(json.dumps(fields).encode(), _ADDR)


@pytest.mark.asyncio
async def test_records_announced_session() -> None:
    protocol = discovery._AnnouncementProtocol()
    _announce(protocol, sessionName="World", sessionID="S-1", linkPort=49152)
    assert protocol.sessions == {
        "S-1": discovery.LinkSession(
            name="World", session_id="S-1", host="192.168.0.5", port=49152,
        ),
    }
    assert protocol.first_seen.is_set()


@pytest.mark.asyncio
async def test_later_announcement_replaces_earlier() -> None:
    # A world can be renamed during its session.
    protocol = discovery._AnnouncementProtocol()
    _announce(protocol, sessionName="Old", sessionID="S-1", linkPort=49152)
    _announce(protocol, sessionName="New", sessionID="S-1", linkPort=49152)
    assert protocol.sessions["S-1"].name == "New"


@pytest.mark.asyncio
async def test_negative_port_removes_session() -> None:
    protocol = discovery._AnnouncementProtocol()
    _announce(protocol, sessionName="World", sessionID="S-1", linkPort=49152)
    _announce(protocol, sessionName="World", sessionID="S-1", linkPort=-1)
    assert not protocol.sessions


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "datagram",
    [
        b"not json",
        b"[]",
        json.dumps({"sessionName": "No ID", "linkPort": 1}).encode(),
        json.dumps({"sessionName": "Empty ID", "sessionID": "", "linkPort": 1}).encode(),
        json.dumps({"sessionID": "S-1", "linkPort": "x"}).encode(),
    ],
)
async def test_ignores_invalid_datagrams(datagram: bytes) -> None:
    protocol = discovery._AnnouncementProtocol()
    protocol.datagram_received(datagram, _ADDR)
    assert not protocol.sessions
    assert not protocol.first_seen.is_set()
