for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    if (x1, y1) == (x4, y4) or (x2, y1) == (x3, y4) or (x2, y2) == (x3, y3) or (x1, y2) == (x4, y3):
        print('c')
    elif y1 > y4 or y2 < y3 or x1 > x4 or x2 < x3:
        print('d')
    elif list(set(list(range(x1, x2))) & set(list(range(x3, x4)))) and list(set(list(range(y1, y2))) & set(list(range(y3, y4)))):
        print('a')
    else:
        print('b')
