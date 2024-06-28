n = int(input())
days = [list(map(str, input().split())) for _ in range(n)]

days.sort(key=lambda x:x[0])
for i in range(n):
    if days[i][2] == 'Rain':
        print(' '.join(days[i]))
        break