N, X = map(int, input().split())
A = input().split()
print(*([int(n) for n in A if int(n) < X]))
