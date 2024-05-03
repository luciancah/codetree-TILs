arr = []
for _ in range(19):
    arr.append(list(map(int, input().split())))

win = 0
black = False
black_pos = []
white = False
white_pos = []

for i in range(15):
    for j in range(15):
        if arr[i][j] == 1:
            if arr[i][j+1] == arr[i][j+2] == arr[i][j+3] == arr[i][j+4] == 1:
                win = 1
                black_pos = [i, j+2]
            if arr[i+1][j] == arr[i+2][j] == arr[i+3][j] == arr[i+4][j] == 1:
                win = 1
                black_pos = [i+2, j]
            if arr[i+1][j+1] == arr[i+2][j+2] == arr[i+3][j+3] == arr[i+4][j+4] == 1:
                win = 1
                black_pos = [i+2, j+2]
            if arr[i-1][j-1] == arr[i-2][j-2] == arr[i-3][j-3] == arr[i-4][j-4] == 1:
                win = 1
                black_pos = [i-2, j-2]
        
        if arr[i][j] == 2:
            if arr[i][j+1] == arr[i][j+2] == arr[i][j+3] == arr[i][j+4] == 2:
                win = 2
                white_pos = [i, j+2]
            if arr[i+1][j] == arr[i+2][j] == arr[i+3][j] == arr[i+4][j] == 2:
                win = 2
                white_pos = [i+2, j]
            if arr[i+1][j+1] == arr[i+2][j+2] == arr[i+3][j+3] == arr[i+4][j+4] == 2:
                win = 2
                white_pos = [i+2, j+2]
            if arr[i-1][j-1] == arr[i-2][j-2] == arr[i-3][j-3] == arr[i-4][j-4] == 1:
                win = 1
                white_pos = [i-2, j-2]

print(win)
if win == 1:
    print(black_pos[0]+1, black_pos[1]+1)
if win == 2:
    print(white_pos[0]+1, white_pos[1]+1)