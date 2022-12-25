# https://www.acmicpc.net/problem/2667
import sys
from collections import deque
input=sys.stdin.readline
d=[(-1,0),(0,1),(0,-1),(1,0)]

def bfs(sx,sy):
    visited[sx][sy]=1
    q=deque()
    q.append((sx,sy))
    cnt=1
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx=dx+x
            ny=dy+y
            if -1<nx<N and -1<ny<N:
                if board[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    cnt+=1
    answer.append(cnt)

N=int(input())
board=[list(map(int,list(input().strip()))) for _ in range(N)]
visited=[[0]*N for _ in range(N)]
answer=[]
for i in range(N):
    for j in range(N):
        if board[i][j] and not visited[i][j]:
            bfs(i,j)
print(len(answer))
for a in sorted(answer):
    print(a)