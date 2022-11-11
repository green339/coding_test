# https://school.programmers.co.kr/learn/courses/30/lessons/133499
def solution(babbling):
    answer = 0
    cannot=[ "ayaaya", "yeye", "woowoo", "mama"]
    can=[ "aya", "ye", "woo", "ma"]
    for b in babbling:
        for cn in cannot:
            if cn in b:
                break
        else:
            for c in can:
                b=b.replace(c,"0")
        if b.isdigit():
            answer+=1
    return answer