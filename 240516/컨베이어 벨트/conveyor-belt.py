n, t = list(map(int, input().split()))
arr = []
for i in range(2):
    arr += list(map(int,input().split()))

last = arr.pop()
arr.insert(0, last)

print(*arr[:3])
print(*arr[3:])