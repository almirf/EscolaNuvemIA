import functools
from typing_extensions import Self

from .backend_bases import RendererBase

class TexManager:
    texcache = ...

    grey_arrayd = ...
    font_family = ...
    font_families = ...
    font_info = ...
    @functools.lru_cache
    def __new__(cls) -> Self: ...
    def get_font_config(self): ...
    @classmethod
    def get_basefile(cls, tex: str, fontsize: float, dpi: None = ...) -> str: ...
    @classmethod
    def get_font_preamble(cls): ...
    @classmethod
    def get_custom_preamble(cls) -> str: ...
    @classmethod
    def make_tex(cls, tex: str, fontsize: float) -> str: ...
    @classmethod
    def make_dvi(cls, tex: str, fontsize: float): ...
    @classmethod
    def make_png(cls, tex: str, fontsize: float, dpi: float): ...
    @classmethod
    def get_grey(cls, tex: str, fontsize: float = ..., dpi: float = ...): ...
    @classmethod
    def get_rgba(cls, tex: str, fontsize: float = ..., dpi: float = ..., rgb=...): ...
    @classmethod
    def get_text_width_height_descent(cls, tex: str, fontsize: float, renderer: RendererBase = ...): ...
