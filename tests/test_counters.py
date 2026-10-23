"""Unit tests for pyresonitelink.utils.counters, built against the Dergflux builder's mock client.

The server ignores a reference to a member that a node doesn't have, so
each build here checks every wired reference name against the node's
generated class, as TestFunctionAudit in test_dergflux_builder.py does.
The values the expressions compute are checked live, in
test_counters_integration.py.
"""

# pylint: disable=missing-function-docstring,redefined-outer-name

from typing import Any

import pytest

from pyresonitelink.data import workers
from pyresonitelink.dergflux import Graph
from pyresonitelink.dergflux import _builder
from pyresonitelink.utils import counters
from tests.test_dergflux_builder import (  # noqa: F401  (fixture)
    MockClient,
    _build,
    _member_names,
    mock_client,
)


@pytest.fixture
def checked(monkeypatch: pytest.MonkeyPatch) -> None:
    """Makes the builder check every reference name against the node's class."""
    original = _builder._create_and_wire

    async def check(
        resolink: Any, slot: Any, component_class: Any,
        references: dict[str, str], debug: bool = False,
    ) -> Any:
        unknown = set(references) - _member_names(component_class)
        assert not unknown, f"{component_class.__name__} has no member {sorted(unknown)}"
        return await original(resolink, slot, component_class, references, debug=debug)

    monkeypatch.setattr(_builder, "_create_and_wire", check)


def _types(mock: MockClient) -> list[str]:
    """Returns the type of every component the build added."""
    return [c.component_type for c in mock.components.values()]


class TestDrumTurns:

    @pytest.mark.asyncio
    @pytest.mark.parametrize("place", [1, 10, 1000])
    async def test_builds(self, mock_client: MockClient, checked: None, place: int) -> None:
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="drum")
        s.n = s.FloatModelVar("n", value=129.5)
        s.r = s.FloatModelVar("r")
        with g.Under(slot):
            s.r = counters.drum_turns(s.n, place)
        await _build(mock_client, g)
        types = _types(mock_client)
        assert any("ValueMod" in t for t in types)
        assert any("Floor" in t for t in types) == (place > 1)
        assert any("Clamp01" in t for t in types) == (place > 1)

    @pytest.mark.parametrize("place", [0, 5, 20, -10])
    def test_place_is_a_power_of_ten(self, place: int) -> None:
        g = Graph()
        s = g.Space(workers.Slot(id="test-slot"), space_name="drum")
        s.n = s.FloatModelVar("n")
        with pytest.raises(ValueError, match="power of 10"):
            counters.drum_turns(s.n, place)


class TestAddDetents:

    @pytest.mark.asyncio
    async def test_builds_with_and_without_held(self, mock_client: MockClient, checked: None) -> None:
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="detents")
        s.a = s.FloatModelVar("a")
        s.b = s.FloatModelVar("b")
        s.held = s.BoolModelVar("held")
        position_a = counters.add_detents(g, s, slot, "a", scale=100, held=s.held, name="da")
        position_b = counters.add_detents(g, s, slot, "b", name="db")
        s.r = s.FloatModelVar("r")
        with g.Under(slot):
            s.r = counters.drum_turns(position_a, 10) + counters.drum_turns(position_b, 1)
        await _build(mock_client, g)
        vars_declared = object.__getattribute__(s, "_vars")
        for name in ("da", "da_lag", "da_position", "db", "db_lag", "db_position"):
            assert name in vars_declared
        types = _types(mock_client)
        assert any("Round" in t for t in types)
        assert any("DeltaTime" in t for t in types)

    def test_threshold_over_half(self) -> None:
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="detents")
        s.a = s.FloatModelVar("a")
        with pytest.raises(ValueError, match="snap back"):
            counters.add_detents(g, s, slot, "a", threshold=0.5)
