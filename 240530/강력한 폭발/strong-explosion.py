import sys
sys.setrecursionlimit(10000)

n = int(input())
grid = []
bombs = []
bombs_placed = []
bp2 = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

for r in range(n):
    for c in range(n):
        if grid[r][c] == 1:
            bombs.append([r, c])


# bombs_count = 0

# def place_bomb(bombs_count):
#     if bombs_count == len(bombs):
#         print(bombs_placed)
#         return

#     for i in range(1, 4):
#         bombs_placed.append(i)
#         place_bomb(bombs_count + 1)
#         bombs_placed.pop
    
# place_bomb(0)


def choose(curr_num):
    if curr_num == len(bombs) + 1:
        print(bombs_placed)
        return

    for i in range(1, 4):
        bombs_placed.append(i)
        choose(curr_num + 1)
        bombs_placed.pop()

    return

choose(1)