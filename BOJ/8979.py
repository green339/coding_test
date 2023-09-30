# https://www.acmicpc.net/problem/8979
import sys
input=sys.stdin.readline
N,K=map(int,input().split())
board=[list(map(int,input().split())) for i in range(N)]
board.sort(key=lambda x:(-x[1],-x[2],-x[3]))
rank=1
for idx in range(1,N):
    if board[idx-1][1:]!=board[idx][1:]:
        rank=idx+1
    if board[idx][0]==K:
        print(rank)
        break
else:
    print(1)