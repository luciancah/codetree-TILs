n, m = list(map(int, input().split()))
k = 1
arr = []
max_price = 0

for _ in range(n):
    arr.append(list(map(int, input().split())))

for k in range(n+2):
    cb = k*k+(k+1)*(k+1)

    for _ in range(k):
        arr.insert(0, [0] * n)
        arr.append([0] * n)

    for a in arr:
        for _ in range(k):
            a.insert(0, 0)
            a.append(0)

    for i in range(k, n+k):
        for j in range(k, n+k):
            price = 0
            # 마름모 탐색
            for x in range(i-k, i+k):
                for y in range(j-k, j+k):
                    if abs(x-i) + abs(y-j) > k:
                        continue
                    price += arr[x][y]
            if m * price >= cb:
                max_price = max(price, max_price)

print(max_price)