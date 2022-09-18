d = int(input())
board = []
max_location = 0
for _ in range(d):
    l, h = map(int, input().split())
    if max_location < h:
        max_location = h
    board.append((l, h))
board.sort(key=lambda x: (x[0], x[1]))
answer = (board[-1][0] - board[0][0] + 1) * max_location
start = board[0]# (2, 4)
end = board[-1]# (15, 8)
for i in range(1, d):
    if board[i][1] > start[1]:
        answer -= (board[i][0] - start[0]) * (max_location - start[1])
        if board[i][1] == max_location:
            break
        start = board[i]

for i in range(d-2, -1, -1):
    if board[i][1] > end[1]:
        answer -= (end[0] - board[i][0]) * (max_location - end[1])
        if board[i][1] == max_location:
            break
        end = board[i]
print(answer)