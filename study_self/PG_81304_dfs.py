import sys

sys.setrecursionlimit(10 ** 8)


def solution(n, start, end, roads, traps):
    def dfs(location, distance, repeat):
        nonlocal answer
        if distance >= answer or repeat > 3:
            return
        if location == end:
            answer = distance
            return
        res = 0
        if location in traps:
            res += trap_activated[location]
        for next_location, dis, chk_go in graphs[location]:
            if next_location in traps:
                if (res + trap_activated[next_location] + chk_go) % 2 == 0:
                    trap_activated[next_location] += 1
                    dfs(next_location, distance + dis, repeat + 1)
                    trap_activated[next_location] -= 1
            else:
                if (res + chk_go) % 2 == 0:
                    dfs(next_location, distance + dis, 0)

    answer = 3000 * 3000
    traps = set(traps)
    trap_activated = dict()
    for i in traps:
        trap_activated[i] = 0
    graphs = [[] for _ in range(n + 1)]
    for s, e, d in roads:
        graphs[s].append([e, d, 0])
        graphs[e].append([s, d, 1])
    dfs(start, 0, 0)
    return answer
