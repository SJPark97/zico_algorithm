
n, m = map(int, input().split())

n_m_list = [[0 for _ in range(m)] for _ in range(n)]
num_cnt = 0

for k in range(n+m):
    for j in range(m):
        for i in range(n):
            if i + j == k:
                num_cnt += 1
                n_m_list[i][j] = num_cnt

for pnt_list in n_m_list[::-1]:
    print(*pnt_list)
