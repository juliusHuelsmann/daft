"""
Recursively generated graph
===========================

**Daft** is Python, so you can do anything Python can do.  This graph is
generated by recursive code.

"""

from __future__ import division
from matplotlib import rc
rc("font", family="serif", size=12)
rc("text", usetex=True)

import daft

def recurse(pgm, nodename, level, c):
    if level > 4:
        return nodename
    r = c // 2
    r1nodename = "r{0:02d}{1:04d}".format(level, r)
    if 2 * r == c:
        print("adding {0}".format(r1nodename))
        pgm.add_node(daft.Node(r1nodename, r"reduce",
                               2 ** level * (r + 0.5) - 0.5,
                               3 - 0.7 * level, aspect=1.9))
    pgm.add_edge(nodename, r1nodename)
    if 2 * r == c:
        return recurse(pgm, r1nodename, level + 1, r)

pgm = daft.PGM([16.2, 8], origin=[-0.6, -1.5])

pgm.add_node(daft.Node("query", r'\texttt{"kittens?"}', 3, 6., aspect=3.,
                       plot_params={"ec": "none"}))
pgm.add_node(daft.Node("input", r"input", 7.5, 6., aspect=3.))
pgm.add_edge("query", "input")

for c in range(16):
    nodename = "map {0:02d}".format(c)
    pgm.add_node(daft.Node(nodename, str(nodename), c, 3., aspect=1.9))
    pgm.add_edge("input", nodename)
    level = 1
    recurse(pgm, nodename, level, c)

pgm.add_node(daft.Node("output", r"output", 7.5, -1., aspect=3.))
pgm.add_edge("r040000", "output")
pgm.add_node(daft.Node("answer", r'\texttt{"http://dwh.gg/"}', 12., -1.,
                       aspect=4.5, plot_params={"ec": "none"}))
pgm.add_edge("output", "answer")

pgm.render()
pgm.figure.savefig("recursive.pdf")
pgm.figure.savefig("recursive.png", dpi=200)
