# https://www.acmicpc.net/problem/16234
import sys
from collections import deque
input=sys.stdin.readline

d=[(-1,0),(1,0),(0,1),(0,-1)]
def move(sx,sy):
    q=deque([(sx,sy)])
    visited.add((sx,sy))
    res=set()
    res.add((sx,sy))
    ppl=board[sx][sy]
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx=x+dx
            ny=y+dy
            if -1<nx<N and -1<ny<N:
                if (nx,ny) not in visited:
                    if L<=abs(board[nx][ny]-board[x][y])<=R:
                        visited.add((nx,ny))
                        res.add((nx,ny))
                        ppl+=board[nx][ny]
                        q.append((nx,ny))
    if len(res)==1:
        return 0
    else:
        ppl=ppl//len(res)
        for x,y in res:
            board[x][y]=ppl
        return 1


N,L,R=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]

flag=1
ans=0
while flag:
    visited=set()
    flag=0
    for i in range(N):
        for j in range(N):
            if (i,j) not in visited:
                if move(i,j):
                    flag=1
    if flag:
        ans+=1
print(ans)