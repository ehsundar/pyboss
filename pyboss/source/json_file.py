import json
from typing import Dict

from jsonmerge import Merger

from pyboss.source.base import BaseSource


class JsonFileSource(BaseSource):
    def __init__(self, file_path, merger: Merger = None):
        super().__init__(merger)
        self.file_path = file_path

    def load(self) -> Dict:
        with open(self.file_path, 'r') as f:
            cfg_str = f.read()
            cfg_dict = json.loads(cfg_str)
            assert type(cfg_dict) == dict
            return cfg_dict
