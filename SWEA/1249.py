import sys
input=sys.stdin.readline

import heapq
t=int(input())
d=[(-1,0),(0,1),(0,-1),(1,0)]
for tc in range(1,t+1):
    n=int(input())
    board=[list(map(int,list(input().strip()))) for _ in range(n)]
    cost=[[1e9]*n for _ in range(n)]
    cost[0][0]=board[0][0]
    q=[(board[0][0],0,0)]
    while q:
        cur,x,y=heapq.heappop(q)
        if cur>cost[x][y]:
            continue
        for dx,dy in d:
            nx=x+dx
            ny=y+dy
            if -1<nx<n and -1<ny<n:
                tmp=cur+board[nx][ny]
                if tmp<cost[nx][ny]:
                    cost[nx][ny]=tmp
                    heapq.heappush(q,(tmp,nx,ny))
    print(f'#{tc} {cost[n-1][n-1]}')
