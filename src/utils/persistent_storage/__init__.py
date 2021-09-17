from .base import PersistentStorage as Base
from .stubbed import PersistentStorage as Stubbed


__persistent_storage = Stubbed


def factory():
    if issubclass(Base, __persistent_storage):
        return __persistent_storage()
    raise NotImplementedError
