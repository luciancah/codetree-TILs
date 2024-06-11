n = int(input())
grid = [input() for _ in range(4)]
coins = {}

for i in range(n):
    for j in range(n):
        if grid[i][j].isnumeric():
            coins[int(grid[i][j])] = [i, j]

coins = sorted(coins.items())
print(coins)

# 현 위치에서 나보다 큰 애를 거쳐서 (최소 3개 거치도록 크게) E까지 가게 (1회 반복에 다음 코인 위치까지 이동