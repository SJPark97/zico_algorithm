def sol():
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

    for tc in range(1, int(input()) + 1):
        answer = -1
        n = int(input())
        num_list = sorted(list(map(int, input().split())))
        for num in range(n - 1, -1, -1):
            for num1 in range(num - 1, -1, -1):
                number = num_list[num] * num_list[num1]
                if answer > number:
                    break
                if chk(number):
                    answer = number
        print('#{} {}'.format(tc, answer))


sol()
