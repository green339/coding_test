# https://www.acmicpc.net/problem/6593
import sys
import heapq


def bfs(s, e, board, L, R, C):
    d = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    q = [(0, s[0], s[1], s[2])]
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    visited[s[0]][s[1]][s[2]] = 1
    while q:
        ct, cl, cr, cc = heapq.heappop(q)
        for z, x, y in d:
            nl = cl + z
            nr = cr + x
            nc = cc + y
            if nl == e[0] and nr == e[1] and nc == e[2]:
                return ct + 1
            if -1 < nl < L and -1 < nr < R and -1 < nc < C and not visited[nl][nr][nc]:
                visited[nl][nr][nc] = 1
                if board[nl][nr][nc] == '.':
                    heapq.heappush(q, (ct + 1, nl, nr, nc))
    return 0


if __name__ == "__main__":
    while True:
        L, R, C = map(int, sys.stdin.readline().split())
        if L == 0 and R == 0 and C == 0:
            break
        building = dict()
        start = (0, 0, 0)
        end = (0, 0, 0)
        for i in range(L):
            building[i] = []
            for x in range(R):
                building[i].append(list(sys.stdin.readline().strip()))
                if 'S' in building[i][-1]:
                    start = (i, x, building[i][-1].index('S'))
                elif 'E' in building[i][-1]:
                    end = (i, x, building[i][-1].index('E'))
            _ = sys.stdin.readline()
        minute = bfs(start, end, building, L, R, C)
        if minute:
            print("Escaped in %d minute(s)." % minute)
        else:
            print("Trapped!")
