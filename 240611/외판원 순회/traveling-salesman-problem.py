n = int(input())
weight = []
for _ in range(n):
    weight.append(list(map(int,input().split())))

visited = [False] * n

track = []
min_dist = 999999999

def recur(count, curr_pos, dist, track):
    global min_dist
    if count == n:
        d = dist + weight[curr_pos][0]
        min_dist = min(min_dist, d)
        return

    for i in range(n):
        if not visited[i]:
            d = weight[curr_pos][i]
            track.append(i)
            visited[i] = True
            dist += d
            recur(count+1, i, dist, track)
            visited[i] = False
            dist -= d
            track.pop()

recur(0, 0, 0, track)

print(min_dist)