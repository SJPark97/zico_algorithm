a, b = map(int, input().split())
c = [True] * (b + 1)
for i in range(2, b + 1):
    if c[i] == True:
        if i >= a:
            print(i)
        if i <= int(b**0.5):
            for j in range(i + i, b + 1, i):
                c[j] = False