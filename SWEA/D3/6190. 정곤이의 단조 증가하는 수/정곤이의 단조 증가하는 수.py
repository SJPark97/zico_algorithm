def init():
    N = int(input())
    num_list = sorted(list(map(int, input().split())))
    return N, num_list


def chk(s):
    num = s % 10
    s //= 10
    while s:
        n = s % 10
        if num < n:
            return False
        num = n
        s //= 10
    return True


def sol():
    answer = -1
    n, num_list1 = init()
    for num in range(n-1, -1, -1):
        for num1 in range(num-1, -1, -1):
            number = num_list1[num] * num_list1[num1]
            if answer > number:
                break
            if chk(number):
                answer = number
    return print(answer)


T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')
    sol()
