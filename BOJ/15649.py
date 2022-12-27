# https://www.acmicpc.net/problem/15649
import sys
input=sys.stdin.readline

def dfs(depth):
    if depth==M:
        print(" ".join(map(str,s)))
        return
    for i in range(1,N+1):
        if i not in s:
            visited[i]=1
            s.append(i)
            dfs(depth+1)
            s.pop()
s=[]
N,M=map(int,input().split())
visited=[0]*(N+1)
dfs(0)