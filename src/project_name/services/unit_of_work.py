# pylint: disable=attribute-defined-outside-init
from __future__ import annotations
import abc
from typing import Any, Iterator, TypeVar

from project_name.adapters.repository import AbstractRepository
from project_name.domain import model
from project_name.domain.events import Event


UnitOfWork = TypeVar("UnitOfWork", bound="AbstractUnitOfWork")


class AbstractUnitOfWork(abc.ABC):
    aggregates: AbstractRepository  # TODO Add model.Aggregate

    def __enter__(self: UnitOfWork) -> UnitOfWork:
        return self

    def __exit__(self, *args: Any) -> None:
        self.rollback()

    def commit(self) -> None:
        self._commit()

    def collect_new_events(self) -> Iterator[Event]:
        pass

    #     for aggregate in self.aggregates.seen:
    #         while aggregate.events:
    #             yield aggregate.events.pop(0)

    @abc.abstractmethod
    def _commit(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError
