# https://www.acmicpc.net/problem/2206
import sys
from collections import deque
d=[(-1,0),(0,-1),(1,0),(0,1)]

input=sys.stdin.readline

def bfs():
    q=deque()
    visited=[[[0,0] for _ in range(M)] for _ in range(N)] # 0: 한번도 벽을 부순적 없이 도착한 경우, 1: 한번이라도 벽을 부수고 도착한 경우
    q.append((0,0,0)) # flag, x,y
    visited[0][0][0]=1
    while q:
        flag,x,y=q.popleft()
        if x==N-1 and y==M-1:
            return visited[x][y][flag]
        for dx,dy in d:
            nx=x+dx
            ny=y+dy
            if -1<nx<N and -1<ny<M:
                if not board[nx][ny] and not visited[nx][ny][flag]:
                    visited[nx][ny][flag]=visited[x][y][flag]+1
                    q.append((flag,nx,ny))
                elif board[nx][ny] and not flag:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((1,nx,ny))
    return -1


N,M=map(int,input().split())
board=[list(map(int,list(input().strip()))) for _ in range(N)]
print(bfs())


