
n = int(input())

n_list = [[i+(j*n) for i in range(1, n+1)] for j in range(n)]
for change_list in range(n):
    if change_list%2:
        n_list[change_list] = n_list[change_list][::-1]

for print_list in n_list:
    print(*print_list)


# n = int(input())
#
# for i in range(n):
#     if not i%2:
#         print(*range(1+i*n, n+i*n+1))
#     elif i%2:
#         print(*range(n+i*n, i*n, -1))
