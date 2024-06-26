n = int(input())
mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])

max_sum = 0

def get_max_sum_in_range(row, col, k):
    if row < k - 1 or col < k - 1: return 0
    range_max = 0
    for c in range(1, k-1):
        # print(k)
        # print(row, col, row-k+1, col-k+1, c)
        # print(row-k+1, col, row, col-k+1, c)
        range_max = max(range_max, sum([
            mat[i][j]
            for i in range(n)
            for j in range(n)
            if i <= row and j <= col
            and i >= row-k+1 and j >= col-k+1
             and (abs(row-i)+abs(col-j) == c or abs(row-k+1 - i)+abs(col-k+1 - j) == c)
        ]))
        range_max = max(range_max, sum([
            mat[i][j]
            for i in range(n)
            for j in range(n)
            if i <= row and j <= col
            and i >= row-k+1 and j >= col-k+1
             and (abs(row-k+1 - i)+abs(col-j) == c or abs(row-i)+abs(col-k+1 - j) == c)
        ]))
    return range_max

for row in range(n):
    for col in range(n):
        if n == 3:
            max_sum = max(get_max_sum_in_range(row, col, 3), max_sum)
        for k in range(3, n+1):
            max_sum = max(get_max_sum_in_range(row, col, k), max_sum)

print(max_sum)