from typing import Dict

import yaml

from pyboss.source import BaseSource


class YamlFileSource(BaseSource):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> Dict:
        with open(self.file_path, 'r') as f:
            entries = {}
            for cfg in yaml.load_all(f, yaml.FullLoader):
                entries.update(cfg)
            return entries
