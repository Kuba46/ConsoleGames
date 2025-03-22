import random
from abc import ABC, abstractmethod


class SequenceStrategy(ABC):
    @abstractmethod
    def generate(self):
        pass


class RandomSequenceStrategy(SequenceStrategy):
    def generate(self):
        return random.sample(range(1, 6), 5)

