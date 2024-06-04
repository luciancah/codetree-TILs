from collections import deque

exp = input()
expq = deque(exp)
expq.appendleft('+')
expq = list(expq)


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

max_ans = -99999
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            for d in range(1, 5):
                for e in range(1, 5):
                    for f in range(1, 5):
                        l = expq[:]
                        for i in range(len(l)):
                            if l[i] == 'a':
                                l[i] = a
                            elif l[i] == 'b':
                                l[i] = b
                            elif l[i] == 'c':
                                l[i] = c
                            elif l[i] == 'd':
                                l[i] = d
                            elif l[i] == 'e':
                                l[i] = e
                            elif l[i] == 'f':
                                l[i] = f
                        max_ans = max(max_ans, solve_exp(l))

print(max_ans)