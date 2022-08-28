def init():
    N = int(input())
    num_list = list(map(int, input().split()))
    return N, num_list


def chk(s):
    for n in range(len(s)-1):
        if s[n] > s[n+1]:
            return False
    return True


def sol():
    answer = -1
    n, num_list1 = init()
    for num in range(n-1):
        for num1 in range(num+1, n):
            number = num_list1[num] * num_list1[num1]
            if chk(str(number)):
                if answer < number:
                    answer = number
    return print(answer)


T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')
    sol()
