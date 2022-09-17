# import sys
# sys.stdin = open('input.txt')


def chk(x, y):
    result = []
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        while True:
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    nx += dx[d]
                    ny += dy[d]
                else:
                    break
            elif nx in success or ny in success:
                result.append(d)
                break
    return result


def chk_true(x, y, d):
    while True:
        x += dx[d]
        y += dy[d]
        if x in success or y in success:
            return True
        elif board[x][y] == 1:
            return False


def dfs(t, c):
    global line, answer_line, answer_core
    if t == len(chk_list):
        if answer_core < c or answer_core == c and answer_line > line:
            answer_core = c
            answer_line = line
    else:
        x, y = chk_list[t]
        for d in chk_direction[t]:
            if chk_true(x, y, d):
                nx, ny = x, y
                while True:
                    nx += dx[d]
                    ny += dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        line += 1
                        board[nx][ny] = 1
                    else:
                        break
                dfs(t+1, c+1)
                nx, ny = x, y
                while True:
                    nx += dx[d]
                    ny += dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        line -= 1
                        board[nx][ny] = 0
                    else:
                        break
        dfs(t+1, c)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for test_case in range(1, int(input())+1):
    print (f'#{test_case}', end=' ')
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    success = (-1, n)
    chk_list = []
    chk_direction = []
    for i in range(1, n-1):
        for j in range(1, n-1):
            ck = chk(i, j)
            if board[i][j] == 1 and ck:
                chk_list.append((i, j))
                chk_direction.append(ck)
    answer = []
    answer_core = 0
    answer_line = n**2
    line = 0
    dfs(0, 0)
    print(answer_line)
