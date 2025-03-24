from abc import ABC, abstractmethod


class GuessTheSeqBase(ABC):
    def __init__(self):
        self.play = True

    @abstractmethod
    def start_game(self):
        pass

    @abstractmethod
    def get_user_input(self):
        pass

    @abstractmethod
    def display_message(self, message):
        pass

    @abstractmethod
    def play_game(self, original_list):
        pass
