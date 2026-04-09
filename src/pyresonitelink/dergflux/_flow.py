"""Flow control contexts and write records for Dergflux.

IfContext tracks the condition and writes for each branch of an
if-else construct.  WriteRecord captures a single variable assignment.
These are pure data structures with no server interaction.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyresonitelink.dergflux import _expr
    from pyresonitelink.dergflux import _space


@dataclass
class WriteRecord:
    """A single variable write: space.var = expr."""

    space: _space.Space
    var_name: str
    expr: _expr.ExprProxy


@dataclass
class IfContext:
    """Tracks an if-else construct during recording.

    Attributes:
        condition: The boolean expression proxy for the branch.
        true_writes: Writes recorded inside the ``with g.If(...)`` block.
        false_writes: Writes recorded inside the ``with g.Else()`` block.
        phase: Which branch is currently being recorded.
    """

    condition: _expr.ExprProxy
    true_writes: list[WriteRecord] = field(default_factory=list)
    false_writes: list[WriteRecord] = field(default_factory=list)
    phase: str = "true"

    def record_write(self, write: WriteRecord) -> None:
        """Append a write to the currently active branch."""
        if self.phase == "true":
            self.true_writes.append(write)
        else:
            self.false_writes.append(write)
