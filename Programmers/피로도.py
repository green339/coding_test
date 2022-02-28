# https://programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations


def solution(k, dungeons):
    answer = 0
    for permu in permutations(dungeons, len(dungeons)):
        cur = k
        temp = 0
        for t, c in permu:
            if cur >= t:
                temp += 1
                cur -= c
            else:
                break
        answer = max(answer, temp)
    return answer

## 백트래킹으로도 풀어보기
