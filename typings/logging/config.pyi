"""
This type stub file was generated by pyright.
"""

import sys
from collections.abc import Callable, Hashable, Iterable, Sequence
from configparser import RawConfigParser
from re import Pattern
from threading import Thread
from typing import Any, Final, IO, Literal, SupportsIndex, TypedDict, overload
from _typeshed import StrOrBytesPath
from typing_extensions import Required, TypeAlias
from . import Filter, Filterer, Formatter, Handler, Logger, _FilterType, _FormatStyle, _Level

"""
This type stub file was generated by pyright.
"""
DEFAULT_LOGGING_CONFIG_PORT: int
RESET_ERROR: Final[int]
IDENTIFIER: Final[Pattern[str]]
if sys.version_info >= (3, 11):
    class _RootLoggerConfiguration(TypedDict, total=False):
        level: _Level
        filters: Sequence[str | _FilterType]
        handlers: Sequence[str]
        ...
    
    
else:
    ...
class _LoggerConfiguration(_RootLoggerConfiguration, TypedDict, total=False):
    propagate: bool
    ...


_FormatterConfigurationTypedDict = TypedDict("_FormatterConfigurationTypedDict", { "class": str,"format": str,"datefmt": str,"style": _FormatStyle }, total=False)
class _FilterConfigurationTypedDict(TypedDict):
    name: str
    ...


_FormatterConfiguration: TypeAlias = ...
_FilterConfiguration: TypeAlias = ...
_HandlerConfiguration: TypeAlias = ...
class _DictConfigArgs(TypedDict, total=False):
    version: Required[Literal[1]]
    formatters: dict[str, _FormatterConfiguration]
    filters: dict[str, _FilterConfiguration]
    handlers: dict[str, _HandlerConfiguration]
    loggers: dict[str, _LoggerConfiguration]
    root: _RootLoggerConfiguration
    incremental: bool
    disable_existing_loggers: bool
    ...


def dictConfig(config: _DictConfigArgs | dict[str, Any]) -> None:
    ...

if sys.version_info >= (3, 10):
    def fileConfig(fname: StrOrBytesPath | IO[str] | RawConfigParser, defaults: dict[str, str] | None = ..., disable_existing_loggers: bool = ..., encoding: str | None = ...) -> None:
        ...
    
else:
    ...
def valid_ident(s: str) -> Literal[True]:
    ...

def listen(port: int = ..., verify: Callable[[bytes], bytes | None] | None = ...) -> Thread:
    ...

def stopListening() -> None:
    ...

class ConvertingMixin:
    def convert_with_key(self, key: Any, value: Any, replace: bool = ...) -> Any:
        ...
    
    def convert(self, value: Any) -> Any:
        ...
    


class ConvertingDict(dict[Hashable, Any], ConvertingMixin):
    def __getitem__(self, key: Hashable) -> Any:
        ...
    
    def get(self, key: Hashable, default: Any = ...) -> Any:
        ...
    
    def pop(self, key: Hashable, default: Any = ...) -> Any:
        ...
    


class ConvertingList(list[Any], ConvertingMixin):
    @overload
    def __getitem__(self, key: SupportsIndex) -> Any:
        ...
    
    @overload
    def __getitem__(self, key: slice) -> Any:
        ...
    
    def pop(self, idx: SupportsIndex = ...) -> Any:
        ...
    


class ConvertingTuple(tuple[Any, ...], ConvertingMixin):
    @overload
    def __getitem__(self, key: SupportsIndex) -> Any:
        ...
    
    @overload
    def __getitem__(self, key: slice) -> Any:
        ...
    


class BaseConfigurator:
    CONVERT_PATTERN: Pattern[str]
    WORD_PATTERN: Pattern[str]
    DOT_PATTERN: Pattern[str]
    INDEX_PATTERN: Pattern[str]
    DIGIT_PATTERN: Pattern[str]
    value_converters: dict[str, str]
    importer: Callable[..., Any]
    def __init__(self, config: _DictConfigArgs | dict[str, Any]) -> None:
        ...
    
    def resolve(self, s: str) -> Any:
        ...
    
    def ext_convert(self, value: str) -> Any:
        ...
    
    def cfg_convert(self, value: str) -> Any:
        ...
    
    def convert(self, value: Any) -> Any:
        ...
    
    def configure_custom(self, config: dict[str, Any]) -> Any:
        ...
    
    def as_tuple(self, value: list[Any] | tuple[Any]) -> tuple[Any]:
        ...
    


class DictConfigurator(BaseConfigurator):
    def configure(self) -> None:
        ...
    
    def configure_formatter(self, config: _FormatterConfiguration) -> Formatter | Any:
        ...
    
    def configure_filter(self, config: _FilterConfiguration) -> Filter | Any:
        ...
    
    def add_filters(self, filterer: Filterer, filters: Iterable[_FilterType]) -> None:
        ...
    
    def configure_handler(self, config: _HandlerConfiguration) -> Handler | Any:
        ...
    
    def add_handlers(self, logger: Logger, handlers: Iterable[str]) -> None:
        ...
    
    def common_logger_config(self, logger: Logger, config: _LoggerConfiguration, incremental: bool = ...) -> None:
        ...
    
    def configure_logger(self, name: str, config: _LoggerConfiguration, incremental: bool = ...) -> None:
        ...
    
    def configure_root(self, config: _LoggerConfiguration, incremental: bool = ...) -> None:
        ...
    


dictConfigClass = DictConfigurator