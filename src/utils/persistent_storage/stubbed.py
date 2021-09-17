from typing import Any

from .base import PersistentStorage


class Stubbed(PersistentStorage):
    def __init__(self):
        super().__init__()

    def read(self):
        pass

    def write(self, key: str, val: Any):
        pass
