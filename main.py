from redis import Redis

from pyboss.boss import Boss
from pyboss.source import JsonFileSource, YamlFileSource
from pyboss.source.redis import RedisSource

json_source = JsonFileSource('test_data/dict_and_array.json')
yaml_source = YamlFileSource('test_data/dict_and_array.yml')

redis = Redis()
redis_source = RedisSource(redis, 'Like_SVC')

b = Boss([yaml_source, redis_source])

print(b.like_svc.host)
print(b.db[1].host)
