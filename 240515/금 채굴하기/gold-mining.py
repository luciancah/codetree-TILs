n, m = list(map(int, input().split()))
arr = []
count = 0

for _ in range(n):
    arr.append(list(map(int, input().split())))

cb = m*m+(m+1)*(m+1)

offset = m // 2

for _ in range(offset):
    arr.insert(0, [0 * m])

print(arr)