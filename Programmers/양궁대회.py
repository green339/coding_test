# https://programmers.co.kr/learn/courses/30/lessons/92342
from copy import deepcopy


def solution(n, info):
    global answer, apeach, diff
    diff = 0
    answer = []
    apeach = info
    dfs(n, [0] * 11, 0)
    if not answer:
        return [-1]
    return sorted(answer, reverse=True, key=lambda x: x[::-1])[0]


def dfs(cnt, record, cur):
    global answer, diff
    if not cnt:
        tmp = 0
        for i in range(11):
            if record[i] > 0 or apeach[i] > 0:
                if record[i] > apeach[i]:
                    tmp += 10 - i
                else:
                    tmp -= 10 - i
        if tmp > 0:  # 이긴 경우
            result = deepcopy(record)
            if tmp == diff:
                answer.append(result)
            elif tmp > diff:
                answer = [result]
                diff = tmp
        return

    if cur == 10:
        record[10] = cnt
        dfs(0, record, cur + 1)
        record[10] = 0
        return

    if apeach[cur] < cnt:
        # 라이언이 점수를 가져간 경우
        record[cur] = apeach[cur] + 1
        dfs(cnt - record[cur], record, cur + 1)
    # 어피치가 점수를 가져간 경우
    record[cur] = 0
    dfs(cnt, record, cur + 1)
