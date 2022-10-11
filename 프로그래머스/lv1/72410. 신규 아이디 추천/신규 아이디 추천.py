def solution(new_id):
    def chk_bool(w):
        return w in chk or w.isalpha() or w.isdecimal()

    answer = ''
    chk = {'-', '_', '.'}
    new_id = new_id.lower()
    for word in new_id:
        if chk_bool(word):
            answer += word
    while answer.count('..'):
        answer = answer.replace('..', '.')
    if answer[0] == '.':
        answer = answer[1:]
    if not answer:
        answer += 'a'
    if len(answer) > 15:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    while len(answer) < 3:
        answer += answer[-1]
    return answer
