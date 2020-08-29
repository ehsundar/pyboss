from pyboss.value import DictValue


class BaseSource:
    def value_tree(self) -> DictValue:
        ...
