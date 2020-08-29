# PyBoss

Manage your app's configurations with PyBoss! you can define several sources for aquiring configurations:

* JsonFileSource
* YamlFileSource
* RedisSource
* MongodbSource
* EnvironmentSource
* Your custom config source...

pass all of your sources to `Boss` then he'll take care of them.

TODO:
* implement sources
* CLI for source check
* reload and interval
* lock for read and write
* unit tests
* source fail safety
* JsonSchema and validation
