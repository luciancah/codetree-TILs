from collections import Counter

t = int(input())

# 상하좌우
dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]
move_dirs = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

def change_dir(curr_dir):
    direction_map = {
        'R': 'L',
        'L': 'R',
        'U': 'D',
        'D': 'U'
    }
    return direction_map[curr_dir]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

for i in range(t):
    n, m = list(map(int, input().split()))
    balls = []
    grid = [[0] * n for _ in range(n)]

    for i in range(m):
        balls.append(list(map(str, input().split())))
        balls[i][0] = int(balls[i][0]) - 1
        balls[i][1] = int(balls[i][1]) - 1

    for _ in range(n*n):
        # grid = [[0] * n for _ in range(n)]
        # for b in balls:
        #     grid[b[0]][b[1]] = b[2]
        # for i in range(len(grid)):
        #     print(*grid[i])
        # print()
        for b in balls:
            y, x, curr_dir = b[0], b[1], move_dirs[b[2]]
            ny, nx = b[0] + dys[curr_dir], b[1] + dxs[curr_dir]

            if in_range(ny, nx):
                # print('1', y, x, ny, nx)
                b[0], b[1] = ny, nx
            else:
                # print('2', y, x, ny, nx)
                b[2] = change_dir(b[2])
        
        dups = []
        for i in range(len(balls)):
            for j in range(i+1, len(balls)):
                if balls[i][0:2] == balls[j][0:2]:
                    dups.append(balls[i])
                    dups.append(balls[j])
        # print(balls)
        # print(dups)
        for d in dups:
            balls.remove(d)

    print(len(balls))