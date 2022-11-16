n = int(input())
a = [input() for _ in range(n)]
a.sort(key=lambda x: (len(x), x))
b = set()
for c in a:
    if c not in b:
        print(c)
        b.add(c)
