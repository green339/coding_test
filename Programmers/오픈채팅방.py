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


from collections import defaultdict


def solution_v2(record):
    answer = []
    mention = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    name = defaultdict(list)
    for r in record:
        r = r.split()
        if r[0][0] == 'E' or r[0][0] == 'C':
            name[r[1]] = r[2]
    for r in record:
        r = r.split()
        if r[0][0] != 'C':
            answer.append(name[r[1]] + mention[r[0]])
    return answer
