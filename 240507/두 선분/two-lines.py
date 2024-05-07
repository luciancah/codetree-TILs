a, b, c, d = list(map(int, input().split()))

if (a < c):
    if (b < c):
        print('notintersecting')
    else:
        print('intersecting')

if (c < a):
    if (c < b):
        print('notintersecting')
    else:
        print('intersecting')