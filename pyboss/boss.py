import json
from typing import Dict, List, Optional


class ListValue:
    def __init__(self, cfg: List):
        self.cfg = cfg
        self._list = []
        for val in cfg:
            if type(val) is dict:
                self._list.append(DictValue(val))
            elif type(val) is list:
                self._list.append(ListValue(val))
            else:
                self._list.append(val)

    def __getitem__(self, item):
        return self._list[item]

    def __iter__(self):
        return self._list

    def __len__(self):
        return len(self._list)


class DictValue:
    def __init__(self, cfg: Dict):
        self.cfg = cfg
        self._dict = {}
        for key, val in cfg.items():
            if type(val) is dict:
                self._dict[key] = DictValue(val)
            elif type(val) is list:
                self._dict[key] = ListValue(val)
            else:
                self._dict[key] = val

    def __getattr__(self, item):
        return self._dict.get(item)

    def __getitem__(self, item):
        return self._dict.get(item)


class BaseSource:
    def value_tree(self) -> DictValue:
        ...


class JsonFileSource(BaseSource):
    def __init__(self, file_path):
        self.file_path = file_path

    def value_tree(self) -> DictValue:
        with open(self.file_path, 'r') as f:
            cfg_str = f.read()
            cfg_dict = json.loads(cfg_str)
            assert type(cfg_dict) == dict
            return DictValue(cfg_dict)


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
