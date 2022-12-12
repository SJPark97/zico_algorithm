import sys

input = sys.stdin.readline
a = [[] for _ in range(201)]
for _ in range(int(input())):
    b, c = input().split()
    a[int(b)].append(c)
for i in range(1, 201):
    for d in a[i]:
        print(i, d)
