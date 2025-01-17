import random
import time
import threading

# initialize the board as global variable so 
# that it can be accessed by all functions
board = ["."] * 42

# loops through each column and displays the board
def display_board():
    for i in range(0, 42, 7):
        print(" ".join(board[i:i+7]))
    print()
    print("1 2 3 4 5 6 7")


def valid_move(column):

    if board[column] != ".":
        return False
    return True

## checks if the column is full 
## if the column is full, the player cannot drop a piece in that column
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
    # display_board()
    return True

def check_win(player):

    # Check for horizontal win
    # checks for 4 consecutive pieces in a row across the horizontal axis
    # it can do this because the board is a 1D array and 
    # It loops through each of the six rows of the board
    # Only loops through the next 4 columns to ensure that a win is possible
    # Start calculates the index of the current position
    # the pieces are dropped in the board from top to bottom
    # so the pieces are placed in the board in a left to right manner
    for row in range(6):
        for col in range(4):
            start  = row * 7 + col
            if(board[start] == player and
               board[start+1] == player and
               board[start+2] == player and
               board[start+3] == player):
                return True
    
    # Check for vertical win
    # does the same as the horizontal win but checks for 4 consecutive pieces in a column
    # it is plus 7 because it is checking for the next piece in the column
    # so if our first piece is at position 1 the piece directly above it is
    # at position 1 + 7 = 8
    for row in range(3):
        for col in range(7):
            start  = row * 7 + col
            if(board[start] == player and
               board[start+7] == player and
               board[start+14] == player and
               board[start+21] == player):
                return True
            
    # Check for diagonal win bottom left to top right
    # diagonal win is a bit more complex but essentially works the same as 
    # the vertical win. 
    # it is the same but it will be + (7 + 1) each time 
    # because it is checking for the next piece in the diagonal
    # so if we at position 1 the diagnol piece is at postion 1 + 8 = 9
    # and the next one will be at 9 + 8 = 17
    for row in range(3):
        for col in range(4):
            start  = row * 7 + col
            if(board[start] == player and
               board[start+8] == player and
               board[start+16] == player and
               board[start+24] == player):
                return True
            
    # Check for diagonal win top left to bottom right
    # works the same as the bottom left to top right but in the opposite direction
    for row in range(3):
        for col in range(4):
            start  = (5 - row) * 7 + col
            if(board[start] == player and
               board[start-6] == player and
               board[start-12] == player and
               board[start-18] == player):
                return True
    return False


def is_board_full():
    return "." not in board

# generates a random move for the AI 
def ai_move():
    while True:
        column = random.randint(0, 6)
        if valid_move(column):
            return column
        
## This is the game loop for the ai function
## it works the same as the game loop for the player
# but instead of getting input from a player it calls the above ai_move function
def game_loop_ai():

    for player in ["R"] + ["B","R"] * 42:
        display_board()
        if player == "R":
            if not take_turn(player):
                print("Game exited. Thanks for playing!")
                break
        else:
            column = ai_move()
            drop_piece(column, player)
        display_board()
        if (check_win(player)):
            print("Player " + player + " wins!")
            break
        if is_board_full():
            display_board()
            print("It's a tie!")
            break

# this is the normal game loop function
# it takes input from the player and checks if the player has won
# calling the previous functions we have
def game_loop():
    for player in ["R"] + ["B","R"] * 42:
        display_board()
        if not take_turn(player):
            print("Game exited. Thanks for playing!")
            break
        display_board()
        if (check_win(player)):
            print("Player " + player + " wins!")
            break
        if is_board_full():
            display_board()
            print("It's a tie!")
            break


# This function gets player input with a time limit
# it uses threading so that it can get the input in the console live
# and not have to wait for the player to press enter
def get_player_input_timeout():
    global player_input

    # This function runs in a separate thread to get player input
    def input_thread():
        global player_input
        try:
            player_input = int(input(f"You have 5 seconds to Enter a column (1-7) or 0 to exit: "))
        except ValueError:
            player_input = -1  

    thread = threading.Thread(target=input_thread)
    thread.start()

    # Time limit for player input
    thread.join(5)

    # Check if the thread is still alive after the timeout
    if thread.is_alive():
        print("\nTime's up!")
        return -1 
    if player_input == 0:
        return -1
    if 1 <= player_input <= 7 and valid_move(player_input - 1):
        return player_input - 1
    else:
        print(f"Invalid input.")
        return -1 


# This is the game loop for the harder AI
# it works the same as the game loop for the player
# but instead of getting input from a player it calls the above get_player_input_timeout function 
# and also the ai_move function
def game_loop_hard_ai():
    for player in ["R"] + ["B", "R"] * 42:
        display_board()
        if player == "R":
            column = get_player_input_timeout()
            if column == -1:  
                break
            drop_piece(column, player)
        else:
            column = ai_move()
            drop_piece(column, player)
        display_board()
        if check_win(player):
            print(f"Player {player} wins!")
            break
        if is_board_full():
            display_board()
            print("It's a tie!")
            break


def main ():
    print("Connect 4!")
    print("1. Play against another player")
    print("2. Play against an AI")
    print("3. Play against a harder AI with timed player moves")
    try:
        
        print("Please select an option (0 to exit): ")
        start = int(input())
        if start == 0:
            print("Game exited. Thanks for playing!")
        if start == 1:
            game_loop()
        if start == 2: 
            game_loop_ai()
        if start == 3:
            game_loop_hard_ai()
        else:
            raise ValueError
    except ValueError:
        print("Please enter a valid option (1 or 2) or 0 to exit:  ")

    # game_loop()


if __name__ == "__main__":
    main()



