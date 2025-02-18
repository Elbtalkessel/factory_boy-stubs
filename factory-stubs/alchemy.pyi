from . import base
from _typeshed import Incomplete

SESSION_PERSISTENCE_COMMIT: str
SESSION_PERSISTENCE_FLUSH: str
VALID_SESSION_PERSISTENCE_TYPES: Incomplete

class SQLAlchemyOptions(base.FactoryOptions): ...

class SQLAlchemyModelFactory(base.Factory):
    class Meta:
        abstract: bool
