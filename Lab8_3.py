#--------------Variable--------------#
board = [['*', '*', '*', '*', '*'],
         ['*', 'M', 'M', '*', '*'],
         ['*', 'K', 'I', 'K', '*'],
         ['*', '*', 'T', '*', '*'],
         ['*', '*', 'L', '*', '*'],]


#--------------Function--------------#
def createBoard(board):
    for i,e in enumerate(board):
        for j in e:
            print(j, end="")
        print()

def scan(board):
    scan_text = 'KMITL'
    lst = []
    for rows in range(5):
        for cols in range(5):
            if board[rows][cols] in scan_text:
                lst.append([board[rows][cols], rows+1, cols+1])
    return lst 
        
def order_text(board): 
    lst = scan(board)
    res = []
    to_addlst = []
    i = 0
    max = len(lst)
    while True:
        for index,items in enumerate(lst):
            pass
        break
    print(to_addlst)
#--------------Main--------------#
print(order_text(board))