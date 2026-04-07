"""Convenience alias for generated components.

This package makes ``pyresonitelink.generated`` importable as
``pyresonitelink.components``, so that::

    from pyresonitelink.components.data import ValueField
    from pyresonitelink.components.data.dynamic import DynamicValueVariable

is equivalent to::

    from pyresonitelink.generated.data import ValueField
    from pyresonitelink.generated.data.dynamic import DynamicValueVariable
"""

import importlib
import sys

_generated = importlib.import_module("pyresonitelink.generated")
sys.modules[__name__] = _generated
