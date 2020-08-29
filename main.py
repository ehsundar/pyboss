from redis import Redis

from pyboss.boss import Boss
from pyboss.source import JsonFileSource, YamlFileSource, RedisSource, EnvironmentSource

json_source = JsonFileSource('test_data/dict_and_array.json')
yaml_source = YamlFileSource('test_data/dict_and_array.yml')

redis = Redis()
redis_source = RedisSource(redis, 'Like_SVC')

env_source = EnvironmentSource()

b = Boss([yaml_source, redis_source, env_source])

print(b.like_svc.port)
print(b.db[1].host)
