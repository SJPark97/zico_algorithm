T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}')
    remove = input()

    word = input()

    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for number in numbers:
        print((number+' ') * word.count(number), end='')
    print()