def solution(n, weak, dist):
    global answer

    def check(cur):
        global answer
        if min(visited) > 0:
            answer = min(cur, answer)
            return
        if cur >= answer - 1:
            return
        # 더이상 탐색할 필요가 없을 때
        flag = sum(dist[cur:])
        if flag < len(left) and flag < max(left) - min(left) and flag < n + min(left) - max(left):
            return
        for w in range(k):  # 시작위치
            if visited[w]:
                continue
            # 반시계/시계 상관없음-> 반시계 끝점이 시계에서 시작점 이런식으로 변경됨
            tmp = []
            for di in range(k):
                wi = (w + di) % k
                d = weak[wi] - weak[w]
                if wi < w:
                    d += n
                if d <= dist[cur]:
                    if visited[wi] == 0:
                        left.remove(weak[wi])
                    tmp.append(wi)
                    visited[wi] += 1

                else:
                    break
            if tmp:
                check(cur + 1)
                for t in tmp:
                    visited[t] -= 1
                    if visited[t] == 0:
                        left.add(weak[t])

    k = len(weak)
    answer = len(dist) + 1
    weak.sort()
    left = set(weak)
    dist.sort(reverse=True)
    visited = [0] * k
    check(0)
    if answer == len(dist) + 1:
        return -1
    return answer


from itertools import permutations


def solution_v2(n, weak, dist):
    answer = len(dist)
    k = len(weak)
    for i in range(k):
        weak.append(weak[i] + n)
    dist.sort(reverse=True)
    for perm in permutations(dist, len(dist)):
        for s in range(k):  # 시작위치
            cnt = 0
            cur = weak[s]
            for p in perm:
                cur += p  # 해당 거리만큼 이동
                if cur < weak[s + k - 1]:
                    cnt += 1
                    cur = [weak[idx] for idx in range(s + 1, s + k) if weak[idx] > cur][0]
                else:
                    answer = min(answer, cnt)
                    break
    return answer + 1 if answer < len(dist) else -1
