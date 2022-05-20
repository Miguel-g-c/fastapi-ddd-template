# pylint: disable=redefined-builtin
import abc
from typing import Generic, TypeVar
from uuid import UUID


T = TypeVar("T")


class AbstractRepository(abc.ABC, Generic[T]):
    def __init__(self) -> None:
        self.seen = set[T]()

    def add(self, entity: T) -> None:
        self._add(entity)
        self.seen.add(entity)

    def get(self, id: UUID) -> T | None:
        entity = self._get(id)
        if entity:
            self.seen.add(entity)
        return entity

    def get_by_user(self, user_id: UUID) -> T | None:
        entity = self._get_by_user(user_id)
        if entity:
            self.seen.add(entity)
        return entity

    def remove(self, entity: T) -> None:
        self._remove(entity)

    @abc.abstractmethod
    def _add(self, entity: T) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, id: UUID) -> T | None:
        raise NotImplementedError

    @abc.abstractmethod
    def _get_by_user(self, user_id: UUID) -> T | None:
        raise NotImplementedError

    @abc.abstractmethod
    def _remove(self, entity: T) -> None:
        raise NotImplementedError
