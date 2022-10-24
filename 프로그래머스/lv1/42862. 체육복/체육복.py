def solution(n, lost, reserve):
    lost, reserve = set(lost) - set(reserve), list(set(reserve) - set(lost))
    for num in reserve:
        if num - 1 in lost:
            lost.remove(num - 1)
        elif num + 1 in lost:
            lost.remove(num + 1)
    return n - len(lost)

