"""Unit tests for pyresonitelink.utils.recorder."""

# pylint: disable=missing-function-docstring

import pytest

from pyresonitelink.data import workers
from pyresonitelink.dergflux import Graph
from pyresonitelink.utils import recorder
from tests.test_dergflux_builder import MockClient
from tests.test_dergflux_builder import _build
from tests.test_dergflux_builder import _ct
from tests.test_dergflux_builder import mock_client  # noqa: F401  pylint: disable=unused-import


class TestParse:

    def test_numbers_bools_and_labels(self) -> None:
        log = "t=1.5 where=ground y=0.121 held=False\nt=1.52 y=-2E-05 held=True\n"
        assert recorder.parse(log) == [
            {"t": 1.5, "where": "ground", "y": 0.121, "held": 0.0},
            {"t": 1.52, "y": -2e-05, "held": 1.0},
        ]

    def test_empty_log(self) -> None:
        assert recorder.parse("") == []


class TestRecord:

    @pytest.mark.asyncio
    async def test_appends_a_line_while_lines_are_left(self, mock_client: MockClient) -> None:
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="rec")
        s.v = s.Float3ModelVar("v")
        rec = recorder.Recorder(g, s, "trace")
        with g.Under(slot):
            rec.record(where="end", v=s.v)
        await _build(mock_client, g)
        m = mock_client

        assert m.count(r"DataModelObjectFieldStore<string>") == 1
        assert m.count(r"DataModelValueFieldStore<int>") == 1
        # One Unpack for the vector, one ToString per element and one for
        # the time.
        assert m.count(_ct("Unpack_Float3")) == 1
        assert m.count(_ct("ToString_Float")) == 3
        assert m.count(_ct("ToString_Double")) == 1
        if_node = m.find_one(_ct("If"))
        assert "ValueGreaterThan<int>" in (m.ref_target_type(if_node, "Condition") or "")
        writes = m.find(r"ObjectWrite<|ValueWrite<")
        assert len(writes) == 2
        assert m.ref_target_comp(if_node, "OnTrue") in writes

    def test_spaces_split_fields(self) -> None:
        # A two-word label would become a label and a field of its own.
        rows = recorder.parse("t=0 where=one two=2")
        assert rows == [{"t": 0.0, "where": "one", "two": 2.0}]

    def test_columns_of_a_vector(self) -> None:
        g = Graph()
        s = g.Space(workers.Slot(id="x"), space_name="rec")
        s.q = s.FloatQModelVar("q")
        s.v = s.Float2ModelVar("v")
        names = [name for name, _ in recorder._columns("v", s.v)]
        assert names == ["v.x", "v.y"]
        # A rotation isn't a vector, and is one column.
        assert [name for name, _ in recorder._columns("q", s.q)] == ["q"]
