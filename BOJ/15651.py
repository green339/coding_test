# https://www.acmicpc.net/problem/15651
import sys
input=sys.stdin.readline

def dfs(depth):
    if depth==M:
        print(" ".join(map(str,s)))
        return
    for i in range(1,N+1):
        s.append(i)
        dfs(depth+1)
        s.pop()

N,M=map(int,input().split())
s=[]
dfs(0)