#!/usr/bin/env python3

import toytree
import toyplot
import toyplot.svg
from toytree.TreeParser import NewickError
import sys

def main():
    try:
        tre = toytree.tree(sys.argv[1])
    except NewickError:
        tre = toytree.tree(sys.argv[1], tree_format=10)
    except FileNotFoundError:
        print("Tree not found!")
    tre = tre.root("Pungent-5")

    # print(tre.get_node_values('prob'))

    canvas, axes, mark = tre.draw(
        layout='c',
        tip_labels_align=True,
        node_style={"stroke": "black"},
        width=1200,
        height=1200,
        node_labels='prob',
        node_sizes=16,
        use_edge_lengths=True,
    );

    outfile = sys.argv[1].rsplit(".", 1)[0]
    toyplot.svg.render(canvas, outfile + ".svg")
    print("Tree drawn successfully.")


if __name__ == '__main__':
    main()
