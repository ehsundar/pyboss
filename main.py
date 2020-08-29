import time

from pymongo import MongoClient
from redis import Redis

from pyboss.boss import Boss
from pyboss.source import JsonFileSource, YamlFileSource, RedisSource, EnvironmentSource, MongodbSource

json_source = JsonFileSource(file_path='test_data/dict_and_array.json')
yaml_source = YamlFileSource(file_path='test_data/dict_and_array.yml')

redis = Redis()
redis_source = RedisSource(rdb=redis, config_key='Like_SVC')

mongo = MongoClient(connect=False)
mongo_source = MongodbSource(mongo, db_name='cfg', collection_name='twitter')

env_source = EnvironmentSource()

b = Boss([
    json_source,
    yaml_source,
    redis_source,
    mongo_source,
    env_source,
], refresh_interval=60)

print(b.like_svc.port)
print(b.db[1].host)

time.sleep(200)
