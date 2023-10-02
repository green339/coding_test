# https://www.acmicpc.net/problem/14658
import sys
input=sys.stdin.readline

N,M,L,K=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(K)]
ans=0
for i in range(K):
    tx=board[i][0]
    for j in range(K):
        ty=board[j][1]
        cnt=0
        for bx,by in board:
            if tx<=bx<=tx+L and  ty<=by<=ty+L:
                cnt+=1
        if ans<cnt:
            ans=cnt
print(K-ans)