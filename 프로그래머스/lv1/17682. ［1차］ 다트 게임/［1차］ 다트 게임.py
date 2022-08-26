def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    bonus = (0, 'S', 'D', 'T')
    sig = -1
    
    for i in point:
        if i.isdigit():
            answer.append(int(i))
            sig += 1
        elif i in bonus:
            answer[sig] = answer[sig] ** bonus.index(i)
        elif i == '#':
            answer[sig] = answer[sig] * (-1)
        else:
            if sig == 0:
                answer[sig] = answer[sig] * 2
            else:
                answer[sig-1] = answer[sig-1] * 2
                answer[sig] = answer[sig] * 2
    return sum(answer)