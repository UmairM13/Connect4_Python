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

def check_win(player):

    # Check for vertical win
    for row in range(6):
        for col in range(4):
            start  = row * 7 + col
            if(board[start] == player and
               board[start+1] == player and
               board[start+2] == player and
               board[start+3] == player):
                return True
    
    # Check for horizontal win
    for row in range(3):
        for col in range(7):
            start  = row * 7 + col
            if(board[start] == player and
               board[start+7] == player and
               board[start+14] == player and
               board[start+21] == player):
                return True
            
    # Check for diagonal win bottom left to top right
    for row in range(3):
        for col in range(4):
            start  = row * 7 + col
            if(board[start] == player and
               board[start+8] == player and
               board[start+16] == player and
               board[start+24] == player):
                return True
            
    # Check for diagonal win top left to bottom right
    for row in range(3):
        for col in range(4):
            start  = row * 7 + col
            if(board[start] == player and
               board[start-6] == player and
               board[start-12] == player and
               board[start-18] == player):
                return True
    return False

def game_loop():
    for player in ["R"] + ["B","R"] * 42:
        display_board()
        if not take_turn(player):
            print("Game exited. Thanks for playing!")
            break
        if (check_win(player)):
            print("Player " + player + " wins!")
            break
    else:
        print("It's a tie!")


def main ():
    game_loop()


if __name__ == "__main__":
    main()



