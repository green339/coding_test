# https://school.programmers.co.kr/learn/courses/30/lessons/17676
def solution(lines):
    def toInteger(date_time, last):
        e = date_time[0] * 3600 + date_time[1] * 60 + date_time[2]
        s = e - last + 0.001
        start_time.append(s)
        end_time.append(e)

    answer = 0
    start_time = []
    end_time = []
    for l in sorted(lines):
        l = l.split()
        toInteger(list(map(float, l[1].split(':'))), float(l[2][:-1]))
    for i in range(len(lines)):
        cur_finish = end_time[i]
        cnt = 0
        for j in range(i, len(lines)):
            if start_time[j] - cur_finish < 1:
                cnt += 1
        answer = max(cnt, answer)
    return answer
