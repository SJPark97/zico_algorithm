
n = int(input())

n_list = [[i+(j*n) for i in range(1, n+1)] for j in range(n)]
n_list = list(zip(*n_list))
for print_list in n_list:
    print(*print_list)