board = [[0]*1001 for _ in range(1001)]
n = 1
num = int(input())
for _ in range(num):
    x1, y1, row, col = map(int, input().split())
    for i in range(x1, x1 + row):
        for j in range(y1, y1 + col):
            board[i][j] = n
    n += 1
answer = [0] * (num + 1)
for i in range(1001):
    for j in range(1001):
        answer[board[i][j]] += 1
print(*answer[1:], sep="\n")