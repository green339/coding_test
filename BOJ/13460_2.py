import sys
from collections import deque
input=sys.stdin.readline


def move(x,y,flag):
    while True:
        nx=x+flag[0]
        ny=y+flag[1]
        if -1<nx<N and -1<ny<M and board[nx][ny]!="#":
            x=nx
            y=ny
            if board[x][y]=="O":
                break
        else:
            break
    return x,y


def order(x1,y1,x2,y2,flag):
    if x1*flag[0]+y1*flag[1]>x2*flag[0]+y2*flag[1]:
        nx1,ny1=move(x1,y1,flag)
        nx2,ny2=move(x2,y2, flag)
        if nx1==nx2 and ny1==ny2:
            if nx1==hole[0] and ny1==hole[1]:
                return -1,-1,-1,-1
            nx2-=flag[0]
            ny2-=flag[1]
    else:
        nx2, ny2 = move(x2, y2, flag)
        nx1, ny1 = move(x1, y1, flag)
        if nx1==nx2 and ny1==ny2:
            if nx1==hole[0] and ny1==hole[1]:
                return -1,-1,-1,-1
            nx1-=flag[0]
            ny1-=flag[1]
    if nx2 == hole[0] and ny2 == hole[1]:
        return -1, -1, -1, -1
    return nx1,ny1,nx2,ny2


N,M=map(int,input().split())
board=[list(input().strip()) for _ in range(N)]
hole=[]
red=[]
blue=[]
for i in range(N):
    for j in range(M):
        if board[i][j]=='O':
            hole=[i,j]
        elif board[i][j]=='B':
            blue=[i,j]
            board[i][j]='.'
        elif board[i][j]=='R':
            red=[i,j]
            board[i][j]='.'

q=deque()
q.append((red[0],red[1],blue[0],blue[1]))
visited=[[[0]*(N*M) for _ in range(M)]for _ in range(N)]
visited[red[0]][red[1]][blue[0]*M+blue[1]]=1
dd=[[-1,0],[0,1],[1,0],[0,-1]]
while q:
    rx,ry,bx,by=q.popleft()
    for d in dd:
        nrx,nry,nbx,nby=order(rx,ry,bx,by,d)
        if nrx==-1:
            continue
        if visited[nrx][nry][nbx*M+nby]:
            continue
        visited[nrx][nry][nbx*M+nby]=visited[rx][ry][bx*M+by]+1
        q.append((nrx,nry,nbx,nby))

ans=12
for v in visited[hole[0]][hole[1]]:
    if v and v<ans:
        ans=v
print(ans-1 if ans!=12 else -1)




