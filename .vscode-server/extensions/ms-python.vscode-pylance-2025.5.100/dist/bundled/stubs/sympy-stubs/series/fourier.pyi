from collections.abc import Generator
from typing import Any, Literal
from typing_extensions import Self

from sympy.core.basic import Basic
from sympy.series.order import Order
from sympy.series.sequences import SeqFormula
from sympy.series.series_class import SeriesBase
from sympy.sets.sets import FiniteSet, Interval

def fourier_cos_seq(func, limits, n) -> tuple[Any, Any | SeqFormula]: ...
def fourier_sin_seq(func, limits, n) -> SeqFormula: ...
def finite_check(f, x, L) -> tuple[Literal[False], Any] | tuple[Literal[True], Any]: ...

class FourierSeries(SeriesBase):
    def __new__(cls, *args) -> Self: ...
    @property
    def function(self) -> Basic: ...
    @property
    def x(self): ...
    @property
    def period(self) -> tuple[Any, Any]: ...
    @property
    def a0(self): ...
    @property
    def an(self): ...
    @property
    def bn(self): ...
    @property
    def interval(self) -> FiniteSet | Interval: ...
    @property
    def start(self): ...
    @property
    def stop(self): ...
    @property
    def length(self): ...
    @property
    def L(self): ...
    def truncate(self, n=...) -> Generator[Any, Any, None] | Order: ...
    def sigma_approximation(self, n=...) -> Order: ...
    def shift(self, s) -> Self: ...
    def shiftx(self, s) -> Self: ...
    def scale(self, s) -> Self: ...
    def scalex(self, s) -> Self: ...
    def __neg__(self) -> Self: ...
    def __add__(self, other) -> Self | Order: ...
    def __sub__(self, other) -> Self | Order: ...

class FiniteFourierSeries(FourierSeries):
    def __new__(cls, f, limits, exprs) -> Self: ...
    @property
    def interval(self) -> FiniteSet | Interval: ...
    @property
    def length(self): ...
    def shiftx(self, s) -> Self: ...
    def scale(self, s) -> Self: ...
    def scalex(self, s) -> Self: ...
    def __add__(self, other) -> FourierSeries | Order | FiniteFourierSeries | None: ...

def fourier_series(f, limits=..., finite=...) -> FiniteFourierSeries | FourierSeries: ...
