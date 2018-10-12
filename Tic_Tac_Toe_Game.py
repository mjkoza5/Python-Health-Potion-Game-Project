#Project: Tic Tac Toe Game
#1) start by making the board. We will use a list. it has 9 elements

board = [" " for i in range(9)] #gives us a board w/ 9 blank strings in it (blank spaces.

#The board needs to be in a grid. We will use a function to achieve this
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

#Function that basically allows to play the game with 2 players
def player_move(icon):
    
    if icon == "X":     #assigning player 1 to X and player 2 to O.
        number = 1
    elif icon == "O":
        number = 2
    print("Your turn player {}".format(number))
    choice = int(input("enter your move 1-9: ").strip())
    if board[choice - 1] ==" ":   #if user entered 1, it would actually move them to second space, as index starts at 0.
        board[choice - 1] = icon  #so if they enter 1, it will actually be 0, which will be top left of Grid.
    else:                         #This also makes it so you can only enter a move when the space is empty.
        print()
        print("That space is taken!")


#Function to check if someone has won the game or not
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

#Function for When there is a DRAW
def is_draw():
    if " " not in board:
        return True
    else:
        return False

#inserting a while loop so the game runs forever.
while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"): #if it's vitory for X
        print("X Wins! Congrats")
        break
    elif is_draw():
        print("It's a draw!") #if there is a draw
        break
    player_move("O")
    if is_victory("O"): #if it's vitory for O
        print_board()
        print("O Wins! Congrats")
        break
    elif is_draw():
        print("It's a draw!") #if there is a draw
        break
