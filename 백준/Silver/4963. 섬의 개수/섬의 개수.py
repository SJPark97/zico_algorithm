import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    visit[x][y] = True

    for n in range(8):
        nx = x + dx[n]
        ny = y + dy[n]
        if 0 <= nx < h and 0 <= ny < w and not visit[nx][ny] and board[nx][ny]:
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    else:
        board = [list(map(int, input().split())) for _ in range(h)]
        visit = [[False] * w for _ in range(h)]

        dx = [-1, 1, 0, 0, -1, -1, 1, 1]
        dy = [0, 0, -1, 1, -1, 1, -1, 1]
        count = 0

        for i in range(h):
            for j in range(w):
                if board[i][j] and not visit[i][j]:
                    dfs(i, j)
                    count += 1

        print(count)