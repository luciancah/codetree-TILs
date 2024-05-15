n, m = list(map(int, input().split()))
arr = []
max_price = 0

for _ in range(n):
    arr.append(list(map(int, input().split())))

cb = m*m+(m+1)*(m+1)

offset = m

for _ in range(offset):
    arr.insert(0, [0] * n)
    arr.append([0] * n)

for a in arr:
    for _ in range(offset):
        a.insert(0, 0)
        a.append(0)

print(arr)  

# for i in range(offset, n+offset):
#     for j in range(offset, n+offset):
#         price = 0
#         # 마름모 탐색
#         for x in range(i-m, i+m):
#             print(arr[x])
#             for y in range(j-m, j+m):
#                 if abs(x-i) + abs(y-j) > m:
#                     continue
#                 price += arr[x][y]
#         max_price = max(price, max_price)

# print(max_price)