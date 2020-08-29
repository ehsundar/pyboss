# PyBoss

Manage your app's configurations with PyBoss! you can define several sources for aquiring configurations:

* JsonFileSource
* YamlFileSource
* RedisSource
* MongodbSource
* EnvironmentSource
* Your custom config source...

pass all of your sources to `Boss` then he'll take care of them. 

*you can partially overwrite config value by defining sources*

TODO:
* mutual lock for read and write
* CLI for source check
* unit tests

## Quick Start

first of all, you need to define your config sources. then pass them as a list to `Boss`. the order of the list matter,
as it expresses which source should come on top of witch one:

```python
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
], refresh_interval=120)
```

when an instance of `Boss` is created, all of the sources will be evaluated and merged respectively.
we use [jsonmerge](https://pypi.org/project/jsonmerge/) for merging output of each source, on top of
result of all previous sources.

```python
print(b.like_svc.host)
print(b.db[1].host)
```

parameter `refresh_interval` indicates interval of reload procedure. default to `0` witch means no 
reload. this feature is intended to be used for having live configs. any failure in further reloads
(except first time), will **not** cause your application exit. 


## In case of emergency...

assume that you override some configs using MongoDB source. if your MongoDB instance is not available
for any reason, you can disable `MongodbSource` load by setting `PYBOSS_NO_MONGODB` environment variable.
so that you don't need to change any line of code or rebuild. same behaviour for redis, by setting `PYBOSS_NO_REDIS`

*you should pass `MongoClient(connect=False)`, so client does not attempt to connect in advance. otherwise `PYBOSS_NO_MONGODB` will have no use...*


## Document schema for MongoDB

```json
{
    "_id": {
        "$oid": "5f4a2856133f34383e3b1000"
    },
    "key": "like_svc",
    "port": 4444
}
```

the field `key` is mandatory. this indicates top level entry name for this document, as a partial config.
the `key` and `_id` will be deleted and rest of the fields will merge with previous source output:

```json
{
  "like_svc": {
    "port": 4444
  }
}
```


## Value schema for Redis

`RedisSource(rdb=redis, config_key='Like_SVC')` the `config_key` parameter tell `RedisSource` witch key to get.
other behaviours are just like a json file


## MergeStrategy for sources

Strategy for merge result of every source, on top of previous ones, can be specified by JsonSchema and some options.
a `Merger` instance might pass to `XSource` constructor. for further information, please read 
[this](https://github.com/avian2/jsonmerge#merge-strategies) section.
