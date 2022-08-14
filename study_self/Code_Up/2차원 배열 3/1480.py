# 방법 1
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
    print(*pnt_list[::-1])

# 방법 2
n, m = map(int, input().split())

n_m_list = [[0 for _ in range(m)] for _ in range(n)]
num_cnt = 0

for k in range(n+m-1, -1, -1):
    for j in range(m-1, -1, -1):
        for i in range(n-1, -1, -1):
            if i + j == k:
                num_cnt += 1
                n_m_list[i][j] = num_cnt

for pnt_list in n_m_list:
    print(*pnt_list)

