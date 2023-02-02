from abc import ABC, abstractmethod


class DataStructure(ABC):

    @property
    def __struct(self):
        raise NotImplementedError

    @property
    def __size(self):
        raise NotImplementedError

    @abstractmethod
    def show(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def add(self, val) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove(self) -> object:
        raise NotImplementedError

    @abstractmethod
    def peek(self) -> object:
        raise NotImplementedError

    @abstractmethod
    def is_empty(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def count(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def _resize(self) -> None:
        raise NotImplementedError
