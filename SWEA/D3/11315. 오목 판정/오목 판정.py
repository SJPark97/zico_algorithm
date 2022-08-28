from collections import deque


def init():
    n = int(input())
    board = [input() for _ in range(n)]
    return n, board


def sol():
    n, board = init()
    for i in range(n):
        if 'ooooo' in board[i]:
            return print('YES')
        for j in range(n):
            if board[i][j] == 'o' and chk(board, n, i, j):
                return print('YES')
    return print('NO')


def chk(board, N, i, j):
    for n in range(len(dx)):
        queue = deque([(i, j, 1)])
        while queue:
            x, y, t = queue.popleft()
            mx, my = x + dx[n], y + dy[n]
            if 0 <= mx < N and 0 <= my < N and board[mx][my] == 'o':
                if t + 1 == 5:
                    return True
                queue.append((mx, my, t + 1))
    return False


T = int(input())
dx = [-1, 1, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1]

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')
    sol()
