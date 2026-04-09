"""Dergflux: a Pythonic DSL for building ProtoFlux graphs.

Dergflux lets you write ProtoFlux logic using natural Python syntax::

    g = Graph()
    s = g.Space(slot)
    s.x = g.Float("x")
    s.z = g.Float("z")

    with g.If(s.x < 3):
        s.z = s.x + 3
    with g.Else():
        s.z = s.x - 3

    await g.build(resolink)
"""

from pyresonitelink.dergflux._graph import Graph
from pyresonitelink.dergflux._space import Space, VarDecl

__all__ = ["Graph", "Space", "VarDecl"]
