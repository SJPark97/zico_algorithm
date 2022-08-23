import sys
sys.setrecursionlimit(10**6)

def find_region(x, y):
    global legion_cnt
    board[x][y] = 1
    legion_cnt += 1
    for n in range(4):
        nx, ny = x + dx[n], y + dy[n]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            find_region(nx, ny)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
M, N, K = map(int, input().split())

board = [[0] * M for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1

result_cnt = 0
legion = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            result_cnt += 1
            legion_cnt = 0
            find_region(i, j)
            legion.append(legion_cnt)

print(result_cnt)
print(*sorted(legion))
