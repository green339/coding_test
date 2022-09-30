# https://school.programmers.co.kr/learn/courses/30/lessons/120876
def solution(lines):
    answer = 0
    arr = [0] * 200
    for l in lines:
        s, e = sorted(l)
        arr[s + 100] += 1
        arr[e + 100] -= 1
    for i in range(1, 200):
        arr[i] += arr[i - 1]
        if arr[i] > 1:
            answer += 1
    return answer
