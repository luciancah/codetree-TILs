a, b, c, d = list(map(int, input().split()))

if (a < c and b <= d):
    if (b < c):
        print('nonintersecting')
    else:
        print('intersecting')

if (c < a):
    if (c < b):
        print('nonintersecting')
    else:
        print('intersecting')