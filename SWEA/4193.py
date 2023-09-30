import heapq
dd=[(-1,0),(0,-1),(1,0),(0,1)]
T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    board=[list(map(int,input().split())) for _ in range(N)]
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    visited=[[-1]*N for _ in range(N)]
    q=[(0,a,b)]
    visited[a][b]=0
    while q:
        cur,x,y=heapq.heappop(q)
        if x==c and y==d:
            break
        for dx,dy in dd:
            nx=x+dx
            ny=y+dy
            if -1<nx<N and -1<ny<N:
                cost=0
                if board[nx][ny]==1:
                    continue
                elif board[nx][ny]==2:
                    cost+=3-cur%3
                else:
                    cost+=1
                if visited[nx][ny]==-1 or cur+cost<visited[nx][ny]:
                    visited[nx][ny]=cur+cost
                    heapq.heappush(q,(cur+cost,nx,ny))
    print(f"#{test_case} {visited[c][d]}")
