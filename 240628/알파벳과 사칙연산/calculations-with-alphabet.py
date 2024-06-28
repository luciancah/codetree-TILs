import sys
from collections import defaultdict
from itertools import product

arr = input()
alps = 'abcdef'
mapper = defaultdict(str)
# mapper = {
#     'a': 0,
#     'b': 1,
#     'c': 2,
#     'd': 3,
#     'e': 4,
#     'f': 5
# }

c = 0
for i in range(len(arr)):
    if arr[i] in alps:
        if arr[i] in mapper.keys():
            continue
        mapper[arr[i]] = c
        c += 1
        

# print(mapper)

prod = list(product([1, 2, 3, 4], repeat=len(mapper)))

# print(prod)

def calc(original, operator, num):
    if operator == '-':
        return original-num
    elif operator == '*':
        return original*num
    elif operator == '+':
        return original+num


# ans = 0
res = []
def recur(ans, count, p):
    # print(count)
    if count+1 >= len(arr):
        res.append(ans)
        # print('asdf')
        # print(ans, count)
        return
    
    if count == 0:
        ans = p[mapper[arr[count]]]
        # print('1', ans)
        recur(ans, count+1, p)
    if count % 2 == 1:
        ans = calc(ans, arr[count], p[mapper[arr[count+1]]])

        # print('2', ans)
        recur(ans, count+2, p)

if len(arr) == 1:
    print('4')
    sys.exit()

for p in prod:
    # print('------------')
    recur(0, 0, p)

print(max(res))