# https://www.acmicpc.net/problem/20303
import sys
input=sys.stdin.readline

def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        x,y=y,x
    parent[x]=y
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

N,M,K=map(int,input().split())
candy=list(map(int,input().split()))
parent=[i for i in range(N)]
cnt=[1]*N
for _ in range(M):
    a,b=map(int,input().split())
    union(a-1,b-1)
res=[]
for i in range(N):
    if parent[i]!=i:
        root=find(i)
        cnt[root]+=1
        candy[root]+=candy[i]
for i in range(N):
    if parent[i]==i:
        res.append((cnt[i],candy[i]))
dp=[0]*K
for a,b in res:
    for j in range(K-1,a-1,-1):
        dp[j]=max(dp[j],dp[j-a]+b)
print(max(dp))

