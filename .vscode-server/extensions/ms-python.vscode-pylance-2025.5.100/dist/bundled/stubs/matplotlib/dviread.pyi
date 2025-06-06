from _typeshed import Incomplete
from collections import namedtuple
from functools import lru_cache
from typing import NamedTuple

from ._typing import *
from .path import Path

Page = ...
Box = ...

class Text(NamedTuple):
    x: float
    y: float
    font: Incomplete
    glyph: Incomplete
    width: int
    @property
    def font_path(self) -> Path: ...
    @property
    def font_size(self): ...
    @property
    def font_effects(self): ...
    @property
    def glyph_name_or_index(self): ...

class Dvi:
    def __init__(self, filename, dpi: float) -> None: ...
    baseline = ...
    def __enter__(self): ...
    def __exit__(self, etype, evalue, etrace): ...
    def __iter__(self): ...
    def close(self) -> None: ...

class DviFont:
    def __init__(self, scale: float, tfm: Tfm, texname: bytes, vf: Vf) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...

class Vf(Dvi):
    def __init__(self, filename: str | PathLike) -> None: ...
    def __getitem__(self, code): ...

class Tfm:
    def __init__(self, filename: str | PathLike) -> None: ...

PsFont = ...

class PsfontsMap:
    @lru_cache
    def __new__(cls, filename): ...
    def __getitem__(self, texname): ...

class _LuatexKpsewhich:
    @lru_cache
    def __new__(cls): ...
    def search(self, filename): ...

def find_tex_file(filename: str | PathLike, format: str | bytes = ...): ...
