n, m = list(map(int, input().split()))
position = 0
moves = []
a_pos = []
b_pos = []
for i in range(n+m):
    moves += [list(map(str,input().split()))]
 
a_moves = moves[0:n]
b_moves = moves[n:]

print(a_moves)

for move in a_moves:
    dir, dist = move
    dist = int(dist)

    for _ in range(dist):
        if dir == 'L':
            position -= 1
        if dir == 'R':
            position += 1
        a_pos.append(position)

for move in b_moves:
    dir, dist = move
    dist = int(dist)

    for _ in range(dist):
        if dir == 'L':
            position -= 1
        if dir == 'R':
            position += 1
        b_pos.append(position)

print(a_pos, b_pos)