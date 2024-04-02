n = int(input())
arr = list(map(int, input().split()))
ans = ''

for i in range(n):

    if 1 % 2 != 0:

        copy = arr[0:i+1]
        sortedArr = sorted(copy)

        if i == 1:
            ans += '1'
            ans += ' '
        
        ans += str(sortedArr[i//2])
        ans += ' '

print(ans)