import sys
# from itertools import combinations

N,K=map(int,sys.stdin.readline().split())
cards=list(map(int,sys.stdin.readline().split()))
hap=set()
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            hap.add(cards[i]+cards[j]+cards[k])
# for c in combinations(cards,3):
#     hap.add(sum(c))
print(sorted(hap,reverse=True)[K-1])