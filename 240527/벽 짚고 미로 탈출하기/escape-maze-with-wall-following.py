n = int(input())
x, y = list(map(int, input().split()))
grid = []

for _ in range(n):
    grid.append(input())

dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]] # 동 북 서 남

x, y = x - 1, y - 1

dist = 0
d = 0
count = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def change_direction(d, direction):
    p1, m1 = d + 1, d - 1
    # ccw
    if direction == 1:
        if p1 >= 4:
            p1 = p1 - 4
            return p1
        return p1
    # cw
    else:
        if m1 < 0:
            m1 = m1 + 4
            return m1
        return m1

f = False
c = 0
while(c < n*n):
    ny, nx = y + dirs[d][0], x + dirs[d][1]
    # print('카운트', y, x, ny, nx)

    # 탈출
    if not in_range(nx, ny):
        # print('out')
        f = True
        count += 1
        break
    
    # 바라보는 방향으로 이동할 수 있을때
    if grid[ny][nx] == '.':
        # 바라보는 방향의 오른쪽 판독
        flag = 0
        if d == 0 and ny != n-1:
            ('1')
            if grid[ny+1][nx] == '#':
                flag = 1
            else:
                flag = -1
        elif d == 3 and nx != 0:
            ('2')
            if grid[ny][nx-1] == '#':
                flag = 1
            else:
                flag = -1
        elif d == 2 and ny != 0:
            ('3')
            if grid[ny-1][nx] == '#':
                flag = 1
            else:
                flag = -1
        elif d == 1 and nx != n-1:
            ('4')
            if grid[ny][nx+1] == '#':
                flag = 1
            else:
                flag = -1

        # 오른쪽에 벽이 있을때
        if flag == 1:
            y, x = ny, nx
            # print('2', y, x, ny, nx)
            count += 1

        # 오른쪽에 벽이 없을때
        if flag == -1:
            y, x = ny, nx
            # print('3', y, x, ny, nx)
            count += 1
            # print('asdf1', y, x, d)
            d = change_direction(d, -1)
            y, x = y + dirs[d][0], x + dirs[d][1]
            # print('asdf2', y, x, d)
            count += 1

    # 바라보는 방향으로 이동할 수 없을때
    else:
        d = change_direction(d, 1)
    c += 1

print(count) if f == True else print(-1)