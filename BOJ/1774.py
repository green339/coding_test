import sys
import heapq
input=sys.stdin.readline

def union(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return False
    elif x>y:
        parent[x]=y
    elif x<y:
        parent[y]=x
    return True

def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]

N,M=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
parent=[i for i in range(N)]
cnt=0
for _ in range(M):
    a,b=map(int,input().split())
    if union(a-1,b-1):
        cnt+=1

q=[]
for i in range(N):
    for j in range(i+1,N):
        dist=((board[i][0]-board[j][0])**2+(board[i][1]-board[j][1])**2)**0.5
        heapq.heappush(q,(dist,i,j))
answer=0
while q:
    dist,i,j=heapq.heappop(q)
    if union(i,j):
        answer+=dist
        cnt+=1
    if cnt==N-1:
        break
print("%.2f" %round(answer,2))
