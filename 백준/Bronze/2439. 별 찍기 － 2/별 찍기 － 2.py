n = int(input())
for i in range(1, n+1):
    w = ' ' * (n - i) + '*' * i
    print(w)