"""Convenience alias for ProtoFlux node packages.

This package re-exports the category subpackages from the deeply
nested generated path, so that::

    from pyresonitelink.protoflux.core import ValueInput

is equivalent to::

    from pyresonitelink.generated.protoflux.runtimes.execution.nodes.core.value_input import ValueInput
"""

import importlib
import sys
from pathlib import Path

# The actual nodes package that contains the category subpackages.
_NODES_PKG = "pyresonitelink.generated.protoflux.runtimes.execution.nodes"

# Discover all category subpackages by scanning the filesystem.
_nodes_dir = Path(__file__).resolve().parent.parent / (
    "generated/protoflux/runtimes/execution/nodes"
)

for _child in _nodes_dir.iterdir():
    if _child.is_dir() and not _child.name.startswith("_"):
        _full = f"{_NODES_PKG}.{_child.name}"
        # Make the subpackage importable as pyresonitelink.protoflux.<name>
        _alias = f"pyresonitelink.protoflux.{_child.name}"
        try:
            _mod = importlib.import_module(_full)
            sys.modules[_alias] = _mod
        except ImportError:
            pass
