# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo
from collections import defaultdict, deque


def routing(x, y, move):
    res = []
    res.append(10 * x + y)
    for dd in move:
        x += d[dd][0]
        y += d[dd][1]
        res.append(10 * x + y)
    return res


d = {0: (0, 0), 1: (-1, 0), 2: (0, 1), 3: (1, 0), 4: (0, -1)}

test = int(input())
for tc in range(1, test + 1):
    a_route = []
    b_route = []
    M, A = map(int, input().split())
    a_move = list(map(int, input().split()))
    b_move = list(map(int, input().split()))
    board = defaultdict(list)
    for i in range(A):
        apy, apx, c, p = map(int, input().split())
        visited = [[0] * 10 for _ in range(10)]
        apx -= 1
        apy -= 1
        q = deque()
        q.append((apx, apy))
        visited[apx][apy] = 1
        board[apx * 10 + apy].append((p, i))
        while q:
            x, y = q.popleft()
            if visited[x][y] > c:
                continue
            for idx in range(1, 5):
                nx = x + d[idx][0]
                ny = y + d[idx][1]
                if -1 < nx < 10 and -1 < ny < 10:
                    if visited[nx][ny]:
                        continue
                    visited[nx][ny] = visited[x][y] + 1
                    board[nx * 10 + ny].append((p, i))
                    q.append((nx, ny))
    a_route = routing(0, 0, a_move)
    b_route = routing(9, 9, b_move)
    answer = 0
    for ar, br in zip(a_route, b_route):
        if not board[ar] and not board[br]:
            continue
        if board[ar] and not board[br]:
            answer += max(board[ar])[0]
        elif not board[ar] and board[br]:
            answer += max(board[br])[0]
        else:
            if max(board[ar])[1] != max(board[br])[1]:
                answer += max(board[ar])[0] + max(board[br])[0]
                continue
            if len(board[ar]) == 1 and len(board[br]) == 1:
                answer += board[ar][0][0]
                continue
            a_second = 0
            b_second = 0
            board[ar].sort(reverse=True)
            board[br].sort(reverse=True)
            if len(board[ar]) > 1:
                a_second = board[ar][1][0]
            if len(board[br]) > 1:
                b_second = board[br][1][0]
            answer += max(a_second, b_second) + board[ar][0][0]
    print(f"#{tc} {answer}")
