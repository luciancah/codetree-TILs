n = int(input())

memo = [0] * (n + 1)

def pick_fib(n):
    if n <= 2:
        memo[n] = 1
        return 1
    if memo[n]:
        return memo[n]
    else:
        memo[n] = pick_fib(n - 1) + pick_fib(n - 2)
    return memo[n]

print(pick_fib(n))