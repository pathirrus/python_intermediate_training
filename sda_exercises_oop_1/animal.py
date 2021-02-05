from abc import ABC


class Animals(ABC):

    def __init__(self, name):
        self.name = name

    @property
    def name(self) -> str:
        return self._name


