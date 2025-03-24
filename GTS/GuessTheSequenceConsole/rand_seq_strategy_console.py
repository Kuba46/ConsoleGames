from GTS.base_strategy import SequenceStrategy
import random


class RandomSequenceStrategy(SequenceStrategy):
    def generate(self):
        return random.sample(range(1, 6), 5)
