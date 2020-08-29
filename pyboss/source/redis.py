import json
import os
from typing import Dict

from jsonmerge import Merger
from redis import Redis

from pyboss.source import BaseSource


class RedisSource(BaseSource):
    def __init__(self, rdb: Redis, config_key: str, merger: Merger = None):
        super().__init__(merger)
        self._rdb: Redis = rdb
        self.config_key: str = config_key

    def load(self) -> Dict:
        if 'PYBOSS_NO_MONGODB' in os.environ.keys():
            return {}

        cfg = self._rdb.get(self.config_key)
        if not cfg:
            return {}

        cfg_dict = json.loads(cfg)
        return cfg_dict
