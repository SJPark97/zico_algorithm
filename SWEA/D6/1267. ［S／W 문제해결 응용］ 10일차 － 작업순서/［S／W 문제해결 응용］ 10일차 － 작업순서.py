def sol():
    def LRV(s):
        if visit[s]:
            return
        visit[s] = True
        for num in parent[s]:
            if not visit[num]:
                LRV(num)
        print(s, end=" ")
        # for num in graph[s]:
        #     LRV(num)
        return

    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visit = [False] * (v + 1)
    parent = [[] for _ in range(v + 1)]
    nums = list(map(int, input().split()))
    for i in range(0, len(nums), 2):
        graph[nums[i]].append(nums[i + 1])
        parent[nums[i + 1]].append(nums[i])
    for start in range(1, v + 1):
        LRV(start)
    print()


for test_case in range(1, 11):
    print(f'#{test_case}', end=' ')
    sol()
