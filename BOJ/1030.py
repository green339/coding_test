# https://www.acmicpc.net/problem/1030
# 메모리 초과
import sys
input=sys.stdin.readline


s, N, K, R1, R2, C1, C2=map(int,input().split())
total=N**s
board=[["0"]*total for _ in range(total)]
for t in range(1,s+1): # 현재 시간
    rec=N**t # 단위 정사각형 크기
    mid=K*(rec//N) # 가운데 정사각형 크기
    for i in range(0,total,rec):
        for j in range(0,total,rec):
            mi=i+(rec-mid)//2
            mj=j+(rec-mid)//2
            for ii in range(mi,mi+mid):
                for jj in range(mj,mj+mid):
                    board[ii][jj]="1"

for r in range(R1,R2+1):
    row=board[r]
    print(''.join(row[C1:C2+1]))




