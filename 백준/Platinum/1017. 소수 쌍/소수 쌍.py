# def chk_list(x):
#     global result_bol
#     if length == x:
#         result_bol = True
#         return
#     for num in result[x]:
#         if not visit[num]:
#             visit[num] = True
#             chk_list(x+1)
#             if result_bol:
#                 return
#             visit[num] = False


def bimatch(N):
    if visited[N]:
        return False
    visited[N] = True

    for num in graph[N]:
        if selected[num] == -1 or bimatch(selected[num]):
            selected[num] = N
            return True
    return False


n = 1999
a = [False, False] + [True]*(n-1)

for i in range(2,n+1):
    if a[i]:
        for j in range(2*i, n+1, i):
            a[j] = False


N = int(input())
nums = list(map(int, input().split()))
# 첫번째 수 저장
first_num = nums[0]

# 짝수
even = []
# 홀수
odd = []
for n in range(N):
    if nums[n] % 2:
        odd.append(nums[n])
    else:
        even.append(nums[n])

if len(odd) != len(even):
    print(-1)
else:
    if first_num % 2:
        m, t = odd, even
    else:
        m, t = even, odd

    length = N // 2
    answer = []
    for i in range(length):
        if a[first_num + t[i]]:
            answer.append(t[i])
            selected = [-1] * length
            selected[i] = 0
            graph = [[] for _ in range(length)]
            # visit = [False] * length
            # visit[i] = True
            # result_bol = False
            for x in range(1, length):
                for y in range(length):
                    if t[i] != t[y] and a[m[x] + t[y]]:
                        graph[x].append(y)

            for p in range(1, length):
                visited = [False] * length
                bimatch(p)

            result = 0
            for o in selected:
                if o >= 0:
                    result += 1
            if result < length:
                answer.pop()
    if answer:
        answer.sort()
        print(*answer)
    else:
        print(-1)
