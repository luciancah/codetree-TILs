a, b = map(int, input().split())
n = input()

num = 0
for i in range(len(n)-1, -1, -1):
    num += int(n[i]) * (a ** i)

# print(num)
ans = []

while num > 0:
    ans.append(str(num % b))
    num = num // b

print(''.join(ans))