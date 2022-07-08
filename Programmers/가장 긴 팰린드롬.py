# https://school.programmers.co.kr/learn/courses/30/lessons/12904
def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):  # 시작
        for p in range(n - i, 0, -1):  # 팰린드롬 길이
            if answer >= p:
                break
            for k in range(p // 2 + 1):
                if s[i + k] != s[i + p - k - 1]:
                    break
            else:
                answer = max(answer, p)
    return answer


def solution_v2(s):
    answer = 0
    n = len(s)
    for i in range(n):  # 시작
        for p in range(n - i, 0, -1):  # 팰린드롬 길이
            if answer >= p:
                break
            tmp = s[i:i + p]
            if tmp == tmp[::-1]:
                answer = max(answer, p)
    return answer
