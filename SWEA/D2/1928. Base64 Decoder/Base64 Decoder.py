def sol():
    word = input()
    chg = ''
    answer = ''
    for w in word:
        sub = bin(base_63.index(w))[2:]
        while len(sub) < 6:
            sub = '0' + sub
        chg += sub
    for i in range(0, len(chg), 8):
        answer += chr(int(chg[i:i+8], 2))
    print(answer)


base_63 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
for test_case in range(1, int(input())+1):
    print(f'#{test_case}', end=' ')
    sol()