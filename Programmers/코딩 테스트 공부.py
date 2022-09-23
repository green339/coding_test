# https://school.programmers.co.kr/learn/courses/30/lessons/118668
import heapq


def solution(alp, cop, problems):
    temp = list(map(max, zip(*problems)))
    max_alp_req = max(alp, temp[0])
    max_cop_req = max(cop, temp[1])
    dist = [[30000] * (max_cop_req + 1) for _ in range(max_alp_req + 1)]
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])
    q = [(0, alp, cop)]
    dist[alp][cop] = 0
    while q:
        cur_cost, cur_alp, cur_cop = heapq.heappop(q)
        if dist[cur_alp][cur_cop] < cur_cost:
            continue
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if alp_req <= cur_alp and cop_req <= cur_cop:
                # 범위를 넘어가는 경우도 고려
                next_alp = min(max_alp_req, alp_rwd + cur_alp)
                next_cop = min(max_cop_req, cop_rwd + cur_cop)
                next_cost = cost + cur_cost
                if dist[next_alp][next_cop] > next_cost:
                    dist[next_alp][next_cop] = next_cost
                    heapq.heappush(q, (next_cost, next_alp, next_cop))
    return dist[-1][-1]
