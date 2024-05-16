n, m = list(map(int, input().split()))
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

def in_range_1(x, y,x1,y1):
    return 0 <= x <= x1 < n and 0 <= y <= y1 < m

def in_range_2(basex, basey, x, y, x1, y1):
    return (basex-1 <= x or basey-1 <= y) and 0 <= x <= x1 < n and 0 <= y <= y1 < m

def calc_sum(bx, by, x, y):
    s = 0
    for i in range(bx, x+1):
        for j in range(by, y+1):
           s += arr[i][j]
    return s

max_sum = -9999999

for ai in range(n):
    for aj in range(m):

        sum1 = 0
        for ai2 in range(n):
            for aj2 in range(m):
                # 사각형 1번
                if not in_range_1(ai, aj, ai2, aj2):
                    continue
                sum1 = calc_sum(ai, aj, ai2, aj2)
                print('sum1', sum1)

                for bi in range(n):
                    for bj in range(m):
                        for bi2 in range(n):
                            for bj2 in range(m):
                                if not in_range_2(ai2, aj2, bi, bj, bi2, bj2):
                                    continue
                                sum2 = calc_sum(bi, bj, bi2, bj2)
                                # print('sum2', sum2)
                                temp_max = max_sum
                                max_sum = max(max_sum, sum1+sum2)
                                if temp_max != max_sum:
                                    print('사각형 1번', sum1, ai, aj, ai2, aj2)
                                    print('사각형 2번', sum2, bi, bj, bi2, bj2)

print(max_sum)