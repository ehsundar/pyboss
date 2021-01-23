import threading
import time
from typing import List, Optional
import traceback

from pyboss.source.base import BaseSource
from pyboss.value import DictValue


class Boss:
    def __init__(self, sources: List[BaseSource], refresh_interval: int = 0):
        self._sources = sources
        self._tree: Optional[DictValue] = None
        self.refresh_interval = refresh_interval if refresh_interval > 60 else 60

        self._start_config_refresher()
        self._load_config()

    def __getattr__(self, item):
        return self._tree[item]

    def __getitem__(self, item):
        return self._tree[item]

    def _load_config(self):
        loaded_value = {}

        for src in self._sources:
            src_value = src.load()
            loaded_value = src.merger.merge(loaded_value, src_value)

        self._tree = DictValue(loaded_value)

    def _start_config_refresher(self):
        if self.refresh_interval > 0:
            def fn():
                while True:
                    time.sleep(self.refresh_interval)
                    try:
                        self._load_config()
                    except Exception as e:
                        traceback.print_exc()

            threading.Thread(target=fn, daemon=True).start()
