from typing import Dict

from jsonmerge import Merger


class BaseSource:
    def __init__(self, merger: Merger = None):
        self.merger: Merger = Merger(schema={})
        if merger:
            self.merger = merger

    def load(self) -> Dict:
        ...
