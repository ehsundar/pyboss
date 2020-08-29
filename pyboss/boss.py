from typing import List, Optional

from pyboss.source.base import BaseSource
from pyboss.value import DictValue


class Boss:
    def __init__(self, sources: List[BaseSource]):
        self._sources = sources
        self._tree: Optional[DictValue] = None

    def __getattr__(self, item):
        if not self._tree:
            self._load_config()
        return self._tree[item]

    def _load_config(self):
        self._tree = self._sources[0].value_tree()
