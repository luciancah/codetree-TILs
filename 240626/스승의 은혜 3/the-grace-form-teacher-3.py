n, m = map(int, input().split())
gifts = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    temp = [0] * n
    for j in range(n):
        temp[j] = sum(gifts[j])
    temp[i] = gifts[i][0] // 2 + gifts[i][1]
    
    temp.sort()
    
    sum_money = 0
    for j in range(n):
        sum_money += temp[j]
        if sum_money > m:
            ans = max(ans, j)
            break

    # student = 0
    # cnt = 0

    # for j in range(n):
    #     if cnt + temp[j] > m:
    #         break
    #     cnt += temp[j]
    #     student += 1

    # ans = max(ans, student)

print(ans)