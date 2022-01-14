# https://programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    answer = []
    uid = dict()
    for r in record:
        r = r.split(" ")
        if len(r) == 3:
            uid[r[1]] = r[2]
    for log in record:
        log = log.split()
        if log[0][0] == "E":
            answer.append(uid[log[1]] + "님이 들어왔습니다.")
        elif log[0][0] == "L":
            answer.append(uid[log[1]] + "님이 나갔습니다.")
    return answer
