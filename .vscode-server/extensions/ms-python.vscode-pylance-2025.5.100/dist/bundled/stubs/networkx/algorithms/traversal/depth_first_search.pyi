from collections import defaultdict
from collections.abc import Mapping

from ...classes.graph import Graph

__all__ = [
    "dfs_edges",
    "dfs_tree",
    "dfs_predecessors",
    "dfs_successors",
    "dfs_preorder_nodes",
    "dfs_postorder_nodes",
    "dfs_labeled_edges",
]

def dfs_edges(G: Graph, source=None, depth_limit=None): ...
def dfs_tree(G: Graph, source=None, depth_limit=None): ...
def dfs_predecessors(G: Graph, source=None, depth_limit=None) -> Mapping: ...
def dfs_successors(G: Graph, source=None, depth_limit=None) -> Mapping: ...
def dfs_postorder_nodes(G: Graph, source=None, depth_limit=None): ...
def dfs_preorder_nodes(G: Graph, source=None, depth_limit=None): ...
def dfs_labeled_edges(G: Graph, source=None, depth_limit=None): ...
