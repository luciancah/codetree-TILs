import sys

n = int(input())
grid = [input() for _ in range(n)]
coins = {}

for i in range(n):
    for j in range(n):
        if grid[i][j].isnumeric():
            coins[int(grid[i][j])] = [i, j]
        if grid[i][j] == 'S':
            coins[0] = [i, j]
        if grid[i][j] == 'E':
            coins[99] = [i, j]

if len(coins) < 5:
    print(-1)
    sys.exit()

def calc_dist(a, b):
    res = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return res

min_dist = 9999

def recur(curr_coin, coin_count, move_dist):
    global min_dist
    if coin_count == 3:
        move_dist += calc_dist(coins[curr_coin], coins[99])
        min_dist = min(move_dist, min_dist)
        return

    for i in range(curr_coin+1, len(coins)-2):
        recur(i, coin_count+1, move_dist+calc_dist(coins[curr_coin], coins[i]))

recur(0, 0, 0)

print(min_dist)