"""Alias for pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async."""

import importlib as _importlib

_mod = _importlib.import_module(
    "pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async"
)

# Re-export all public names from the aliased module
from types import ModuleType as _ModuleType
for _name in dir(_mod):
    if not _name.startswith("_"):
        globals()[_name] = getattr(_mod, _name)
