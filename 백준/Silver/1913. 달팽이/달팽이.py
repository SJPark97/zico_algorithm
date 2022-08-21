N = int(input())
find_num = int(input())

board = [[0]*N for _ in range(N)]
x, y = 0, 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
find_num_result = [1, 1]
board[x][y] = N*N
count = N * N - 1


while count:
    for n in range(4):
        while True:
            if 0 <= x+dx[n] < N and 0 <= y+dy[n] < N and not board[x+dx[n]][y+dy[n]]:
                x += dx[n]
                y += dy[n]
                board[x][y] = count
                if count == find_num:
                    find_num_result = [x+1, y+1]
                count -= 1
            else:
                break

for b in board:
    print(*b)
print(*find_num_result)