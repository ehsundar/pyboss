from pyboss.boss import Boss
from pyboss.source import JsonFileSource, YamlFileSource

json_source = JsonFileSource('test_data/dict_and_array.json')
yaml_source = YamlFileSource('test_data/dict_and_array.yml')

b = Boss([yaml_source])
like = b.like_svc
print(like.host)

print(b.db[1].host)
