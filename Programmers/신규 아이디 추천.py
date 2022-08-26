# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    new_id = new_id.lower()
    answer = []
    for cur in new_id:
        if cur.isdigit() or cur.isalpha():
            answer.append(cur)
        else:
            if answer and answer[-1] != '.' and cur == '.':
                answer.append(cur)
            elif cur == '-' or cur == '_':
                answer.append(cur)
        if len(answer) == 15:
            break
    if not answer:
        answer.append('a')
    while answer[-1] == '.':
        answer.pop()
    while len(answer) < 3:
        answer.append(answer[-1])
    return ''.join(answer)
