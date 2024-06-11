n = int(input())
weight = []
for _ in range(n):
    weight.append(list(map(int,input().split())))

visited = [False] * n
visited[0] = True

track = []
min_dist = 999999999

def recur(count, curr_pos, dist, track):
    global min_dist
    if count == n:
        d = weight[curr_pos][0]
        if not d == 0:
            # print(count, curr_pos, dist, d, track)
            min_dist = min(min_dist, d+dist)
            return

    for i in range(n):
        if not visited[i] and weight[curr_pos][i] != 0:
            d = weight[curr_pos][i]
            track.append(i)
            visited[i] = True
            dist += d
            # print('순회', i, d, dist, track, visited)
            recur(count+1, i, dist, track)
            visited[i] = False
            dist -= d
            track.pop()

recur(1, 0, 0, track)

print(min_dist)