from abc import ABC, abstractmethod
from GTS.base_strategy import SequenceStrategy


class StrategyFactory(ABC):
    @abstractmethod
    def create_strategy(self) -> SequenceStrategy:
        pass
