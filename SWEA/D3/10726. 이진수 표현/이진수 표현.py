def sol():
    n, m = map(int, input().split())
    for i in range(n):
        if not m & (1 << i):
            print("OFF")
            return
    print("ON")
    return


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()