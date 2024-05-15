import copy

n, m = list(map(int, input().split()))
tmp = []
max_count = 0

for _ in range(n):
    tmp.append(list(map(int, input().split())))

k = 0
while k <= 2 * (n-1):
    arr = copy.deepcopy(tmp)
    cb = k*k+(k+1)*(k+1)

    for _ in range(k):
        arr.insert(0, [0] * n)
        arr.append([0] * n)

    for a in range(len(arr)):
        for _ in range(k):
            arr[a].insert(0, 0)
            arr[a].append(0)

    for i in range(k, n+k):
        for j in range(k, n+k):
            count = 0
            # 마름모 탐색
            for x in range(i-k, i+k+1):
                for y in range(j-k, j+k+1):
                    if abs(x-i) + abs(y-j) > k:
                        continue
                    count += arr[x][y]
            if m * count >= cb:
                max_count = max(count, max_count)
    k+=1


print(max_count)