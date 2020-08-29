import copy
import os
from typing import Dict

from jsonmerge import Merger
from pymongo import MongoClient

from pyboss.source import BaseSource


class MongodbSource(BaseSource):
    def __init__(self, mgo: MongoClient, db_name: str, collection_name: str, merger: Merger = None):
        super().__init__(merger)
        self.collection = mgo[db_name][collection_name]

    def load(self) -> Dict:
        if 'PYBOSS_NO_MONGODB' in os.environ.keys():
            return {}

        result = {}
        for doc in self.collection.find({'key': {'$exists': True}}):
            cp = copy.deepcopy(doc)
            del cp['_id']
            del cp['key']
            result[doc['key']] = cp

        return result
