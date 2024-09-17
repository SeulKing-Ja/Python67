#--------------library--------------#
import random as rd

#--------------Variable--------------#
board =[['o|','o|','o|','o|','o|','o|'],
        ['o|','o|','o|','o|','o|','o|'],
        ['o|','o|','o|','o|','o|','o|'],
        ['o|','o|','o|','o|','o|','o|'],
        ['o|','o|','o|','o|','o|','o|'],
        ['o|','o|','o|','o|','o|','o|']]

#--------------Function--------------#
def create_board(board):
    for i in reversed(board):
        for index,e in enumerate(i):
            print(e, end='')
        print()

def play(board, rows, player):
    player_select = rows - 1
    if player == 'player':
        for rows in range(6):
            if board[rows][player_select] == 'o|':
                board[rows][player_select] = 'P|'
                break
    elif player == 'com':
        for rows in range(6):
            if board[rows][player_select] == 'o|':
                board[rows][player_select] = 'C|'
                break

def win(player):
    for rows in range(6): 
        for cols in range(3):
           if  board[rows][cols] == player and board[rows+1][cols+1] == player and board[rows+2][cols+2] == player or board[rows][cols] == player and board[rows-1][cols+1] == player and board[rows-2][cols+2] == player:
               return(True)
           elif board[rows][cols] == player and board[rows][cols+1] == player and board[rows][cols+2] == player:
               return(True)
           elif board[rows][cols] == player and board[rows+1][cols] == player and board[rows+2][cols] == player:
               return(True)

#--------------Main--------------#
create_board(board)
while True:
    #Win
    if win('P|'):
        print('Player Win!!!')
        break
    elif win('C|'):
        print('Computer Win!!!')
        break
    
    #Player Turn
    player = int(input('Enter slot (1-6) : '))
    play(board, player, 'player')
    create_board(board)

    #Computer Turn
    com = rd.randint(1, 6)
    play(board, com, 'com')
    print('Computer Select : ', com)
    create_board(board)
    