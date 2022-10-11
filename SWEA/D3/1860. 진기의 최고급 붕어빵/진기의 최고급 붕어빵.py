def sol():
    for tc in range(1, int(input()) + 1):
        n, m, k = map(int, input().split())
        arrive = sorted(list(map(int, input().split())))
        make = [i * m for i in range(1, n+1) for _ in range(k)]
        result = 'Possible'
        for i in range(n):
            if arrive[i] < make[i]:
                result = 'Impossible'
                break
        print(f'#{tc} {result}')


sol()
