def cnt(x, y):
    visit[x][y] = True
    global chess_cnt
    if chess_list[x][y] == 'F':
        chess_cnt += 1
    for n in range(4):
        n_x = x + dx[n]
        n_y = y + dy[n]
        if 0 <= n_x < 8 and 0 <= n_y < 8 and not visit[n_x][n_y]:
            cnt(n_x, n_y)


visit = [[False] * 8 for _ in range(8)]

chess_list = [input() for _ in range(8)]
chess_cnt = 0

dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]

cnt(0, 0)

print(chess_cnt)