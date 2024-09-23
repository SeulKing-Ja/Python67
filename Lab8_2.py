#Function
def create_board():
    board = []
    size = 10
    for i in range(size): 
        for j in range(size):
            board.append('0')
    return board

def write_board(board):
    for i in range(len(board)):
        if i % 10 == 0:
            print()
        print(board[i], end='')
        


#Main   
board = create_board()
write_board(board)