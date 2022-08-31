def sol():
    num_list = list(map(int, input().split()))
    num_list.sort()
    num_list = num_list[1:-1]
    print(round(sum(num_list)/len(num_list)))


T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')
    sol()