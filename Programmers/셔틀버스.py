# https://programmers.co.kr/learn/courses/30/lessons/17678

def solution(n, t, m, timetable):
    start = 9 * 60
    last = start + (n - 1) * t
    bus = dict()
    for i in range(n):
        bus[start + i * t] = []
    for k, time in enumerate(sorted(timetable)):
        tmp = list(map(int, time.split(":")))
        time = tmp[0] * 60 + tmp[1]
        for k, v in bus.items():
            if time <= k:
                if len(v) < m:
                    bus[k].append(time)
                else:
                    for i in range((last - k) // t + 1):
                        if len(bus[k + t * i]) < m:
                            bus[k + t * i].append(time)
                            break
                break
    if len(bus[last]) >= m:
        answer = max(bus[last]) - 1
    else:
        answer = last
    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)
