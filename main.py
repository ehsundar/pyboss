from pyboss.boss import Boss, JsonFileSource

json_source = JsonFileSource('test_data/dict_and_array.json')

b = Boss([json_source])
like = b.like_svc
print(like.host)

print(b.db[1].host)
