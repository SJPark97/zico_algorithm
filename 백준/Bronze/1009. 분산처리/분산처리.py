T = int(input())
for case in range(T):
    a, b = map(int, input().split())
    case_a = a % 10
    if case_a == 0:
        print(10)
    elif case_a == 1 or case_a == 5 or case_a == 6:
        print(case_a)
    elif case_a == 2 or case_a == 3 or case_a == 7 or case_a == 8:
        case_b = b % 4
        if case_b == 0:
            print((case_a**4) % 10)
        else:
            print((case_a**case_b) % 10)
    else:  # case_a == 4 or case_a == 9:
        case_b = b % 2
        if case_b == 0:
            print((case_a**2) % 10)
        else:
            print((case_a**case_b) % 10)