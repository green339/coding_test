# https://school.programmers.co.kr/learn/courses/30/lessons/118668
import heapq


def solution(alp, cop, problems):
    tmp = list(map(max, zip(*problems)))
    max_alp = max(alp, tmp[0])
    max_cop = max(cop, tmp[1])
    # 시간을 1초씩 증가할 수 있도록
    problems.append([0, 0, 0, 1, 1])
    problems.append([0, 0, 1, 0, 1])
    dist = [[10e9] * (max_cop + 1) for _ in range(max_alp + 1)]  # (알고력, 코딩력) 까지의 거리
    hq = [(0, alp, cop)]
    while hq:
        time, cur_alp, cur_cop = heapq.heappop(hq)
        if dist[cur_alp][cur_cop] < time:
            continue
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if alp_req <= cur_alp and cop_req <= cur_cop:
                # 범위를 넘어도 문제는 풀 수 있음
                next_alp = min(max_alp, cur_alp + alp_rwd)
                next_cop = min(max_cop, cur_cop + cop_rwd)
                tmp = time + cost
                if dist[next_alp][next_cop] > tmp:
                    dist[next_alp][next_cop] = tmp
                    heapq.heappush(hq, (tmp, next_alp, next_cop))
    return dist[-1][-1]
