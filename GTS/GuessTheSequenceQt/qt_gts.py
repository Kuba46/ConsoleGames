from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QHBoxLayout, QMessageBox
from GTS.base_gts import GuessTheSeqBase
from GTS.GuessTheSequenceQt.qbutton_factory import QButtonStrategyFactory
from GTS.GuessTheSequenceQt.qt_status_check import StatusCheckQt as StatusCheck


class GuessTheSeqLogic(GuessTheSeqBase):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.original_list = []
        self.user_list = []

    def start_game(self):
        factory = QButtonStrategyFactory()
        strategy = factory.create_strategy()
        self.original_list, buttons = strategy.generate()
        self.ui.setup_buttons(buttons)
        self.play_game(self.original_list)

    def get_user_input(self, button):
        user_input = int(button.text())
        button.setEnabled(False)
        return user_input

    def display_message(self, message):
        self.ui.display_message(message)

    def play_game(self, original_list):
        self.user_list = []
        sorted_list = sorted(original_list)

        for button in self.ui.buttons:
            button.clicked.connect(lambda _, b=button: self.process_click(b))

    def process_click(self, button):
        user_input = self.get_user_input(button)
        self.user_list.append(user_input)

        if self.user_list == self.original_list:
            self.display_message("You've beaten the game!")
            if StatusCheck.check_status(self.ui):
                self.restart_game()
        elif self.user_list == sorted(self.original_list):
            self.display_message("You've done it, yeah. But actually, you've lost.")
            if StatusCheck.check_status(self.ui):
                self.restart_game()
        elif user_input not in self.original_list or len(self.user_list) > len(self.original_list):
            self.display_message("Error! Try again!")
            if StatusCheck.check_status(self.ui):
                self.restart_game()

    def restart_game(self):
        self.ui.clear_buttons()
        self.user_list = []
        self.start_game()


class GuessTheSeqUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.label = QLabel('Welcome to "Guess the Sequence" game!', self)
        self.layout.addWidget(self.label)

        self.button_layout = QHBoxLayout()
        self.buttons = []

        self.layout.addLayout(self.button_layout)
        self.setLayout(self.layout)

    def setup_buttons(self, buttons):
        self.clear_buttons()
        for button in buttons:
            button.setEnabled(True)
            self.button_layout.addWidget(button)
            self.buttons.append(button)

    def clear_buttons(self):
        for button in self.buttons:
            self.button_layout.removeWidget(button)
            button.deleteLater()
        self.buttons = []

    def display_message(self, message):
        self.label.setText(message)


