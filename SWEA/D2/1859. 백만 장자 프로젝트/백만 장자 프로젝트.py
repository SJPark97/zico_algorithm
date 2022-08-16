T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    N = int(input())
    gain = 0
    price_list = list(map(int, input().split()))

    while price_list:
        max_index = price_list.index(max(price_list))
        if max_index:
            gain += max(price_list) * len(price_list[:max_index]) - sum(price_list[:max_index])
            del price_list[:max_index]
        else:
            del price_list[0]
    print(gain)
