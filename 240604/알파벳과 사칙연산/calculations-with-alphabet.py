from collections import deque

exp = input()
expq = deque(exp)

ans = []
max_ans = 0

expq.appendleft('+')
expq = list(expq)

def solve_exp(res, exp):
    max_ans = -999
    for j in range(1, 5):
        ans = res

        o1 = exp[0]
        o2 = j

        if o1 == '+':
            ans += o2
        elif o1 == '-':
            ans -= o2
        else:
            ans *= o2

        max_ans = max(max_ans, ans)
    return max_ans

res = 0
for i in range(0, len(expq)-1, 2):
    res = solve_exp(res, expq[i:i+2])

print(res)