from typing import Dict


class BaseSource:
    def load(self) -> Dict:
        ...
