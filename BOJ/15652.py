# https://www.acmicpc.net/problem/15652
import sys
input=sys.stdin.readline

def dfs(cur,depth):
    if depth==M:
        print(" ".join(map(str,s)))
        return
    for i in range(cur,N+1):
        s.append(i)
        dfs(i,depth+1)
        s.pop()

N,M=map(int,input().split())
s=[]
dfs(1,0)