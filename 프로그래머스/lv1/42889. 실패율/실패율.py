def solution(N, stages):
    result = list(range(N, 0, -1))
    answer = []
    stages = sorted(stages)[::-1]
    people = 0
    n = N
    cnt = 0
    for stage in stages:
        people += 1
        if stage == n:
            cnt += 1
        elif stage < n:
            if cnt != 0 and people > 1:
                answer.append((n, cnt/(people-1)))
            n = stage
            cnt = 1
    else:
        if cnt != 0:
            answer.append((n, cnt/people))
    answer.sort(key=lambda x: x[1], reverse=False)
    for ans in answer:
        i = ans[0]
        del result[result.index(i)]
        result.append(i)
    return result[::-1]