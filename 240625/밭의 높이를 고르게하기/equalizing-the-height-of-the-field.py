n, h, t = map(int, input().split())
arr = list(map(int, input().split()))

ans = 9999999
for i in range(0, n-t):
    sum_subset = 0
    for j in range(i, i+4):
        print(arr[j])
        sum_subset += abs(arr[j]-h)
    ans = min(ans, sum_subset)
    print()

print(ans)