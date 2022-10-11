def sol():
    for tc in range(1, int(input()) + 1):
        n, m = map(int, input().split())
        board = [input() for _ in range(n)]
        answer = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                result = 0
                for k in range(n):
                    if k <= i:
                        result += board[k].count('W')
                    elif k <= j:
                        result += board[k].count('B')
                    else:
                        result += board[k].count('R')
                answer = max(answer, result)
        print('#{} {}'.format(tc, n * m - answer))


sol()
