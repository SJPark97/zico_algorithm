def circular(string_list):
    for M in range(100, 2, -1):
        for i in range(100):
            for j in range(100-M+1):
                find = True
                find_row = True
                find_col = True
                for checking in range(M//2):
                    if find_row and string_list[i][j+checking] != string_list[i][j+M-1-checking]:
                        find_row = False
                    if find_col and string_list[j+checking][i] != string_list[j+M-1-checking][i]:
                        find_col = False
                    if not find_row and not find_col:
                        find = False
                        break
                if find:
                    return M

for test_case in range(10):
    print(f'#{input()}', end=' ')

    string_list = [list(input()) for _ in range(100)]

    print(circular(string_list))