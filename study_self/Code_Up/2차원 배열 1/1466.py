n, m = map(int, input().split())

n_list = [[i + (j * n) for i in range(n, 0, -1)] for j in range(m)]
n_list = n_list[::-1]
n_list = list(zip(*n_list))
for print_list in n_list:
    print(*print_list)

