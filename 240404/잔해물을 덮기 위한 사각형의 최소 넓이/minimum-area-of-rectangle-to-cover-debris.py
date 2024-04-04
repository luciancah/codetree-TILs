offset = 1001
matrix = [[0 for _ in range(2002)] for _ in range(2002)]
count = 0
positions = []
answers = []
for i in range(2):
    positions += [list(map(int, input().split()))]

for index, values in enumerate(positions):
    c = 1 if index == 0 else -1
    x1, y1, x2, y2 = values
    x1, y1 = x1 + offset, y1 + offset
    x2, y2 = x2 + offset, y2 + offset

    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] += c
            

for i in range(0, 2002):
        for j in range(0, 2002):

            if matrix[i][j] == 1:
                answers += [[i, j]]

x_length = answers[-1][0] - answers[0][0] + 1
y_length = answers[-1][1] - answers[0][1] + 1



print(x_length * y_length)