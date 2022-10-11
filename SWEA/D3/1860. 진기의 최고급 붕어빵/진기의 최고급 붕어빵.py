def sol():
    for tc in range(1, int(input()) + 1):
        n, m, k = map(int, input().split())
        arrive = sorted(list(map(int, input().split())))
        make = 0
        result = 'Possible'
        for i in range(n):
            if i % k == 0:
                make += m
            if arrive[i] < make:
                result = 'Impossible'
                break
        print(f'#{tc} {result}')


sol()
