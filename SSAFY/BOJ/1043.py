# https://www.acmicpc.net/problem/1043
import sys
input=sys.stdin.readline

def union(a,b):
    a=find(a)
    b=find(b)
    if a>b:
        a,b=b,a
    parent[b]=a
def find(a):
    if parent[a]!=a:
        parent[a]=find(parent[a])
    return parent[a]

N,M=map(int,input().split())
truth=list(map(int,input().split()))[1:]
parent=[i for i in range(N+1)]
for t in truth:
    parent[t]=0
board=[]
for i in range(M):
    tmp=list(map(int,input().split()))
    for j in range(1,tmp[0]):
        union(tmp[j],tmp[j+1])
    board.append(tmp[1:])

ans=M
for bb in board:
    for x in bb:
        if not parent[x]:
            ans-=1
            break
        elif not find(x):
            ans-=1
            break
print(ans)

