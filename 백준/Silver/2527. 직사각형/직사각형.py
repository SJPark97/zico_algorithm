for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    xd = min(x2, x4) - max(x1, x3)
    yd = min(y2, y4) - max(y1, y3)

    if (xd > 0 and yd > 0):
        print('a')
    elif (xd < 0 or yd < 0):
        print('d')
    elif (xd == 0 and yd == 0):
        print('c')
    else:
        print('b')