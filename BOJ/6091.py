import sys
import heapq

input = sys.stdin.readline

def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        parent[y]=x
    elif x>y:
        parent[x]=y
    else:
        return False
    return True

def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]

N = int(input())
q = []  # 간선들이라고 가정
for i in range(N - 1):
    tmp = list(map(int, input().split()))
    for j in range(i + 1, N):
        heapq.heappush(q, (tmp[j - i - 1], i, j))

parent=[i for i in range(N)]
board=[[] for _ in range(N)]
cnt=0
while q:
    dist,i,j=heapq.heappop(q)
    if union(i,j):
        board[i].append(j+1)
        board[j].append(i+1)
        cnt+=1
    if cnt==N-1:
        break

for b in board:
    print(len(b),*sorted(b))
