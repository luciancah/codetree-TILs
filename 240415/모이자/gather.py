import sys

n = int(input())
arr = list(map(int, input().split()))
min_distance = sys.maxsize

for i in range(len(arr)):
    diff = 0
    for j in range(len(arr)):
        diff += abs(arr[i] - arr[j])
    
    min_distance = min(min_distance, diff)

print(diff)