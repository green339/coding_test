# https://www.acmicpc.net/problem/20437
import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    W=input().strip()
    board=[ord(i)-97 for i in W]
    K=int(input())
    cnt=[0]*26
    start=[[] for _ in range(26)]
    max_ans=-1
    min_ans=10001
    for i,b in enumerate(board):
        start[b].append(i)
        cnt[b]+=1
        if cnt[b]>=K:
            tmp=i-start[b][cnt[b]-K]+1
            if tmp>max_ans:
                max_ans=tmp
            if tmp<min_ans:
                min_ans=tmp
    if min_ans==10001:
        print(-1)
    else:
        print(min_ans,max_ans)
