from GTS.base_gts import GuessTheSeqBase
from rand_seq_factory import RandomStrategyFactory
from check_status import StatusCheck


class GuessTheSeqConsole(GuessTheSeqBase):
    def start_game(self):
        self.play_game([])

    def get_user_input(self, prompt):
        return int(input(prompt))

    def display_message(self, message):
        print(message)

    @staticmethod
    def string_to_int(string):
        try:
            return int(string)
        except ValueError:
            print("Invalid input! Please enter a valid integer string.")
            return None

    def play_game(self, original_list):
        play = True
        while play:
            print('')
            print('Welcome to "Guess the Sequence" game!')
            print('I have generated a random sequence of numbers.')
            print('Your goal is to guess the correct sequence.')
            print('Good luck!')
            print('')
            factory = RandomStrategyFactory()
            strategy = factory.create_strategy()
            original_list = strategy.generate()

            print(f"Generated sequence: {original_list}")

            user_list = []
            sorted_list = sorted(original_list)

            while len(user_list) < len(original_list):
                user_input = self.string_to_int(input("Enter a number: "))

                if user_input == "":
                    print("You must enter a number!")
                    continue

                if user_input not in original_list or user_input in user_list:
                    print("Enter something from given sequence!")
                    break

                if len(user_list) == 0:
                    if user_input != original_list[0] and user_input != min(original_list):
                        print("Error! You selected the wrong number! Try again!")
                        break
                else:
                    if user_input != original_list[len(user_list)] and user_input != sorted_list[len(user_list)]:
                        print("Error! Try again!")
                        break

                user_list.append(user_input)

                if user_list == original_list:
                    print("You've beaten the game!")
                    play = StatusCheck.check_status(self=play)
                if user_list == sorted(original_list):
                    print("You've done it, yeah. But actually, you've lost.")
                    play = StatusCheck.check_status(self=play)
