# https://school.programmers.co.kr/learn/courses/30/lessons/84021

from collections import defaultdict, deque
from copy import deepcopy


def solution(game_board, table):
    def rotate90(arr):  # 90도 회전
        min_x = 6
        min_y = 6
        result = []
        for ax, ay in arr:
            rx = -ay
            ry = ax
            min_x = min(rx, min_x)
            min_y = min(ry, min_y)
            result.append([rx, ry])
        for r in range(len(result)):
            result[r][0] -= min_x
            result[r][1] -= min_y
        return result

    n = len(table)
    answer = 0
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    puzzles = defaultdict(list)
    for x in range(n):
        for y in range(n):
            if table[x][y]:
                table[x][y] = 0
                q = deque()
                q.append((x, y))
                pz = []  # 퍼즐
                min_i = x
                min_j = y
                pz.append([x, y])
                while q:
                    i, j = q.popleft()
                    for di, dj in d:
                        ni = i + di
                        nj = j + dj
                        if -1 < ni < n and -1 < nj < n:
                            if table[ni][nj]:
                                q.append((ni, nj))
                                pz.append([ni, nj])
                                table[ni][nj] = 0
                                min_i = min(ni, min_i)
                                min_j = min(nj, min_j)
                for p in range(len(pz)):
                    pz[p][0] -= min_i
                    pz[p][1] -= min_j
                puzzles[len(pz)].append(pz)

    for x in range(n):
        for y in range(n):
            if not game_board[x][y]:
                game_board[x][y] = 1
                q = deque()
                q.append((x, y))
                sc = []  # 빈공간
                min_i = x
                min_j = y
                sc.append([x, y])
                while q:
                    i, j = q.popleft()
                    for di, dj in d:
                        ni = i + di
                        nj = j + dj
                        if -1 < ni < n and -1 < nj < n:
                            if not game_board[ni][nj]:
                                q.append((ni, nj))
                                sc.append([ni, nj])
                                game_board[ni][nj] = 1
                                min_i = min(ni, min_i)
                                min_j = min(nj, min_j)
                k = len(sc)
                for s in range(k):
                    sc[s][0] -= min_i
                    sc[s][1] -= min_j
                sc.sort()
                for vi, v in enumerate(puzzles[k]):
                    rv = deepcopy(v)
                    for t in range(4):
                        rv = sorted(rotate90(rv))
                        for a, b in zip(rv, sc):
                            if a != b:
                                break
                        else:
                            answer += k
                            puzzles[k].pop(vi)
                            break
                    else:
                        continue
                    break
    return answer

# 공통 부분 함수로 만들기
def solution_v2(game_board, table):
    def rotate90(arr):
        min_x, min_y = 6, 6
        result = []
        for ax, ay in arr:
            rx, ry = -ay, ax
            min_x, min_y = min(rx, min_x), min(ry, min_y)
            result.append([rx, ry])
        for r in range(len(result)):
            result[r][0] -= min_x
            result[r][1] -= min_y
        return result

    def bfs(flag):
        if flag:
            table[x][y] = 0
        else:
            game_board[x][y] = 1
        q = deque()
        q.append((x, y))
        tile = []
        min_i, min_j = x, y
        tile.append([x, y])
        while q:
            i, j = q.popleft()
            for di, dj in d:
                ni, nj = i + di, j + dj
                if -1 < ni < n and -1 < nj < n:
                    if flag and table[ni][nj]:
                        table[ni][nj] = 0
                    elif not flag and not game_board[ni][nj]:
                        game_board[ni][nj] = 1
                    else:
                        continue
                    q.append((ni, nj))
                    tile.append([ni, nj])
                    min_i, min_j = min(ni, min_i), min(nj, min_j)
        for t in range(len(tile)):
            tile[t][0] -= min_i
            tile[t][1] -= min_j
        return tile

    n = len(table)
    answer = 0
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # 테이블에서 조각 찾기
    puzzles = defaultdict(list)
    for x in range(n):
        for y in range(n):
            if table[x][y]:
                pz = bfs(1)
                puzzles[len(pz)].append(pz)
    # 빈공간 찾아서 넣기
    for x in range(n):
        for y in range(n):
            if not game_board[x][y]:
                sc = bfs(0)
                k = len(sc)
                sc.sort()
                for vi, v in enumerate(puzzles[k]):
                    rv = deepcopy(v)
                    for t in range(4):
                        rv = sorted(rotate90(rv))
                        for a, b in zip(rv, sc):
                            if a != b:
                                break
                        else:
                            answer += k
                            puzzles[k].pop(vi)
                            break
                    else:
                        continue
                    break
    return answer
