from PyQt6.QtWidgets import QMessageBox


class StatusCheckQt:
    @staticmethod
    def check_status(parent):
        message_box = QMessageBox(parent)
        message_box.setWindowTitle("Play Again")
        message_box.setText("Do you wish to play again?")
        message_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        message_box.setDefaultButton(QMessageBox.StandardButton.Yes)

        response = message_box.exec()

        if response == QMessageBox.StandardButton.Yes:
            return True
        else:
            parent.close()
            return False
