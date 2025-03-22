import os


class StatusCheck:
    @staticmethod
    def check_status(self):
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
