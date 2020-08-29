from typing import List, Dict


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
