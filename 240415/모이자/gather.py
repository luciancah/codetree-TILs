import sys

n = int(input())
arr = list(map(int, input().split()))
min_distance = sys.maxsize

for i in range(1, len(arr)+1):
    diff = 0
    for j in range(1, len(arr)+1):
        # diff += abs(arr[i] - arr[j])
        diff += abs(i - j) * arr[j-1]
    

    min_distance = min(min_distance, diff)

print(diff)