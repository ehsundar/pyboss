import os
from typing import Dict

from jsonmerge import Merger

from pyboss.source import BaseSource


class EnvironmentSource(BaseSource):
    def __init__(self, prefix: str = '', delimiter: str = '__', merger: Merger = None):
        super().__init__(merger)
        self.prefix = prefix
        self.delimiter = delimiter

    def load(self) -> Dict:
        bound_env = {}
        for key, val in os.environ.items():
            if key.startswith(self.prefix):
                key_parts = key.split(self.delimiter)
                curr_dict = bound_env
                for part in key_parts[:-1]:
                    if part in curr_dict:
                        curr_dict = curr_dict[part]
                    else:
                        curr_dict[part] = {}
                        curr_dict = curr_dict[part]

                curr_dict[key_parts[-1]] = val

        return bound_env
