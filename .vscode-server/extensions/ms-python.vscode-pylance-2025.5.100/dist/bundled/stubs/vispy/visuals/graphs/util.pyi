# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

import numpy as np

def _get_edges(adjacency_mat): ...
def _sparse_get_edges(adjacency_mat): ...
def _ndarray_get_edges(adjacency_mat): ...
def _get_directed_edges(adjacency_mat): ...
def _straight_line_vertices(adjacency_mat, node_coords, directed=False): ...
def _rescale_layout(pos, scale=1): ...
