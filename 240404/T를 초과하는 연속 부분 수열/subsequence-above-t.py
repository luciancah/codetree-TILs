n, t = list(map(int, input().split()))
numbers = list(map(int, input().split()))

ans, count = 0, 0
for i in range(n):
    if i >= 1 and numbers[i] > t:
        count += 1
    else:
        count = 1

    ans = max(ans, count)

print(ans)