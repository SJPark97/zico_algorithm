n, m = map(int, input().split())

n_list = [[i + (j * m) for i in range(1, m+1)] for j in range(n)]
for change_list in range(n):
    if not change_list%2:
        n_list[change_list] = n_list[change_list][::-1]

n_list = n_list[::-1]
for print_list in n_list:
    print(*print_list)


