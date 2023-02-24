from heapq import heappop, heappush
import copy


def solution(n, start, end, roads, traps):
    def bfs():
        heap = [(0, start, 0, trap_activated)]
        while heap:
            distance, location, past_location, trap = heappop(heap)
            if location == end:
                return distance
            for info in graphs[location]:
                next_location, dis, way = info
                if next_location in trap and location in trap:
                    if (trap[location] + trap[next_location] + way) % 2 == 0:
                        trap_copy = copy.deepcopy(trap)
                        trap_copy[next_location] += 1
                        heappush(heap, (distance + dis, next_location, location, trap_copy))
                elif next_location in trap:
                    if (trap[next_location] + way) % 2 == 0:
                        trap_copy = copy.deepcopy(trap)
                        trap_copy[next_location] += 1
                        heappush(heap, (distance + dis, next_location, location, trap_copy))
                elif location in trap:
                    if (trap[location] + way) % 2 == 0:
                        heappush(heap, (distance + dis, next_location, location, trap))
                else:
                    if past_location == next_location:
                        continue
                    if way % 2 == 0:
                        heappush(heap, (distance + dis, next_location, location, trap))

    trap_activated = dict()
    for i in traps:
        trap_activated[i] = 0
    graphs = [[] for _ in range(n + 1)]
    for s, e, d in roads:
        graphs[s].append([e, d, 0])
        graphs[e].append([s, d, 1])
    return bfs()


print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))