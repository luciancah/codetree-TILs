n, m = list(map(int, input().split()))
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

def in_range_1(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def in_range_2(basex, basey, x, y):
    return (basex <= x or basey <= y) and x < n and y < m


max_sum = -9999999

for ai in range(n):
    for aj in range(m):

        sum1 = 0
        for ai2 in range(n):
            for aj2 in range(m):
                # 사각형 1번
                if not in_range_1(ai2, aj2):
                    continue
                sum1 += arr[ai2][aj2]
                print('sum1', sum1)

                for bi in range(n):
                    for bj in range(m):
                        sum2 = 0
                        for bi2 in range(n):
                            for bj2 in range(m):
                                if not in_range_2(ai2, aj2, bi2, bj2):
                                    continue
                                sum2 += arr[bi2][bj2]
                        print('sum2', sum2)
                print(sum1)
                temp_max = max_sum
                max_sum = max(max_sum, sum1+sum2)
                if temp_max != max_sum:
                    print('사각형 1번', sum1, ai, aj, ai2, aj2)
                    print('사각형 2번', sum2, bi, bj, bi2, bj2)

print(max_sum)