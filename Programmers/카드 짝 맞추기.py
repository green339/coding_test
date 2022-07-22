# https://school.programmers.co.kr/learn/courses/30/lessons/72415

from collections import defaultdict, deque


def solution(board, r, c):
    global answer

    def check(start, dest):
        q = deque()
        d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        si, sj = start
        q.append((si, sj))
        arr = [[10e9] * 4 for _ in range(4)]
        arr[si][sj] = 0
        while q:
            i, j = q.popleft()
            cost=arr[i][j]
            for di, dj in d:
                ni = i + di
                nj = j + dj
                if -1 < ni < 4 and -1 < nj < 4:
                    if arr[ni][nj] > cost + 1:
                        arr[ni][nj] = cost + 1
                        q.append((ni, nj))  # 방향키로 움직이는 경우
                    if not board[ni][nj]:
                        for k in range(3):  # ctrl로 움직이는 경우
                            ni += di
                            nj += dj
                            if -1 < ni < 4 and -1 < nj < 4:
                                # 다른 카드가 있는 경우
                                if board[ni][nj] and arr[ni][nj] > cost + 1:
                                    arr[ni][nj] = cost + 1
                                    q.append((ni, nj))
                                    break
                            else:
                                # 맨 끝까지 간 경우
                                if k > 0:
                                    if arr[ni - di][nj - dj] > cost + 1:
                                        arr[ni - di][nj - dj] = cost + 1
                                        q.append((ni - di, nj - dj))
                                break
        return arr[dest[0]][dest[1]]

    # permutation
    def dfs(loc, cnt):
        global answer
        if min(visited):
            answer = min(answer, cnt)
            return
        for idx in range(1, n + 1):
            if not visited[idx]:
                visited[idx] = 1
                for l, r in [(0, 1), (1, 0)]:
                    left = card[idx][l]
                    right = card[idx][r]
                    tmp = check(loc, left)
                    board[left[0]][left[1]] = 0
                    move = check(left, right)
                    board[right[0]][right[1]] = 0
                    dfs(right, cnt + move + tmp + 2)
                    board[left[0]][left[1]] = idx
                    board[right[0]][right[1]] = idx
                visited[idx] = 0

    answer = 10e9
    card = defaultdict(list)
    for x in range(4):
        for y in range(4):
            if board[x][y]:
                card[board[x][y]].append((x, y))
    n = len(card.keys())
    visited = [0] * (n + 1)
    visited[0] = 1
    dfs((r, c), 0)
    return answer
