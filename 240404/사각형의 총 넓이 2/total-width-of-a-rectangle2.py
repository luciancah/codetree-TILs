n = int(input())
positions = []
offset = 101
count = 0

matrix = [[0] * 202] * 202
for i in range(n):
    positions += [list(map(int, input().split()))]

for position in positions:
    x1, y1, x2, y2 = position
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i+offset][j+offset] += 1

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] > 0:
            count += 1

print(matrix)