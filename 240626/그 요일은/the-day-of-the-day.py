m1, d1, m2, d2 = map(int, input().split())
day = input()
day_map = {
    'Mon': 1,
    'Tue': 2,
    'Wed': 3,
    'Thu': 4,
    'Fri': 5,
    'Sat': 6,
    'Sun': 7
}
months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

ans = 0
for i in range(m1, m2+1):
    if m1 == m2:
        ans += d2 - d1 + 1
        continue
    if i == m1:
        ans += months[i] - d1
        continue
    if i == m2:
        ans += d2
        continue
    ans += months[i]

# print(ans)
print((ans - day_map[day]) // 7 + 1)