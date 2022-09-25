# https://school.programmers.co.kr/learn/courses/30/lessons/92343
from collections import defaultdict


def solution(info, edges):
    global answer

    def dfs(cur):
        global answer
        if visited[cur]:
            return
        visited[cur] = 1
        # 가능한지 체크
        wolf = 0
        sheep = 0
        for i in range(n):
            if cur & (1 << i):
                if info[i]:
                    wolf += 1
                else:
                    sheep += 1
        if sheep <= wolf:
            return
        answer = max(answer, sheep)
        # 다음 탐색 찾기
        for i in range(n):
            if cur & (1 << i):
                for b in board[i]:
                    dfs(cur | (1 << b))

    n = len(info)
    board = defaultdict(list)
    # 노드 방문? (0/1) 이진수->십진수 ..0010 -> 2 visited[2]=1
    visited = [0] * (2 ** n)
    for s, e in edges:
        board[s].append(e)
    answer = 0
    dfs(1)
    return answer
