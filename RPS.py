import random
import os
import re


def checkStatus():
    valid_responses = ['y', 'n']
    while True:
        try:
            response = input('Do you wish to play again? (Yes (y) or No (n)): ')
            if response.lower() not in valid_responses:
                raise ValueError('Yes or No only')
            if response.lower() == 'y':
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Thanks for playing!')
                exit()
        except ValueError as err:
            print(err)


def playRPS():
    play = True
    while play:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print('Rock, Paper, Scissors - Shoot!')

        userChoice = input('Choose your weapon'
                           ' Rock (R), Paper (P), or Scissors (S): ')

        if not re.match("[SsRrPp]", userChoice):
            print('Invalid input. Please choose a letter:')
            print('Rock (R), Paper (P), or Scissors (S)')
            continue

        print(f'You chose: {userChoice}')

        choices = ['R', 'P', 'S']
        oppChoice = random.choice(choices)

        print(f'I chose: {oppChoice}')

        if oppChoice == userChoice.upper():
            print('Tie!')
            play = checkStatus()
        elif oppChoice == 'R' and userChoice.upper() == 'S':
            print('Rock beats scissors, I win!')
            play = checkStatus()
        elif oppChoice == 'S' and userChoice.upper() == 'P':
            print('Scissors beats paper! I win!')
            play = checkStatus()
        elif oppChoice == 'P' and userChoice.upper() == 'R':
            print('Paper beats rock, I win!')
            play = checkStatus()
        else:
            print('You win!\n')
            play = checkStatus()