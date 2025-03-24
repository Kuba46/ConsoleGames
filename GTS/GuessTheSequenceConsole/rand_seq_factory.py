from GTS.base_factory import StrategyFactory
from GTS.base_strategy import SequenceStrategy
from GTS.GuessTheSequenceConsole.rand_seq_strategy_console import RandomSequenceStrategy


class RandomStrategyFactory(StrategyFactory):
    def create_strategy(self) -> SequenceStrategy:
        return RandomSequenceStrategy()
