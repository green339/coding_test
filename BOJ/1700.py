# https://www.acmicpc.net/problem/1700
import sys
input=sys.stdin.readline

N,K=map(int,input().split())
board=[[] for _ in range(K+1)]
order=list(map(int,input().split()))
for i in range(K):
    board[order[i]].append(i)
for i in range(1,K+1):
    board[i].append(K+1)
cnt=0
visited=[0]*(K+1)
plug=[0]*(K+1)
ans=0
for o in order:
    if plug[o]:
        visited[o]+=1
        continue
    if cnt<N:
        cnt+=1
    else:
        tmp=-1
        tmp_idx=-1
        for i in range(1,K+1):
            if plug[i] and board[i][visited[i]]>tmp:
                tmp_idx=i
                tmp=board[i][visited[i]]
        plug[tmp_idx]=0
        ans+=1
    plug[o]=1
    visited[o]+=1
print(ans)

