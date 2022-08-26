def solution(dartResult):
    string = dartResult
    word = ''
    signal = True
    for i in range(len(string)):
        if signal:
            if string[i].isdigit():
                word += ' ' + string[i]
                if string[i+1].isdigit():
                    word += string[i+1]
                    string.replace(string[i+1], ' ')
                    signal = False
            else:
                word += string[i]
        else:
            signal = True
    
    word_list = list(word.split())
    result = []
    signal = []
    for n in range(3):
        num = ''
        for i in word_list[n]:
            if i.isdigit():
                num += i
            elif i == 'S':
                nu = int(num)
            elif i == 'D':
                nu = int(num) ** 2
            elif i == 'T':
                nu = int(num) ** 3
            elif i == '#':
                nu = nu * (-1)
            elif i == '*':
                signal.append(n)
        result.append(nu)
    if signal:
        for i in signal:
            if i == 0:
                result[i] = result[i] * 2
            else:
                result[i-1] = result[i-1] * 2
                result[i] = result[i] * 2
    return sum(result)