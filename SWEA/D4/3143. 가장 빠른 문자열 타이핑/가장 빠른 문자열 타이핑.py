
T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    A, B = input().split()
    print(len(A) - A.count(B)*(len(B)-1))