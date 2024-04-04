n = int(input())
positions = []
offset = 500

matrix = [[0] * 1001] * 1001
for i in range(n):
    positions += [list(map(int, input().split()))]

for position in positions:
    x1, y1, x2, y2 = position.split()
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            matrix[i+offset][j+offset] += 1

print(matrix)