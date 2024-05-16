n, m = list(map(int, input().split()))
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

def in_range_1(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def in_range_2(bx, by, x, y):
    return 0 <= x and x < n and 0 <= y and y < n and (bx <= x or by <= y)


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
                print(sum1)

                for bi in range(n):
                    for bj in range(m):
                        sum2 = 0
                        for bi2 in range(1, n):
                            for bj2 in range(1, m):
                                if not in_range_2(ai2, aj2, bi2, bj2):
                                    continue
                                sum2 += arr[bi2][bj2]

                temp_max = max_sum
                max_sum = max(max_sum, sum1+sum2)
                if temp_max != max_sum:
                    print(sum1, sum2)

print(max_sum)