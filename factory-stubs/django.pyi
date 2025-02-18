from . import base, declarations
from _typeshed import Incomplete
from typing import TypeVar

logger: Incomplete
DEFAULT_DB_ALIAS: str
T = TypeVar('T')

def get_model(app, model): ...

class DjangoOptions(base.FactoryOptions):
    model: Incomplete
    def get_model_class(self): ...

class DjangoModelFactory(base.Factory[T]):
    class Meta:
        abstract: bool

class Password(declarations.Transformer):
    def __init__(self, password, transform=..., **kwargs) -> None: ...

class FileField(declarations.BaseDeclaration):
    DEFAULT_FILENAME: str
    def evaluate(self, instance, step, extra): ...

class ImageField(FileField):
    DEFAULT_FILENAME: str

class mute_signals:
    signals: Incomplete
    paused: Incomplete
    def __init__(self, *signals) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def copy(self): ...
    def __call__(self, callable_obj): ...
    def wrap_method(self, method): ...
