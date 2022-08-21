
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test_case in range(1, 11):
    print(f'#{test_case}', end=' ')

    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]
    abs_sum = 0

    for i in range(N):
        for j in range(N):
            for n in range(4):
                i_x = i + dx[n]
                j_y = j + dy[n]
                if 0 <= i_x < N and 0 <= j_y < N:
                    abs_sum += abs(board[i][j] - board[i_x][j_y])

    print(abs_sum)
