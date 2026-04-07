"""Pytest configuration for pyresonitelink tests."""

from typing import AsyncGenerator
import uuid

import pytest
import pytest_asyncio

from pyresonitelink import client
from pyresonitelink.data import responses


def pytest_addoption(parser: pytest.Parser) -> None:
    """Add command line options for tests."""
    parser.addoption(
        "--port",
        action="store",
        type=int,
        help="Port number for ResoniteLink connection",
    )


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def resolink(
    request: pytest.FixtureRequest,
) -> AsyncGenerator[client.Client, None]:
    """Fixture providing a ResoniteLink client."""
    host = "localhost"
    resolink_port = request.config.getoption("--port")
    print(f"Connecting to ws://{host}:{resolink_port}...")
    resolink_client = client.Client()
    await resolink_client.connect(resolink_port, host)
    yield resolink_client
    await resolink_client.close()


@pytest_asyncio.fixture(loop_scope="session")
async def test_slot_id(
    resolink: client.Client,  # pylint: disable=redefined-outer-name
) -> AsyncGenerator[str, None]:
    """Fixture providing the ID of a test slot, created and removed for each test."""
    slot_id = str(uuid.uuid4())
    response = await resolink.add_slot_to_root(
        id=slot_id,
        name="Test Slot",
        debug=True,
    )
    assert isinstance(response, responses.NewEntityId)
    yield slot_id
    await resolink.remove_slot(slotId=slot_id, debug=True)
