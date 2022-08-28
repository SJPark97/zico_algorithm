def sol():
    N = int(input())
    board = [list(map(int, list(input()))) for _ in range(N)]
    n = N // 2
    answer = sum(board[n])
    for i in range(1, n+1):
        answer += sum(board[n + i][i:-i])
        answer += sum(board[n - i][i:-i])
    return print(answer)


T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')
    sol()