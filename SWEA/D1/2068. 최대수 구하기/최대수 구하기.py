T = int(input())
for case in range(T):
    number_list = list(map(int, input().split()))
    highest_number = max(number_list)
    print(f'#{case + 1} {highest_number}')