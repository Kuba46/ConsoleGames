from GTS.base_factory import StrategyFactory
from GTS.base_strategy import SequenceStrategy
from GTS.GuessTheSequenceQt.qbutton_seq_strategy import ButtonSequenceStrategy


class QButtonStrategyFactory(StrategyFactory):
    def create_strategy(self) -> SequenceStrategy:
        return ButtonSequenceStrategy()

