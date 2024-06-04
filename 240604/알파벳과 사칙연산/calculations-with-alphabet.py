from collections import deque

exp = input()
expq = deque(exp)
expq.appendleft('+')
expq = list(expq)

ans = []
max_ans = 0


def solve_exp(expq):
    ans = 0
    i = 0
    while i < len(expq):
        o1 = expq[i]
        o2 = expq[i+1]

        if o1 == '+':
            ans += o2
        elif o1 == '-':
            ans -= o2
        else:
            ans *= o2
        i+= 2
    return ans

# solve_exp(['+', '4', '-', '1', '*', '2'])
nums = ['a', 'b', 'c', 'd']

max_ans = 0
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            for d in range(1, 5):
                # print(a, b, c, d)
                l = expq[:]
                for i in range(len(l)):
                    # print(i, a, b, c, d)
                    if l[i] == 'a':
                        l[i] = a
                    elif l[i] == 'b':
                        # print('asf', l[i], b)
                        l[i] = b
                        # print('asf', l[i], b)
                    elif l[i] == 'c':
                        l[i] = c
                    elif l[i] == 'd':
                        l[i] = d
                # print(l)
                max_ans = max(max_ans, solve_exp(l))

print(max_ans)

# def recur(expq):
#     global ans
#     if len(expq) == 0:
#         print(ans)
#         return

#     n = expq.popleft()
#     if n in nums:
#         for a in range(1, 5):
#             ans.append(str(a))
#             recur(expq)
#             ans.pop()
#     else:
#         ans.append(n)
#         recur(expq)
#         ans.pop()

# recur(expq)