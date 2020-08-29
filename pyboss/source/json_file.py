import json

from pyboss.source.base import BaseSource
from pyboss.value import DictValue


class JsonFileSource(BaseSource):
    def __init__(self, file_path):
        self.file_path = file_path

    def value_tree(self) -> DictValue:
        with open(self.file_path, 'r') as f:
            cfg_str = f.read()
            cfg_dict = json.loads(cfg_str)
            assert type(cfg_dict) == dict
            return DictValue(cfg_dict)
