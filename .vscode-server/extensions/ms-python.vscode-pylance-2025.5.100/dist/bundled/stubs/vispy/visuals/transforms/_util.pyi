import functools
from functools import wraps
from typing import Callable

import numpy as np
from numpy.typing import ArrayLike

from ...util import logger

# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

def arg_to_array(func: Callable) -> Callable: ...
def as_vec4(obj: ArrayLike, default: ArrayLike = ...) -> ArrayLike: ...
def arg_to_vec4(func): ...

class TransformCache:
    def __init__(self, max_age=1): ...
    def get(self, path): ...
    def _create(self, path): ...
    def roll(self): ...
