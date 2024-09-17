#--------------Variable--------------#
board =[['*','*','*','*','*',],
        ['*','M','M','*','*',],
        ['*','K','I','K','*',],
        ['*','*','T','*','*',],
        ['*','*','L','*','*',]]

#--------------Function--------------#
def position(board):
    text_position = []
    text = 'KMITL'
    for rows in range(5):
        for cols in range(5):
            if board[rows][cols] in text:
                text_position.append([board[rows][cols], rows+1, cols+1])
    return text_position

def scan():
    pass
def count_kmitl(board):
    p = position(board)
    p = sorted(p)
    #Order alphabet pattern
    for index, items in enumerate(p):
        for j in items:
            print(j)
    #Stored Pattern
    #Count
    #Return Pattern, Count
    
#--------------Main--------------#
print(position(board))
#print(count_kmitl(board))