from abc import ABC, abstractmethod


class SequenceStrategy(ABC):
    @abstractmethod
    def generate(self):
        pass
