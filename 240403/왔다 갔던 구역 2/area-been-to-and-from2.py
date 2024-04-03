n = int(input())
positions = []
current = 50
line = [0] * 101

for i in range(n):
    positions += [list(map(str, input().split()))]

for position in positions:
    dist, direction = position

    if direction == 'L':
        for x in range(int(dist)):
            line[current - x] += 1

    if direction == 'R':
        for x in range(int(dist)):
            line[current + x - 1] += 1

print(len([x for x in line if x >= 2]))