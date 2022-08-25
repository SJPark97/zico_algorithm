N = int(input())
if N == 1:
    print(N)
else:
    card_list = list(range(2, N+1, 2))
    for i in range(1, 20):
        if N <= 2**i:
            print(card_list[N - 2**(i-1) -1])
            break