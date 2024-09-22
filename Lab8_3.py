#--------------Variable--------------#
board = [['*', '*', '*', '*', '*'],
         ['*', 'M', 'M', '*', '*'],
         ['*', 'K', 'I', 'K', '*'],
         ['*', '*', 'T', '*', '*'],
         ['*', '*', 'L', '*', '*']]

#--------------Function--------------#
def scan(board):
    scan_text = 'KMITL'
    scan_lst = []
    for rows in range(5):
        for cols in range(5):
            if board[rows][cols] in scan_text:
                scan_lst.append([board[rows][cols], rows+1,cols+1])
    return scan_lst
def allCase(board):
    res = []
    lst = scan(board)
    for i in lst:
        if i[0] == 'K':
            for j in lst:
                if j[0] == 'M':
                    for k in lst:
                        if k[0] == 'I':
                            for l in lst:
                                if l[0] == 'T':
                                    for m in lst:
                                        if m[0] == 'L':
                                            temp = [i, j, k, l, m]
                                            res.append(temp)
    return res
def beautifulText(all_case):
    lst = allCase(all_case)
    res_str = ''
    for i in lst:
        for j in i:
            res_str += j[0] + ' ' + str(j[1]) + ' ' + str(j[2]) + ' ' + ' '
        res_str += '\n'
    return res_str

#--------------Main-----------------#
print(beautifulText(board))
print('KMITL Count = ', len(allCase(board)))