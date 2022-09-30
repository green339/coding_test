# https://school.programmers.co.kr/learn/courses/30/lessons/120956
def solution(babbling):
    answer = 0
    p = {"aya": "1", "ye": "2", "woo": "3", "ma": "4", "ayaaya": "5", "yeye": "6", "woowoo": "7", "mama": "8"}
    for b in babbling:
        for k in ["ayaaya", "yeye", "woowoo", "mama", "aya", "ye", "woo", "ma"]:
            b = b.replace(k, p[k])
        if b.isdigit() and max(map(int, list(b))) < 5:
            answer += 1
    return answer
