def chk(x, y, dir, visit):
    li = [(x, y)]
    print(visit)
    for n in dir:
        l_x, l_y = x, y
        while True:
            l_x += nx[n]
            l_y += ny[n]
            if (l_x, l_y) not in visit:
                break
            li.append((l_x, l_y))
    return li


def sol(board):
    visit = set(board)
    for x, y in board:
        for n in range(4):
            ans = chk(x, y, direction[n], visit)
            if len(ans) == 5:
                ans.sort(key=lambda x: (x[1], x[0]))
                return ans[0]
    return False


direction = [(0, 4), (2, 6), (1, 5), (3, 7)]
nx = [0, -1, -1, -1, 0, 1, 1, 1]
ny = [-1, -1, 0, 1, 1, 1, 0, -1]
white = []
black = []
for i in range(19):
    board = input().split()
    for j in range(19):
        if board[j] == "1":
            black.append((i + 1, j + 1))
        elif board[j] == "2":
            white.append((i + 1, j + 1))
ans_black = sol(black)
ans_white = sol(white)
if ans_black:
    print(1)
    print(ans_black[0], ans_black[1])
elif ans_white:
    print(2)
    print(ans_white[0], ans_white[1])
else:
    print(0)
