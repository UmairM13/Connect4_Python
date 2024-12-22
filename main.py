board = ["."] * 42

def display_board():
    for i in range(0, 42, 7):
        print(" ".join(board[i:i+7]))
    print()
    print("1 2 3 4 5 6 7")


def valid_move(column):

    if board[column] != ".":
        return False
    return True


def drop_piece(column, player):
    for i in range(5, -1, -1):
        if board[column + i * 7] == ".":
            board[column + i * 7] = player
            break

def get_player_input():
    while True:
        try:
            column = int(input("Enter a column (1-7) or 0 to exit: "))
            if column == 0:
                return -1
            if column < 1 or column > 7:
                raise ValueError
            if not valid_move(column - 1):
                raise ValueError
            return column - 1
        except ValueError:
            print("Please enter a valid column (1-7) or 0 to exit")

def take_turn(player):
    column = get_player_input()
    if column == -1:
        return False
    drop_piece(column, player)
    display_board()
    return True

def game_loop():
    for player in ["R"] + ["B","R"] * 42:
        display_board()
        if not take_turn(player):
            print("Game exited. Thanks for playing!")
            break
        


def main ():
    game_loop()


if __name__ == "__main__":
    main()



