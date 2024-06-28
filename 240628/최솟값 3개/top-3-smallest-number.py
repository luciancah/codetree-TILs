from heapq import heappush, heappop

n = int(input())
nums = list(map(int, input().split()))

heap = []
for i in range(len(nums)):
    heappush(heap, nums[i])
    if i >=2:
        res = 1
        for j in range(3):
            res *= heap[j]
        print(res)
    else:
        print(-1)

# print(heap)