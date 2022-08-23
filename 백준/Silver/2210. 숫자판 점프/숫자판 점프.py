def board_check(arr, x, y):
    if len(arr) == 6:
        if tuple(arr) not in result:
            result.add(tuple(arr.copy()))
        return
    for n in range(4):
        nx, ny = x + dx[n], y + dy[n]
        if 0 <= nx < 5 and 0 <= ny < 5:
            arr.append(board[x][y])
            board_check(arr, nx, ny)
            arr.pop()


board = [list(map(int, input().split())) for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = set()

for i in range(5):
    for j in range(5):
        board_check([], i, j)

print(len(result))