# 선언시에 (n+1)*(m+1), -1로 초기화 해서 평균 구할때 빼고 구하기

n, m, q = list(map(int, input().split()))
grid = [[-1] * (m+2) for _ in range(n+2)]

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        grid[i+1][j+1] = arr[j]

# 한바퀴 돌리는 함수 (2차원 배열 받아서 2차원 배열 반환)
def turn_grid(grid):
    # print('old', grid)
    arr = []

    for i in range(len(grid[0])):
        arr.append(grid[0][i])

    for i in range(1, len(grid)-1):
        arr.append(grid[i][-1])

    for i in range(len(grid[0])-1, -1, -1):
        arr.append(grid[-1][i])

    for i in range(len(grid)-2, 0, -1):
        arr.append(grid[i][0])

    arr.insert(0, arr.pop(arr[-1]))

    # grid[0] = arr[:len(grid[0])]

    # print('new', grid)
    return arr

temp = [[6, 1, 0, 5, 5], [1, 2, 1, 6, 6], [2, 5, 2, 8, 8]]
print(turn_grid(temp))

# [1, 6, 0, 5, 5, 6, 8, 8, 2, 5, 2, 1]