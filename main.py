
'''
def power_until(n):
    res = 0
    if n < 9:
        return n
    else:
        for i in str(n):
            res += int(i) ** 2
        return power_until(res)
print(power_until(10))
'''

'''
Input: [1,6], [3,7], [10,11]
Output: [1,7], [10,11]
(1,4), (5,8), (9,13), (15,20)
'''

n = [[1,6], [10,11], [3,7]]
def interval_lst(lst):
    lst.sort()
    res = []
    for i in range(len(lst)):
        if i <= len(lst) and lst[i]  < lst[i+1]:
            res.append(lst[i][0]+lst[i+1][1])
        else:
            res.append(i) 
    return res
print(interval_lst(n))




x = [[1,6], [3,7], [10,11]]
lst = [] 
for i in x:
    for j in i:
        lst.append(j) 
#[1, 6, 3, 7, 10, 11]

ans = []
ban = False
for i in range(len(lst)):
    if i != len(lst)-1:
        # print(lst[i],lst[i+1])
        if lst[i] < lst[i+1] and not ban:
            ans.append(lst[i])
        elif ban:
            ban = False
        else:
            ban = True

    else:
        ans.append(lst[i])
ans_final = [[ans[i], ans[i+1]] for i in range(0, len(ans), 2)]
print(ans_final)