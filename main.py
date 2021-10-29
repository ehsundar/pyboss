from pymongo import MongoClient

from pyboss.boss import Boss
from pyboss.source import JsonFileSource, YamlFileSource, EnvironmentSource, MongodbSource

json_source = JsonFileSource(file_path='test_data/dict_and_array.json')
yaml_source = YamlFileSource(file_path='test_data/dict_and_array.yml')

mongo = MongoClient(port=27018, connect=False, serverSelectionTimeoutMS=5000)
collection = mongo.pyboss.similarity

b = Boss([
    MongodbSource(collection),
    EnvironmentSource(),
], refresh_interval=10)
