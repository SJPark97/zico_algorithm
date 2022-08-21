def find_seat(f):
    x, y = 0, 0
    count = 1

    while True:
        for n in range(4):
            while True:
                if count == f:
                    result = [x + 1, y + 1]
                    return result
                elif 0 <= x+dx[n] < N and 0 <= y+dy[n] < M and not board[x+dx[n]][y+dy[n]]:
                    board[x][y] = 1
                    x += dx[n]
                    y += dy[n]
                    count += 1
                else:
                    break
    return 0

N, M = map(int, input().split())
find_num = int(input())

board = [[0]*M for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

if find_num <= N*M:
    print(*find_seat(find_num))
else:
    print(0)
