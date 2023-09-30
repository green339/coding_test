# https://www.acmicpc.net/problem/2293
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
coin=[int(input()) for _ in range(n)]
dp=[0]*(k+1)
dp[0]=1
for c in coin:
    for i in range(1,k+1):
        if c<=i:
            dp[i]+=dp[i-c]
print(dp[-1])


