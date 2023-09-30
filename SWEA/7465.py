import sys
input=sys.stdin.readline

from collections import defaultdict,deque

t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())
    board=defaultdict(list)
    for _ in range(m):
        a,b=map(int,input().split())
        board[a].append(b)
        board[b].append(a)
    visited=[0]*(n+1)
    answer = 0
    for i in range(1,n+1):
        if visited[i]:
            continue
        answer+=1
        q=deque([i])
        while q:
            x=q.popleft()
            for nx in board[x]:
                if not visited[nx]:
                    q.append(nx)
                    visited[nx]=1
    print(f"#{tc} {answer}")