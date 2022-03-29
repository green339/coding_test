# https://programmers.co.kr/learn/courses/30/lessons/70129
def solution(s):
    answer = [0, 0]
    while s != "1":
        before = len(s)
        s = s.replace("0", "")
        answer[1] += before - len(s)
        answer[0] += 1
        s = format(len(s), 'b')
    return answer
