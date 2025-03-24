import random
from GTS.base_strategy import SequenceStrategy
from PyQt6.QtWidgets import QPushButton


class ButtonSequenceStrategy(SequenceStrategy):
    def generate(self):
        original_list = random.sample(range(1, 6), 5)
        buttons = [QPushButton(str(number)) for number in original_list]
        for button in buttons:
            button.clicked.connect(self.on_button_click)
        return original_list, buttons

    def on_button_click(self):
        self.play_game(self.original_list)
