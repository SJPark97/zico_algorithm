T = int(input())
for number in range(T):
    A, B = map(int, input().split())
    print(A + B)

import sys

T = int(sys.stdin.readline())
for number in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)
