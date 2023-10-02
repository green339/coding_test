# https://www.acmicpc.net/problem/12919
import sys
from collections import deque
input=sys.stdin.readline

S=input().strip()
T=input().strip()
q=deque([T])
visited=set()
visited.add(T)
while q:
    x=q.popleft()
    if x==S:
        print(1)
        break
    if len(x)==len(S):
        continue
    cand=[]
    if x[-1]=="A":
        cand.append(x[:-1])
    if x[0]=="B":
        cand.append(x[::-1][:-1])
    for nx in cand:
        if nx not in visited:
            visited.add(nx)
            q.append(nx)
else:
    print(0)
