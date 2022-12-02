import sys

input = sys.stdin.readline

a = [list(map(int, input().split())) for _ in range(int(input()))]
a.sort(key=lambda x: (x[1], x[0]))
for b in a:
    print(*b)
