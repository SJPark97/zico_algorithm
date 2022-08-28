def sol():
    board = input()
    chk = '0'
    cnt = 0
    for n in range(len(board)):
        if board[n] != chk:
            cnt += 1
            chk = board[n]
    return print(cnt)


T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')
    sol()