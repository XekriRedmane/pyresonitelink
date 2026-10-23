"""Records values inside a Dergflux graph, for a script to read afterwards.

Reading a value through ResoniteLink while a graph runs takes a request
per sample. A sample can land anywhere in an engine update, and several
updates can pass between two samples, so short events such as a bounce
are easy to miss. A Recorder instead appends the values to a string model
variable from inside the flow, at the point in the update where
record() is called, and the script reads the whole log in one request
when it is done.

    rec = recorder.Recorder(g, s, "trace")
    with g.Under(slot):
        ...                                   # the flow being studied
        rec.record(y=p.y, v=s.v)              # one line per update
    await g.build(resolink)

    await rec.start(resolink, lines=300)
    rows = await rec.read(resolink)           # waits for 300 lines
    print(rows[0]["t"], rows[0]["y"], rows[0]["v.y"])

Each line holds the world time as "t" and the recorded values. A vector
is recorded as one column per element, such as "v.x", "v.y", and "v.z".
Each time the flow reaches a record() call while lines are left, the call
appends a line and uses up one line. A graph can call record() at
several points, with a "where" label to tell the lines apart.

The log is a model variable, so the host sends it to every other user in
the session each time it grows. Keep recordings to a few thousand lines.
"""

import asyncio
from typing import Any

from pyresonitelink.data import protocols
from pyresonitelink.dergflux import _expr
from pyresonitelink.dergflux import _graph
from pyresonitelink.dergflux import _space
from pyresonitelink.dergflux import _types
from pyresonitelink.dergflux import strings
from pyresonitelink.dergflux import time

# How often read() checks whether the recording is done.
_POLL_INTERVAL = 0.2  # seconds


class Recorder:
    """Represents a log of values that a Dergflux flow appends to.

    The log and the count of lines left are model variables on a Space,
    named "<name>_log" and "<name>_left".

    Args:
        graph: The graph whose flows record.
        space: The space to declare the two variables on.
        name: The prefix of the variables' names.
    """

    def __init__(self, graph: _graph.Graph, space: _space.Space, name: str) -> None:
        self._graph = graph
        self._space = space
        self._log = f"{name}_log"
        self._left = f"{name}_left"
        setattr(space, self._log, space.StringModelVar(self._log, value=""))
        setattr(space, self._left, space.IntModelVar(self._left, value=0))

    def record(self, where: str | None = None, **values: Any) -> None:
        """Records a line of values, if any lines are left.

        Must be called inside a flow, such as inside g.Under(slot). The
        values are read when the flow reaches this point.

        Args:
            where: A label for the line, recorded as "where", or None. It
                is one word, since spaces separate the fields.
            **values: The values, by column name. Each is a number, a
                Bool, or a vector expression.
        """
        line = _expr._coerce("t=") + strings.to_string(time.world_time())
        if where is not None:
            line = line + f" where={where}"
        for column, value in values.items():
            for name, part in _columns(column, _expr._coerce(value)):
                line = line + f" {name}=" + strings.to_string(part)
        left = getattr(self._space, self._left)
        with self._graph.If(left > 0):
            setattr(self._space, self._log, getattr(self._space, self._log) + line + "\n")
            setattr(self._space, self._left, left - 1)

    async def start(self, resolink: protocols.ResoniteLinkClient, lines: int) -> None:
        """Clears the log and starts recording, after the graph is built.

        Args:
            resolink: The connected client.
            lines: How many lines to record.
        """
        await self._space.WriteModelVar(resolink, self._left, 0)
        await self._space.WriteModelVar(resolink, self._log, "")
        await self._space.WriteModelVar(resolink, self._left, lines)

    async def read(
        self, resolink: protocols.ResoniteLinkClient, *, timeout: float = 30.0,
    ) -> list[dict[str, float | str]]:
        """Waits until the recording is done, then reads and parses the log.

        Args:
            resolink: The connected client.
            timeout: How many seconds to wait for the last line. After
                that, the lines recorded so far are returned.

        Returns:
            One dict per line, by column name. Numbers are floats, Bools
            are 1.0 or 0.0, and "where" labels are strings.
        """
        waited = 0.0
        while waited < timeout and await self._space.ReadModelVar(resolink, self._left) > 0:
            await asyncio.sleep(_POLL_INTERVAL)
            waited += _POLL_INTERVAL
        return parse(await self._space.ReadModelVar(resolink, self._log) or "")


def _columns(name: str, value: _expr.ExprProxy) -> list[tuple[str, _expr.ExprProxy]]:
    """Splits a vector value into one column per element."""
    value_type = value._node._type
    if value_type in _types._VECTORS:
        _, dim = _types._VECTORS[value_type]
        return [(f"{name}.{axis}", getattr(value, axis)) for axis in "xyzw"[:dim]]
    return [(name, value)]


def parse(log: str) -> list[dict[str, float | str]]:
    """Parses a log into one dict per line, by column name.

    A value that reads as a float becomes one. "True" and "False" become
    1.0 and 0.0, and anything else, such as a "where" label, stays a
    string.

    Args:
        log: The log, one line per record, with "name=value" fields
            separated by spaces.
    """
    rows: list[dict[str, float | str]] = []
    for line in log.splitlines():
        row: dict[str, float | str] = {}
        for field in line.split():
            name, _, text = field.partition("=")
            if text in ("True", "False"):
                row[name] = 1.0 if text == "True" else 0.0
                continue
            try:
                row[name] = float(text)
            except ValueError:
                row[name] = text
        if row:
            rows.append(row)
    return rows
