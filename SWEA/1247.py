def dfs(depth,dist,i):
    global answer
    if answer<dist:
        return
    if depth==N:
        dist+=abs(hx-board[i][0])+abs(hy-board[i][1])
        if answer>dist:
            answer=dist
        return

    for ni in range(N):
        if not visited[ni]:
            if depth>0:
                cur=abs(board[ni][0]-board[i][0])+abs(board[ni][1]-board[i][1])
            else:
                cur=abs(cx-board[ni][0])+abs(cy-board[ni][1])
            visited[ni]=1
            dfs(depth+1,cur+dist,ni)
            visited[ni]=0

T = int(input())
for test_case in range(1, T + 1):
    answer=10e9
    N=int(input())
    tmp=list(map(int,input().split()))
    board=[[0]*2 for _ in range(N)]
    hx,hy=tmp[0],tmp[1]
    cx,cy=tmp[2],tmp[3]
    for idx in range(4,2*N+4,2):
        board[idx//2-2][0]=tmp[idx]
        board[idx//2-2][1]=tmp[idx+1]
    visited=[0]*N
    dfs(0,0,0)
    print(f"#{test_case} {answer}")
