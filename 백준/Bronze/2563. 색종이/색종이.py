def sol():
    board = [[0] * 100 for _ in range(100)]
    for _ in range(int(input())):
        x, y = map(int, input().split())
        for i in range(x, x + 10):
            for j in range(y, y + 10):
                if board[i][j] == 0:
                    board[i][j] = 1
    answer = sum(map(sum, board))
    return print(answer)


sol()
