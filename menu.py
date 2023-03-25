
def menu(c: int = None) -> int:
    choice = c if c else input(
        "\nWelcome in my Rock Paper Scissor game! Select what you want to do:\n"
        "1- Play\n"
        "2- Rules\n"
        "3- Quit\n"
    )
    if choice in ['1', '2', '3']:
        return int(choice)
    else:
        print("Wrong input, please select 1 to PLAY or 2 to know RULES.\n")
        menu()


def restart(fail: bool = False) -> int:
    if fail:
        print('\nWrong input, please select 1 for YES or 2 for NO')

    a = input('\n\nDo you want to restart a game?\n'
              '1- Yes\n'
              '2- No\n'
              )
    return int(a) if a in ['1', '2'] else restart(True)


def player_input(fail: bool = False) -> int:
    if fail:
        print("\nWrong input, please select a number between 1 and 3 to select your token.")

    pl_token = input("\n(1) Rock\n"
                     "(2) Paper\n"
                     "(3) Scissor\n")
    if pl_token not in ['1', '2', '3']:
        return player_input(True)
    else:
        return int(pl_token)
