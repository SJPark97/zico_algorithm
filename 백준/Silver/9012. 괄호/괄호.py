for _ in range(int(input())):
    a = 0
    c = 'YES'
    for b in input():
        if b == '(':
            a += 1
        elif b == ')':
            a -= 1
            if a < 0:
                break
    if a != 0:
        c = 'NO'
    print(c)
