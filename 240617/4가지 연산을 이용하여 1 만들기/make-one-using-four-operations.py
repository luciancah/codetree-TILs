n = int(input())

def calc(n):
    if n % 3 == 0:
        return n // 3
    if n % 2 == 0:
        return n // 2
    if (n+1) % 3 == 0:
        return n + 1
    return n - 1

# def bfs():
#     while n:
#         depth = 0

#         for i in range(4):

i = 0
while n > 1:
    n = calc(n)
    i += 1
print(i)