import sys
input=sys.stdin.readline

def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

N=int(input())
M=int(input())
board = [list(map(int, input().split())) for _ in range(N)]
city=list(map(int,input().split()))
parent=[i for i in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j]:
            union(i, j)

for i in range(1,M):
    if parent[city[i-1]-1]!=parent[city[i]-1]:
        print("NO")
        break
else:
    print("YES")