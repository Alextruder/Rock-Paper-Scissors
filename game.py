from constant import Token
import random
from menu import menu, restart, player_input


def round_winner():
    hierarchy = {1: 3, 2: 1, 3: 2}
    pl_token = player_input()
    ai_token = random.randint(1, 3)
    print(f'\nYou: {Token(pl_token).name} - AI: {Token(ai_token).name}')

    if pl_token == ai_token:
        print('DRAW')
        return 3
    elif hierarchy[pl_token] == ai_token:
        print('You won this round!')
        return 2
    elif hierarchy[ai_token] == pl_token:
        print('You lost this round!')
        return 1


def is_winner(win_list=None) -> int:
    if win_list is None:
        win_list = []
    rw = round_winner()
    if rw in [1, 2, 3]:
        win_list.append(rw)
    if win_list.count(1) == 3:
        return 1
    elif win_list.count(2) == 3:
        return 2
    else:
        print(win_list)
        is_winner(win_list)


def play(restart_val: bool = False) -> None:
    if restart_val:
        choice = menu(1)
    else:
        choice = menu()

    if choice == 1:
        print(f'\n\nNew Game!')
        print(is_winner())
        restart_val = restart()

        if restart_val == 1:
            play(True)
    elif choice == 2:
        print(
            '\n'
            'The game is a best of 5. The first player who win 3 rounds win the game.\n'
            'The hierarchy of tokens is the following:\n'
            'ROCK win against SCISSORS\n'
            'SCISSORS win against PAPER\n'
            'PAPER win against ROCK\n'
        )
        input('Tap enter to continue\n')
        menu()
