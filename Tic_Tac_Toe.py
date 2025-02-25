"""Description: This is a Tic-Tac-Toe game where player plays against computer.
   Player is 'O' and computer is 'X'."""

import random

def display_board(board):
    """Displays the Tic-Tac-Toe Board"""
    rl = "+-------+-------+-------+"
    rl2 = "|       |       |       |"
    
    for i in range(3):
        print(rl)
        print(rl2) 
        print("|  ",board[i][0],"  |  ",board[i][1],"  |  ",board[i][2],"  |")
        print(rl2)
    print(rl)

def enter_move(board):
    """Allows player to enter a move."""
    while True:
        try:
            move = int(input("Enter your move: "))   

            """Check the input whether it is valid"""
            if move < 1 or move > 9:
                print("Invalid choice! Choose a number between 1 and 9")
                continue
                
            if move <= 3:
                board[0][move - 1] = "O"
                break
            elif 3 < move <= 6:
                board[1][move - 4] = "O"
                break
            else:
                board[2][move - 7] = "O"
                break
            display_board(board)
        except ValueError:
            print("Invalid input! Enter a number (1-9)")
            
def make_list_of_free_fields(board):
    """Returns a list free fields in board"""
    free = [(row,column) for row in range(3) for column in range(3) if isinstance(board[row][column],int)]
    return free

def victory_for(board, sign):
    """Check whether given sign has won or not.........."""
    vic = False

    # Checking whether its row victory.........
    for row in board:
        if set(row) == {sign}:
            vic =  True
            
    # Checking whether its column victory........       
    for col in range(3):
        if set(board[r][col] for r in range(3)) == {sign}:
            vic =  True

    if set(board[i][i] for i in range(3)) == {sign} or set(board[i][2-i] for i in range(3)) == {sign}:
        vic = True
        
    return vic

def draw_move(board):
        """Check whether its a draw.........."""
        print("It's a tie!")
    

# Main Program.............
       
board = [[1,2,3],[4,5,6],[7,8,9]]  # Initial board            
board[1][1] = "X"
display_board(board)
isVic = False # Check whether game is over or not

free = make_list_of_free_fields(board)
while free != []:

    """Player's turn"""
    enter_move(board)

    """Check whether player has won or not""" 
    if victory_for(board, "O"):
        print("You won!")
        isVic = True
        break
        
    free = make_list_of_free_fields(board)

    """Computer's turn"""
    if free:
        row, col = random.choice(free)
        board[row][col] = "X"
    display_board(board)

    """Check whether computer has won or not"""
    if victory_for(board, "X"):
        print("Computer won!")
        isVic = True
        break        
    free = make_list_of_free_fields(board)

"""Check whether its a draw or not"""
if not(isVic):  # Check if board is full
        print("It's a tie!")
