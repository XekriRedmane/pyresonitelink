"""Dergflux: a Pythonic DSL for building ProtoFlux graphs.

Dergflux lets you write ProtoFlux logic using natural Python syntax::

    g = Graph()
    with g.Under(slot):
        s = g.Space()
        s.x = s.FloatDynVar("x")
        s.z = s.FloatDynVar("z")

        with g.If(s.x < 3):
            s.z = s.x + 3
        with g.Else():
            s.z = s.x - 3

    await g.build(resolink)
"""

from pyresonitelink.dergflux._action import ActionDef, InputDef, OutputDef
from pyresonitelink.dergflux._graph import Graph, Outcome
from pyresonitelink.dergflux._space import ModelVarDecl, Space, VarDecl
from pyresonitelink.dergflux import _math as math
from pyresonitelink.dergflux import interaction
from pyresonitelink.dergflux import keyboard
from pyresonitelink.dergflux import mouse
from pyresonitelink.dergflux import slots
from pyresonitelink.dergflux import strings
from pyresonitelink.dergflux import time
from pyresonitelink.dergflux import transform
from pyresonitelink.dergflux import users
from pyresonitelink.dergflux import variables

__all__ = [
    "ActionDef", "InputDef", "OutputDef",
    "Graph", "ModelVarDecl", "Outcome", "Space", "VarDecl",
    "interaction", "keyboard", "math", "mouse", "slots", "strings", "time", "transform", "users", "variables",
]
