def sol():
    for tc in range(1, int(input()) + 1):
        n, k = map(int, input().split())
        k_list = sorted(list(set(list(range(1, n + 1))) - set(map(int, input().split()))))
        print(f'#{tc}', end=" ")
        print(*k_list)


sol()
