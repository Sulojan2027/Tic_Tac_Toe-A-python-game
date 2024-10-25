#changed
def display_board(board):
    rl = "+-------+-------+-------+"
    rl2 = "|       |       |       |"
    
    for i in range(3):
        print(rl)
        print(rl2) 
        print("|  ",board[i][0],"  |  ",board[i][1],"  |  ",board[i][2],"  |")
        print(rl2)
    print(rl)

def enter_move(board):
    move = int(input("Enter your move: "))
    if move <= 3:
        board[0][move - 1] = "0"
    elif 3 < move <= 6:
        board[1][move - 4] = "0"
    else:
        board[2][move - 7] = "0"
    display_board(board)

def make_list_of_free_fields(board):
    free = []
    num = [i for i in range(1,10)]
    for row in board:
        for x in row:
            if x in num:
                free.append((board.index(row),row.index(x)))
    return free

def victory_for(board, sign):
    vic = False
    for row in board:
        c = 0
        for x in row:
            if x == sign:
                c = c + 1
        if c == 3:
            vic =  True
    for i in range(3):
        c = 0
        for j in range(3):
            if board[j][i] == sign:
                c = c + 1
        if c == 3:
            vic =  True
    if vic:
        if sign == "X":
            print("Computer won!")
        elif sign == "0":
            print("You won!")
    return vic

def draw_move(board):
        print("It's a tie!")
    

        
board = [[1,2,3],[4,5,6],[7,8,9]]        
from random import randrange            
board[1][1] = "X"
display_board(board)

free = make_list_of_free_fields(board)
while free != []:
    enter_move(board)
    a = victory_for(board, "0")
    if a:
        break
    free = make_list_of_free_fields(board)   
    x = randrange(3)
    y = randrange(3)
    while (x,y) not in free:
        x = randrange(3)
        y = randrange(3)    
    board[x][y] = "X"
    display_board(board)
    b = victory_for(board, "X")
    if b:
        break        
    free = make_list_of_free_fields(board)
if not(a or b):
    draw_move(board)
