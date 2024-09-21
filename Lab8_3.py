#--------------Variable--------------#
board = [['*', '*', '*', '*', '*'],
         ['*', 'M', 'M', '*', '*'],
         ['*', 'K', 'I', 'K', '*'],
         ['*', '*', 'T', '*', '*'],
         ['*', '*', 'L', '*', '*'],]


#--------------Function--------------#

def scan(board):
    scan_text = 'KMITL'
    scan_lst = []
    for rows in range(5):
        for cols in range(5):
            if board[rows][cols] in scan_text:
                scan_lst.append([board[rows][cols], rows+1, cols+1])
    return scan_lst

def order_scan(board):
    scan_lst = scan(board)
    res = []
    add_to = []
    for i,e in enumerate(scan_lst):
        for j in str(e):
            if j not in add_to and j == 'K':
                add_to.append(scan_lst[i])
    return add_to

def count_Kmitl(board):
    pass
#--------------Main--------------#
print(order_scan(board))