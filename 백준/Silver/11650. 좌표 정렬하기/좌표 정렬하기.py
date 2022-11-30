import sys

input = sys.stdin.readline
li = [list(map(int, input().split())) for _ in range(int(input()))]
li.sort(key=lambda x: (x[0], x[1]))
for a in li:
    print(*a)
