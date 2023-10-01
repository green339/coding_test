import sys
input=sys.stdin.readline

shape=[[(1,0),(0,1),(1,1)],
       [(1,0),(2,0),(3,0)], [(0,1),(0,2),(0,3)],
       [(0,1),(1,1),(2,1)], [(1,0),(2,0),(0,1)], [(1,0),(2,0),(2,-1)], [(1,0),(2,0),(2,1)],
       [(1,0),(1,1),(1,2)],[(1,0),(1,-1),(1,-2)],[(-1,0),(-1,1),(-1,2)],[(-1,0),(-1,-1),(-1,-2)],
       [(1,0),(1,-1),(2,-1)], [(1,0),(1,1),(2,1)], [(0,1),(1,1),(1,2)], [(0,1),(1,0),(1,-1)],
       [(-1,0),(1,0),(0,1)], [(-1,0),(0,-1),(1,0)], [(-1,0),(0,-1),(0,1)], [(0,-1),(1,0),(0,1)]]

N,M=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
max_num=max(map(max,board))
ans=0
for x in range(N):
    for y in range(M):
        if board[x][y]+3*max_num<=ans:
            continue
        for s in shape:
            cur=board[x][y]
            cnt=3
            for dx,dy in s:
                if cur+cnt*max_num<=ans:
                    break
                if -1<dx+x<N and -1<dy+y<M:
                    cur+=board[dx+x][dy+y]
                    cnt-=1
                else:
                    break
            else:
                if ans<cur:
                    ans=cur
print(ans)