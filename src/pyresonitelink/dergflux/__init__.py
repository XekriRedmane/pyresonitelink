"""Dergflux: a Pythonic DSL for building ProtoFlux graphs.

Dergflux lets you write ProtoFlux logic using natural Python syntax::

    g = Graph()
    with g.Under(slot):
        s = g.Space()
        s.x = s.FloatVar("x")
        s.z = s.FloatVar("z")

        with g.If(s.x < 3):
            s.z = s.x + 3
        with g.Else():
            s.z = s.x - 3

    await g.build(resolink)
"""

from pyresonitelink.dergflux._action import ActionDef, InputDef, OutputDef
from pyresonitelink.dergflux._graph import Graph
from pyresonitelink.dergflux._space import Space, VarDecl
from pyresonitelink.dergflux import _math as math

__all__ = [
    "ActionDef", "InputDef", "OutputDef",
    "Graph", "Space", "VarDecl", "math",
]
