from abc import ABC, abstractmethod
from seq_strategy import SequenceStrategy, RandomSequenceStrategy


class StrategyFactory(ABC):
    @abstractmethod
    def create_strategy(self) -> SequenceStrategy:
        pass


class RandomStrategyFactory(StrategyFactory):
    def create_strategy(self) -> SequenceStrategy:
        return RandomSequenceStrategy()
