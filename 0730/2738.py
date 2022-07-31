N, M = map(int, input().split())
A = []
B = []
for n in range(N):
    A.append(list(map(int, input().split())))
for n in range(N):
    B.append(list(map(int, input().split())))
for n in range(N):
    for m in range(M):
        A[n][m] += B[n][m]
    print(*A[n])
