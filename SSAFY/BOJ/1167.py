# https://www.acmicpc.net/problem/1167
import sys
from collections import defaultdict

input=sys.stdin.readline

def dfs(x):
    global ans
    visited[x]=True
    subtrees=[0]
    for nx,nc in board[x]:
        if not visited[nx]:
            subtrees.append(dfs(nx)+nc)
    subtrees.sort(reverse=True)
    if len(subtrees)>2:
        ans=max(ans,subtrees[0]+subtrees[1])
    return subtrees[0]

V=int(input())
board=defaultdict(list)
for _ in range(V):
    inputs=list(map(int,input().split()))
    for i in range(1,len(inputs)-1,2):
        board[inputs[0]].append((inputs[i],inputs[i+1]))
visited=[False]*(V+1)
ans=0
print(max(dfs(1),ans)) # 순서 중요...

'''
트리의 지름 
한 노드에서 트리의 지름 구하기
1. (1포함x) 여러 개의 자식 노드 중에서 최대인 두개의 값 더해서 -> 이건 이번 노드만 해당 (일단 ans로 저장해두기)
2. (1포함o) 가장 큰 노드는 부모 노드로 보내기 -> 지금은 자식노드 두개 더한거 보다 안 크지만 부모, 부모의부모.. 이렇게 더하면 커질수도?
분할 정복이랑 비슷 하기도 하고...
'''
