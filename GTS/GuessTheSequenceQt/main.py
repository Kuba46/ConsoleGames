import sys
from PyQt6.QtWidgets import QApplication
from GTS.GuessTheSequenceQt.qt_gts import GuessTheSeqUI, GuessTheSeqLogic


def main():
    app = QApplication(sys.argv)
    ui = GuessTheSeqUI()
    game_logic = GuessTheSeqLogic(ui)
    ui.game_logic = game_logic
    ui.show()
    game_logic.start_game()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
