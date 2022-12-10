import sys

input = sys.stdin.readline
q = []
b = int(input())
for _ in range(b):
    a = input()[:-1]
    if 'push' in a:
        q.append(int(a[5:]))
    elif a == 'top':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif a == 'pop':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif a == 'size':
        print(len(q))
    elif a == 'empty':
        if q:
            print(0)
        else:
            print(1)
