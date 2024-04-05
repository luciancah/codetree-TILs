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
for i, a in enumerate(a_pos):
    if a in set(b_pos):
        a_meet = a
    break

b_meet = -1
for i, b in enumerate(b_pos):
    if a in set(a_pos):
        b_meet = b
    break

print(max(a_meet, b_meet))