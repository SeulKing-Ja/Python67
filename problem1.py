n = int(input('Type N:'))
p_lst = []
def divide_zero(n):
    while True:
        if n == 1:
            return p_lst
        else:
            if n % 2 == 0:
                p_lst.append(2)
                n = n / 2
            elif n % 3 == 0:
                p_lst.append(3)
                n = n / 3
            elif n % 5 == 0:
                p_lst.append(5)
                n = n / 5
            elif n % 7 == 0:
                p_lst.append(7)
                n = n / 7

    
def sum_num(p_lst):
    res = 0
    for i in p_lst:
        res += i
    return res

def is_prime(res):
    c = 0
    if (res == 2 or res == 5 or res == 3 or res == 7):
        c += 0
    elif(res % 2 == 0 or res % 3 == 0 or res % 5 == 0 or res % 7 == 0):
        c -= 1

    if res % 1 == 0:
        c += 1

    if c == 1:
        return True
    else:
        return False


r = 0
n_new = n
while True:
    if is_prime(n_new):
        if is_prime(n):
            r+=1
        print(f'N = {n} {r} รอบ')
        break
    p_lst = []
    p_lst = divide_zero(n_new)
    n_new = sum_num(p_lst)
    print(n_new, p_lst)
    r += 1
    