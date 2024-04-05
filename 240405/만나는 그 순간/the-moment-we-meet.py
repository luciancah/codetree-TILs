n, m = list(map(int, input().split()))
moves = []
a_pos = []
b_pos = []
for i in range(n+m):
    moves += [list(map(str,input().split()))]

a_moves = moves[0:n]
b_moves = moves[n:]

position = 0
for dir, dist in a_moves:
    if dir == 'R':
        position += int(dist)
    else:
        position -= int(dist)
    a_pos.append(position)

position = 0
for dir, dist in b_moves:
    if dir == 'R':
        position += int(dist)
    else:
        position -= int(dist)
    b_pos.append(position)

a_meet = -1
count = 0
for i, a in enumerate(a_pos):
    print('a', i, a, a_moves[i][1], b_pos)
    count += int(a_moves[i][1])
    if a in b_pos:
        a_meet = count
        break

b_meet = -1
count = 0
for i, b in enumerate(b_pos):
    print('b', i, b, b_moves[i][1], a_pos)
    count += int(b_moves[i][1])
    if a in a_pos:
        b_meet = count
        break

print(max(a_meet, b_meet))