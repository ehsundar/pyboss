from typing import Dict

from jsonmerge import Merger


class BaseSource:
    def __init__(self):
        self.merger: Merger = Merger(schema={})

    def load(self) -> Dict:
        ...
