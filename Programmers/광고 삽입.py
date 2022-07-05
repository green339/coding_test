# https://school.programmers.co.kr/learn/courses/30/lessons/72414

def toSecond(string):
    string = list(map(int, string.split(":")))
    return string[0] * 3600 + string[1] * 60 + string[2]


def toHMS(seconds):
    H = seconds // 3600
    M = seconds % 3600 // 60
    S = seconds % 60
    return '%02d:%02d:%02d' % (H, M, S)


def solution(play_time, adv_time, logs):
    play_time = toSecond(play_time)
    adv_time = toSecond(adv_time)
    times = [0] * (play_time + 1)
    for l in logs:
        s, e = l.split("-")
        times[toSecond(s)] += 1
        times[toSecond(e)] -= 1
    for i in range(1, play_time + 1):
        times[i] += times[i - 1]
    cnt = 0
    answer = 0
    start = 0
    tmp = 0
    for end in range(play_time + 1):
        tmp += times[end]
        if end >= adv_time:
            tmp -= times[start]
            start += 1
        if tmp > cnt:
            cnt = tmp
            answer = start
    return toHMS(answer)
