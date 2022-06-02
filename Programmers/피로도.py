# https://programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations


def solution(k, dungeons):
    answer = 0
    for permu in permutations(dungeons, len(dungeons)):
        cur = k
        temp = 0
        for t, c in permu:
            if cur >= t:
                temp += 1
                cur -= c
            else:
                break
        answer = max(answer, temp)
    return answer

## 다른 풀이
def dfs(depth, left):
    global answer
    if depth > answer:
        answer = depth
    for i in range(len(d)):
        if not visited[i]:
            if left >= d[i][0]:
                visited[i] = 1
                dfs(depth + 1, left - d[i][1])
                visited[i] = 0


def solution_v2(k, dungeons):
    global visited, d, answer
    d = dungeons
    visited = [0] * len(d)
    answer = 0
    dfs(0, k)
    return answer
