a = [False, False] + [True] * (999)
for i in range(2, 1001):
    if a[i] == True:
        if i <= int(1000**0.5):
            for j in range(i + i, 1001, i):
                a[j] = False
c = 0
n = int(input())
for b in map(int, input().split()):
    if a[b]:
        c += 1
print(c)
