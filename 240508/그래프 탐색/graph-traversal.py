count = 0
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

visited = [False for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)



def DFS(v):
    for curr_v in graph[v]:
        if not visited[curr_v]:
            visited[curr_v] = True
            # count = count + 1
            DFS(curr_v)


DFS(1)
for i in visited:
    if i == True:
        count += 1
print(count)