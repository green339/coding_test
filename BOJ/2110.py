import sys
input=sys.stdin.readline

N,C=map(int,input().split())
board=[int(input()) for _ in range(N)]
board.sort()
left=1
right=board[N-1]-board[0]
while left<=right:
    mid=(left+right)//2
    cnt=1 # 첫번째 위치는 설치
    prior=board[0]
    for i in range(1,N):
        if board[i]-prior>mid:
            cnt+=1
            prior=board[i]
    if cnt>=C:
        left=mid+1
    else:
        right=mid-1
print(left)
