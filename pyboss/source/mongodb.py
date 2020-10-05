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

        bound_query = {'$query':{'_version': {'$exists': True}}, '$orderby': {'_version': -1}}
        latest_version = self.collection.find_one(bound_query)
        if latest_version:
            del latest_version['_id']
            return latest_version
        else:
            return {}
