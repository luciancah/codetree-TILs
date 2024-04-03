n = int(input())
positions = []
current = 50


line = [''] * 26
for i in range(n):
    positions += [list(map(str, input().split()))]

for position in positions:
    dist, direction = position


    if direction == 'L':
        for _ in range(int(dist)):
            current -= 1
            line[current] = 'white'
        print(line)

    if direction == 'R':
        for _ in range(int(dist)):
            current += 1
            line[current - 1] = 'black'
        print(line)

print(line)


print(len([x for x in line if x == 'white']), len([x for x in line if x == 'black']))