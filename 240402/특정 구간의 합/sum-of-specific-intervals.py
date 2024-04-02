n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr2 = []

for i in range(m):
    arr2.append(list(map(int, input().split())))

print(n, m, arr, arr2)

prefixSum = []

for i in range(len(arr)):
    if i == 0:
        prefixSum.append(arr[i])
    prefixSum.append(arr[i] + prefixSum[i])

print(prefixSum)