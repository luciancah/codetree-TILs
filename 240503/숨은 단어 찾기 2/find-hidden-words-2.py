n, m = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(input())

count = 0

for i in range(n - 2):
    for j in range(m - 2):
        if arr[i][j] == 'L':
            if arr[i][j+1] == arr[i][j+2] == 'E':
                # print(1, count, i, j)
                count += 1
            if arr[i+1][j] == arr[i+2][j] == 'E':
                # print(1, count, i, j)
                count += 1
            if arr[i+1][j+1] == arr[i+2][j+2] == 'E':
                # print(1, count, i, j)
                count += 1

        if arr[i][j] == 'E':
            if arr[i][j+1] == 'E' and arr[i][j+2] == 'L':
                # print(2, count, i, j)
                count += 1
            if arr[i+1][j] == 'E' and arr[i+2][j] == 'L':
                # print(2, count, i, j)
                count += 1
            if arr[i+1][j+1] == 'E' and arr[i+2][j+2] == 'L':
                # print(2, count, i, j)
                count += 1

for i in range(n-3, n):
    for j in range(m - 2):
        if arr[i][j] == 'L':
            if arr[i][j+1] == arr[i][j+2] == 'E':
                # print(3, count, i, j)
                count += 1

        if arr[i][j] == 'E':
            if arr[i][j+1] == 'E' and arr[i][j+2] == 'L':
                # print(3, count, i, j)
                count += 1

for i in range(n-2):
    for j in range(m - 3, m):
        if arr[i][j] == 'L':
            if arr[i+1][j] == arr[i+2][j] == 'E':
                # print(4, count, i, j)
                count += 1

        if arr[i][j] == 'E':
            if arr[i+1][j] == 'E' and arr[i+2][j] == 'L':
                # print(4, count, i, j)
                count += 1


print(count)