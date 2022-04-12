# https://programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    answer = []
    for e in s.split(" "):
        if e=="":
            answer.append("")
            continue
        e=e[0].upper()+e[1:].lower()
        answer.append(e)
    return ' '.join(answer)