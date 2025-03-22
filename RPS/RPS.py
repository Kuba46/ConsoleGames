import random
from re import match as rm
import os
from check_status import StatusCheck


class RPS:
    @staticmethod
    def play_rps(self):
        play = True
        while play:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('')
            print('Rock, Paper, Scissors - Shoot!')
            user_choice = input('Choose your weapon: Rock (R), Paper (P), or Scissors (S): ')

            if not rm("[SsRrPp]", user_choice):
                print('Invalid input. Please choose a letter:')
                print('Rock (R), Paper (P), or Scissors (S)')
                continue

            print(f'You chose: {user_choice}')

            choices = ['R', 'P', 'S']
            opp_choice = random.choice(choices)

            print(f'I chose: {opp_choice}')

            if opp_choice == user_choice.upper():
                print('Tie!')
                play = StatusCheck.check_status(self=play)
            elif opp_choice == 'R' and user_choice.upper() == 'S':
                print('Rock beats scissors, I win!')
                play = StatusCheck.check_status(self=play)
            elif opp_choice == 'S' and user_choice.upper() == 'P':
                print('Scissors beats paper! I win!')
                play = StatusCheck.check_status(self=play)
            elif opp_choice == 'P' and user_choice.upper() == 'R':
                print('Paper beats rock, I win!')
                play = StatusCheck.check_status(self=play)
            else:
                print('You win!\n')
                play = StatusCheck.check_status(self=play)

