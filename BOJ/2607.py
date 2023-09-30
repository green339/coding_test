# https://www.acmicpc.net/problem/2607
import sys
from collections import defaultdict
input=sys.stdin.readline

def make_set(word):
    cnt=defaultdict(int)
    res=set()
    for w in word:
        cnt[w]+=1
        res.add(w+str(cnt[w]))
    return res

n=int(input())
target=make_set(input().strip())

ans=0
for _ in range(n-1):
    comp=make_set(input().strip())
    if len(target-comp)<2 and len(comp-target)<2:
        ans+=1

print(ans)