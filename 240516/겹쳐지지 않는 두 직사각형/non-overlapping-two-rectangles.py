n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def calc_sum(bx, by, x, y):
    s = 0
    for i in range(bx, x + 1):
        for j in range(by, y + 1):
            s += arr[i][j]
    return s

def rectangles_overlap(a, b):
    # a and b are tuples of (x1, y1, x2, y2)
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    # Return true if there is no overlap
    return not (ax2 < bx1 or bx2 < ax1 or ay2 < by1 or by2 < ay1)

max_sum = -float('inf')

# Iterate over all pairs of rectangles
for ai in range(n):
    for aj in range(m):
        for ai2 in range(ai, n):
            for aj2 in range(aj, m):
                sum1 = calc_sum(ai, aj, ai2, aj2)
                # Now, for every possible second rectangle
                for bi in range(n):
                    for bj in range(m):
                        for bi2 in range(bi, n):
                            for bj2 in range(bj, m):
                                if rectangles_overlap((ai, aj, ai2, aj2), (bi, bj, bi2, bj2)):
                                    continue
                                sum2 = calc_sum(bi, bj, bi2, bj2)
                                max_sum = max(max_sum, sum1 + sum2)

print(max_sum)


# n, m = list(map(int, input().split()))
# arr = []

# for _ in range(n):
#     arr.append(list(map(int, input().split())))

# def in_range_1(x, y,x1,y1):
#     return 0 <= x <= x1 < n and 0 <= y <= y1 < m

# def in_range_2(basex, basey, x, y, x1, y1):
#     return (not (basex >= x and basey >= y)) and 0 <= x <= x1 < n and 0 <= y <= y1 < m
    


# def calc_sum(bx, by, x, y):
#     s = 0
#     for i in range(bx, x+1):
#         for j in range(by, y+1):
#            s += arr[i][j]
#     return s

# max_sum = -9999999

# for ai in range(n):
#     for aj in range(m):

#         sum1 = 0
#         for ai2 in range(n):
#             for aj2 in range(m):
#                 # 사각형 1번
#                 if not in_range_1(ai, aj, ai2, aj2):
#                     continue
#                 sum1 = calc_sum(ai, aj, ai2, aj2)
#                 # print('sum1', sum1)
#                 for bi in range(n):
#                     for bj in range(m):
#                         for bi2 in range(n):
#                             for bj2 in range(m):

#                                 if not in_range_2(ai2, aj2, bi, bj, bi2, bj2):
#                                     continue
#                                 sum2 = calc_sum(bi, bj, bi2, bj2)
#                                 # print('sum2', sum2)
#                                 # temp_max = max_sum
#                                 max_sum = max(max_sum, sum1+sum2)
#                                 # if temp_max != max_sum:
#                                 #     print('사각형 1번', sum1, ai, aj, ai2, aj2)
#                                 #     print('사각형 2번', sum2, bi, bj, bi2, bj2)

# print(max_sum)