from collections import defaultdict
from itertools import product

arr = input()
alps = 'abcdef'
mapper = defaultdict(str)
for i in range(len(arr)):
    if arr[i] in alps:
        mapper[arr[i]] = 0

prod = product([x for x in range(1,len(mapper)+1)], repeat=len(mapper))
print(list(prod))

def calc(original, operator, num):
    if operator == '-':
        return origial-num
    elif operator == '*':
        return original*num
    elif operator == '+':
        return original+num


# ans = 0
res = []
def recur(ans, count, p):
    if count+2 == len(arr):
        res.append(ans)
        print('asdf')
        print(ans, count)
        return
    
    if count == 0:
        ans = p[count]
        # print('1', ans)
        recur(ans, count+1)
    if count % 2 == 1:
        ans = calc(ans, arr[count+1], p[count])
        # print('2', ans)
        recur(ans, count+1)

for p in prod:
    recur(0, 0, p)

print(res)