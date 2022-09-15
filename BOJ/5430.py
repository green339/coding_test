# https://www.acmicpc.net/problem/5430
import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().strip()
    n = int(input())
    if n:
        q = deque(input().strip().lstrip('[').rstrip(']').split(','))
    else:
        _ = input()
        q = []
    flag=0
    for o in p:
        if o == 'R':
            flag=abs(flag-1)
        else:
            if not q:
                print("error")
                break
            if flag:
                q.pop()
            else:
                q.popleft()
    else:
        if flag:
            s = ','.join(reversed(q))
        else:
            s = ','.join(q)
        print(f"[{s}]")
