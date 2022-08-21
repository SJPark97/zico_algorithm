import sys
input = sys.stdin.readline

board = []

for i in range(9):
    board.extend(list(map(int, input().split())))

highest_num = max(board)
index = board.index(highest_num)
x = index // 9 + 1
y = index % 9 + 1

print(max(board))
print(x, y)