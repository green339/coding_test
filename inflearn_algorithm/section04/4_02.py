import sys

K, N=map(int,sys.stdin.readline().split())
lans=[int(sys.stdin.readline()) for _ in range(K)]
lans.sort()
left=1
right=lans[-1]
ans=0
while left<=right:
    mid=(left+right)//2
    count_l=0
    for lan in lans:
        count_l+=(lan//mid)
    if count_l>=N:
        left=mid+1
        ans=mid
    else:
        right=mid-1
print(ans)

# 이분탐색을 이용한 결정알고리즘은 답이 특정범위안에 있다는 것을 알고있을때