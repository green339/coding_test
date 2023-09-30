# https://www.acmicpc.net/problem/2636
import sys
from collections import deque
d=[(-1,0),(0,-1),(1,0),(0,1)]

input=sys.stdin.readline

def bfs():
    cnt=0
    q=deque()
    q.append((0,0))
    visited=[[0]*M for _ in range(N)]
    visited[0][0]=1
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx=x+dx
            ny=y+dy
            if -1<nx<N and -1<ny<M:
                if not visited[nx][ny]:
                    visited[nx][ny]=1
                    if board[nx][ny]:
                        board[nx][ny]=0
                        cnt+=1
                    else:
                        q.append((nx,ny))
    return cnt

N,M=map(int,input().split())
board=[list(map(int,input().split()))for _ in range(N)]
answer=0
t=0
while True:
    flag=bfs()
    if flag:
        answer=flag
        t+=1
    else:
        break

print(t)
print(answer)
