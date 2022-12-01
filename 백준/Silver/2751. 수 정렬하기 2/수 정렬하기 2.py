import sys
input = sys.stdin.readline
a = [int(input()) for _ in range(int(input()))]
a.sort()
print(*a, sep="\n")